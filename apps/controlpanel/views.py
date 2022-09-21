from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from apps.users.models import User
from apps.funolympic.models import Category, OlympicGame 
from .forms import CategoryForm

# Create your views here.
class DashboardOverView(TemplateView):
    template_name = 'controlpanel/base.html'

class CategoryListView(TemplateView):
    # model = User
    # context_object_name = 'users'
    template_name = 'controlpanel/category/category_list.html'

class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'controlpanel/category/create_category.html'
    success_url = reverse_lazy('category-list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        import ipdb; ipdb.set_trace()
        if form.is_valid():
            print('djhj')
            # form.save()
        return super().post(request, *args, **kwargs)

        
class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'controlpanel/users/user_list.html'
    paginate_by = 10
    ordering = ['-id']