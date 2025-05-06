from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('normal', 'Normal'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='normal',
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

    def save(self, *args, **kwargs):
        if self.role not in dict(self.ROLE_CHOICES):
            raise ValueError(f"Invalid role: {self.role}")
        super().save(*args, **kwargs)

