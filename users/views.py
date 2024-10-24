from django.shortcuts import render, redirect
from django.contrib.auth import (
    logout, 
    login,
)
from .forms import UserForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm

#! email ile giriş yapabilmek için;
from .forms import EmailAuthenticationForm


# Create your views here.
def user_logout(request):
    logout(request)
    return redirect('weatherapp:home')


def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user=user
            profile.save()
            
            login(request, user)
            return redirect('weatherapp:home')
    
    context = {
        'form_user': form_user,
        'form_profile': form_profile
    }
    
    return render(request, 'users/register.html', context)

## username ve password ile giriş yapabilmek için;
# def user_login(request):
#     form = AuthenticationForm(request, data=request.POST)
#     if form.is_valid():
#       user = form.get_user()
#       login(request, user)
#       return redirect('weatherapp:home')
#     return render(request, 'users/login.html', {'form' : form})


#! email ile giriş yapabilmek için;
def user_login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('weatherapp:home')
    else:
        form = EmailAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})