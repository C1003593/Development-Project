from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    conversation_id = models.CharField(max_length=100)

    class Meta:
        ordering = ['timestamp']
