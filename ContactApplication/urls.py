from django.urls import path
from . import views

app_name = 'ContactApplication'
urlpatterns = [
    path('', views.home, name = 'home'),
    
]