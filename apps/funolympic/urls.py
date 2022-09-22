from django.urls import path
from .views import OnlympicGameView, CategoryDetailView, user_profile

urlpatterns = [
    # path('', home, name='homepage'),
    path('profile/', user_profile, name='user-profile'),

    path("", OnlympicGameView.as_view(), name="homepage"),
    path("game-category/", CategoryDetailView.as_view(), name="game-category"),
]