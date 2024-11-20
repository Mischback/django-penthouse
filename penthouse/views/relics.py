# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to ``Relics``."""

# Django imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, Value, When
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

# app imports
from penthouse.models.profile import Profile
from penthouse.models.relics import Relic
from penthouse.views.mixins import ProfileIDMixin, RestrictToUserMixin


class RelicListView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.ListView
):
    """Generic class-based view implementation to see all ``Relic`` instances of a given ``Profile``."""

    model = Relic

    template_name = "penthouse/relic_list.html"

    def get_queryset(self):  # noqa: D102
        return self.model.objects.annotate(
            is_claimed=(
                Case(
                    When(claimed_by__id=self.request.user.id, then=Value(True)),
                    default=False,
                )
            )
        )


@login_required
def relic_claim(request, relic_id):
    """Claim a relic.

    This view will add the relic to the currently active profile. Technically
    it is the other way around, the ``Profile`` object is added to the ``Relic``
    object.
    """
    try:
        relic = Relic.objects.get(pk=relic_id)
    except Relic.DoesNotExist:
        return redirect(reverse_lazy("penthouse:relics-list"))

    # FIXME: This should actually not return the relic list, as there is no
    #        existing profile. It should show a generic error page about how
    #        to create a Profile or just redirect to the form to create the
    #        profile.
    # FIXME: Same principle for other views that require a Profile!
    try:
        profile = Profile.objects.get(pk=request.user.id)
    except Profile.DoesNotExist:
        return redirect(reverse_lazy("penthouse:relics-list"))

    relic.claimed_by.add(profile)
    relic.save()

    return redirect(reverse_lazy("penthouse:relics-list"))


@login_required
def relic_unclaim(request, relic_id):
    """Unclaim a relic.

    This view will remove the relic to the currently active profile. Technically
    it is the other way around, the ``Profile`` object is removed from the
    ``Relic`` object.
    """
    try:
        relic = Relic.objects.get(pk=relic_id)
    except Relic.DoesNotExist:
        return redirect(reverse_lazy("penthouse:relics-list"))

    # FIXME: This should actually not return the relic list, as there is no
    #        existing profile. It should show a generic error page about how
    #        to create a Profile or just redirect to the form to create the
    #        profile.
    # FIXME: Same principle for other views that require a Profile!
    try:
        profile = Profile.objects.get(pk=request.user.id)
    except Profile.DoesNotExist:
        return redirect(reverse_lazy("penthouse:relics-list"))

    relic.claimed_by.remove(profile)
    relic.save()

    return redirect(reverse_lazy("penthouse:relics-list"))
