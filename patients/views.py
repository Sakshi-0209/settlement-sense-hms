from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm


def patient_list(request):

    patients = Patient.objects.all()

    return render(
        request,
        "patients/patient_list.html",
        {"patients": patients},
    )


def add_patient(request):

    if request.method == "POST":

        form = PatientForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect("patients")

    else:

        form = PatientForm()

    return render(
        request,
        "patients/add_patient.html",
        {"form": form},
    )