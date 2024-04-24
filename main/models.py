from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


# Create your models here.


class Category(models.Model):

    title = models.CharField(max_length=150, blank=False)
    subtitle = models.CharField(max_length=200, blank=False)
    category_slug = models.SlugField(null=False, blank=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    category_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    featured_category_image = CloudinaryField('image', default='placeholder.jpeg')

    class Meta:

        verbose_name_plural = "Categories"
        ordering = ["-created_on"]

    def __str__(self):

        return f'Category title: {self.title}'


class Article(models.Model):

    title = models.CharField(max_length=200, blank=False)
    subtitle = models.CharField(max_length=200, blank=False)
    article_slug = models.SlugField(null=False, blank=False, unique=True)
    content = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    article_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article_likes = models.ManyToManyField(get_user_model(), blank=True, related_name='liked_by')
    article_likes_count = models.BigIntegerField(default=0)
    featured_article_image = CloudinaryField('image', default='placeholder.jpeg')


    class Meta:

        ordering = ["-created_on"]

    def __str__(self):

        return f'Article title: {self.title}'
class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    comment_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_likes = models.ManyToManyField(get_user_model(), blank=True, related_name='liked_comments')
    comment_likes_count = models.BigIntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Author: {self.comment_author}"