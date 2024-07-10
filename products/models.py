from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    minimum_order_amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Flavour(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    flavour = models.ForeignKey(
        "Flavour", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField("image", null=True, blank=True)

    def __str__(self):
        return self.name
