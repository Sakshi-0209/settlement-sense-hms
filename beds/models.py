from django.db import models
from wards.models import Ward


class Bed(models.Model):

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Occupied", "Occupied"),
        ("Cleaning", "Cleaning"),
        ("Maintenance", "Maintenance"),
    ]

    bed_number = models.CharField(
        max_length=20,
        unique=True
    )

    ward = models.ForeignKey(
        Ward,
        on_delete=models.PROTECT,
        related_name="beds"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.bed_number} ({self.ward.ward_name})"