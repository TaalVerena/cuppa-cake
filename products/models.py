from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Model representing a product category.
    """

    class Meta:
        verbose_name_plural = "Categories"  # Display name for the admin interface

    name = models.CharField(max_length=254)  # Internal category name
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True
    )  # Display name
    minimum_order_amount = models.PositiveIntegerField(
        default=1
    )  # Minimum order amount for the category

    def __str__(self):
        return self.name  # Return category name as string

    def get_friendly_name(self):
        return self.friendly_name  # Return the friendly name of the category


class Flavour(models.Model):
    """
    Model representing a product flavour.
    """

    name = models.CharField(max_length=254)  # Internal flavour name
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True
    )  # Display name

    def __str__(self):
        return self.name  # Return flavour name as string


class Product(models.Model):
    """
    Model representing a product.
    """

    category = models.ForeignKey(
        "Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # Link to a category
    )
    flavour = models.ForeignKey(
        "Flavour", null=True, blank=True, on_delete=models.SET_NULL  # Link to a flavour
    )
    sku = models.CharField(
        max_length=254, null=True, blank=True
    )  # Stock keeping unit identifier
    name = models.CharField(max_length=254)  # Product name
    description = models.TextField()  # Product description
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Product price
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )  # Product rating
    image_url = models.URLField(
        max_length=1024, null=True, blank=True
    )  # URL for product image
    image = CloudinaryField(
        "image", null=True, blank=True
    )  # Cloudinary image field for storing product images

    def __str__(self):
        return self.name  # Return product name as string
