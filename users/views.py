from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, userUpdateProfileForm


# Create your views here.


def register(request):
    """
    View for registering a new user.

    **Context:**

    - ``form``: An instance of :class:`~users.forms.UserRegistrationForm`.

    **Template:**

    - ``users/register.html``: The registration form template.
    - ``account/login.html``: The login form template.

    """
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
        template_name=["users/register.html", "account/login.html"],
        context={"form": form}
    )


@login_required
def view_profile(request, username):
    """
    View to view a user profile or display a
    'User Not Found Page' if the user doesn't exist.

    **Context:**

    - ``form``: An instance of :class:`~users.forms.UserUpdateProfileForm`.
    - ``user``: The user whose profile is being viewed.

    **Template:**

    - ``users/profile_page.html``: The user profile page template.
    - ``users/user_not_found.html``: Template for when the requested user
                                     does not exist.

    """
    if request.method == "POST":
        user = request.user
        form = userUpdateProfileForm(request.POST, request.FILES,
                                     instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(
                request,
                f"{user_form.username}, your profile has been updated!"
                 )
            return redirect("view_profile", user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = userUpdateProfileForm(instance=user)
        return render(
               request=request,
               template_name="users/profile_page.html",
               context={"form": form,
                        'user': user}
        )

    return render(
        request=request,
        template_name="users/user_not_found.html"
    )
