from django.db import models
from django.contrib.auth.models import User
from applications.models import Application



class Interview(models.Model):

    class InterviewType(models.TextChoices):
        PHONE = "PHONE", "Phone Screen"
        TECHNICAL = "TECHNICAL", "Technical"
        HR = "HR", "HR Interview"
        FINAL = "FINAL", "Final Round"


    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="interviews"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    interview_type = models.CharField(
        max_length=20,
        choices=InterviewType.choices
    )

    date = models.DateTimeField()

    interviewer = models.CharField(
        max_length=200,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.application} Interview"