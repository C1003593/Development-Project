from django.contrib import admin
from .models import StudentProfile, MentorProfile, StudentRepProfile, MentorRefNumberGen

admin.site.register(StudentProfile)
admin.site.register(MentorProfile)
admin.site.register(StudentRepProfile)
admin.site.register(MentorRefNumberGen)
# Register your models here.
