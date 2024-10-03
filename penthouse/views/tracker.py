# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to the run tracker functions."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# app imports
from penthouse.models.profile import Profile
from penthouse.models.tracker import Run, RunForm
from penthouse.views.mixins import ProfileIDMixin


def tracker_overview(request):
    """Provide an overview over all runs."""
    profile = Profile.objects.get(owner=request.user)
    runs = Run.objects.filter(profile=profile)

    return render(request, "penthouse/tracker_overview.html", {"runs": runs})


class RunCreateView(LoginRequiredMixin, ProfileIDMixin, generic.CreateView):
    """Generic class-based view implementation to add ``Run`` instances."""

    model = Run

    form_class = RunForm

    template_name_suffix = "_create"

    success_url = reverse_lazy("penthouse:tracker-run-add")

    def form_valid(self, form):  # noqa: D102
        form.instance.profile = Profile.objects.get(owner=self.request.user)

        return super().form_valid(form)
