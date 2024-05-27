"""
URL configuration for healthifyzone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import handler403, handler404, handler500
from django.shortcuts import render
from users import views as user_views


def custom_404(request, exception):
    """
    Render a custom 404 error page.
    """
    return render(request, '404.html', status=404)


def custom_403(request, exception):
    """
    Render a custom 403 error page.
    """
    return render(request, '403.html', status=403)


def custom_500(request):
    """
    Render a custom 500 error page.
    """
    return render(request, '500.html', status=500)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='account/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('register/', user_views.register, name='register'),
    path('', include('users.urls')),
    path('', include('recipes.urls')),
    path('', include('main.urls')),
]

handler404 = 'healthifyzone.urls.custom_404'
handler403 = 'healthifyzone.urls.custom_403'
handler500 = 'healthifyzone.urls.custom_500'
