from django import forms
from .models import Interview


class InterviewForm(forms.ModelForm):

    class Meta:

        model = Interview

        fields = [
            "application",
            "interview_type",
            "date",
            "interviewer",
            "notes",
        ]

        widgets = {
            "application": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "interview_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),
            "interviewer": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Interviewer name"
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Interview preparation notes..."
                }
            ),

        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop(
            "user",
            None
        )

        super().__init__(
            *args,
            **kwargs
        )

        if user:
            self.fields["application"].queryset = (
                user.applications.all()
            )