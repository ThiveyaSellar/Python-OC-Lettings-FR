"""
------------------
lettings.models.py
------------------
This module contains Django models for the lettings application.
Each model represents a database table and its fields.

Classes:
    Address
    Letting
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address of a letting.

    Attributes:
        number (int): House or building number (max 9999).
        street (str): Street name (max 64 characters).
        city (str): City name (max 64 characters).
        state (str): State code (2 characters).
        zip_code (int): ZIP or postal code (max 99999).
        country_iso_code (str): ISO 3166-1 alpha-3 country code (3 characters).
    """

    class Meta:
        verbose_name_plural = "Addresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)]
    )
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        Return a human-readable string representing the address.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a letting in the application.

    Attributes:
        title (str) : The title or name of the letting (max 256 characters).
        address (Address): The associated address of the letting (one to one relationship).
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a human-readable string representing the letting.
        """
        return self.title
