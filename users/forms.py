from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, MentorProfile, StudentRepProfile, MentorRefNumberGen
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string

#User forms
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
        

#Profile update forms
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
    Description = forms.CharField()
    class Meta:
        model = MentorProfile
        fields = ['MentorRefNumber', 'AreaOfStudy', 'Description', 'DOB']

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


#Profile creation forms
class StudentProfileCreation(forms.ModelForm):
    StudentNumber = forms.CharField(label='Your university student number.')
    AreaOfStudy = forms.CharField(label='Your area of study.', help_text = 'Enter which area of study you are involved with.')
    DOB = forms.DateField(label='Your date of birth.', help_text = 'Enter in the format YYYY-MM-DD')
    class Meta:
        model = StudentProfile
        fields = ['StudentNumber', 'AreaOfStudy', 'DOB']


class MentorProfileCreation(forms.ModelForm):
    MentorRefNumber = forms.CharField(label='Your given mentor number.', help_text='You must request a number from an already approved mentor')
    AreaOfStudy = forms.CharField(label='Your area of study.', help_text='Enter which area of study you are involved with.')
    DOB = forms.DateField(label='Your date of birth.', help_text='Enter in the format YYYY-MM-DD')

    def clean_MentorRefNumber(self):
        mentor_ref_number = self.cleaned_data['MentorRefNumber']

        if not MentorRefNumberGen.objects.filter(MentorRefNumberRan=mentor_ref_number).exists():
            raise forms.ValidationError("Your mentor number must be unique. Please ensure you have entered the correct number.")
        return mentor_ref_number
    class Meta:
        model = MentorProfile
        fields = ['MentorRefNumber', 'AreaOfStudy', 'DOB']
    
class StudentRepProfileCreation(forms.ModelForm):
    StudentNumber = forms.CharField(label='Your university student number.')
    AreaOfStudy = forms.CharField(label='Your area of study.', help_text = 'Enter which area of study you are involved with.')
    DOB = forms.DateField(label='Your date of birth.', help_text = 'Enter in the format YYYY-MM-DD')
    Description = forms.CharField(label='Enter a description about what you will do as a mentor')
    class Meta:
        model = StudentRepProfile
        fields = ['StudentNumber', 'AreaOfStudy', 'Description', 'DOB']