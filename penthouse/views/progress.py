# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to *progress planning*."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

# app imports
from penthouse.models.profile import Profile
from penthouse.models.progress import Milestone, MilestoneForm
from penthouse.views.mixins import ProfileIDMixin, RestrictToUserMixin


class MilestoneListView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.ListView
):
    """Generic class-based view implementation to see all ``Milestone`` instances."""

    model = Milestone

    template_name = "penthouse/milestone_list.html"


class MilestoneCreateView(LoginRequiredMixin, ProfileIDMixin, generic.CreateView):
    """Generic class-based view implementation to add ``Milestone`` instances."""

    model = Milestone

    form_class = MilestoneForm

    template_name_suffix = "_create"

    success_url = reverse_lazy("penthouse:progress-milestones")

    def form_valid(self, form):  # noqa: D102
        form.instance.profile = Profile.objects.get(owner=self.request.user)

        return super().form_valid(form)
