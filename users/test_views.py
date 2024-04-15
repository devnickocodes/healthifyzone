from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.forms.models import model_to_dict
from .views import view_profile
from .forms import userUpdateProfileForm

class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.username = "user"
        self.password = "userpassword"
        self.user = get_user_model().objects.create_user(username=self.username, password=self.password)

    def test_view_profile_get(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("view_profile", kwargs={"username": self.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile_page.html")
    
    def test_post_request_with_valid_form(self):
        form_data = {
            "username": self.user.username,
            "first_name": "Test",
            "last_name": "User",
            "email": "test@email.com",
            "bio": "This is a test bio.",
        }
        form = userUpdateProfileForm(data=form_data)
        if form.is_valid():
            form_dict = model_to_dict(form.save())
            response = self.client.post(
                reverse("view_profile", args=[self.user.username]),
                data=form_dict
            )
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse("view_profile", args=[self.user.username]))
            self.assertEqual(self.user.first_name, "Test")
            self.assertEqual(self.user.last_name, "User")
            self.assertEqual(self.user.email, "test@email.com")
            self.assertEqual(self.user.bio, "This is a test bio.")
        
    def test_post_request_with_invalid_form(self):
        form_data = {
            "username": self.user.username,
            "first_name": "",
            "last_name": "",
            "email": "",
            "bio": "",
        }
        form = userUpdateProfileForm(data=form_data)
        if form.is_valid():
            form_dict = model_to_dict(form.save())
            response = self.client.post(
                reverse("view_profile", args=[self.user.username]),
                data=form_dict
            )
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "users/profile_page.html")
            self.assertContains(response, "This field is required.")
            self.assertContains(response, "This field is required.")
            self.assertContains(response, "This field is required.")
            self.assertContains(response, "This field is required.")