from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from applications.models import Application


@login_required
def dashboard_view(request):

    applications = Application.objects.filter(
        user=request.user
    )

    total_applications = applications.count()

    applied_count = applications.filter(
        status=Application.Status.APPLIED
    ).count()

    screening_count = applications.filter(
        status=Application.Status.SCREENING
    ).count()

    interview_count = applications.filter(
        status=Application.Status.INTERVIEW
    ).count()

    offer_count = applications.filter(
        status=Application.Status.OFFER
    ).count()

    rejected_count = applications.filter(
        status=Application.Status.REJECTED
    ).count()

    recent_applications = (
        applications
        .select_related("company")
        .order_by("-applied_at")[:5]
    )

    context = {
        "total_applications": total_applications,
        "applied_count": applied_count,
        "screening_count": screening_count,
        "interview_count": interview_count,
        "offer_count": offer_count,
        "rejected_count": rejected_count,
        "recent_applications": recent_applications,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )