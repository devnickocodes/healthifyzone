from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisplayArticles.as_view(), name='homepage'),
    path('create_article/', views.create_article, name='create_article'),
    path('<slug:article_slug>/delete/', views.delete_article, name='delete_article'),
    path('like_comment/', views.like_comment, name='like_comment'),
    path('like_article/', views.like_article, name='like_article'),
    path('categories/', views.DisplayCategories.as_view(), name='categories'),
    path('<slug:article_slug>/', views.view_article, name='view_article'),
    path('<slug:article_slug>/edit_comment/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
    path('<slug:article_slug>/delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('category/<slug:category_slug>/', views.view_by_category,
         name='view_by_category'),
]
