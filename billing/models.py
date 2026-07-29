from django.db import models

from patients.models import Patient
from admissions.models import Admission
from appointments.models import Appointment


class Billing(models.Model):

    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Partial", "Partial"),
        ("Paid", "Paid"),
    ]

    PAYMENT_METHOD = [
        ("Cash", "Cash"),
        ("Card", "Card"),
        ("UPI", "UPI"),
        ("Net Banking", "Net Banking"),
    ]

    bill_id = models.CharField(
        max_length=20,
        unique=True,
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="bills",
    )

    admission = models.ForeignKey(
        Admission,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bills",
    )

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bills",
    )

    bill_date = models.DateField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    balance_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending",
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD,
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.bill_id} - {self.patient}"