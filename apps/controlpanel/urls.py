from django.urls import path
from .views import DashboardOverView

urlpatterns = [
    path("overview/", DashboardOverView.as_view(), name="overview"),
]
