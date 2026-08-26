from django.urls import path

from .views import (
    interview_list,
    interview_create,
    interview_detail,
    interview_update,
    interview_delete
)



urlpatterns = [
    path(
        "",
        interview_list,
        name="interview_list"
    ),
    path(
        "create/",
        interview_create,
        name="interview_create"
    ),
    path(
        "<int:pk>/",
        interview_detail,
        name="interview_detail"
    ),
    path(
        "<int:pk>/update/",
        interview_update,
        name="interview_update"
    ),
    path(
        "<int:pk>/delete/",
        interview_delete,
        name="interview_delete"
    ),
]