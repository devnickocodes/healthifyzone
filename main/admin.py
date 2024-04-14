from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Article, Comment
# Register your models here.

@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category_slug', 'created_on',)
    prepopulated_fields = {'category_slug': ('title',)}


@admin.register(Article)  
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'article_slug', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'category')
    prepopulated_fields = {'article_slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('article', 'approved', 'comment_author')
    list_filter = ('approved', 'created_on')