from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beach House", "description": "A lovely house by the sea.", "price_per_night": 120.50, "location": "Lagos"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.", "price_per_night": 85.00, "location": "Jos"},
            {"title": "City Apartment", "description": "Modern apartment in the city center.", "price_per_night": 200.00, "location": "Abuja"},
        ]

        for data in sample_listings:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
