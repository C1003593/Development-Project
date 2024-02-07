from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, MentorProfile, StudentRepProfile, MentorRefNumberGen
from django.utils.crypto import get_random_string


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address', help_text='Your university email address')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        

class StudentProfileUpdateForm(forms.ModelForm):
    StudentNumber = forms.CharField(label='Your university student number.')
    AreaOfStudy = forms.CharField(label='Your area of study.', help_text = 'Enter which area of study you are involved with.')
    DOB = forms.DateField(label='Your date of birth.', help_text = 'Enter in the format YYYY-MM-DD')
    class Meta:
        model = StudentProfile
        fields = ['StudentNumber', 'AreaOfStudy', 'DOB']

class MentorProfileUpdateForm(forms.ModelForm):
    MentorRefNumber = forms.CharField()
    AreaOfStudy = forms.CharField(label='Your area of study.', help_text = 'Enter which area of study you are involved with.')
    DOB = forms.DateField(label='Your date of birth.', help_text = 'Enter in the format YYYY-MM-DD')
    class Meta:
        model = MentorProfile
        fields = ['MentorRefNumber', 'AreaOfStudy', 'DOB']

class StudentRepProfileUpdateForm(forms.ModelForm):
    StudentNumber = forms.CharField(label='Your university student number.')
    AreaOfStudy = forms.CharField(label='Your area of study.', help_text = 'Enter which area of study you are involved with.')
    DOB = forms.DateField(label='Your date of birth.', help_text = 'Enter in the format YYYY-MM-DD')
    class Meta:
        model = StudentRepProfile
        fields = ['StudentNumber', 'AreaOfStudy', 'DOB']

class MentorRefNumGenForm(forms.ModelForm):
    MentorRefNumberRan = forms.CharField(label='Mentor reference number.', help_text = 'Make sure to copy this number before pressing confirm. <br> Give this code to someone who is qualified to be a mentor and click confirm below.')
    class Meta:
        model = MentorRefNumberGen
        fields = ['MentorRefNumberRan']

    



    