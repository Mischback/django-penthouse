# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to *progress planning*."""

# Django imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

# app imports
from penthouse.models.profile import Profile
from penthouse.models.progress import (
    Milestone,
    MilestoneForm,
    MilestoneSection,
    MilestoneSectionForm,
    MilestoneStep,
    MilestoneStepForm,
)
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


class MilestoneSectionCreateView(
    LoginRequiredMixin, ProfileIDMixin, generic.CreateView
):
    """Generic class-based view implementation to add ``MilestoneSection`` instances."""

    model = MilestoneSection

    form_class = MilestoneSectionForm

    template_name_suffix = "_create"

    success_url = reverse_lazy("penthouse:progress-milestones")

    def form_valid(self, form):  # noqa: D102
        # form.instance.profile = Profile.objects.get(owner=self.request.user)
        try:
            # This checks two things in one step:
            # 1) The requesting user is actually manipulating one of his Milestones
            # 2) The Milestone actually exists
            parent_milestone = Milestone.objects.filter(
                profile__owner=self.request.user
            ).get(id=self.kwargs["milestone_id"])
        except Milestone.DoesNotExist:
            raise ValidationError(
                _("Could not find parent milestone object"), code="invalid"
            )

        form.instance.milestone = parent_milestone

        return super().form_valid(form)


class MilestoneSectionUpdateView(
    LoginRequiredMixin, ProfileIDMixin, generic.UpdateView
):
    """Generic class-based view implementation to update ``MilestoneSection`` instances."""

    model = MilestoneSection

    form_class = MilestoneSectionForm

    template_name_suffix = "_update"

    pk_url_kwarg = "section_id"

    success_url = reverse_lazy("penthouse:progress-milestones")


class MilestoneStepCreateView(LoginRequiredMixin, ProfileIDMixin, generic.CreateView):
    """Generic class-based view implementation to add ``MilestoneStep`` instances."""

    model = MilestoneStep

    form_class = MilestoneStepForm

    template_name_suffix = "_create"

    success_url = reverse_lazy("penthouse:progress-milestones")

    def form_valid(self, form):  # noqa: D102
        try:
            parent_section = MilestoneSection.objects.filter(
                milestone__profile__owner=self.request.user
            ).get(id=self.kwargs["milestonesection_id"])
        except MilestoneStep.DoesNotExist:
            raise ValidationError(
                _("Could not find parent milestone section"), code="invalid"
            )

        form.instance.section = parent_section

        return super().form_valid(form)


class MilestoneStepUpdateView(LoginRequiredMixin, ProfileIDMixin, generic.UpdateView):
    """Generic class-based view implementation to update ``MilestoneStep`` instances."""

    model = MilestoneStep

    form_class = MilestoneStepForm

    template_name_suffix = "_update"

    pk_url_kwarg = "step_id"

    success_url = reverse_lazy("penthouse:progress-milestones")


@login_required
def milestonestep_toggle(request, step_id):
    """Toggle the completion status of a ``MilestoneStep`` instance.

    Permission checking should be working, so a user can only toggle *his*
    own steps.
    """
    try:
        step = MilestoneStep.objects.get(pk=step_id)
    except MilestoneStep.DoesNotExist:
        return redirect(reverse_lazy("penthouse:progress-milestones"))

    if step.section.milestone.profile.owner.id != request.user.id:
        return redirect(reverse_lazy("penthouse:progress-milestones"))

    # this is the actual toggle
    if step.completed is True:
        step.completed = False
    else:
        step.completed = True
    step.save()

    return redirect(reverse_lazy("penthouse:progress-milestones"))
