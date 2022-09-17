from django.views.generic import TemplateView

# Create your views here.
class DashboardOverView(TemplateView):
    template_name = 'controlpanel/base.html'