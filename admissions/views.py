from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Admission
from .forms import AdmissionForm


@login_required
def admission_list(request):

    search = request.GET.get("search", "")

    admissions = Admission.objects.select_related(
        "patient",
        "doctor",
        "ward",
        "bed",
    )

    if search:

        admissions = admissions.filter(

            Q(admission_id__icontains=search)
            | Q(patient__first_name__icontains=search)
            | Q(patient__last_name__icontains=search)
            | Q(doctor__first_name__icontains=search)
            | Q(doctor__last_name__icontains=search)

        )

    return render(
        request,
        "admissions/admission_list.html",
        {
            "admissions": admissions,
            "search": search,
        },
    )


@login_required
def add_admission(request):

    if request.method == "POST":

        form = AdmissionForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Admission created successfully.",
            )

            return redirect("admissions")

    else:

        form = AdmissionForm()

    return render(
        request,
        "admissions/add_admission.html",
        {
            "form": form,
        },
    )


@login_required
def view_admission(request, pk):

    admission = get_object_or_404(
        Admission,
        pk=pk,
    )

    return render(
        request,
        "admissions/view_admission.html",
        {
            "admission": admission,
        },
    )


@login_required
def edit_admission(request, pk):

    admission = get_object_or_404(
        Admission,
        pk=pk,
    )

    if request.method == "POST":

        form = AdmissionForm(
            request.POST,
            instance=admission,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Admission updated successfully.",
            )

            return redirect("admissions")

    else:

        form = AdmissionForm(
            instance=admission,
        )

    return render(
        request,
        "admissions/edit_admission.html",
        {
            "form": form,
            "admission": admission,
        },
    )


@login_required
def delete_admission(request, pk):

    admission = get_object_or_404(
        Admission,
        pk=pk,
    )

    if request.method == "POST":

        admission.delete()

        messages.success(
            request,
            "Admission deleted successfully.",
        )

        return redirect("admissions")

    return render(
        request,
        "admissions/delete_admission.html",
        {
            "admission": admission,
        },
    )