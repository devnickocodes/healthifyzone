from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator, MinLengthValidator


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.',
                             required=True)
    username = forms.CharField(validators=[MinLengthValidator(3),
                               MaxLengthValidator(16)], required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.replace('_', '').isalnum():
            raise forms.ValidationError(
             'Username can only contain letters, numbers, and underscores.'
            )
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user


class userUpdateProfileForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'bio',
            'status',
            'profile_image'
        ]
