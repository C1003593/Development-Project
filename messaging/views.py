from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Text
from django.contrib.auth.models import User
from django.db.models import Q
import hashlib
from django.contrib import messages

@login_required
def inbox(request):
    conversations = {}
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
    
    # Check if the recipient is the only other participant in the conversation
    conversation_id = generate_conversation_id(request.user, recipient)
    if Text.objects.filter(conversation_id=conversation_id).count() > 0:
        participants = {request.user, recipient}
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
    original_text = get_object_or_404(Text, pk=message_id)
    conversation_id = original_text.conversation_id
    
    # Check if the current user is one of the participants of the conversation
    participants = {original_text.sender, original_text.recipient}
    if request.user not in participants:
        messages.warning(request, 'You are not allowed to access this conversation.')
        return redirect('ContactApplication:home')
        
    
    texts = Text.objects.filter(conversation_id=conversation_id).exclude(content='')
    
    if request.method == 'POST':
        recipient = original_text.sender if request.user == original_text.recipient else original_text.recipient
        content = request.POST['content']
        Text.objects.create(sender=request.user, recipient=recipient, content=content, conversation_id=conversation_id)
        return redirect('messaging:reply_message', message_id=message_id)
    else:
        return render(request, 'messaging/conversation_view.html', {'texts': texts, 'original_text': original_text})

def generate_conversation_id(user1, user2):
    usernames = [user1.username, user2.username]
    usernames.sort()
    concatenated_names = '_'.join(usernames)
    conversation_id = hashlib.sha256(concatenated_names.encode()).hexdigest()
    return conversation_id
