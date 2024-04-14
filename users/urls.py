from django.urls import path
from . import views 

urlpatterns = [
    path("register", views.register, name="register"),
    path("profile/<username>", views.view_profile, name="view_profile"),
]