from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Doctor
from .forms import DoctorForm


def doctor_list(request):

    search = request.GET.get("search", "")

    doctors = Doctor.objects.all()

    if search:

        doctors = doctors.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(doctor_id__icontains=search)
            | Q(phone__icontains=search)
            | Q(department__icontains=search)
            | Q(specialization__icontains=search)
        )

    return render(
        request,
        "doctors/doctor_list.html",
        {
            "doctors": doctors,
            "search": search,
        },
    )


def add_doctor(request):

    if request.method == "POST":

        form = DoctorForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Doctor added successfully.",
            )

            return redirect("doctors")

    else:

        form = DoctorForm()

    return render(
        request,
        "doctors/add_doctor.html",
        {
            "form": form,
        },
    )


def edit_doctor(request, pk):

    doctor = get_object_or_404(
        Doctor,
        pk=pk,
    )

    if request.method == "POST":

        form = DoctorForm(
            request.POST,
            request.FILES,
            instance=doctor,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Doctor updated successfully.",
            )

            return redirect("doctors")

    else:

        form = DoctorForm(
            instance=doctor,
        )

    return render(
        request,
        "doctors/edit_doctor.html",
        {
            "form": form,
            "doctor": doctor,
        },
    )


def delete_doctor(request, pk):

    doctor = get_object_or_404(
        Doctor,
        pk=pk,
    )

    if request.method == "POST":

        doctor.delete()

        messages.success(
            request,
            "Doctor deleted successfully.",
        )

        return redirect("doctors")

    return render(
        request,
        "doctors/delete_doctor.html",
        {
            "doctor": doctor,
        },
    )


def view_doctor(request, pk):

    doctor = get_object_or_404(
        Doctor,
        pk=pk,
    )

    return render(
        request,
        "doctors/view_doctor.html",
        {
            "doctor": doctor,
        },
    )