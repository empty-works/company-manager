from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def index(request):
    emps = Employee.objects.all()
    return render(request, 'employees/index.html', {'emps': emps})

def about(request):
    return render(request, 'employees/about.html')
