from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        "doctor_id",
        "first_name",
        "last_name",
        "department",
        "specialization",
        "phone",
        "status",
    )

    search_fields = (
        "doctor_id",
        "first_name",
        "last_name",
        "department",
        "phone",
    )

    list_filter = (
        "department",
        "status",
    )

    ordering = (
        "first_name",
    )