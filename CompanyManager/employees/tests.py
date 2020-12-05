from django.test import TestCase
from CompanyManager.factories import UserFactory
from CompanyManager.forms import EmployeeForm

class EmployeeFormTest(TestCase):
    def setup(self):
        self.user = UserFactory()
        self.client.login(username=self.user.email, password='pass')

    def form_data(self, first, last, position, dateHired, wage, employeeType, address, email):
        return EmployeeForm(
                user = self.user,
                data = {
                    'first_name':first,
                    'last_name':last,
                    'position':position,
                    'date_hired':dateHired,
                    'wage':wage,
                    'employee_type':employeeType,
                    'address':address,
                    'email':email,
                    }
                ) 

