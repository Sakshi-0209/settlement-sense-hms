from django.contrib import admin
from .models import Bed


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):

    list_display = (
        "bed_number",
        "ward",
        "status",
        "created_at",
    )

    list_filter = (
        "ward",
        "status",
    )

    search_fields = (
        "bed_number",
        "ward__ward_name",
    )

    ordering = (
        "bed_number",
    )