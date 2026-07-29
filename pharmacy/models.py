from django.db import models


class Medicine(models.Model):

    medicine_id = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    manufacturer = models.CharField(max_length=100)

    batch_number = models.CharField(max_length=50)

    expiry_date = models.DateField()

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name