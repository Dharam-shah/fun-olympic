from django import forms
from .models import User

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
    }
    password1 = forms.CharField (
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField (
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ('email', 'first_name','last_name')


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
    # password1 = forms.CharField (
    #     label = "Password",
    #     max_length = 26,
    #     required = True,
    #     widget = forms.PasswordInput(),
    # )

    class Meta:
        model = User
        fields=[ 'first_name', 'last_name', 'email', 'password1', 'password2']
