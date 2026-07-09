from django.db import models


class Ward(models.Model):

    WARD_TYPES = [
        ("General", "General"),
        ("Private", "Private"),
        ("ICU", "ICU"),
        ("Emergency", "Emergency"),
        ("Maternity", "Maternity"),
    ]

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Full", "Full"),
        ("Closed", "Closed"),
    ]

    ward_name = models.CharField(
        max_length=100,
        unique=True,
    )

    ward_type = models.CharField(
        max_length=30,
        choices=WARD_TYPES,
    )

    floor = models.CharField(
        max_length=30,
    )

    total_beds = models.PositiveIntegerField()

    available_beds = models.PositiveIntegerField()

    incharge = models.CharField(
        max_length=100,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available",
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.ward_name

    class Meta:
        ordering = ["ward_name"]