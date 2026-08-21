from django import forms

from .models import Application, Company

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
            "company",
            "position",
            "job_url",
            "status",
            "employment_type",
            "location",
            "salary_min",
            "salary_max",
            "applied_at",
            "deadline",
            "follow_up_date",
            "contact_person",
            "notes",
        ]

        widgets = {
            "company": forms.Select(
                attrs={
                    "class":"form-select",
                }
            ),
            "position": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g, Machine Learning Engineer",
                }
            ),
            "job_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://...",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class":"form-select",
                }
            ),
            "employment_type": forms.Select(
                attrs={
                    "class":"form-select",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g, Karachi / Remote",
                }
            ),
            "salary_min": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Minimum salary",
                }
            ),
            "salary_max": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Maximum salary",
                }
            ),
            "applied_at": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "date",
                }
            ),
            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "date",
                }
            ),
            "follow_up_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "date",
                }
            ),
            "contact_person": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Recruiter / Hiring Manager",
                }
            ),
            "notes": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Add notes about this applications...",
                }
            ),
        }


class CompanyForm(forms.ModelForm):

    class Meta:

        model = Company

        fields = [
            "name",
            "website",
            "industry",
            "location"
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Google"
                }
            ),
            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com"
                }
            ),
            "industry": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Artificial Intelligence"
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Karachi / Remote"
                }
            ),
        }