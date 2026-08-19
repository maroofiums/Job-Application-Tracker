from django.contrib import admin

from .models import Application, Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "industry",
        "location",
        "created_at"
    )

    search_fields = (
        "name",
        "industry",
        "location",
    )

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "company",
        "user",
        "status",
        "employment_type",
        "applied_at"
    )

    list_filter = (
        "status",
        "employment_type",
        "applied_at"
    )

    search_fields = (
        "position",
        "company__name",
        "user__username"
    )

    autocomplete_fields = (
        "company",
        "user"
    )