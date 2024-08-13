from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration for the home app.
    """

    default_auto_field = (
        "django.db.models.BigAutoField"  # Default primary key field type
    )
    name = "home"  # Name of the app
