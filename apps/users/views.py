from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView, UpdateView
from apps.funolympic.models import Category
from .forms import SignUpForm, UpdateProfileForm
from .forms import UpdateUserDetailForm
from .models import User
# from apps.funolympic.forms import FeaturedCategoryForm

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


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name='account/change_password.html'

    def get_success_url(self ,*args, **kwargs):
        return reverse('login')


class UserProfile(TemplateView):
    model = User
    template_name = 'user/user_profile.html'


class UpdateProfile(UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = 'user/update_profile.html'

    def get_success_url(self ,*args, **kwargs):
        return reverse('profile')


class UpdateUserView(UpdateView):
    model = User
    form_class = UpdateUserDetailForm
    template_name = 'controlpanel/users/update_user.html'

    def get_success_url(self ,*args, **kwargs):
        return reverse('user-list')
