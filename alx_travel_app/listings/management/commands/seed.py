from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from django_seed import Seed
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        # Ensure at least 2 users exist
        if User.objects.count() < 2:
            User.objects.create_user(username='user1', password='password')
            User.objects.create_user(username='user2', password='password')

        users = list(User.objects.all())

        # Seed Listings
        seeder.add_entity(Listing, 10, {
            'owner': lambda x: random.choice(users),
            'price_per_night': lambda x: round(random.uniform(50, 500), 2)
        })

        # Seed Bookings
        seeder.add_entity(Booking, 20, {
            'user': lambda x: random.choice(users),
            'listing': lambda x: random.choice(Listing.objects.all()),
            'start_date': lambda x: datetime.today() + timedelta(days=random.randint(1, 30)),
            'end_date': lambda x: datetime.today() + timedelta(days=random.randint(31, 60))
        })

        # Seed Reviews
        seeder.add_entity(Review, 20, {
            'user': lambda x: random.choice(users),
            'listing': lambda x: random.choice(Listing.objects.all()),
            'rating': lambda x: random.randint(1, 5),
            'comment': lambda x: f"This is a sample review {random.randint(1,100)}"
        })

        seeder.execute()
        self.stdout.write(self.style.SUCCESS('Database successfully seeded!'))
