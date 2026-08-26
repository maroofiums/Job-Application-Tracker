from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from .models import Interview
from .forms import InterviewForm


@login_required
def interview_list(request):
    interviews = (
        Interview.objects
        .filter(user=request.user)
        .select_related(
            "application",
            "application__company"
        )
        .order_by(
            "date"
        )
    )

    return render(
        request,
        "interviews/interview_list.html",
        {
            "interviews": interviews
        }
    )


@login_required
def interview_create(request):
    if request.method == "POST":

        form = InterviewForm(
            request.POST,
            user=request.user
        )

        if form.is_valid():
            interview = form.save(
                commit=False
            )

            interview.user = request.user

            interview.save()

            messages.success(
                request,
                "Interview added successfully."
            )

            return redirect(
                "interview_list"
            )

    else:
        form = InterviewForm(
            user=request.user
        )

    return render(
        request,
        "interviews/interview_form.html",
        {
            "form": form,
            "title": "Add Interview"
        }
    )


@login_required
def interview_detail(request, pk):
    interview = get_object_or_404(
        Interview,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "interviews/interview_detail.html",
        {
            "interview": interview
        }
    )



@login_required
def interview_update(request, pk):
    interview = get_object_or_404(
        Interview,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = InterviewForm(
            request.POST,
            instance=interview,
            user=request.user
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Interview updated."
            )

            return redirect(
                "interview_detail",
                pk=pk
            )
        
    else:
        form = InterviewForm(
            instance=interview,
            user=request.user
        )

    return render(
        request,
        "interviews/interview_form.html",
        {
            "form": form,
            "title": "Edit Interview"
        }
    )


@login_required
def interview_delete(request, pk):
    interview = get_object_or_404(
        Interview,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        interview.delete()

        messages.success(
            request,
            "Interview deleted."
        )

        return redirect(
            "interview_list"
        )

    return render(
        request,
        "interviews/interview_confirm_delete.html",
        {
            "interview": interview
        }
    )