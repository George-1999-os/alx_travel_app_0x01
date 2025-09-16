from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from ..models import Listing, Booking


class TestAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="apiuser", password="password")
        self.listing = Listing.objects.create(title="API House", description="desc", price_per_night=150)

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
