from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Django ka default User already username, email, password deta hai
    # Hum bas 2 extra cheez add kar rahe hain: role aur phone number

    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('worker', 'Worker'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
