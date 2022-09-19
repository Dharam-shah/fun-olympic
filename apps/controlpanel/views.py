from django.views.generic import TemplateView, ListView
from apps.users.models import User
# Create your views here.
class DashboardOverView(TemplateView):
    template_name = 'controlpanel/base.html'

class CategoryListView(TemplateView):
    template_name = 'controlpanel/category/category_list.html'


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'controlpanel/users/user_list.html'
    paginate_by = 10
    ordering = ['-id']