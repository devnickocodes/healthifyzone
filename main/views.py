# pylint: disable=no-member
# pylint: disable=missing-docstring
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article, Category
# Create your views here.

class DisplayArticles(generic.ListView):
    
    queryset = Article.objects.filter(approved=True).order_by("-created_on")
    template_name = 'main/index.html'
    paginate_by = 6 


def view_article(request, article_slug):

    queryset = Article.objects.filter(approved=True)
    article = get_object_or_404(queryset, article_slug=article_slug)

    return render(
        request,
        "main/view_article.html",
        {"article": article},
    )
