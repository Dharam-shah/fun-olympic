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
        

# class UpdateCategoryForm(forms.ModelForm):

#     class Meta:
#         model = Category
#         fields = ['user']

#     def __init__(self, *args, **kwargs):
#         # User = get_user_model()
        
#         self.request = kwargs.pop('request')
#         # import ipdb; ipdb.set_trace()
#         super(UpdateCategoryForm, self).__init__(*args, **kwargs)
#         # current_user = kwargs.pop('c_user')
        
#         self.fields['user'] = forms.ModelMultipleChoiceField(queryset=Category.objects.exclude(user=self._user), required=False)

#     def save(self, commit=True):
#         inst = super(UpdateCategoryForm, self).save(commit=False)
#         inst.user = self._user
#         if commit:
#             inst.save()
#             self.save_m2m()
#         return inst

    # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    
        

class UpdateCategoryForm(forms.ModelForm):

    class Meta:
        model = FeaturedCategory
        fields = ['category']

