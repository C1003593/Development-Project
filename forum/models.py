from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#This is how the posts are stored
class Post(models.Model):
    #This gives the user the option between the 2 types of post
    typeofpost = models.CharField(max_length=50 , choices = [('Problem', 'Problem'), ('Discussion', 'Discussion')])
    title = models.CharField(max_length=40)
    #This makes sure that a user is attached to a post
    user = models.ForeignKey(User, related_name= 'Post', on_delete=models.DO_NOTHING)
    description = models.TextField()
    timesubmitted = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return f'{self.title}'
    
    #This makes sure that a user will see their post after making it
    def get_absolute_url(self):
        return reverse('forums:post-detail', kwargs = {'pk' : self.pk})
    
#This handles the comments, which are directly associated with posts
class Comment(models.Model):
    #This is what attaches comments to the post
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    #This is used to track the user who posts the comment
    usercomment = models.ForeignKey(User, related_name= 'Comment', on_delete=models.DO_NOTHING)
    timesent = models.DateTimeField(default= timezone.now)


