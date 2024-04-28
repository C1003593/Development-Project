from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class PostForm(forms.ModelForm):
    typeofpost = forms.ChoiceField(choices=[('Problem', 'Problem'), ('Discussion', 'Discussion')], label='The type of post you want to make.')
    title = forms.CharField(label='The title of your post.')
    description = forms.CharField(label='The content of your post', max_length=600)
    class Meta: 
        model = Post
        fields = ['typeofpost', 'title', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment here...', 'rows': 4}),
        }