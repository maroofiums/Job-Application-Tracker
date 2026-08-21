from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="companies"
    )

    name = models.CharField(
        max_length=200
    )

    website = models.URLField(
        blank=True
    )

    industry = models.CharField(
        max_length=100,
        blank=True
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Application(models.Model):

    class Status(models.TextChoices):

        APPLIED = "APPLIED", "Applied"
        SCREENING = "SCREENING", "Screening"
        INTERVIEW = "INTERVIEW", "Interview"
        OFFER = "OFFER", "Offer"
        REJECTED = "REJECTED", "Rejected"
        WITHDRAWN = "WITHDRAWN", "Withdrawn"

    class EmploymentType(models.TextChoices):

        FULL_TIME = "FULL_TIME", "Full Time"
        PART_TIME = "PART_TIME", "Part Time"
        CONTRACT = "CONTRACT", "Contract"
        INTERNSHIP = "INTERNSHIP", "Internship"
        FREELANCE = "FREELANCE", "Freelance"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    position = models.CharField(
        max_length=200
    )

    job_url = models.URLField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.APPLIED
    )

    employment_type = models.CharField(
        max_length=20,
        choices=EmploymentType.choices,
        default=EmploymentType.FULL_TIME
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    salary_min = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    salary_max = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    applied_at = models.DateField()

    deadline = models.DateField(
        null=True,
        blank=True
    )

    follow_up_date = models.DateField(
        null=True,
        blank=True
    )

    contact_person = models.CharField(
        max_length=200,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-applied_at"]

    def __str__(self):
        return f"{self.position} at {self.company}"