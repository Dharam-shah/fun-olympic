from django.urls import path
from .views import DashboardOverView, CategoryListView, UserListView, CreateCategoryView, UpdateCategoryView
                

urlpatterns = [
    path("overview/", DashboardOverView.as_view(), name="overview"),

    path("create-category/", CreateCategoryView.as_view(), name="create-category"),
    path("category-list/", CategoryListView.as_view(), name="category-list"),
    path("category/update/<int:pk>", UpdateCategoryView.as_view(), name="update-category"),

    path("user-list/", UserListView.as_view(), name="user-list"),
]
