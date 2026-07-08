from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Patient
from .forms import PatientForm


def patient_list(request):

    search = request.GET.get("search", "")

    patients = Patient.objects.all()

    if search:
        patients = patients.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(uhid__icontains=search)
            | Q(phone__icontains=search)
        )

    return render(
        request,
        "patients/patient_list.html",
        {
            "patients": patients,
            "search": search,
        },
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


def edit_patient(request, pk):

    patient = get_object_or_404(
        Patient,
        pk=pk,
    )

    if request.method == "POST":

        form = PatientForm(
            request.POST,
            request.FILES,
            instance=patient,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Patient updated successfully."
            )

            return redirect("patients")

    else:

        form = PatientForm(
            instance=patient,
        )

    return render(
        request,
        "patients/edit_patient.html",
        {
            "form": form,
            "patient": patient,
        },
    )


def delete_patient(request, pk):

    patient = get_object_or_404(
        Patient,
        pk=pk,
    )

    if request.method == "POST":

        patient.delete()

        messages.success(
            request,
            "Patient deleted successfully."
        )

        return redirect("patients")

    return render(
        request,
        "patients/delete_patient.html",
        {
            "patient": patient,
        },
    )
def view_patient(request, pk):

    patient = get_object_or_404(
        Patient,
        pk=pk,
    )

    return render(
        request,
        "patients/view_patient.html",
        {
            "patient": patient,
        },
    )
    