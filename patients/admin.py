from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (
        "uhid",
        "first_name",
        "last_name",
        "gender",
        "blood_group",
        "phone",
        "status",
    )

    search_fields = (
        "uhid",
        "first_name",
        "last_name",
        "phone",
    )

    list_filter = (
        "gender",
        "blood_group",
        "status",
    )

    ordering = ("uhid",)