from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class StudentProfile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    StudentNumber = models.CharField(max_length=15, primary_key= 'StudentNumber')
    AreaOfStudy = models.CharField(max_length=20, null = True)
    DOB = models.DateField(null = True)
    
    def __str__(self):
        return f'{self.StudentNumber}'
    
class StudentRepProfile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    StudentNumber = models.CharField(max_length=15, primary_key= 'StudentNumber')
    AreaOfStudy = models.CharField(max_length=20, null = True)
    DOB = models.DateField(null = True)
    def __str__(self):
        return f'{self.StudentNumber}'
    
class MentorRefNumberGen(models.Model):
    MentorRefNumberRan = models.CharField(default=get_random_string(length=32), max_length=33)
    def __str__(self):
        return f'{self.MentorRefNumberRan}'
    
class MentorProfile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    MentorRefNumber = models.OneToOneField(MentorRefNumberGen, unique = True, blank = False, max_length=33, on_delete = models.DO_NOTHING)
    AreaOfStudy = models.CharField(max_length=20, null = True)
    DOB = models.DateField(null = True)

    def __str__(self):
        return f'{self.MentorRefNumber}'

    
# as_crispy_field to render individual fields
