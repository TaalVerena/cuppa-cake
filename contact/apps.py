from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    Configuration for the contact app.
    """

    default_auto_field = (
        "django.db.models.BigAutoField"  # Default primary key field type
    )
    name = "contact"  # Name of the app
