from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from interviews.models import Interview

from applications.models import Application

@login_required
def dashboard(request):
    user = request.user

    total_applications = Application.objects.filter(
        user=user
    ).count()


    applied_count = Application.objects.filter(
        user=user,
        status="APPLIED"
    ).count()


    interview_count = Application.objects.filter(
        user=user,
        status="INTERVIEW"
    ).count()


    offer_count = Application.objects.filter(
        user=user,
        status="OFFER"
    ).count()


    rejected_count = Application.objects.filter(
        user=user,
        status="REJECTED"
    ).count()


    recent_applications = (
        Application.objects
        .filter(user=user)
        .select_related("company")
        .order_by("-created_at")[:5]
    )


    upcoming_interviews = (
        Interview.objects
        .filter(
            user=user,
            date__gte=timezone.now()
        )
        .select_related(
            "application",
            "application__company"
        )
        .order_by(
            "date"
        )[:5]
    )



    context = {
        "total_applications": total_applications,
        "applied_count": applied_count,
        "interview_count": interview_count,
        "offer_count": offer_count,
        "rejected_count": rejected_count,
        "recent_applications": recent_applications,
        "upcoming_interviews": upcoming_interviews,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )