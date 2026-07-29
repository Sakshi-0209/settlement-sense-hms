from django import forms
from .models import Billing


class BillingForm(forms.ModelForm):

    class Meta:

        model = Billing

        fields = "__all__"

        widgets = {

            "bill_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Bill ID",
                }
            ),

            "patient": forms.Select(
                attrs={"class": "form-select"}
            ),

            "admission": forms.Select(
                attrs={"class": "form-select"}
            ),

            "appointment": forms.Select(
                attrs={"class": "form-select"}
            ),

            "bill_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "total_amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Total Amount",
                }
            ),

            "paid_amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Paid Amount",
                }
            ),

            "balance_amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Balance Amount",
                }
            ),

            "payment_status": forms.Select(
                attrs={"class": "form-select"}
            ),

            "payment_method": forms.Select(
                attrs={"class": "form-select"}
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Notes",
                }
            ),
        }