from django.urls import path
from .views import subscribe_view

# URL patterns for the newsletter app
urlpatterns = [
    path("subscribe/", subscribe_view, name="subscribe"),
]
