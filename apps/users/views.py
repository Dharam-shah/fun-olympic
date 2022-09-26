from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView, UpdateView
from apps.funolympic.models import Category
from .forms import SignUpForm, UpdateProfileForm
from .forms import UpdateCategoryForm
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


class UserProfile(FormView):
    model = User
    form_class = UpdateCategoryForm
    template_name = 'user/user_profile.html'
    
    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super(UserProfile, self).get_form_kwargs()
    #     kwargs['c_user'] = self.request.user
    #     import ipdb; ipdb.set_trace()
    #     return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.request.user
    #     context["selected_category"] = Category.objects.filter(user=user)
    #     return context

    # def post(self, request, *args, **kwargs):
    #     form = UpdateCategoryForm(request.POST)
    #     if form.is_valid():
    #         # selected_category = form.cleaned_data.get('category')
    #         # current_user = self.request.user
    #         # current_user.user.set(selected_category)
    #         # current_user.save()
    #         self.object = form.save(commit=False)
            
    #         form.save()
    #         self.object.user.set(self.request.user)
            

    #     return super().post(request, *args, **kwargs)

    # def get_success_url(self ,*args, **kwargs):
    #     return reverse('profile')


class UpdateProfile(UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = 'user/update_profile.html'

    def get_success_url(self ,*args, **kwargs):
        return reverse('profile')
