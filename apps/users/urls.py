from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, LogInView

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", LogInView.as_view(), name="login"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='account/reset_password.html'), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='account/reset_password_sent.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_form.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/reset_password_complete.html'), name ='password_reset_complete'),
]
