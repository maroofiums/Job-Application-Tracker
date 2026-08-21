from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404

from .models import Application, Company
from .forms import ApplicationForm, CompanyForm


@login_required
def application_list(request):

    applications = (
        Application.objects
        .filter(user=request.user)
        .select_related("company")
    )

    return render(
        request,
        "applications/application_list.html",
        {
            "applications": applications
        },
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