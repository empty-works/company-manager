from django.test import TestCase
from CompanyManager.factories import UserFactory
from CompanyManager.forms import EmployeeForm

class EmployeeFormTest(TestCase):
    def setup(self):
        self.user = UserFactory()
        self.client.login(username=self.user.email, password='pass')

    def form_data(self, first, last, position, wage, employeeType, address, email):
        return EmployeeForm(
                user = self.user,
                data = {
                    'first_name':first,
                    'last_name':last,
                    'position':position,
                    'wage':wage,
                    'employee_type':employeeType,
                    'address':address,
                    'email':email,
                }
        ) 
    
    def test_valid_data(self):
        form = self.form_data('First', 'Last', 'Position', 'Wage', 'EmployeeType', 'Address', 'Email')
        self.assertTrue(form.is_valid())

    def test_missing_first_name(self):
        form = self.form_data('', 'Last', 'Position', 'Wage', 'EmployeeType', 'Address', 'Email')
        errors = form['first_name'].errors.as_data()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')

    def test_missing_last_name(self):
        form = self.form_data('First', '', 'Position', 'Wage', 'EmployeeType', 'Address', 'Email')
        errors = form['last_name'].errors.as_data()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')

    def test_missing_position(self):
        form = self.form_data('First', 'Last', '', 'Wage', 'EmployeeType', 'Address', 'Email')
        errors = form['position'].errors.as_data()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')

    def test_missing_wage(self):
        form = self.form_data('First', 'Last', 'Position', '', 'EmployeeType', 'Address', 'Email')
        errors = form['wage'].errors.as_data()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')

    def test_missing_employee_type(self):
        form = self.form_data('First', 'Last', 'Position', 'Wage', '', 'Address', 'Email')
        errors = form['employee_type'].errors.as_data()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')

    def test_missing_address(self):
        form = self.form_data('First', 'Last', 'Position', 'Wage', 'EmployeeType', '', 'Email')
        errors = form['address'].errors.as_data()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')

    def test_missing_email(self):
        form = self.form_data('First', 'Last', 'Position', 'Wage', 'EmployeeType', 'Address', '')
        errors = form['email'].errors.as_data()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')
