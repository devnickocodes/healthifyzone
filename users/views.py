from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome on board {user.username}!")
            return redirect('/')

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name = ["users/register.html", "account/login.html"],
        context={"form": form}
    )