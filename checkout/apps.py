from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the checkout app.
    """

    name = "checkout"

    def ready(self):
        """
        Import signals on app ready.
        """
        import checkout.signals
