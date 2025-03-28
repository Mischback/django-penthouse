# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provides all views associated with the *progression* component.

The *progression component* is used to track the meta progression of a single
:class:`~penthouse.models.account.Account`.
"""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# app imports
from penthouse.models.progression import Sample
from penthouse.views.mixins import RestrictToUserMixin


class ProgressionOverview(
    LoginRequiredMixin, RestrictToUserMixin, generic.list.ListView
):
    """CBV to display the list of all :class:`~penthouse.models.progression.Sample` instances.

    The list will be filtered by the currently active *account*.
    """

    model = Sample

    template_name = "penthouse/progression_overview.html"

    def get_queryset(self):
        """Apply a filter to the queryset in order to limit the objects to the current account.

        The ``account_id`` is provided in the view's URL.
        """
        return super().get_queryset().filter(account=self.kwargs["account_id"])

    def get_context_data(self, **kwargs):
        """Provide the currently active account in the rendering context."""
        context = super().get_context_data(**kwargs)

        # Force evaluation of the QuerySet
        #
        # The ``object_list`` is looped in the template (which triggers
        # evaluation of the QuerySet) and must be accessed here to access the
        # currently active account. In order to mitigate two evaluations (and
        # thus, two database hits), the evaluation is forced here. The template
        # loop doesn't need an actual QuerySet.
        plain_obj_list = list(context["object_list"])
        context["object_list"] = plain_obj_list
        context["active_account"] = plain_obj_list[0].account

        return context
