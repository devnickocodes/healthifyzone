# pylint: disable=no-member
# pylint: disable=missing-docstring
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Article, Category, Comment
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
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for commenting!'
            )

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

@login_required
def edit_comment(request, article_slug, comment_id):

    if request.method == "POST":

        queryset = Article.objects.all()
        article = get_object_or_404(queryset, article_slug=article_slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.comment_author == request.user:
            
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('view_article', args=[article_slug]))

@login_required
def delete_comment(request, article_slug, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.comment_author == request.user or request.user.is_superuser:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('view_article', args=[article_slug]))

@login_required
def like_comment(request):
    if request.POST.get('action') == 'post':
        comment_id = int(request.POST.get('commentid'))
        comment = get_object_or_404(Comment, id=comment_id)
        
        if comment.comment_likes.filter(id=request.user.id).exists():
            comment.comment_likes.remove(request.user)
            comment.comment_likes_count -= 1
        else:
            comment.comment_likes.add(request.user)
            comment.comment_likes_count += 1
        
        comment.save()
        result = comment.comment_likes_count
        return JsonResponse({'result': result})
    
    return JsonResponse({'error': 'Invalid request method or action'}, status=400)

@login_required
def like_article(request):
    if request.POST.get('action') == 'post':
        article_id = int(request.POST.get('articleid'))
        article = get_object_or_404(Article, id=article_id)
        
        if article.article_likes.filter(id=request.user.id).exists():
            article.article_likes.remove(request.user)
            article.article_likes_count -= 1
        else:
            article.article_likes.add(request.user)
            article.article_likes_count += 1
        
        article.save()
        result = article.article_likes_count
        return JsonResponse({'result': result})
    
    return JsonResponse({'error': 'Invalid request method or action'}, status=400)