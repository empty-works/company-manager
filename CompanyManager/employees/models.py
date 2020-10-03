from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length = 1000)
    lastName = models.CharField(max_length = 1000)
    birthdate = models.DateField(blank = True)
    address = models.CharField(max_length = 2000)
    email = models.EmailField(blank = True)
    picture = models.ImageField(upload_to = 'employees/images/', default = None)
