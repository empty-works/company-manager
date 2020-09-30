from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all();
    return render(request, 'main_app/index.html', {'employees': employees})

def help(request):
    return render(request, 'main_app/help.html')

def about(request):
    return render(request, 'main_app/about.html')
