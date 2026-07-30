from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Medicine
from .forms import MedicineForm


@login_required
def medicine_list(request):

    medicines = Medicine.objects.all()

    context = {
        "medicines": medicines
    }

    return render(
        request,
        "pharmacy/medicine_list.html",
        context,
    )


@login_required
def add_medicine(request):

    if request.method == "POST":

        form = MedicineForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("pharmacy")

    else:

        form = MedicineForm()

    context = {
        "form": form
    }

    return render(
        request,
        "pharmacy/add_medicine.html",
        context,
    )


@login_required
def view_medicine(request, pk):

    medicine = get_object_or_404(
        Medicine,
        pk=pk
    )

    context = {
        "medicine": medicine
    }

    return render(
        request,
        "pharmacy/view_medicine.html",
        context,
    )


@login_required
def edit_medicine(request, pk):

    medicine = get_object_or_404(
        Medicine,
        pk=pk
    )

    if request.method == "POST":

        form = MedicineForm(
            request.POST,
            instance=medicine
        )

        if form.is_valid():

            form.save()

            return redirect("pharmacy")

    else:

        form = MedicineForm(
            instance=medicine
        )

    context = {
        "form": form
    }

    return render(
        request,
        "pharmacy/edit_medicine.html",
        context,
    )


@login_required
def delete_medicine(request, pk):

    medicine = get_object_or_404(
        Medicine,
        pk=pk
    )

    if request.method == "POST":

        medicine.delete()

        return redirect("pharmacy")

    context = {
        "medicine": medicine
    }

    return render(
        request,
        "pharmacy/delete_medicine.html",
        context,
    )