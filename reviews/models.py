from django.db import models
from bookings.models import Booking


class Review(models.Model):
    # Kaam complete hone ke baad customer worker ko rating deta hai

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(help_text="1 se 5 ke beech")
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for Booking #{self.booking.id} - {self.rating} stars"
