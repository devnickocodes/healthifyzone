from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing custom user accounts.

    Attributes:
        list_display: Fields to display in the list
        view of the admin interface.
    """
    list_display = ('username', 'date_joined',)
