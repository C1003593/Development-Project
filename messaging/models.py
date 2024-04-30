from django.db import models
from django.contrib.auth.models import User

#This is what stores the messages being sent
class Text(models.Model):
    #A conversation ID will be generated when users send the first message
    #After that all future messages between them will be under that specific conversation ID
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    conversation_id = models.CharField(max_length=100)

    #This makes sure that the most recent messages are shown first
    class Meta:
        ordering = ['timestamp']
