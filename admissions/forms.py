from django import forms
from .models import Admission
from beds.models import Bed
from django.db.models import Q


class AdmissionForm(forms.ModelForm):

    class Meta:
        model = Admission
        fields = "__all__"

        widgets = {

            "admission_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Admission ID",
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

            "ward": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "bed": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "admission_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),

            "discharge_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),

            "diagnosis": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Admission
        if not self.instance.pk:
            self.fields["bed"].queryset = Bed.objects.filter(
                status="Available"
            )

        # Edit Admission
        else:
            self.fields["bed"].queryset = Bed.objects.filter(
                Q(status="Available") |
                Q(pk=self.instance.bed.pk)
            )