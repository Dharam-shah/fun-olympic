from django import forms
from .models import FeaturedCategory


class FeaturedCategoryForm(forms.ModelForm):
    class Meta:
        model = FeaturedCategory
        fields = ['category', 'user']
