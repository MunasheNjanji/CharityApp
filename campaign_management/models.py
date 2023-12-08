from django.db import models
from charity_management.models import Charity

class Campaign(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    start_date = models.DateField()
    end_date = models.DateField()
    # Other fields as needed

    def __str__(self):
        return self.title
            