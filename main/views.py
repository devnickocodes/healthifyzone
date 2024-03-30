from django.shortcuts import render
from django.views import generic
from .models import Article
# Create your views here.

class DisplayArticles(generic.ListView):
    
    queryset = Article.objects.filter(approved=False).all()
    template_name = 'article_list.html'