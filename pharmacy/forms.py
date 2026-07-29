from django import forms
from .models import Medicine


class MedicineForm(forms.ModelForm):

    class Meta:

        model = Medicine

        fields = "__all__"

        widgets = {

            "medicine_id": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "category": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "manufacturer": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "batch_number": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "expiry_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "quantity": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "price": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
            }),
        }