from django.urls import path
from . import views



urlpatterns = [
    path('search/', views.recipe_search, name='recipe_search'),
]