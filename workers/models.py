from django.db import models
from accounts.models import User
from categories.models import Category


class WorkerProfile(models.Model):
    # Ek worker (labour) ki extra details yaha store hongi

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    experience_years = models.PositiveIntegerField(default=0)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bio = models.TextField(blank=True)
    area = models.CharField(max_length=150, help_text="Worker ka area/location")

    is_verified = models.BooleanField(default=False)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.category}"
