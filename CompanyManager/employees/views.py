from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

def employees(request):
    emps = Employee.objects.all()
    return render(request, 'employees/employees.html', {'emps': emps})

def addEmployee(request):
    if request.method == 'GET':
        return render(request, 'employees/addemployee.html', {'form': EmployeeForm()})
    else:
        pass
