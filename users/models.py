from django.db import models
from django.contrib.auth.models import User



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
    MentorRefNumberRan = models.CharField(max_length=33, primary_key= 'MentorRefNumberRan')
    def __str__(self):
        return f'{self.MentorRefNumberRan}'
    
class MentorProfile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    MentorRefNumber = models.OneToOneField(MentorRefNumberGen, blank = False, max_length=33, on_delete = models.DO_NOTHING)
    AreaOfStudy = models.CharField(max_length=20, null = True)
    DOB = models.DateField(null = True)
    Image = models.ImageField(default = 'defaultpi.png', upload_to = 'mentor_pics')

    def __str__(self):
        return f'{self.user}'

    
# as_crispy_field to render individual fields
