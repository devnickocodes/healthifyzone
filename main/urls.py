from django.urls import path
from . import views 

urlpatterns = [
    path('', views.DisplayArticles.as_view(), name='homepage'),
    path('<slug:slug>/', views.view_article, name='view_article'),
]