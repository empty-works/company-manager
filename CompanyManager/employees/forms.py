from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['firstName', 'lastName', 'birthDate', 'dateHired', 'dateFired', 'wage', 'employeeType', 'address', 'email', 'picture', 'notes']
