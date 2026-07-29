from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.reports_dashboard,
        name="reports",
    ),

    path(
        "patients/",
        views.patient_report,
        name="patient_report",
    ),

    path(
        "doctors/",
        views.doctor_report,
        name="doctor_report",
    ),

    path(
        "admissions/",
        views.admission_report,
        name="admission_report",
    ),

    path(
        "appointments/",
        views.appointment_report,
        name="appointment_report",
    ),

    path(
        "billing/",
        views.billing_report,
        name="billing_report",
    ),

    path(
        "pharmacy/",
        views.pharmacy_report,
        name="pharmacy_report",
    ),

]