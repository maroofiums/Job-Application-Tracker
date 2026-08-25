from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.core.paginator import Paginator

from .models import Application, Company
from .forms import ApplicationForm, CompanyForm


@login_required
def application_list(request):

    applications = (
        Application.objects
        .filter(user=request.user)
        .select_related("company")
    )

    # Search
    search = request.GET.get("search", "").strip()

    if search:
        applications = applications.filter(
            models.Q(position__icontains=search)
            | models.Q(company__name__icontains=search)
        )

    # Status
    status = request.GET.get("status", "")

    if status:
        applications = applications.filter(
            status=status
        )

    # Employment Type
    employment_type = request.GET.get(
        "employment_type",
        ""
    )

    if employment_type:
        applications = applications.filter(
            employment_type=employment_type
        )

    # Latest applications first
    applications = applications.order_by(
        "-applied_at"
    )

    # Pagination
    paginator = Paginator(
        applications,
        10
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )

    context = {
        "page_obj": page_obj,

        "search": search,

        "selected_status": status,

        "selected_employment_type": employment_type,

        "status_choices": Application.Status.choices,

        "employment_choices": (
            Application.EmploymentType.choices
        ),
    }

    return render(
        request,
        "applications/application_list.html",
        context,
    )


@login_required
def application_create(request):
    if request.method == "POST":

        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            messages.success(
                request,
                "Application added successfully."
            )

            return redirect("application_list")

    else:
        form = ApplicationForm()

    return render(
        request,
        "applications/application_form.html",
        {
            "form": form,
            "title": "Add Application",
        }
    )

@login_required
def application_detail(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "applications/application_detail.html",
        {
            "application": application
        }
    )

@login_required
def application_update(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
    )
    
    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Application updated successfully."
            )
            return redirect(
                "application_detail",
                pk=application.pk
            )

    else:
        form = ApplicationForm(
            instance=application
        )

    return render(
        request,
        "applications/application_form.html",
        {
            "form": form,
            "title": "Edit Application",
            "application": application
        }
    )

@login_required
def application_delete(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        application.delete()

        messages.success(
            request,
            "Application deleted successfully."
        )

        return redirect("application_list")

    return render(
        request,
        "applications/application_confirm_delete.html",
        {
            "application": application
        }
    )


@login_required
def company_list(request):

    companies = (
        Company.objects
        .filter(owner=request.user)
    )

    return render(
        request,
        "applications/company_list.html",
        {
            "companies": companies,
        },
    )

@login_required
def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)

        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()


            messages.success(
                request,
                "Company added successfully."
            )

            return redirect("company_list")

    else:
        form = CompanyForm()

    return render(
        request,
        "applications/company_form.html",
        {
            "form": form,
            "title": "Add Company"
        }
    )


@login_required
def company_update(request, pk):

    company = get_object_or_404(
        Company,
        pk=pk,
        owner=request.user
    )
    if request.method == "POST":
        form = CompanyForm(
            request.POST,
            instance=company
        )

        if form.is_valid():
            company = form.save()

            messages.success(
                request,
                "Company updated successfully."
            )

            return redirect("company_list")

    else:
        form = CompanyForm(
            instance=company
        )

    return render(
        request,
        "applications/company_form.html",
        {
            "form": form,
            "title": "Edit Company",
            "company": company,
        }
    )


@login_required
def company_delete(request, pk):

    company = get_object_or_404(
        Company,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        company.delete()

        messages.success(
            request,
            "Application deleted successfully."
        )

        return redirect("company_list")

    return render(
        request,
        "applications/company_confirm_delete.html",
        {
            "company": company
        }
    )