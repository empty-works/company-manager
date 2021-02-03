from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
    if request.user.is_authenticated:
        return redirect('overview:overview')
    return render(request, 'home/home.html')

def signupuser(request):
    if request.method == "GET":
        return render(request, 'home/signupuser.html', {'form': UserCreationForm()})
    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(request.POST['username'],
                                            password=request.POST['password2'])
            user.save()
            login(request, user)
            return redirect('employees:employees')
        except IntegrityError:
            return render(request, 'home/signupuser.html',
                          {'form': UserCreationForm(), 'error':'Usernames must be unique.'})
    else:
        return render(request, 'home/signupuser.html',
                      {'form': UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == "GET":
        return render(request, 'home/loginuser.html', {'form': AuthenticationForm()})
    user = authenticate(request,
                        username=request.POST['username'], 
                        password=request.POST['password'])
    if user is None:
        return render(request,
                      'home/loginuser.html',
                      {'form': AuthenticationForm(),
                             'error':'Username and/or password are not valid'})
    login(request, user)
    return redirect('employees:employees')
     
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home:home')
