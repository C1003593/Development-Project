from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    typeofpost = models.CharField(max_length=50 , choices = [('Problem', 'Problem'), ('Discussion', 'Discussion')])
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, related_name= 'Post', on_delete=models.DO_NOTHING)
    description = models.TextField()
    timesubmitted = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('forums:post-detail', kwargs = {'pk' : self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    usercomment = models.ForeignKey(User, related_name= 'Comment', on_delete=models.DO_NOTHING)
    timesent = models.DateTimeField(default= timezone.now)


