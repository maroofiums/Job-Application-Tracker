from .views import dashboard_view
from django.urls import path

urlpatterns = [
    path("", dashboard_view, name="dashboard")
]
