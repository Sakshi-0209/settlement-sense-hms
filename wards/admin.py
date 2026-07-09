from django.contrib import admin
from .models import Ward


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):

    list_display = (
        "ward_name",
        "ward_type",
        "floor",
        "total_beds",
        "available_beds",
        "status",
    )

    list_filter = (
        "ward_type",
        "status",
    )

    search_fields = (
        "ward_name",
        "incharge",
    )