from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField (
        label = "First name",
        max_length = 25,
        required = True
    )
    last_name = forms.CharField (
        label = "Last name",
        max_length = 25, 
        required = True,
    )
    email = forms.EmailField (
        label = "Email",
        max_length = 50, 
        required = True,
    )

    class Meta:
        model = User
        fields=[ 'first_name', 'last_name', 'email', 'password1', 'password2']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields=[ 'first_name', 'last_name', 'email', 'image']