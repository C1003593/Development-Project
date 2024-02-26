from django.shortcuts import render
from users.models import MentorProfile, StudentRepProfile
from django.views.generic import ListView

def home(request):
    return render(request, 'ContactApplication/home.html', {'title':'Welcome'})

def mentors(request):

        mentor_list = {'mentors': MentorProfile.objects.all(), 'title': 'Here are our mentors'}
        return render(request, 'ContactApplication/mentors.html', {'mentorprofiles': mentor_list})

class mentorListView(ListView):
    model = MentorProfile
    template_name = 'ContactApplication/mentors.html'
    context_object_name = 'mentorprofiles'
    ordering = ['user']
    paginate_by = 5
    
