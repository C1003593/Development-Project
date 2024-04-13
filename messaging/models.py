import uuid
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name="message_sender")
    recipient = models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name="message_recipient")
    subject = models.CharField(max_length=30)
    body = models.TextField()
    
    def __str__(self):
        return f'{self.message_id} {self.sender} {self.recipient}'
