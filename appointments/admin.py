from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "appointment_id",
        "patient",
        "doctor",
        "appointment_date",
        "appointment_time",
        "status",
    )

    search_fields = (
        "appointment_id",
        "patient__first_name",
        "patient__last_name",
        "doctor__first_name",
        "doctor__last_name",
    )

    list_filter = (
        "status",
        "appointment_date",
        "doctor",
    )

    ordering = (
        "-appointment_date",
        "-appointment_time",
    )