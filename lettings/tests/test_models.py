"""
Tests for lettings models.

This module contains unit tests for the Address and Letting models,
using pytest.mark.django_db for database access.
"""
import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from lettings.models import Address, Letting


class TestAddress:
    """Test cases for the Address model."""

    @pytest.mark.django_db
    def test_address_creation(self):
        """Test that an address can be created with valid data."""
        address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        
        assert address.number == 123
        assert address.street == 'Test Street'
        assert address.city == 'Test City'
        assert address.state == 'TS'
        assert address.zip_code == 12345
        assert address.country_iso_code == 'TST'

    @pytest.mark.django_db
    def test_address_str_method(self):
        """Test the string representation of an address."""
        address = Address.objects.create(
            number=456,
            street='Main Avenue',
            city='Test City',
            state='TS',
            zip_code=54321,
            country_iso_code='TST'
        )
        
        assert str(address) == '456 Main Avenue'

    @pytest.mark.django_db
    def test_address_verbose_name_plural(self):
        """Test that the plural name is correctly set."""
        assert Address._meta.verbose_name_plural == 'addresses'


class TestLetting:
    """Test cases for the Letting model."""

    @pytest.mark.django_db
    def test_letting_creation(self):
        """Test that a letting can be created with valid data."""
        # Create address first
        address = Address.objects.create(
            number=789,
            street='Rental Street',
            city='Rental City',
            state='RS',
            zip_code=98765,
            country_iso_code='RST'
        )
        
        # Create letting
        letting = Letting.objects.create(
            title='Beautiful Apartment',
            address=address
        )
        
        assert letting.title == 'Beautiful Apartment'
        assert letting.address == address

    @pytest.mark.django_db
    def test_letting_str_method(self):
        """Test the string representation of a letting."""
        address = Address.objects.create(
            number=101,
            street='Test Lane',
            city='Test City',
            state='TS',
            zip_code=10101,
            country_iso_code='TST'
        )
        
        letting = Letting.objects.create(
            title='Cozy House',
            address=address
        )
        
        assert str(letting) == 'Cozy House'

    @pytest.mark.django_db
    def test_letting_address_relationship(self):
        """Test the one-to-one relationship between letting and address."""
        address = Address.objects.create(
            number=202,
            street='Unique Street',
            city='Test City',
            state='TS',
            zip_code=20202,
            country_iso_code='TST'
        )
        
        letting = Letting.objects.create(
            title='Unique Property',
            address=address
        )
        
        # Test the relationship works both ways
        assert letting.address == address
        assert address.letting == letting

    @pytest.mark.django_db
    def test_letting_cascade_delete(self):
        """Test that deleting an address also deletes the associated letting."""
        address = Address.objects.create(
            number=303,
            street='Delete Street',
            city='Test City',
            state='TS',
            zip_code=30303,
            country_iso_code='TST'
        )
        
        letting = Letting.objects.create(
            title='Property to Delete',
            address=address
        )
        
        letting_id = letting.id
        
        # Delete the address
        address.delete()
        
        # Verify the letting was also deleted
        assert not Letting.objects.filter(id=letting_id).exists()

    @pytest.mark.django_db
    def test_letting_verbose_name_plural(self):
        """Test that the plural name is correctly set."""
        assert Letting._meta.verbose_name_plural == 'lettings'