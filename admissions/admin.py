from django.contrib import admin
from .models import Admission


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):

    list_display = (
        "admission_id",
        "patient",
        "doctor",
        "ward",
        "bed",
        "status",
        "admission_date",
    )

    list_filter = (
        "status",
        "ward",
        "doctor",
    )

    search_fields = (
        "admission_id",
        "patient__first_name",
        "patient__last_name",
        "doctor__first_name",
        "doctor__last_name",
    )

    ordering = (
        "-admission_date",
    )