from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from apps.users.models import User
from apps.funolympic.models import Category, OlympicGame 
from .forms import CategoryForm

# Create your views here.
class DashboardOverView(TemplateView):
    template_name = 'controlpanel/base.html'

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
    