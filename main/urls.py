from django.urls import path
from . import views 

urlpatterns = [
    path('', views.DisplayArticles.as_view(), name='homepage'),
    path('categories', views.DisplayCategories.as_view(), name='categories'),
    path('<slug:article_slug>/', views.view_article, name='view_article'),
    path('category/<slug:category_slug>/', views.view_by_category, name='view_by_category'),
]