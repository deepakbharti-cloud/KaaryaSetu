from django.db import models
from accounts.models import User
from workers.models import WorkerProfile


class Booking(models.Model):
    # Jab customer kisi worker ko hire karta hai, ek Booking banti hai

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_made')
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, related_name='bookings_received')

    service_date = models.DateField()
    description = models.TextField(help_text="Customer kya kaam chahta hai, uska detail")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer.username} -> {self.worker.user.username}"
