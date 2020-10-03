from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def index(request):
    emps = Employee.objects.all()
    return render(request, 'main_app/index.html', {'emps': emps})

def about(request):
    return render(request, 'main_app/about.html')
