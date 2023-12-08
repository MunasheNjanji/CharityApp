# models.py

from django.db import models
from user_management.models import CustomUser  # Import CustomUser model from the Authentication and User Management App
from campaign_management.models import Campaign  # Import Campaign model from the Campaign Management App

class Donation(models.Model):
    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.username} - {self.campaign.title}"
