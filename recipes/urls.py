from django.urls import path
from . import views



urlpatterns = [
    path('search/', views.recipe_search, name='recipe_search'),
    path('search/results/', views.recipe_search_results, name='recipe_search_results'),
]