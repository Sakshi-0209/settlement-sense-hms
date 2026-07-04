from django.db import models

class Ward(models.Model):
    WARD_TYPES = [
        ("General", "General"),
        ("ICU", "ICU"),
        ("NICU", "NICU"),
        ("Private", "Private"),
        ("Semi Private", "Semi Private"),
        ("Emergency", "Emergency"),
    ]

    STATUS = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    ward_name = models.CharField(max_length=100)
    ward_type = models.CharField(max_length=30, choices=WARD_TYPES)
    floor = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default="Active")

    def __str__(self):
        return self.ward_name
