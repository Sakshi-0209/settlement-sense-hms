from django.db import models
from django.db.models import Max


class Doctor(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    doctor_id = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )

    department = models.CharField(
        max_length=100,
    )

    specialization = models.CharField(
        max_length=100,
    )

    qualification = models.CharField(
        max_length=150,
    )

    experience = models.PositiveIntegerField(
        help_text="Experience in years",
    )

    phone = models.CharField(
        max_length=15,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
    )

    address = models.TextField()

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    photo = models.ImageField(
        upload_to="doctors/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def save(self, *args, **kwargs):

        if not self.doctor_id:

            last = Doctor.objects.aggregate(Max("id"))

            last_id = last["id__max"] or 0

            self.doctor_id = f"DOC{last_id + 1:04d}"

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.doctor_id} - Dr. {self.first_name} {self.last_name}"

    class Meta:

        ordering = ["first_name"]