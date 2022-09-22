from django.urls import path
from .views import DashboardOverView, CategoryListView, UserListView, CreateCategoryView, UpdateCategoryView, \
                GameListView, GameCreateView, UpdateGameView
                

urlpatterns = [
    path("overview/", DashboardOverView.as_view(), name="overview"),
    path("create-category/", CreateCategoryView.as_view(), name="create-category"),
    path("category-list/", CategoryListView.as_view(), name="category-list"),
    path("category/update/<int:pk>", UpdateCategoryView.as_view(), name="update-category"),
    path("user-list/", UserListView.as_view(), name="user-list"),
    path("game-list/", GameListView.as_view(), name="game-list"),
    path("create-game/", GameCreateView.as_view(), name="create-game"),
    path("game/update/<int:pk>", UpdateGameView.as_view(), name="update-game"),
]
