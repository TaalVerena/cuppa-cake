from django.urls import path
from . import views

# URL patterns for profile-related views
urlpatterns = [
    path("", views.profile, name="profile"),
    path("order_history/<order_number>", views.order_history, name="order_history"),
]
