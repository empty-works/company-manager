from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError

def home(request):
    if request.method == "GET":
        return render(request, 'home/home.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password2'])
                user.save()
            except IntegrityError:
                return render(request, 'home/home.html', {'form': UserCreationForm(), 'error':'Usernames must be unique.'})
        else:
            return render(request, 'home/home.html', {'form': UserCreationForm(), 'error':'Passwords did not match'})
