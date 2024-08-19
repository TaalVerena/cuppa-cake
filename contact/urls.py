from django.urls import path
from .views import contact_view, contact_thank_you_view

# URL patterns for the contact app
urlpatterns = [
    path("", contact_view, name="contact"),
    path("thank-you/", contact_thank_you_view, name="contact_thank_you"),
]
