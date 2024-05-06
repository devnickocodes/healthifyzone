from django.test import TestCase
from django import forms
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

    def test_username_min_length(self):
        form = UserRegistrationForm(data={'username': 'a'})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_valid_data(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'username@example.com',
            'password1': '<Uf&xiMp.7H*&zE',
            'password2': '<Uf&xiMp.7H*&zE'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'invalidemail',
            'password1': 'password',
            'password2': 'password',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_clean_username_valid(self):

        form = UserRegistrationForm(data={'username': 'janedoe123'})
        form.is_valid()
        self.assertEqual(form.clean_username(), 'janedoe123')

    def test_clean_username_invalid(self):
        invalid_usernames = ['johndoe@', 'john doe', 'johndoe$%^']
        for username in invalid_usernames:
            form = UserRegistrationForm(data={'username': username})
            self.assertFalse(form.is_valid())
            if 'username' in form.cleaned_data:
                with self.assertRaisesMessage(
                    forms.ValidationError,
                    'Username can only contain letters, numbers,'
                    'and underscores.'
                ):
                    form.clean_username()
