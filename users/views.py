from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, StudentProfileUpdateForm


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
def studentprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        sp_form = StudentProfileUpdateForm(request.POST, request.FILES, instance = request.user.studentprofile)
        if u_form.is_valid and sp_form.is_valid:
            u_form.save()
            sp_form.save()
            messages.success(request, 'Your account has been successfully updated')
        return redirect('studentprofile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        sp_form = StudentProfileUpdateForm(instance = request.user.studentprofile)
    context = {'u_form': u_form, 'sp_form': sp_form, 'title': 'Student Profile'}
    return render(request, 'users/studentprofile.html', context)


# Create your views here.
