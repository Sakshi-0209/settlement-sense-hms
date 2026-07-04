from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "specialization",
        "department",
        "phone",
        "consultation_fee",
        "status",
    )

    search_fields = (
        "full_name",
        "department",
        "phone",
    )

    list_filter = (
        "specialization",
        "status",
    )