from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment

        fields = "__all__"

        widgets = {

            "appointment_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Appointment ID",
                }
            ),

            "patient": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "doctor": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "appointment_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "appointment_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),

            "reason": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Reason for appointment",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Additional notes",
                }
            ),
        }