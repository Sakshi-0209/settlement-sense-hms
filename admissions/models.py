from django.db import models

from patients.models import Patient
from doctors.models import Doctor
from wards.models import Ward
from beds.models import Bed


class Admission(models.Model):

    STATUS_CHOICES = [
        ("Admitted", "Admitted"),
        ("Discharged", "Discharged"),
    ]

    admission_id = models.CharField(
        max_length=20,
        unique=True,
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name="admissions",
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name="admissions",
    )

    ward = models.ForeignKey(
        Ward,
        on_delete=models.PROTECT,
        related_name="admissions",
    )

    bed = models.ForeignKey(
        Bed,
        on_delete=models.PROTECT,
        related_name="admissions",
    )

    admission_date = models.DateTimeField()

    discharge_date = models.DateTimeField(
        blank=True,
        null=True,
    )

    diagnosis = models.TextField()

    notes = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Admitted",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.admission_id} - {self.patient}"

    class Meta:
        ordering = ["-admission_date"]