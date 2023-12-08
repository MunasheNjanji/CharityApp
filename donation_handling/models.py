# models.py

from django.db import models
from django.contrib.auth import get_user_model
from campaign_management.models import Campaign  # Import Campaign model from the Campaign Management App

class Donation(models.Model):
    User = get_user_model()
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.username} - {self.campaign.title}"
