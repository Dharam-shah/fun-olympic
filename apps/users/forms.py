from django import forms
from apps.funolympic.models import Category
from .models import User
from django.contrib.auth.forms import UserCreationForm
from apps.funolympic.models import FeaturedCategory

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


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'image']


class UpdateUserDetailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'image']
        
