from django.db import models
from django.contrib.auth.models import User

# Employee types list for the employeeType choice field.
EMP_TYPES = {
        ("1", "Potential"),
        ("2", "Hourly"),
        ("3", "Salaried"),
        ("4", "Manager"),
        ("5", "Executive"),
}

class Employee(models.Model):
    firstName = models.CharField(max_length = 1000)
    lastName = models.CharField(max_length = 1000)
    birthdate = models.DateField(blank = True)
    dateCreated = models.DateTimeField(auto_now_add = True, null = True) # Required so no blank=True
    dateHired = models.DateTimeField(null = True, blank = True)
    dateFired = models.DateTimeField(null = True, blank = True)
    wage = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True) 
    employeeType = models.CharField(
            max_length = 20,
            choices = EMP_TYPES,
            default = '1'
            )
    address = models.CharField(max_length = 2000)
    email = models.EmailField(blank = True)
    picture = models.ImageField(upload_to = 'employees/images/', default = None)
    notes = models.TextField(blank = True)

    # So the actual name of the object appears when looking at the database in Django Admin for example
    def __str__(self):
        return self.lastName + ", " + self.firstName
