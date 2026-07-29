"""
URL configuration for settlementsense project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        include("dashboard.urls"),
    ),

    path(
        "patients/",
        include("patients.urls"),
    ),

    path(
        "doctors/",
        include("doctors.urls"),
    ),

    path(
        "wards/",
        include("wards.urls"),
    ),

    path(
        "beds/",
        include("beds.urls"),
    ),
    path(
        "admissions/",
        include("admissions.urls"),
    ),

    path(
        "appointments/",
        include("appointments.urls"),
    ),

    path(
        "billing/",
        include("billing.urls"),
    ),
    path(
        "pharmacy/",
        include("pharmacy.urls"),
    ),
    path(
        "reports/",
        include("reports.urls"),
    )
    

] 