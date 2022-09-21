from django.urls import path
from .views import home, user_profile

urlpatterns = [
    path('', home, name='homepage'),
    path('profile/', user_profile, name='user-profile'),
]