from django.shortcuts import render
from .models import Employee

def employees(request):
    emps = Employee.objects.all()
    return render(request, 'employees/employees.html', {'emps': emps})
