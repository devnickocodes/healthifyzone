from django.test import TestCase
from .forms import UserRegistrationForm

# Create your tests here.

class TestUserRegistrationForm(TestCase):

    def test_form_initialization(self):
        form = UserRegistrationForm()
        self.assertIsNotNone(form)

    def test_form_fields_presence(self):
        form = UserRegistrationForm()
        self.assertTrue('first_name' in form.fields)
        self.assertTrue('last_name' in form.fields)
        self.assertTrue('username' in form.fields)
        self.assertTrue('email' in form.fields)
        self.assertTrue('password1' in form.fields)
        self.assertTrue('password2' in form.fields)

    def test_email_field_required(self):
        form = UserRegistrationForm(data={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
    
    def test_username_max_length(self):
        form = UserRegistrationForm(data={'username': 'a' * 17})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)