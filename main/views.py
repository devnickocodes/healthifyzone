# pylint: disable=no-member
# pylint: disable=missing-docstring
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

class DisplayCategories(generic.ListView):

    queryset = Category.objects.filter(approved=True)

    template_name = 'main/categories.html'


def view_by_category(request, category_slug):
    category = Category.objects.get(category_slug=category_slug)
    articles_related_to_category = category.article_set.all()

    return render(
        request,
        'main/articles_by_category.html',
        {'articles_related_to_category': articles_related_to_category, 'category': category}
    )