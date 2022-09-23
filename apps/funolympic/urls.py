from django.urls import path
from .views import OnlympicGameView, CategoryWiseGameView, user_profile

urlpatterns = [
    path('profile/', user_profile, name='user-profile'),
    path("", OnlympicGameView.as_view(), name="homepage"),
    path("game-category/<int:id>", CategoryWiseGameView.as_view(), name="game-category"),
]