from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views as auth_views
from .forms import SignUpForm


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


# class ResetPasswordView(PasswordResetView):
#     template_name='account/reset_password.html'

#     def form_valid(self, form, *args, **kwargs):
#         # email = form.cleaned_data.get('email')
#         # try:
#         #     user = UserDetail.objects.get(user__email=email)
#         #     if user.is_email_verified == False:
#         #         messages.error(self.request, 'Your account is not verified')
#         #         return super().form_invalid(form, *args, **kwargs)
#         # except:
#         #     return super().form_valid(form)
#         return super().form_valid(form)