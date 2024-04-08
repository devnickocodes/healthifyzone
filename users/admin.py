from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(SummernoteModelAdmin):
    list_display = ('username', 'date_joined',)