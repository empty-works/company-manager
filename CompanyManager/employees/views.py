from django.shortcuts import render
from .models import Employee

def employees(request):
    emps = Employee.objects.all()
    return render(request, 'employees/employees.html', {'emps': emps})

def addEmployee(request):
    if request.method == 'GET':
        return render(request, 'home/addemployee.html', {'form': AuthenticationForm()})
    else:
        pass
