from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory
from .models import Employee
from .models import Experience 
from .models import Skill

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['firstName', 
                'lastName', 
                'position',
                'birthDate', 
                'dateHired', 
                'dateFired', 
                'wage', 
                'emergencyContact',
                'employeeType', 
                'address', 
                'email', 
                'picture', 
                'cur_assignment']
        widgets = {
                'birthDate': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'dateHired': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'dateFired': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['dateHired'].required = False
        self.fields['dateFired'].required = False
        self.fields['picture'].required = False
        self.fields['cur_assignment'].required = False

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name',
                  'rank',]

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['from_date',
                  'to_date', 
                  'text',]
        # Using widgets to specify date type in the form fixed issue where it 
        # only showed up as a text field.
        widgets = {
                'from_date':forms.DateInput(attrs={'type':'date'}),
                'to_date':forms.DateInput(attrs={'type':'date'}),
                }
