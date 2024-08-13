from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Admin interface options for FAQ model.
    """

    list_display = ("question",)  # Display the question in the admin list
    search_fields = ("question", "answer")  # Enable search by question and answer
