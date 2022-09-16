from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm


# # Create your views here.
# def home(request):
#     #return HttpResponse("Homepage")
#     return render(request, "account/register.html")

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/register.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()

        return render(request, self.template_name, {'form': form})
