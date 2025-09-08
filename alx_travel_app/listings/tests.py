from django.test import TestCase
from .models import Listing

class ListingModelTest(TestCase):
    def test_create_listing(self):
        listing = Listing.objects.create(title="Test", description="Testing", price=100.00)
        self.assertEqual(listing.title, "Test")
