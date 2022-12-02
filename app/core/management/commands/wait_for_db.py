"""
Django command to wait for the DB to become available
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for the DB."""

    def handle(self, *args, **options):
        pass