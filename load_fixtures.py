#!/usr/bin/env python
"""
Script to load existing data fixtures for the OC Lettings application.
Run this after migrations to populate the database with production data.
"""
import os
import sys
import django
from pathlib import Path
from django.core.management import call_command
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
django.setup()


def load_fixtures():
    """Load data from fixtures.json if it exists."""
    fixtures_path = Path(__file__).parent / 'fixtures.json'

    if not fixtures_path.exists():
        print("fixtures.json not found. Skipping data import.")
        print("   Run 'python manage.py dumpdata' locally to create fixtures.")
        return

    print("📦 Loading existing data from fixtures.json...")

    try:
        # Load the fixtures
        call_command('loaddata', 'fixtures.json', verbosity=2)

        print("\nData loaded successfully!")
        print(f"Total users: {User.objects.count()}")

        # Display admin credentials if exists
        admin_user = User.objects.filter(username='admin', is_superuser=True).first()
        if admin_user:
            print(f"Admin user found: {admin_user.username} ({admin_user.email})")
            print("   Use your existing password to login.")

    except Exception as e:
        print(f"Error loading fixtures: {e}")
        sys.exit(1)


if __name__ == '__main__':
    load_fixtures()
