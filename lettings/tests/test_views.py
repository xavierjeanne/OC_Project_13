"""
Tests for lettings views.

This module contains unit and integration tests for the lettings views,
using pytest.mark.django_db for database access.
"""
import pytest
from django.urls import reverse
from django.test import Client

from lettings.models import Address, Letting


class TestLettingsViews:
    """Test cases for lettings views."""

    @pytest.mark.django_db
    def test_lettings_index_view(self):
        """Test the lettings index view displays all lettings."""
        client = Client()
        
        # Create test data
        address1 = Address.objects.create(
            number=123,
            street='First Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        
        address2 = Address.objects.create(
            number=456,
            street='Second Street',
            city='Test City',
            state='TS',
            zip_code=54321,
            country_iso_code='TST'
        )
        
        letting1 = Letting.objects.create(
            title='First Property',
            address=address1
        )
        
        letting2 = Letting.objects.create(
            title='Second Property',
            address=address2
        )
        
        # Test the view
        url = reverse('lettings:index')
        response = client.get(url)
        
        assert response.status_code == 200
        assert 'lettings_list' in response.context
        assert len(response.context['lettings_list']) == 2
        assert letting1 in response.context['lettings_list']
        assert letting2 in response.context['lettings_list']
        assert 'First Property' in response.content.decode()
        assert 'Second Property' in response.content.decode()

    @pytest.mark.django_db
    def test_letting_detail_view(self, client):
        """Test the letting detail view displays specific letting info."""
        # Create test data
        address = Address.objects.create(
            number=789,
            street='Detail Street',
            city='Detail City',
            state='DS',
            zip_code=78901,
            country_iso_code='DST'
        )
        
        letting = Letting.objects.create(
            title='Detailed Property',
            address=address
        )
        
        # Test the view
        url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        response = client.get(url)
        
        assert response.status_code == 200
        assert response.context['title'] == 'Detailed Property'
        assert response.context['address'] == address
        assert 'Detailed Property' in response.content.decode()
        assert '789 Detail Street' in response.content.decode()

    @pytest.mark.django_db
    def test_letting_detail_view_not_found(self, client):
        """Test the letting detail view returns 404 for non-existent letting."""
        url = reverse('lettings:letting', kwargs={'letting_id': 999})
        response = client.get(url)
        
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_empty_lettings_index(self, client):
        """Test the lettings index view when no lettings exist."""
        url = reverse('lettings:index')
        response = client.get(url)
        
        assert response.status_code == 200
        assert 'lettings_list' in response.context
        assert len(response.context['lettings_list']) == 0