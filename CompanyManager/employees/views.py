from django.contrib import messages
from django.db import IntegrityError, transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from .models import Employee
from .forms import EmployeeForm
from .models import Experience
from .forms import ExperienceForm
from .models import Skill
from .forms import SkillForm
from .models import Assignment
from .forms import AssignmentForm
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def employees(request):
    emps = Employee.objects.all()
    return render(request, 'employees/employees.html', {'emps': emps})

@login_required
def addEmployee(request):
    ExpFormSet = formset_factory(ExperienceForm, extra=1)
    SkillFormSet = formset_factory(SkillForm, extra=1)
    if request.method == 'GET':
        employee_form = EmployeeForm()
        exp_formset = ExpFormSet()
        skill_formset = SkillFormSet()
        context = {'employee_form':employee_form,
                   'exp_formset':exp_formset,
                   'skill_formset':skill_formset}
        return render(request, 'employees/addemployee.html', context)

    if request.method == 'POST':
        # Essentially takes the form from GET and melds the fields into a POST thing. Awesome.
        try:
            employee_form = EmployeeForm(request.POST)
            exp_formset_post = ExpFormSet(request.POST)
            skill_formset_post = SkillFormSet(request.POST)

            if employee_form.is_valid() and exp_formset_post.is_valid() and skill_formset_post.is_valid():
                #employee = employee_form.save(commit = False)
                #employee.recorded_by(request.user)
                emp = employee_form.save()

                saveExperience(exp_formset_post, emp, request)
                saveSkill(skill_formset_post, emp, request)

            # Redirect is the action in the form in the addemployee template.
            context = {'employee_form': employee_form, 'exp_formset': exp_formset_post}
            return render(request, 'employees/addemployeesuccess.html', context)
        except ValueError:
            return render(request, 'employees/addemployee.html',
                          {'employee_form': EmployeeForm(),
                           'error':'Bad data passed in. Try again.'})

#Helper function for addEmployee
def saveExperience(exp_formset_post, emp, request):
    new_exp = [] #Save the data for each form in the formset.

    for exp in exp_formset_post:
        from_date = exp.cleaned_data.get('from_date')
        to_date = exp.cleaned_data.get('to_date')
        text = exp.cleaned_data.get('text')

        if from_date and to_date and text:
            new_exp.append(Experience(from_date=from_date,
                                      to_date=to_date, text=text,
                                      employee=emp))

    saveFormset(new_exp, request, Experience)

# Helper function for addEmployee
def saveSkill(skill_formset_post, emp, request):
    new_skill = [] # Save the data for each form in the formset

    for skill in skill_formset_post:
        name = skill.cleaned_data.get('name')
        rank = skill.cleaned_data.get('rank')

        if name and rank:
            new_skill.append(Skill(name=name, rank=rank, employee=emp))

    saveFormset(new_skill, request, Skill)

# Helper function for addEmployee
def saveAssignment(assignment_formset_post, emp, request):
    new_assignment = [] # Save the data for each form in the formset

    for assignment in assignment_formset_post:
        title = assignment.cleaned_data.get('title')
        description = assignment.cleaned_data.get('description')

        if title and description:
            new_assignment.append(Assignment(title=title, description=description, employee=emp))

    saveFormset(new_assignment, request, Assignment)

# Helper function for the saveExperience and saveSkill functions.
def saveFormset(form_list, request, model):

    try:
        with transaction.atomic():
            #Replace old entries with the new ones
            #Experience.objects.filter(user=user).delete()
            model.objects.bulk_create(form_list)

            #Notify users that it worked
            messages.success(request, 'Experience has been updated.')
    except IntegrityError: #transaction failed
        messages.error(request, 'There was an error updating experience.')
        return redirect('employees:employees')

@login_required
def showSuccessAdd(request):
    return render(request, 'employees/addemployeesuccess.html')

@login_required
def viewEmployee(request, employees_pk):
    emp = get_object_or_404(Employee, pk=employees_pk)
    exp_list = emp.experience_set.all()
    skill_list = emp.skill_set.all()
    if request.method == 'GET':
        emp_form = EmployeeForm(instance=emp)
        return render(request, 'employees/employeedetail.html',
                      {'emp':emp, 'exp_list':exp_list, 'skill_list':skill_list})

    try:
        emp_form = EmployeeForm(request.POST, instance=emp)
        emp_form.save()
        return redirect('employees:employees')
    except ValueError:
        return render(request, 'employees/addemployee.html',
                      {'form': EmployeeForm(), 'error':'Bad data passed in. Try again.'})

@login_required
#DON'T USE THIS VIEW. MAKE IT SO INDIVIDUAL ELEMENTS LIKE IMAGE OR PERSONAL SECTIONS ARE DIRECTLY LINKED
def editEmployee(request, employees_pk):
    emp = get_object_or_404(Employee, pk=employees_pk)
    if request.method == 'GET':
        form = EmployeeForm(instance=emp)
        return render(request,
                      'employees/edit_sections/editemployeebase.html',
                      {'emp':emp, 'form':form})
    try:
        form = EmployeeForm(request.POST, instance=emp)
        form.save()
        return redirect('employees:employees')
    except ValueError:
        return render(request, 'employees/addemployee.html',
                      {'form': EmployeeForm(),
                       'error':'Bad data passed in. Try again.'})

@login_required
def deleteEmployee(request, employees_pk):
    emp = get_object_or_404(Employee, pk=employees_pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('employees:employees')

@login_required
def viewEmergencyContact(request, employees_pk):
    emp = get_object_or_404(Employee, pk=employees_pk)
    return render(request, 'employees/emp_emergency_contact.html', {'emp':emp})
