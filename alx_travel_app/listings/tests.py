from django.test import TestCase
from .models import Listing

class ListingModelTest(TestCase):
    def test_create_listing(self):
        listing = Listing.objects.create(
            title="Test Listing",
            description="Test description",
            price=100.00,
        )
        self.assertEqual(str(listing), "Test Listing")
