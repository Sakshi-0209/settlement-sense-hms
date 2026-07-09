from django import forms
from .models import Ward


class WardForm(forms.ModelForm):

    class Meta:
        model = Ward
        fields = "__all__"

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control",
                }
            ),
        }