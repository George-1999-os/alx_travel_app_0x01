from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Listing, Booking, Review


class TestListingModel(TestCase):
    def test_create_listing(self):
        listing = Listing.objects.create(
            title="Test House",
            description="A nice test house",
            price_per_night=100
        )
        self.assertEqual(listing.title, "Test House")
        self.assertEqual(listing.price_per_night, 100)


class TestBookingModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.listing = Listing.objects.create(title="Test Listing", description="desc", price_per_night=50)

    def test_create_booking(self):
        booking = Booking.objects.create(
            listing=self.listing,
            user=self.user,
            start_date="2025-09-15",
            end_date="2025-09-20",
        )
        self.assertEqual(booking.listing.title, "Test Listing")
        self.assertEqual(booking.user.username, "testuser")


class TestReviewModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="reviewer", password="password")
        self.listing = Listing.objects.create(title="Review House", description="desc", price_per_night=200)

    def test_create_review(self):
        review = Review.objects.create(
            listing=self.listing,
            user=self.user,
            rating=4,
            comment="Great place!"
        )
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.comment, "Great place!")
