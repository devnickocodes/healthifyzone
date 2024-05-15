from django import forms
from .models import Article, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'content', 'category', 'featured_article_image']