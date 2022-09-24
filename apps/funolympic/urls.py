from django.urls import path
from .views import OnlympicGameView, CategoryWiseGameView

urlpatterns = [
    path("", OnlympicGameView.as_view(), name="homepage"),
    path("game-category/<int:id>", CategoryWiseGameView.as_view(), name="game-category"),
]