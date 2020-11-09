from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .models import Experience
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

@login_required
def employees(request):
    emps = Employee.objects.all()
    return render(request, 'employees/employees.html', {'emps': emps})

@login_required
def addEmployee(request):
    if request.method == 'GET':
        return render(request, 'employees/addemployee.html', {'form': EmployeeForm()})
    else:
        # Essentially takes the form from GET and melds the fields into a POST thing. Awesome.
        try:
            # TODO include forms for Experience and Skills
            form = EmployeeForm(request.POST)
            form.save() 
            return render(request, 'employees/employees.html')
        except ValueError:
            return render(request, 'employees/addemployee.html', {'form': EmployeeForm(), 'error':'Bad data passed in. Try again.'})

@login_required
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

@login_required
def editEmployee(request, employees_pk):
    emp = get_object_or_404(Employee, pk = employees_pk)
    if request.method == 'GET':
        form = EmployeeForm(instance = emp) 
        return render(request, 'employees/editemployeedetail.html', {'emp':emp, 'form':form})
    else:
        try: 
            form = EmployeeForm(request.POST, instance = emp)
            form.save()
            return redirect('employees:employees')
        except ValueError:
            return render(request, 'employees/addemployee.html', {'form': EmployeeForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def deleteEmployee(request, employees_pk):
    emp = get_object_or_404(Employee, pk = employees_pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('employees:employees')

@login_required
def viewEmergencyContact(request, employees_pk):
    emp = get_object_or_404(Employee, pk = employees_pk)
    return render(request, 'employees/emp_emergency_contact.html', {'emp':emp})

@login_required
def viewAllExperience(request, employees_pk):
    pass

@login_required
def viewExperience(request, employees_pk):
    pass

@login_required
def editExperience(request, employees_pk):
    emp = get_object_or_404(Employee, pk = employees_pk)
    return render(request, 'employees/edit_experience.html', {'emp':emp})
    
@login_required
def viewAllSkills(request, employees_pk):
    pass

@login_required
def viewSkill(request, employees_pk):
    pass

@login_required
def editSkill(request, employees_pk):
    emp = get_object_or_404(Employee, pk = employees_pk)
    return render(request, 'employees/edit_skill.html', {'emp':emp})
    
