"""
URL configuration for DevelopmentProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from users import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ContactApplication.urls')),
    path('messaging/', include('messaging.urls')),

    path('register', user_views.register, name = 'register'),
    path('login', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),

    #Different profile creation pages
    path('studentprofilecreate', user_views.studentprofilecreate, name = 'studentprofilecreate'),
    path('mentorprofilecreate', user_views.mentorprofilecreate, name = 'mentorprofilecreate'),
    path('studentrepprofilecreate', user_views.studentrepprofilecreate, name = 'studentrepprofilecreate'),
    path('profileselector', views.profileselection, name = 'profileselector'),

    #Profile/update pages
    path('studentprofile', user_views.studentprofile, name = 'studentprofile'),
    path('mentorprofile', user_views.mentorprofile, name = 'mentorprofile'),
    path('studentrepprofile', user_views.studentrepprofile, name = 'studentrepprofile'),

    path('mentorrefgen', user_views.MentorNumGen, name = 'mentornumgen'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
