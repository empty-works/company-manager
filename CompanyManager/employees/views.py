from django.shortcuts import render, get_object_or_404, redirect
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
        try:
            form = EmployeeForm(request.POST)
            form.save() 
            return render(request, 'employees/employees.html')
        except ValueError:
            return render(request, 'employees/addemployee.html', {'form': EmployeeForm(), 'error':'Bad data passed in. Try again.'})

def viewEmployee(request, employees_pk):
    emp = get_object_or_404(Employee, pk = employees_pk)
    if request.method == 'GET':
        form = EmployeeForm(instance = emp) 
        return render(request, 'employees/employeedetail.html', {'emp':emp, 'form':form})
    else:
        try: 
            form = EmployeeForm(request.POST, instance = emp)
            form.save()
            return redirect('employees:employees')
        except ValueError:
            return render(request, 'employees/addemployee.html', {'form': EmployeeForm(), 'error':'Bad data passed in. Try again.'})

def deleteEmployee(request, employees_pk):
    emp = get_object_or_404(Employee, pk = employees_pk, user = request.user)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance = emp)
        form.delete()
        return redirect('employees:employees')
