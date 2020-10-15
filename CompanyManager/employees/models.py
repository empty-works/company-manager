from django.db import models
from django.contrib.auth.models import User

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
    dateCreated = models.DateTimeField(auto_now_add = True)
    dateHired = models.DateTimeField(null = True, blank = True)
    dateFired = models.DateTimeField(null = True, blank = True)
    wage = 
    employeeType = 
    address = models.CharField(max_length = 2000)
    email = models.EmailField(blank = True)
    picture = models.ImageField(upload_to = 'employees/images/', default = None)
    notes = models.TextField(blank = True)

    # So the actual name of the object appears when looking at the database in Django Admin for example
    def __str__(self):
        return self.lastName + ", " + self.firstName
