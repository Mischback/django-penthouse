# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific mixins to be used with class-based views."""

# app imports
from penthouse.models.profile import Profile


class ProfileIDMixin:
    """Injects the current user's profile ID into the context.

    This mixin can only be used on views that also use the
    ``LoginRequiredMixin``.
    """

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)

        context["profile_id"] = Profile.objects.get(owner=self.request.user).id

        return context
