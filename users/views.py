from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, StudentProfileUpdateForm, MentorProfileUpdateForm, StudentRepProfileUpdateForm, MentorRefNumGenForm
from .forms import StudentProfileCreation, MentorProfileCreation, StudentRepProfileCreation
from django.utils.crypto import get_random_string
from django.contrib import messages

#This is for when the user needs to decide which profile they would like
def profileselection(request):
    return render(request, 'users/profileselection.html', {'title':'Please select profile type'})

#Registration views
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account!')
        return redirect('ContactApplication:home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form , 'title': 'Registration form'})

@login_required
def studentprofilecreate(request):
    if request.method == 'POST':
        #This uses the StudentProfileCreation form from forms.py
        s_form = StudentProfileCreation(request.POST)
        if s_form.is_valid():
            student_profile = s_form.save(commit=False)
            student_profile.user = request.user
            student_profile.save()
            messages.success(request, f'Your student profile has been created')
            return redirect('studentprofile')
        else:
            messages.warning(request, 'Please correct the errors below.')
        return render(request, 'users/studentregister.html', {'s_form': s_form , 'title': 'Student registration form'})
    #This ensures that the page is rendered before the user enters anything
    else:
        s_form = StudentProfileCreation()
        return render(request, 'users/studentregister.html', {'s_form': s_form , 'title': 'Student registration form'})
    
@login_required
def studentrepprofilecreate(request):
    if request.method == 'POST':
        sr_form = StudentRepProfileCreation(request.POST)
        if sr_form.is_valid():
            studentrep_profile = sr_form.save(commit=False)
            studentrep_profile.user = request.user
            studentrep_profile.save()
            messages.success(request, f'Your student rep profile has been created')
            return redirect('studentrepprofile')
        else:
            messages.warning(request, 'Please correct the errors below.')
        return render(request, 'users/studentrepregister.html', {'sr_form': sr_form , 'title': 'Student rep registration form'})
    else:
        sr_form = StudentRepProfileCreation()
        return render(request, 'users/studentrepregister.html', {'sr_form': sr_form , 'title': 'Student rep registration form'})
        

@login_required
def mentorprofilecreate(request):
    if request.method == 'POST':
        m_form = MentorProfileCreation(request.POST)
        if m_form.is_valid():
            mentor_profile = m_form.save(commit=False)
            mentor_profile.user = request.user
            mentor_profile.save()
            messages.success(request, f'Your mentor profile has been created')
            return redirect('mentorprofile')
        else:
            messages.warning(request, 'Please correct the errors below.')
        return render(request, 'users/mentorregister.html', {'m_form': m_form , 'title': 'Mentor registration form'})
    else:
        m_form = MentorProfileCreation()
        return render(request, 'users/mentorregister.html', {'m_form': m_form , 'title': 'Mentor registration form'})



#Update views
@login_required
def studentprofile(request):
    if request.method == 'POST':
        #This checks for both the user account and student account before allowing the user to update
        u_form = UserUpdateForm(request.POST, instance = request.user)
        sp_form = StudentProfileUpdateForm(request.POST, request.FILES, instance = request.user.studentprofile)
        if u_form.is_valid() and sp_form.is_valid():
            u_form.save()
            sp_form.save()
            messages.success(request, 'Your student profile has been successfully updated')
            return redirect('studentprofile')      
        else:
            messages.warning(request, 'Unable to update student profile!')
            context = {'u_form': u_form, 'sp_form': sp_form, 'title': 'Student Profile'}
            return render(request, 'users/studentprofile.html', context)
    else:
        u_form = UserUpdateForm(instance = request.user)
        sp_form = StudentProfileUpdateForm(instance = request.user.studentprofile)
        context = {'u_form': u_form, 'sp_form': sp_form, 'title': 'Student Profile'}
        return render(request, 'users/studentprofile.html', context)
    
@login_required
def mentorprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        mp_form = MentorProfileUpdateForm(request.POST, request.FILES, instance = request.user.mentorprofile)
        if u_form.is_valid() and mp_form.is_valid():
            u_form.save()
            mp_form.save()
            messages.success(request, 'Your mentor profile has been successfully updated')
            return redirect('mentorprofile')      
        else:
            messages.warning(request, 'Unable to update mentor profile!')
            context = {'u_form': u_form, 'mp_form': mp_form, 'title': 'Mentor Profile'}
            return render(request, 'users/mentorprofile.html', context)
    else:
        u_form = UserUpdateForm(instance = request.user)
        mp_form = MentorProfileUpdateForm(instance = request.user.mentorprofile)
        context = {'u_form': u_form, 'mp_form': mp_form, 'title': 'Mentor Profile'}
        return render(request, 'users/mentorprofile.html', context)

@login_required
def studentrepprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        srp_form = StudentRepProfileUpdateForm(request.POST, request.FILES, instance = request.user.studentrepprofile)
        if u_form.is_valid() and srp_form.is_valid():
            u_form.save()
            srp_form.save()
            messages.success(request, 'Your student rep profile has been successfully updated')
            return redirect('studentrepprofile')      
        else:
            messages.warning(request, 'Unable to update student rep profile!')
            context = {'u_form': u_form, 'srp_form': srp_form, 'title': 'Student Rep Profile'}
            return render(request, 'users/studentrepprofile.html', context)
    else:
        u_form = UserUpdateForm(instance = request.user)
        srp_form = StudentRepProfileUpdateForm(instance = request.user.studentrepprofile)
        context = {'u_form': u_form, 'srp_form': srp_form, 'title': 'Student Rep Profile'}
        return render(request, 'users/studentrepprofile.html', context)
    
@login_required
def MentorNumGen(request):
    if request.method == 'POST':
        MNG_form = MentorRefNumGenForm(request.POST)
        if MNG_form.is_valid():
            MNG_form.save()
            messages.success(request, 'You have generated a Mentor Reference Number')
            return redirect('ContactApplication:home')      
        else:
            messages.warning(request, 'Unable to generate Mentor Reference Number!')
            context = {'MNG_form': MNG_form, 'title': 'Mentor Ref Gen'}
            return render(request, 'users/mentorrefnum.html', context)
    else:
        MNG_form = MentorRefNumGenForm()
        #This renders a 32 digit random string in the form where a mentor would get a reference number
        MNG_form.fields['MentorRefNumberRan'].initial = get_random_string(length=32)
        context = {'MNG_form': MNG_form, 'title': 'Mentor Ref Gen'}
        return render(request, 'users/mentorrefnum.html', context)