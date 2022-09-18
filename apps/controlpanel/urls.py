from django.urls import path
from .views import DashboardOverView, CategoryListView

urlpatterns = [
    path("overview/", DashboardOverView.as_view(), name="overview"),
    path("category-list/", CategoryListView.as_view(), name="category-list"),
]
