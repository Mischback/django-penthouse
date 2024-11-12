# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to the run tracker functions."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

# app imports
from penthouse.models.profile import Profile, ProfileSettingsForm
from penthouse.models.relics import Relic
from penthouse.views.mixins import ProfileIDMixin, RestrictToUserMixin


class ProfileDeleteView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.DeleteView
):
    """Generic class-based view implementation to delete ``Profile`` instances."""

    model = Profile

    context_object_name = "profile_item"

    success_url = reverse_lazy("penthouse:profile-settings-update")


class ProfileSettingsUpdateView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.UpdateView
):
    """Generic class-based view implementation to update ``Profile`` instances."""

    model = Profile

    form_class = ProfileSettingsForm

    template_name_suffix = "_settings_update"

    success_url = reverse_lazy("penthouse:profile-settings-update")


class ProfileRelicListView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.ListView
):
    """Generic class-based view implementation to see all ``Relic`` instances of a given ``Profile``."""

    model = Relic

    template_name = "penthouse/profile_relic_list.html"

    def get_queryset(self):  # noqa: D102
        return self.model.objects.all()
