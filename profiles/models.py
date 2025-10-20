"""
------------------
profiles.models.py
------------------
This module contains a Django model for the profile application.
The model represents a database table and its fields.

Classes:
    Profile
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user's profile in the application.

    Attributes:
        user (User): The associated user of the profile (one to one relationship).
        favorite_city (str): The user's favorite city for renting (max characters:64)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return a human-readable string representing the profile.
        """
        return self.user.username
