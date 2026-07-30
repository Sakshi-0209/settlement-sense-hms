from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Ward
from .forms import WardForm


@login_required
def ward_list(request):

    search = request.GET.get("search", "")

    wards = Ward.objects.all()

    if search:
        wards = wards.filter(
            Q(ward_name__icontains=search)
            | Q(ward_type__icontains=search)
            | Q(incharge__icontains=search)
        )

    return render(
        request,
        "wards/ward_list.html",
        {
            "wards": wards,
            "search": search,
        },
    )


@login_required
def add_ward(request):

    if request.method == "POST":

        form = WardForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Ward added successfully.",
            )

            return redirect("wards")

    else:

        form = WardForm()

    return render(
        request,
        "wards/add_ward.html",
        {
            "form": form,
        },
    )


@login_required
def view_ward(request, pk):

    ward = get_object_or_404(
        Ward,
        pk=pk,
    )

    return render(
        request,
        "wards/view_ward.html",
        {
            "ward": ward,
        },
    )


@login_required
def edit_ward(request, pk):

    ward = get_object_or_404(
        Ward,
        pk=pk,
    )

    if request.method == "POST":

        form = WardForm(
            request.POST,
            instance=ward,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Ward updated successfully.",
            )

            return redirect("wards")

    else:

        form = WardForm(
            instance=ward,
        )

    return render(
        request,
        "wards/edit_ward.html",
        {
            "form": form,
            "ward": ward,
        },
    )


@login_required
def delete_ward(request, pk):

    ward = get_object_or_404(
        Ward,
        pk=pk,
    )

    if request.method == "POST":

        ward.delete()

        messages.success(
            request,
            "Ward deleted successfully.",
        )

        return redirect("wards")

    return render(
        request,
        "wards/delete_ward.html",
        {
            "ward": ward,
        },
    )