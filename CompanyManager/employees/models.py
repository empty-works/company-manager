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

SKILL_RANKS = {
    ("novice", "Novice"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced"),
    ("expert", "Expert"),
}

class Employee(models.Model):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200, blank = True)
    birthDate = models.DateField(blank = True)
    dateCreated = models.DateTimeField(auto_now_add = True, null = True) # Required so no blank=True
    dateHired = models.DateTimeField(null = True, blank = True)
    dateFired = models.DateTimeField(null = True, blank = True)
    wage = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True) 
    emergencyContact = models.CharField(max_length = 400, blank = True)
    #TODO phone = models.
    employeeType = models.CharField(
            max_length = 20,
            choices = EMP_TYPES,
            default = 'potential',
            )
    address = models.CharField(max_length = 1000)
    email = models.EmailField(blank = True)
    picture = models.ImageField(upload_to = 'employees/images/', default = 'employees/images/240x240_default_img.jpg', blank = True)
    cur_assignment = models.TextField(blank = True)
    recorded_by = models.ForeignKey(User, default= None, null=True, on_delete=models.CASCADE)
    
    # So the actual name of the object appears when looking at the database in Django Admin for example
    def __str__(self):
        return self.lastName + ", " + self.firstName

# TODO MAKE EMPLOYEE AN ABSTRACT CLASS AND EMPLOYEE TYPES AS SUBCLASSES

class Experience(models.Model):
    employee = models.ForeignKey(
            Employee,
            on_delete = models.CASCADE,
            null = True,
            )
    from_date = models.DateField(null = True)
    to_date = models.DateField(null = True)
    text = models.TextField(default = "INSIDE EXPERIENCE TEXT", blank = True)

class Skill(models.Model):
    employee = models.ForeignKey(
            Employee,
            on_delete = models.CASCADE,
            null = True,
            ) 
    name = models.CharField(max_length = 200, blank = True)
    rank = models.CharField(
            max_length = 50,
            choices = SKILL_RANKS,
            default = 'novice',
            ) 

