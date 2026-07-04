from django.contrib import admin
from .models import Bed


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):

    list_display = (
        "bed_number",
        "ward",
        "status",
    )

    list_filter = (
        "ward",
        "status",
    )

    search_fields = (
        "bed_number",
    )

    ordering = (
        "ward",
        "bed_number",
    )