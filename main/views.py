# pylint: disable=no-member
# pylint: disable=missing-docstring
from django.shortcuts import render
from django.views import generic
from .models import Article
# Create your views here.

class DisplayArticles(generic.ListView):
    
    queryset = Article.objects.filter(approved=True).order_by("-created_on")
    template_name = 'main/index.html'
    paginate_by = 6 