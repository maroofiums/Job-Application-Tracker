from django.urls import path

from .views import (
    application_create,
    application_list,
    application_detail,
    application_update,
    application_delete,
    company_list,
    company_create,
    company_update,
    company_delete
)


urlpatterns = [
    path("", application_list, name="application_list"),
    path("add/", application_create, name="application_create"),
    path("<int:pk>/", application_detail, name="application_detail"),
    path("<int:pk>/edit/", application_update, name="application_update"),
    path("<int:pk>/delete/", application_delete, name="application_delete"),
    path("companies/", company_list, name="company_list"),
    path("companies/add/", company_create, name="company_create"),
    path("companies/<int:pk>/edit/", company_update, name="company_update"),
    path("companies/<int:pk>/delete/", company_delete, name="company_delete"),
]
