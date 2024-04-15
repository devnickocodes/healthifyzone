from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib import messages
from .forms import UserRegistrationForm, userUpdateProfileForm
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

def view_profile(request, username):
    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = userUpdateProfileForm(instance=user)
        return render(
            request=request,
            template_name="users/profile_page.html",
            context={"form": form}
        )
    return redirect("homepage")