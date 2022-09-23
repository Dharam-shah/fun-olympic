from pipes import Template
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from .forms import SignUpForm
from .models import User

# # Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/register.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


class LogInView(SuccessMessageMixin, LoginView):
    template_name = 'account/login.html'
    success_message = "You are successfully logged in."

    def get_success_url(self ,*args, **kwargs):
        return reverse('homepage')


class UserLogoutView(LogoutView):

    def get_success_url(self ,*args, **kwargs):
        return reverse('homepage')


class UserProfile(TemplateView):
    model = User
    template_name = 'user/user_profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["user"] = User.objects.filter(id=self.kwargs['id'])
    #     return context
        