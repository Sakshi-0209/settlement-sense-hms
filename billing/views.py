from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Billing
from .forms import BillingForm


@login_required
def billing_list(request):

    bills = Billing.objects.all()

    context = {
        "bills": bills
    }

    return render(
        request,
        "billing/billing_list.html",
        context,
    )


@login_required
def add_billing(request):

    if request.method == "POST":

        form = BillingForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("billing")

    else:

        form = BillingForm()

    context = {
        "form": form
    }

    return render(
        request,
        "billing/add_billing.html",
        context,
    )


@login_required
def view_billing(request, pk):

    bill = get_object_or_404(
        Billing,
        pk=pk
    )

    context = {
        "bill": bill
    }

    return render(
        request,
        "billing/view_billing.html",
        context,
    )


@login_required
def edit_billing(request, pk):

    bill = get_object_or_404(
        Billing,
        pk=pk
    )

    if request.method == "POST":

        form = BillingForm(
            request.POST,
            instance=bill
        )

        if form.is_valid():

            form.save()

            return redirect("billing")

    else:

        form = BillingForm(
            instance=bill
        )

    context = {
        "form": form
    }

    return render(
        request,
        "billing/edit_billing.html",
        context,
    )


@login_required
def delete_billing(request, pk):

    bill = get_object_or_404(
        Billing,
        pk=pk
    )

    if request.method == "POST":

        bill.delete()

        return redirect("billing")

    context = {
        "bill": bill
    }

    return render(
        request,
        "billing/delete_billing.html",
        context,
    )