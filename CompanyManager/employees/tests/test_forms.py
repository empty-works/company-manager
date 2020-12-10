from django.test import TestCase
from employees.factories import UserFactory
from django.core.urlresolvers import reverse
from employees.forms import EmployeeForm
import datetime

# Test basic add employee form
class EmployeeFormTest(TestCase):
    def setup(self):
        self.user = UserFactory()
        self.client.login(username=self.user.email, password='pass')

    def form_data(self, first, last, position, wage, employeeType, address, email):
        return EmployeeForm(
                user = self.user,
                data = {
                    'firstName':first,
                    'lastName':last,
                    'position':position,
                    'wage':wage,
                    'employeeType':employeeType,
                    'address':address,
                    'email':email,
                }
        ) 
    
    def test_valid_data(self):
        form = self.form_data('First', 'Last', 'Position', 'Wage', 'EmployeeType', 'Address', 'Email')
        self.assertTrue(form.is_valid())

    def test_missing_first_name(self):
        form = self.form_data('', 'Last', 'Position', 'Wage', 'EmployeeType', 'Address', 'Email')
        errors = form['firstName'].errors.as_data()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')

    def test_missing_last_name(self):
        form = self.form_data('First', '', 'Position', 'Wage', 'EmployeeType', 'Address', 'Email')
        errors = form['lastName'].errors.as_data()
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
        errors = form['employeeType'].errors.as_data()
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

# Test add employee formset for adding experience
class ExperienceFormsetTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.login(username=self.user.email, password='pass')

    def form_data(self, fromDate, toDate, text):
        return EmployeeForm(
            user=self.user,
            data={
                'firstName': 'First',
                'lastName': 'Last',
                'position': 'Position',
                'wage': 'Wage',
                'employeeType': 'EmployeeType',
                'address': 'Address',
                'email': 'Email',
                'form-TOTAL_FORMS': 1,
                'form-INITIAL_FORMS': 0,
                'form-0-from_date': fromDate,
                'form-0-to_date': toDate,
                'form-0-text': text,
            }
        )

    def post_data(self, from_date1, to_date1, text1, from_date2='', to_date2='', text2=''):
        return self.client.post(
            reverse('employees:addEmployee'),
            data={
                'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 0,
                'form-0-from_date': from_date1,
                'form-0-to_date': to_date1,
                'form-0-text': text1,
                'form-1-from_date': from_date2,
                'form-1-to_date': to_date2,
                'form-1-text': text2,
            }
        )

    def raise_formset_error(self, response, error):
        self.assertFormsetError(
            response,
            formset='exp_formset',
            form_index=None,
            field=None,
            errors=error
        )

    def test_valid_data(self):
        from_date = datetime.datetime(2008, 11, 28)
        to_date = datetime.datetime(2012, 12, 11)
        form = self.form_data(from_date, to_date, 'Some text.')
        self.assertTrue(form.is_valid())

    def test_empty_fields(self):
        """
        Test validation passes when no data is provided
        (data is not required).
        """
        form = self.form_data(None, None, '')
        self.assertTrue(form.is_valid())

    def test_duplicate_dates(self):
        """
        Test validation fails when working dates are submitted more than once.
        """
        from_date = datetime.datetime(2008, 11, 28)
        to_date = datetime.datetime(2012, 12, 11)
        response = self.post_data(from_date, to_date, 'Some text.',
                                  from_date, to_date, 'Some more text.')

        self.raise_formset_error(response,
                                 'Each work experience must have unique dates.')

    def test_to_date_without_from_date(self):
        """
        Test validation fails when a to date is submitted without a from date.
        """
        to_date = datetime.datetime(2012, 12, 11)
        response = self.post_data('', to_date, 'Some text.')

        self.raise_formset_error(response, 'All to dates must be paired with a from date.')
