from django.views.generic import ListView
from apps.funolympic.models import Category, OlympicGame 
from django.shortcuts import render


# Create your views here.
class OnlympicGameView(ListView):
    model = OlympicGame
    context_object_name = 'game_lists'
    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryDetailView(ListView):
    model = Category
    context_object_name = 'category_lists'
    template_name = 'homepage/game_category.html'


def user_profile(request):
    return render(request, "user/user_profile.html")