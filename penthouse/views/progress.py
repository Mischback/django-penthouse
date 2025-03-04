# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to *progress planning*."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# app imports
from penthouse.models.progress import Milestone
from penthouse.views.mixins import ProfileIDMixin, RestrictToUserMixin


class MilestoneListView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.ListView
):
    """Generic class-based view implementation to see all ``Milestone`` instances."""

    model = Milestone

    template_name = "penthouse/milestone_list.html"
