# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to the run tracker functions."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

# app imports
from penthouse.models.profile import Profile, ProfileForm
from penthouse.views.mixins import ProfileIDMixin, RestrictToUserMixin


class ProfileDeleteView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.DeleteView
):
    """Generic class-based view implementation to delete ``Profile`` instances."""

    model = Profile

    context_object_name = "profile_item"

    success_url = reverse_lazy("penthouse:profile-update")


class ProfileUpdateView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.UpdateView
):
    """Generic class-based view implementation to update ``Profile`` instances."""

    model = Profile

    form_class = ProfileForm

    template_name_suffix = "_update"

    success_url = reverse_lazy("penthouse:profile-update")
