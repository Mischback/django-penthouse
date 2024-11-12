# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to ``Relics``."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, Value, When
from django.views import generic

# app imports
from penthouse.models.relics import Relic
from penthouse.views.mixins import ProfileIDMixin, RestrictToUserMixin


class RelicListView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.ListView
):
    """Generic class-based view implementation to see all ``Relic`` instances of a given ``Profile``."""

    model = Relic

    template_name = "penthouse/profile_relic_list.html"

    def get_queryset(self):  # noqa: D102
        return self.model.objects.annotate(
            is_claimed=(
                Case(
                    When(claimed_by__id=self.request.user.id, then=Value(True)),
                    default=False,
                )
            )
        )
