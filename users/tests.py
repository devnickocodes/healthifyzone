from django.test import TestCase
from .forms import UserRegistrationForm

# Create your tests here.

class TestUserRegistrationForm(TestCase):

    def test_form_initialization(self):
        form = UserRegistrationForm()
        self.assertIsNotNone(form)

