from django.contrib import admin
from .models import Billing


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):

    list_display = (
        "bill_id",
        "patient",
        "bill_date",
        "total_amount",
        "paid_amount",
        "balance_amount",
        "payment_status",
    )

    search_fields = (
        "bill_id",
        "patient__first_name",
        "patient__last_name",
    )

    list_filter = (
        "payment_status",
        "payment_method",
        "bill_date",
    )

    ordering = (
        "-bill_date",
    )