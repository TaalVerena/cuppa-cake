from django.urls import path
from . import views

# URL patterns for the faq app
urlpatterns = [
    path("", views.faq_list, name="faq_list"),
]
