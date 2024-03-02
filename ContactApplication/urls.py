from django.urls import path
from . import views
from .views import mentorListView, repListView

app_name = 'ContactApplication'
urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('mentors', mentorListView.as_view(), name = 'mentors'),
    path('reps', repListView.as_view(), name = 'reps'),
]