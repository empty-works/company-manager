from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def employees(request):
    emps = Employee.objects.all()
    return render(request, 'employees/employees.html', {'emps': emps})

def about(request):
    return render(request, 'employees/about.html')
