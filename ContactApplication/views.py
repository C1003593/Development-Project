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
    ordering = ['AreaOfStudy']
    paginate_by = 6
    
def studentreps(request):
     
     rep_list = {'studentreps': StudentRepProfile.objects.all(), 'title': 'These are the student reps working with us'}
     return render(request, 'ContactApplication/reps.html', {'studentrepprofiles': rep_list})

class repListView(ListView):
     model = StudentRepProfile
     template_name = 'ContactApplication/reps.html'
     context_object_name = 'studentrepprofiles'
     ordering = ['AreaOfStudy']
     paginate_by = 6