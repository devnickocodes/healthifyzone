from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


# Create your models here.


class Category(models.Model):
    """
    Stores a single category entry related to :model:`users.CustomUser`.
    """
    title = models.CharField(max_length=150, blank=False)
    subtitle = models.CharField(max_length=200, blank=False)
    category_slug = models.SlugField(null=False, blank=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    category_author = models.ForeignKey(get_user_model(),
                                        on_delete=models.CASCADE)
    featured_category_image = CloudinaryField('image',
                                              default='placeholder.jpeg')

    class Meta:
        """
        Meta class for Category model.

        Attributes:
            verbose_name_plural: A human-readable name
            for the object in plural form.
            ordering: Specifies the default ordering
            of records when queried from the database.
                      Records will be ordered by
                      the created_on field in descending order.
        """
        verbose_name_plural = "Categories"
        ordering = ["-created_on"]

    def __str__(self):

        return f'Category title: {self.title}'


class Article(models.Model):
    """
    Stores a single article entry related to :model:`users.CustomUser`.
    And :model:`main.Category`
    """

    title = models.CharField(max_length=200, blank=False, unique=True)
    subtitle = models.CharField(max_length=200, blank=False)
    article_slug = models.SlugField(null=False, blank=False, unique=True)
    content = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null=False,
                                 on_delete=models.CASCADE)
    article_author = models.ForeignKey(get_user_model(),
                                       on_delete=models.CASCADE)
    article_likes = models.ManyToManyField(get_user_model(),
                                           blank=True, related_name='liked_by')
    article_likes_count = models.BigIntegerField(default=0)
    featured_article_image = CloudinaryField('image',
                                             default='placeholder.jpeg')

    class Meta:
        """
        Meta class for Article model.

        Attributes:
            ordering: Specifies the default ordering of records
                      when queried from the database.
                      Records will be ordered by the created_on
                      field in descending order.
        """
        ordering = ["-created_on"]

    def __str__(self):

        return f'Article title: {self.title}'


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`users.CustomUser`.
    And :model:`main.Article`
    """

    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="comments")
    body = models.TextField(blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    comment_author = models.ForeignKey(get_user_model(),
                                       on_delete=models.CASCADE)
    comment_likes = models.ManyToManyField(get_user_model(), blank=True,
                                           related_name='liked_comments')
    comment_likes_count = models.BigIntegerField(default=0)

    class Meta:
        """
        Meta class for Comment model.

        Attributes:
            ordering: Specifies the default ordering of records
                      when queried from the database.
                      Records will be ordered by the created_on
                      field in descending order.
        """
        ordering = ["-created_on"]

    def __str__(self):
        return f"Author: {self.comment_author}"
