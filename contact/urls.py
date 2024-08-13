from django.urls import path
from .views import contact_view

# URL patterns for the contact app
urlpatterns = [
    path("", contact_view, name="contact"),
]
