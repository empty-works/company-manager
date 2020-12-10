from django.core.urlresolvers import reverse
from django.test import TestCase
from employees.factories import UserFactory
from employees.models import Employee, Experience 

class AddEmployeeTest(TestCase):
    def test_can_update_employee(self):
        user = UserFactory()
        self.client.login(username=user.email, password='pass')
        response = self.client.post(
                reverse('employees:addEmployee'),
                data = {
                       'firstName': 'New First Name',
                       'lastName': 'New Last Name',
                       'position': 'Lead Programmer'
                       'wage': '1000000',
                       'employeeType': 'Salaried',
                       'address': '1100 Hobart Ave. Culvert City, CA',
                       'email': 'hello_there@123.com',
                    },
                )

        employee = Employee.objects.get(id=user.id)
        experience = Experience.objects.get(employee=employee)

        self.assertEqual(employee.firstName, 'New First Name')
        self.assertEqual(employee.lastName, 'New Last Name')
         
