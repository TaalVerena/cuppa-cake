from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.
    """

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )  # Fields to display in the list view
    search_fields = ("name", "email", "subject")  # Fields to search
    list_filter = ("created_at",)  # Filter by creation date
