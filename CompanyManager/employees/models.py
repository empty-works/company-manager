from django.db import models
from django.contrib.auth.models import User

# Employee types list for the employeeType choice field.
EMP_TYPES = {
    ("potential", "Potential"),
    ("hourly", "Hourly"),
    ("salaried", "Salaried"),
    ("manager", "Manager"),
    ("executive", "Executive"),
}

STATUS_TYPES = {
    ("active", "Active"),
    ("hiatus", "Hiatus"),
    ("former", "Former"),
}

class Employee(models.Model):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    birthdate = models.DateField(blank = True)
    dateCreated = models.DateTimeField(auto_now_add = True, null = True) # Required so no blank=True
    dateHired = models.DateTimeField(null = True, blank = True)
    dateFired = models.DateTimeField(null = True, blank = True)
    wage = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True) 
    #TODO phone = models.
    employeeType = models.CharField(
            max_length = 20,
            choices = EMP_TYPES,
            default = 'potential'
            )
    address = models.CharField(max_length = 1000)
    email = models.EmailField(blank = True)
    picture = models.ImageField(upload_to = 'employees/images/', default = None)
    cur_assignment = models.TextField(blank = True)

    # So the actual name of the object appears when looking at the database in Django Admin for example
    def __str__(self):
        return self.lastName + ", " + self.firstName
