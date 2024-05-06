from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.recipe_search, name='recipe_search'),
    path('search/results/', views.recipe_search_results,
         name='recipe_search_results'),
    path('recipe/<int:recipe_id>/', views.recipe_detail_with_instructions,
         name='recipe_detail_with_instructions'),
]
