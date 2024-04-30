from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Text
from django.contrib.auth.models import User
from django.db.models import Q
import hashlib
from django.contrib import messages

#This shows the user's message inbox
@login_required
def inbox(request):
    conversations = {}
    #This filters the users' inbox to show the most recent messages, this also displays the messages that the user has either sent or received
    all_texts = Text.objects.filter(Q(sender=request.user) | Q(recipient=request.user)).order_by('-timestamp')
    
    for text in all_texts:
        if text.conversation_id not in conversations:
            conversations[text.conversation_id] = []
        conversations[text.conversation_id].append(text)
    
    conversations = {key: sorted(value, key=lambda x: x.timestamp, reverse=True) for key, value in conversations.items()}
    
    return render(request, 'messaging/inbox.html', {'conversations': conversations})

@login_required
def send_message(request, recipient_username):
    recipient = get_object_or_404(User, username=recipient_username)
    
    #this generates the conversation ID, which is important for ensuring a conversation is continuous
    conversation_id = generate_conversation_id(request.user, recipient)
    if Text.objects.filter(conversation_id=conversation_id).count() > 0:
        participants = {request.user, recipient}
        #This ensures that there are only 2 people in the conversation
        if len(participants) != 2:
            messages.warning(request, 'You are not allowed to access this conversation.')
            return redirect('ContactApplication:home')
            
    
    if request.method == 'POST':
        content = request.POST['content']
        Text.objects.create(sender=request.user, recipient=recipient, content=content, conversation_id=conversation_id)
        return redirect('messaging:inbox')
    else:
        return render(request, 'messaging/send_message.html', {'recipient': recipient})
    

@login_required
def reply_message(request, message_id):
    #This gets the original message that's shown as the most recent on the inbox page
    original_text = get_object_or_404(Text, pk=message_id)
    conversation_id = original_text.conversation_id
    
    #This gets both people involved in the conversation
    participants = {original_text.sender, original_text.recipient}
    #This ensures that only people in the conversation are allowed to access it
    if request.user not in participants:
        messages.warning(request, 'You are not allowed to access this conversation.')
        return redirect('ContactApplication:home')
        
    
    texts = Text.objects.filter(conversation_id=conversation_id).exclude(content='')
    
    if request.method == 'POST':
        #This checks for if the current user is the sender or recipient of the original message
        recipient = original_text.sender if request.user == original_text.recipient else original_text.recipient
        content = request.POST['content']
        #This creates the message between the two participents
        Text.objects.create(sender=request.user, recipient=recipient, content=content, conversation_id=conversation_id)
        return redirect('messaging:reply_message', message_id=message_id)
    else:
        return render(request, 'messaging/conversation_view.html', {'texts': texts, 'original_text': original_text})

#This generates the conversation ID when 2 users message each other
def generate_conversation_id(user1, user2):
    usernames = [user1.username, user2.username]
    usernames.sort()
    concatenated_names = '_'.join(usernames)
    #This creates a random string that's extremely unlikely to ever be used again
    conversation_id = hashlib.sha256(concatenated_names.encode()).hexdigest()
    #This sends the ID back so the other views can use it
    return conversation_id
