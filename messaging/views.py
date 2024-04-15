from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from django.db.models import Q
import hashlib

@login_required
def inbox(request):
    conversations = {}
    # Retrieve all messages where the current user is either the sender or the recipient
    all_messages = Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user))
    
    for message in all_messages:
        if message.conversation_id not in conversations:
            conversations[message.conversation_id] = []
        conversations[message.conversation_id].append(message)
    
    return render(request, 'messaging/inbox.html', {'conversations': conversations})

@login_required
def send_message(request, recipient_username):
    recipient = get_object_or_404(User, username=recipient_username)
    if request.method == 'POST':
        content = request.POST['content']
        conversation_id = generate_conversation_id(request.user, recipient)
        Message.objects.create(sender=request.user, recipient=recipient, content=content, conversation_id=conversation_id)
        return redirect('messaging:inbox')
    else:
        return render(request, 'messaging/send_message.html', {'recipient': recipient})

@login_required
def reply_message(request, message_id):
    original_message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        recipient = original_message.sender if request.user == original_message.recipient else original_message.recipient
        content = request.POST['content']
        Message.objects.create(sender=request.user, recipient=recipient, content=content, conversation_id=original_message.conversation_id)
        return redirect('messaging:inbox')
    else:
        return render(request, 'messaging/reply_message.html', {'original_message': original_message})

def generate_conversation_id(user1, user2):
    usernames = [user1.username, user2.username]
    usernames.sort()
    concatenated_names = '_'.join(usernames)
    conversation_id = hashlib.sha256(concatenated_names.encode()).hexdigest()
    return conversation_id
