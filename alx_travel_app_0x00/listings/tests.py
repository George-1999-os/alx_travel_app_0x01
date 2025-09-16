from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Listing, Booking, Review


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


class TestAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="apiuser", password="password")
        self.listing = Listing.objects.create(title="API House", description="desc", price_per_night=150
)

    def test_list_listings(self):
        response = self.client.get("/api/listings/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "API House")

    def test_create_booking(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "listing": self.listing.id,
            "user": self.user.id,
            "start_date": "2025-09-15",
            "end_date": "2025-09-18"
        }
        response = self.client.post("/api/bookings/", data)
        self.assertEqual(response.status_code, 201)
