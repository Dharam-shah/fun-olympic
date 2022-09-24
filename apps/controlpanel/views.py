from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from apps.users.models import User
from apps.funolympic.models import Category, OlympicGame 
from .forms import CategoryForm, GameCreateForm

# Create your views here.
class DashboardOverView(TemplateView):
    template_name = 'controlpanel/overview.html'


class GameListView(ListView):
    model = OlympicGame
    context_object_name = 'game_lists'
    template_name = 'controlpanel/olympic-games/game_list.html'
    paginate_by = 10
    ordering = ['-id']


class GameCreateView(CreateView):
    model = OlympicGame
    form_class = GameCreateForm
    template_name = 'controlpanel/olympic-games/create_game.html'
    success_url = reverse_lazy('game-list')


class UpdateGameView(UpdateView):
    model = OlympicGame
    form_class = GameCreateForm
    template_name = 'controlpanel/olympic-games/update_game.html'
    success_url = reverse_lazy('game-list')


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_lists'
    template_name = 'controlpanel/category/category_list.html'
    paginate_by = 10
    ordering = ['-id']


class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'controlpanel/category/create_category.html'
    success_url = reverse_lazy('category-list')

        
class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'controlpanel/category/update_category.html'
    success_url = reverse_lazy('category-list')


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'controlpanel/users/user_list.html'
    paginate_by = 10
    ordering = ['-id']
    