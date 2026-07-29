from django.contrib import admin
from .models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):

    list_display = (
        "medicine_id",
        "name",
        "category",
        "manufacturer",
        "quantity",
        "price",
        "expiry_date",
    )

    search_fields = (
        "medicine_id",
        "name",
        "manufacturer",
    )

    list_filter = (
        "category",
        "expiry_date",
    )

    ordering = (
        "name",
    )