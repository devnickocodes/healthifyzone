from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from .views import view_profile

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