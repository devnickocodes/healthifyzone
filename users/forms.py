from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    username = forms.CharField(validators=[MaxLengthValidator(16)], required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.replace('_', '').isalnum():
            raise forms.ValidationError('Username can only contain letters, numbers, and underscores.')
        return username