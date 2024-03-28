from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Article
# Register your models here.

@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category_slug', 'created_on',)
    prepopulated_fields = {'category_slug': ('title',)}


@admin.register(Article)  
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'article_slug', 'created_on', 'approved', 'category')
    list_filter = ('approved', 'created_on')
    prepopulated_fields = {'article_slug': ('title',)}
    summernote_fields = ('content',)
