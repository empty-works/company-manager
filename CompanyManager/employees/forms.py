from django.forms import ModelForm
from django import forms
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['firstName', 
                'lastName', 
                'birthdate', 
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
                'birthdate': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'dateHired': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'dateFired': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['dateHired'].required = False
        self.fields['dateFired'].required = False
        self.fields['picture'].required = False
        self.fields['cur_assignment'].required = False
