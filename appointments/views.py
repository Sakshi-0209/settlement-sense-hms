from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Appointment
from .forms import AppointmentForm


@login_required
def appointment_list(request):

    appointments = Appointment.objects.all()

    context = {
        "appointments": appointments
    }

    return render(
        request,
        "appointments/appointment_list.html",
        context,
    )


@login_required
def add_appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("appointments")

    else:

        form = AppointmentForm()

    context = {
        "form": form
    }

    return render(
        request,
        "appointments/add_appointment.html",
        context,
    )


@login_required
def view_appointment(request, pk):

    appointment = get_object_or_404(
        Appointment,
        pk=pk
    )

    context = {
        "appointment": appointment
    }

    return render(
        request,
        "appointments/view_appointment.html",
        context,
    )


@login_required
def edit_appointment(request, pk):

    appointment = get_object_or_404(
        Appointment,
        pk=pk
    )

    if request.method == "POST":

        form = AppointmentForm(
            request.POST,
            instance=appointment
        )

        if form.is_valid():

            form.save()

            return redirect("appointments")

    else:

        form = AppointmentForm(
            instance=appointment
        )

    context = {
        "form": form
    }

    return render(
        request,
        "appointments/edit_appointment.html",
        context,
    )


@login_required
def delete_appointment(request, pk):

    appointment = get_object_or_404(
        Appointment,
        pk=pk
    )

    if request.method == "POST":

        appointment.delete()

        return redirect("appointments")

    context = {
        "appointment": appointment
    }

    return render(
        request,
        "appointments/delete_appointment.html",
        context,
    )