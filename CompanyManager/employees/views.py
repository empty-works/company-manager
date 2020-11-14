from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from .models import Employee
from .models import Experience
from .forms import EmployeeForm
from .forms import SkillForm
from django.contrib.auth.decorators import login_required

@login_required
def employees(request):
    emps = Employee.objects.all()
    return render(request, 'employees/employees.html', {'emps': emps})

@login_required
def addEmployee(request):
    if request.method == 'GET':
        employee_form = EmployeeForm()
        skill_form = SkillForm()
        context = {'employee_form':employee_form, 'skill_form':skill_form}
        return render(request, 'employees/addemployee.html', context)
    else:
        # Essentially takes the form from GET and melds the fields into a POST thing. Awesome.
        try:
            employee_form = forms.EmployeeForm(request.POST)
            skill_form = forms.SkillForm(request.POST)
            if employee_form.is_valid and exp_form.is_valid and skill_form.is_valid:
                employee = employee_form.save(commit = False) 
                employee.recorded_by(request.user)
                #employee_form.save() 

                skill = skill_form.save(False)
                skill.employee = employee
                skill_form.save()

            return render(request, 'employees/employees.html')
        except ValueError:
            return render(request, 'employees/addemployee.html', {'employee_form': EmployeeForm(), 'error':'Bad data passed in. Try again.'})

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
def addExperienceForm(request):
    ExpFormSet = modelformset_factory(Experience, fields = ('from_date', 'to_date', 'text'))
    if request.method == 'GET':
        # Don't display already saved model instance
        formset = ExpFormSet()
    elif request.method == 'POST':
        formset = ExpFormSet(request.POST, request.FILES)
        if formset.is_valid():
            form.save()
    return render(request, 'employees/addexperience.html', {'formset': formset})

@login_required
def editExperience(request, employees_pk):
    emp = get_object_or_404(Employee, pk = employees_pk)
    return render(request, 'employees/editexperience.html', {'emp':emp})
    
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
    
