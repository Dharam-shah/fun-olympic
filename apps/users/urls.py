from django.urls import path
# from .views import SignUpView
from .views import register

urlpatterns = [
    # path('register/', SignUpView.as_view(), name='register'),
    path("register/", register, name="register"),
]