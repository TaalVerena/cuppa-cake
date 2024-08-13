from django.contrib import admin
from .models import Product, Category, Flavour


class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface options for Product model.
    """

    list_display = (
        "sku",
        "name",
        "category",
        "flavour",
        "price",
        "rating",
        "image",
    )
    ordering = ("sku",)  # Order products by SKU


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface options for Category model.
    """

    list_display = (
        "friendly_name",  # User-friendly category name
        "name",  # Internal category name
    )


class FlavourAdmin(admin.ModelAdmin):
    """
    Admin interface options for Flavour model.
    """

    list_display = (
        "friendly_name",  # User-friendly flavour name
        "name",  # Internal flavour name
    )


# Register models with the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Flavour, FlavourAdmin)
