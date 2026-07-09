from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Bed
from .forms import BedForm


def bed_list(request):

    search = request.GET.get("search", "")

    beds = Bed.objects.select_related("ward").all()

    if search:

        beds = beds.filter(

            Q(bed_number__icontains=search)
            | Q(ward__ward_name__icontains=search)
            | Q(status__icontains=search)

        )

    return render(
        request,
        "beds/bed_list.html",
        {
            "beds": beds,
            "search": search,
        },
    )


def add_bed(request):

    if request.method == "POST":

        form = BedForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Bed added successfully.",
            )

            return redirect("beds")

    else:

        form = BedForm()

    return render(
        request,
        "beds/add_bed.html",
        {
            "form": form,
        },
    )


def view_bed(request, pk):

    bed = get_object_or_404(
        Bed,
        pk=pk,
    )

    return render(
        request,
        "beds/view_bed.html",
        {
            "bed": bed,
        },
    )


def edit_bed(request, pk):

    bed = get_object_or_404(
        Bed,
        pk=pk,
    )

    if request.method == "POST":

        form = BedForm(
            request.POST,
            instance=bed,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Bed updated successfully.",
            )

            return redirect("beds")

    else:

        form = BedForm(
            instance=bed,
        )

    return render(
        request,
        "beds/edit_bed.html",
        {
            "form": form,
            "bed": bed,
        },
    )


def delete_bed(request, pk):

    bed = get_object_or_404(
        Bed,
        pk=pk,
    )

    if request.method == "POST":

        bed.delete()

        messages.success(
            request,
            "Bed deleted successfully.",
        )

        return redirect("beds")

    return render(
        request,
        "beds/delete_bed.html",
        {
            "bed": bed,
        },
    )