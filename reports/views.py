from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from patients.models import Patient
from doctors.models import Doctor
from admissions.models import Admission
from appointments.models import Appointment
from billing.models import Billing
from pharmacy.models import Medicine


@login_required
def reports_dashboard(request):

    context = {

        "patient_count": Patient.objects.count(),

        "doctor_count": Doctor.objects.count(),

        "admission_count": Admission.objects.count(),

        "appointment_count": Appointment.objects.count(),

        "billing_count": Billing.objects.count(),

        "medicine_count": Medicine.objects.count(),

    }

    return render(
        request,
        "reports/report_dashboard.html",
        context,
    )


@login_required
def patient_report(request):

    patients = Patient.objects.all()

    return render(
        request,
        "reports/patient_report.html",
        {
            "patients": patients
        },
    )


@login_required
def doctor_report(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        "reports/doctor_report.html",
        {
            "doctors": doctors
        },
    )


@login_required
def admission_report(request):

    admissions = Admission.objects.all()

    return render(
        request,
        "reports/admission_report.html",
        {
            "admissions": admissions
        },
    )


@login_required
def appointment_report(request):

    appointments = Appointment.objects.all()

    return render(
        request,
        "reports/appointment_report.html",
        {
            "appointments": appointments
        },
    )


@login_required
def billing_report(request):

    bills = Billing.objects.all()

    return render(
        request,
        "reports/billing_report.html",
        {
            "bills": bills
        },
    )


@login_required
def pharmacy_report(request):

    medicines = Medicine.objects.all()

    return render(
        request,
        "reports/pharmacy_report.html",
        {
            "medicines": medicines
        },
    )