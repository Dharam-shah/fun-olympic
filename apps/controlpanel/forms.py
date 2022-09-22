from django import forms
from apps.funolympic.models import Category, OlympicGame


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'image', 'description']


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = OlympicGame
        fields = ['title', 'thumbnail_image', 'video_url', 'category', 'description']