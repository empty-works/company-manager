from django.test import TestCase
from CompanyManager.factories import UserFactory
from CompanyManager.forms import EmployeeForm

class EmployeeFormTest(TestCase):
    def self(request):
        self.user = UserFactory()
        self.client.login(username=self.user.email, password='pass')
