from django.db import models

# Create your models here.


class Category(models.Model):

    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    category_slug = models.SlugField(null=False, blank=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = "Categories"
        ordering = ["-created_on"]

    def __str__(self):

        return f'Title: {self.title}'


class Article(models.Model):

    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200, blank=True)
    article_slug = models.SlugField(null=False, blank=False, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:

        ordering = ["-created_on"]

    def __str__(self):

        return f'Title: {self.title}'