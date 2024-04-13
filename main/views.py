# pylint: disable=no-member
# pylint: disable=missing-docstring
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article, Category
from .forms import CommentForm
# Create your views here.

class DisplayArticles(generic.ListView):
    
    queryset = Article.objects.filter(approved=True).order_by("-created_on")
    template_name = 'main/index.html'
    paginate_by = 6 


def view_article(request, article_slug):

    queryset = Article.objects.filter(approved=True)
    article = get_object_or_404(queryset, article_slug=article_slug)

    comments = article.comments.all().order_by("-created_on")
    comment_count = article.comments.filter(approved=True).count()

    
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_author = request.user
            comment.article = article
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "main/view_article.html",
        {"article": article,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form},
    )

class DisplayCategories(generic.ListView):

    queryset = Category.objects.filter(approved=True)

    template_name = 'main/categories.html'


def view_by_category(request, category_slug):
    category = Category.objects.get(category_slug=category_slug)
    articles_related_to_category = category.article_set.all()

    # Pagination
    paginator = Paginator(articles_related_to_category, 4)  
    page_number = request.GET.get('page')
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(
        request,
        'main/articles_by_category.html',
        {'articles': articles, 'category': category}
    )