from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Property(models.Model):
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    num_rooms = models.IntegerField()
    created_by = models.ForeignKey(
            User, 
            on_delete=models.CASCADE, 
            related_name='properties'
        )

    def __str__(self):
        return f"{self.address}, {self.city}"
