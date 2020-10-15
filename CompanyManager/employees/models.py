from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    firstName = models.CharField(max_length = 1000)
    lastName = models.CharField(max_length = 1000)
    birthdate = models.DateField(blank = True)
    dateHired = models.DateTimeField(null = True, blank = True)
    dateFired = models.DateTimeField(null = True, blank = True)
    address = models.CharField(max_length = 2000)
    email = models.EmailField(blank = True)
    picture = models.ImageField(upload_to = 'employees/images/', default = None)
    notes = models.TextField(blank = True)

    def __str__(self):
        return self.lastName + ", " + self.firstName
