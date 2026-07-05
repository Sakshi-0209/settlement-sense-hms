from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Patient
from .forms import PatientForm


def patient_list(request):
    patients = Patient.objects.all()

    context = {
        "patients": patients,
    }

    return render(
        request,
        "patients/patient_list.html",
        context,
    )


def add_patient(request):

    if request.method == "POST":

        form = PatientForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Patient added successfully."
            )

            return redirect("patients")

    else:

        form = PatientForm()

    return render(
        request,
        "patients/add_patient.html",
        {
            "form": form,
        },
    )