from django.db import models


class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ("Cardiologist", "Cardiologist"),
        ("Neurologist", "Neurologist"),
        ("Orthopedic", "Orthopedic"),
        ("Pediatrician", "Pediatrician"),
        ("Gynecologist", "Gynecologist"),
        ("General Physician", "General Physician"),
        ("Dermatologist", "Dermatologist"),
        ("Psychiatrist", "Psychiatrist"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    full_name = models.CharField(max_length=100)
    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATION_CHOICES
    )
    qualification = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    experience = models.PositiveIntegerField(help_text="Years of Experience")
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name