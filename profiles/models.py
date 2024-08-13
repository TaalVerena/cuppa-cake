from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # Link to the User model
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )  # Default phone number
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )  # Default street address line 1
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )  # Default street address line 2
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )  # Default town or city
    default_county = models.CharField(
        max_length=80, null=True, blank=True
    )  # Default county
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True
    )  # Default postcode
    default_country = CountryField(
        blank_label="Country", null=True, blank=True
    )  # Default country

    def __str__(self):
        return self.user.username  # Return the username as the string representation


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile when the User object is saved.
    """
    if created:
        UserProfile.objects.create(
            user=instance
        )  # Create a new UserProfile if a new User is created
    # For existing users, just save the profile
    instance.userprofile.save()
