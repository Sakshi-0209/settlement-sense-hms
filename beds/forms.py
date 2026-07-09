from django import forms
from .models import Bed


class BedForm(forms.ModelForm):

    class Meta:
        model = Bed
        fields = "__all__"

        widgets = {

            "bed_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Bed Number",
                }
            ),

            "ward": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter Remarks",
                }
            ),
        }