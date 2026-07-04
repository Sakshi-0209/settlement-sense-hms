from django.db import models
from django.db.models import Max


class Patient(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Discharged", "Discharged"),
    ]

    uhid = models.CharField(
        max_length=12,
        unique=True,
        editable=False
    )

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUP_CHOICES
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField(
        blank=True,
        null=True
    )

    address = models.TextField()

    emergency_contact = models.CharField(max_length=15)

    guardian_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    allergies = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.uhid:
            last_patient = Patient.objects.aggregate(Max("id"))
            last_id = last_patient["id__max"] or 0
            self.uhid = f"UHID{last_id + 1:06d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.uhid} - {self.first_name} {self.last_name}"