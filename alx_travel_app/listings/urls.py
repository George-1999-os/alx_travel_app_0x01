from django.urls import path
from .views import ListingsView

urlpatterns = [
    path("listings/", ListingsView.as_view(), name="listings"),
]
