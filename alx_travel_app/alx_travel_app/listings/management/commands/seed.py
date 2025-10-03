echo "from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **options):
        self.stdout.write('Seeder placeholder')" > alx_travel_app/listings/management/commands/seed.py
