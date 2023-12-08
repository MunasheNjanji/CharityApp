from django.db import models

# Create your models here.
class Charity(models.Model):
    name = models.CharField(max_length=255, verbose_name="Charity")
    description = models.TextField()
    verification_status = models.BooleanField(default=False)


    def __str__(self):
        return self.name
