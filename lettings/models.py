"""
Models for the lettings application.

This module defines the data models for managing property addresses and letting
information. It includes proper validation and relationships between addresses
and letting properties.

Models:
    Address: Represents a physical address with validation
    Letting: Represents a property letting with a reference to an address
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing a physical address.

    This model stores complete address information with appropriate validation
    to ensure data integrity. Each address can be associated with one letting.

    Attributes:
        number (PositiveIntegerField): Street number (1-9999)
        street (CharField): Street name (max 64 characters)
        city (CharField): City name (max 64 characters)
        state (CharField): State code (exactly 2 characters)
        zip_code (PositiveIntegerField): ZIP code (1-99999)
        country_iso_code (CharField): ISO country code (exactly 3 characters)
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Meta configuration for Address model."""
        verbose_name_plural = "addresses"

    def __str__(self):
        """
        Return string representation of the address.

        Returns:
            str: Formatted address as "number street"
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Model representing a property letting.

    This model represents a rental property with a title and associated address.
    Each letting has a one-to-one relationship with an address, ensuring
    data consistency and preventing address reuse.

    Attributes:
        title (CharField): Descriptive title for the letting (max 256 characters)
        address (OneToOneField): Reference to the associated Address object
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """Meta configuration for Letting model."""
        verbose_name_plural = "lettings"

    def __str__(self):
        """
        Return string representation of the letting.

        Returns:
            str: The letting title
        """
        return self.title
