from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    REGISTRATION_CHOICES = [
        ('email', 'Email'),
        ('facebook', 'Facebook'),
        ('google', 'Google'),
    ]

    registration_method = models.CharField(
        max_length=20, 
        choices=REGISTRATION_CHOICES, 
        default='email'
    )

    def __str__(self):
        return self.username
