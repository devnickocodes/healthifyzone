from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Article, Comment

class CategoryAdmin(SummernoteModelAdmin):
    """
    Admin configuration for Category model.

    Attributes:
        list_display: Fields to display in the list view of the admin interface.
        prepopulated_fields: Field to automatically populate based on the title field.
    """
    list_display = ('title', 'category_slug', 'created_on',)
    prepopulated_fields = {'category_slug': ('title',)}

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(SummernoteModelAdmin):
    """
    Admin configuration for Article model.

    Attributes:
        list_display: Fields to display in the list view of the admin interface.
        list_filter: Fields to use for filtering in the admin interface.
        prepopulated_fields: Fields to automatically populate based on the title field.
        summernote_fields: Fields to render using Summernote WYSIWYG editor.
    """
    list_display = ('title', 'category', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'category')
    prepopulated_fields = {'article_slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(SummernoteModelAdmin):
    """
    Admin configuration for Comment model.

    Attributes:
        list_display: Fields to display in the list view of the admin interface.
        list_filter: Fields to use for filtering in the admin interface.
    """
    list_display = ('article', 'approved', 'comment_author')
    list_filter = ('approved', 'created_on')

admin.site.register(Comment, CommentAdmin)
