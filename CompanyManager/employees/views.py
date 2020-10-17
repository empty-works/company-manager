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
        # Essentially takes the form from GET and melds the fields into a POST thing. Awesome.
        form = EmployeeForm(request.POST)
        form.save() 
        #newEmployee = form.save(commit = False)
        # Does not allow current user to make changes for other users. However, this is not really 
        # necessary for this app because all users are "super-users" anyway.
        #newEmployee.user = request.user
        #newEmployee.save()
        return render(request, 'employees/employees.html')
