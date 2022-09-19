from django.urls import path
from .views import DashboardOverView, CategoryListView, UserListView, \
                    CreateCategoryView

urlpatterns = [
    path("overview/", DashboardOverView.as_view(), name="overview"),

    path("create-category/", CreateCategoryView.as_view(), name="create-category"),
    path("category-list/", CategoryListView.as_view(), name="category-list"),

    path("user-list/", UserListView.as_view(), name="user-list"),
]
