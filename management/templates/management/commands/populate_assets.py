from django.core.management.base import BaseCommand
from management.models import Asset

class Command(BaseCommand):
    help = 'Populate database with sample assets'

    def handle(self, *args, **kwargs):
        Asset.objects.create(serial_number="SN12345", brand="HP", model="EliteBook", status="Available", assigned_to=None)
        Asset.objects.create(serial_number="SN67890", brand="Dell", model="XPS 13", status="Available", assigned_to=None)
        self.stdout.write(self.style.SUCCESS('Sample assets added successfully'))
