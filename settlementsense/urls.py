from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    # Authentication
    path(
        "",
        include("authentication.urls"),
    ),

    # Dashboard
    path(
        "",
        include("dashboard.urls"),
    ),

    # Patients
    path(
        "patients/",
        include("patients.urls"),
    ),

    # Doctors
    path(
        "doctors/",
        include("doctors.urls"),
    ),

    # Wards
    path(
        "wards/",
        include("wards.urls"),
    ),

    # Beds
    path(
        "beds/",
        include("beds.urls"),
    ),

    # Admissions
    path(
        "admissions/",
        include("admissions.urls"),
    ),

    # Appointments
    path(
        "appointments/",
        include("appointments.urls"),
    ),

    # Billing
    path(
        "billing/",
        include("billing.urls"),
    ),

    # Pharmacy
    path(
        "pharmacy/",
        include("pharmacy.urls"),
    ),

    # Reports
    path(
        "reports/",
        include("reports.urls"),
    ),

]