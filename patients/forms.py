from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient

        exclude = [
            "uhid",
            "created_at",
            "updated_at",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),

            "gender": forms.Select(attrs={"class": "form-select"}),

            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),

            "blood_group": forms.Select(attrs={"class": "form-select"}),

            "phone": forms.TextInput(attrs={"class": "form-control"}),

            "aadhaar_number": forms.TextInput(attrs={"class": "form-control"}),

            "email": forms.EmailInput(attrs={"class": "form-control"}),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "guardian_name": forms.TextInput(attrs={"class": "form-control"}),

            "emergency_contact": forms.TextInput(attrs={"class": "form-control"}),

            "allergies": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "photo": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),

            "status": forms.Select(attrs={"class": "form-select"}),
        }