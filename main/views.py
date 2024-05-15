# pylint: disable=no-member
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Article, Category, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.


class DisplayArticles(generic.ListView):
    """
    Display a list of approved articles
    ordered by the created_on field in descending order.

    **Context**

    ``queryset``
        A queryset containing approved articles
        ordered by the created_on field in descending order.

    **Template:**

    :template:`main/index.html`
    """
    queryset = Article.objects.filter(approved=True).order_by("-created_on")
    template_name = 'main/index.html'
    paginate_by = 6


def view_article(request, article_slug):
    """
    Display an individual article and its comments.

    **Context**

    ``queryset``
        A queryset of approved articles.

    ``article``
        An instance of :model:`main.Article` based on the article slug.

    ``comments``
        A queryset containing all comments related to the article,
        ordered by the created_on field in descending order.

    ``comment_count``
        The count of approved comments related to the article.

    ``comment_form``
        A form for submitting comments or editing existing comments.


    **Template:**

    :template:`main/view_article.html`
    """
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
    """
    Display a list of approved categories.

    **Context**

    ``queryset``
        A queryset containing approved categories.

    **Template:**

    :template:`main/categories.html`
    """
    queryset = Category.objects.filter(approved=True)

    template_name = 'main/categories.html'


def view_by_category(request, category_slug):
    """
    Display articles belonging to a specific category.

    **Context**

    ``articles_related_to_category``
        A paginated list of articles related to the category.

    ``category``
        An instance of :model:`main.Category` based on the category slug.

    **Template:**

    :template:`main/articles_by_category.html`

    **Pagination:**

    This view paginates the articles related to the category
    with 4 articles per page.
    """
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
    """
    Edit a comment associated with an article.

    **Context**

    ``article``
        An instance of :model:`main.Article`.

    ``comment``
        An instance of :model:`main.Comment`.

    **Template:**

    :template:`main/view_article.html`
    """
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
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('view_article', args=[article_slug]))


@login_required
def delete_comment(request, article_slug, comment_id):
    """
    Delete a comment associated with an article.

    **Template:**

    :template:`main/view_article.html`
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.comment_author == request.user or request.user.is_superuser:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('view_article', args=[article_slug]))


@login_required
def like_comment(request):
    """
    Like or unlike a comment.

    **Template:**

    :template:`main/view_article.html`
    """
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

    return JsonResponse({'error': 'Invalid request method or action'},
                        status=400)


@login_required
def like_article(request):
    """
    Like or unlike an article.

    **Template:**

    :template:`main/view_article.html`
    """
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

    return JsonResponse({'error': 'Invalid request method or action'},
                        status=400)


@login_required
def create_article(request):
    """
    Create an article

    **Template:**

    :template:`main/create_article.html`
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_author = request.user
            article.article_slug = slugify(article.title)
            if 'featured_article_image' in request.FILES:
                article.featured_article_image = request.FILES['featured_article_image']
            article.save()
            return redirect('homepage')
    else:
        form = ArticleForm()
    return render(request, 'main/create_article.html', {'form': form})