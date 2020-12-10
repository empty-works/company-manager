from django.core.urlresolvers import reverse
from django.test import TestCase
from employees.factories import UserFactory
from employees.models import Employee, Experience 
import datetime

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
                       'wage': 1000000,
                       'employeeType': 'Salaried',
                       'address': '1100 Hobart Ave. Culvert City, CA',
                       'email': 'hello_there@123.com',
                       'form-TOTAL_FORMS': 1,
                       'form-INITIAL_FORMS': 0,
                       'form-0-from_date': datetime.datetime(2008, 11, 28),
                       'form-0-to_date': datetime.datetime(2012, 12, 11),
                       'form-0-text': 'Some text.',
                    },
                )

        employee = Employee.objects.get(id=user.id)
        experience = Experience.objects.get(employee=employee)

        self.assertEqual(employee.firstName, 'New First Name')
        self.assertEqual(employee.lastName, 'New Last Name')
        self.assertEqual(employee.position, 'Lead programmer') 
        self.assertEqual(employee.wage, 1000000)
        self.assertEqual(employee.employeeType, 'Salaried')
        self.assertEqual(employee.address, '1100 Hobart Ave. Culvert City, CA')
        self.assertEqual(employee.email, 'hello_there@123.com')
        self.assertEqual(experience.from_date, datetime.datetime(2008, 11, 28))
        self.assertEqual(experience.to_date, datetime.datetime(2012, 12, 11))
        self.assertEqual(experience.text, 'Some text.')
