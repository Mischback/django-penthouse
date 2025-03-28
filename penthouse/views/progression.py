# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provides all views associated with the *progression* component.

The *progression component* is used to track the meta progression of a single
:class:`~penthouse.models.account.Account`.
"""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import generic

# app imports
from penthouse.models.account import Account
from penthouse.models.progression import Sample, SampleForm
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


class SampleCreateView(LoginRequiredMixin, generic.CreateView):
    """CBV to create instances of :class:`~penthouse.models.progression.Sample`.

    This CBV uses the :class:`~penthouse.models.progression.SampleForm` and
    will inject the currently active :class:`~penthouse.models.account.Account`
    instance during the form validation process.
    """

    model = Sample

    form_class = SampleForm

    template_name = "penthouse/progression_sample_create.html"

    def form_valid(self, form):
        """Inject the currently active :class:`~penthouse.models.account.Account`."""
        try:
            parent_account = Account.objects.filter_by_user(self.request.user).get(
                id=self.kwargs["account_id"]
            )
        except Account.DoesNotExist:
            raise ValidationError(
                _("Could not find parent Account object"), code="invalid"
            )

        form.instance.account = parent_account

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Provide the currently active account in the rendering context."""
        context = super().get_context_data(**kwargs)

        context["active_account"] = Account.objects.filter_by_user(
            self.request.user
        ).get(id=self.kwargs["account_id"])

        return context

    def get_success_url(self):
        """Dynamically determine the success url.

        Usually the class attribute ``sucess_url`` is used to handle this. But
        the required ``account_id`` has to be fetched  dynamically.
        """
        return reverse(
            "penthouse:progression-overview", args=[self.kwargs["account_id"]]
        )
