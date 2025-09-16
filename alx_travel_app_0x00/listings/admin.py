from django.contrib import admin
from .models import Listing, Booking, Review


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price_per_night", "created_at")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "user", "start_date", "end_date")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "user", "rating", "created_at")
