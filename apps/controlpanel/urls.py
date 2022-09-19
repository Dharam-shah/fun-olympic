from django.urls import path
from .views import DashboardOverView, CategoryListView, UserListView

urlpatterns = [
    path("overview/", DashboardOverView.as_view(), name="overview"),
    path("category-list/", CategoryListView.as_view(), name="category-list"),
    path("user-list/", UserListView.as_view(), name="user-list"),
]
