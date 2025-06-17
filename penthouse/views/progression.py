# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provides all views associated with the *progression* component.

The *progression component* is used to track the meta progression of a single
:class:`~penthouse.models.account.Account`.
"""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import generic

# app imports
from penthouse.models.account import Account
from penthouse.models.progression import Sample, SampleForm
from penthouse.views.mixins import ProvideActiveAccountMixin


class SampleBaseView:
    """Provide a module-specific base class.

    This class is mostly intended to provide common implementation of CBVs,
    in particular for :class:`~penthouse.views.mixins.ProvideActiveAccountMixin`.
    """

    def get_active_account(self):
        """Fetch the currently active account.

        This is the implementation required by
        :class:`~penthouse.views.mixins.ProvideActiveAccountMixin`.
        """
        try:
            acc = Account.objects.filter_by_user(self.request.user).get(
                progression_samples=self.kwargs["sample_id"]
            )
        except Account.DoesNotExist:
            raise ValueError(_("Could not identify parent Account object"))
        else:
            return acc

    def get_success_url(self):
        """Dynamically determine the success url.

        Usually the class attribute ``sucess_url`` is used to handle this. But
        the required ``account_id`` has to be fetched  dynamically.
        """
        return reverse("penthouse:progression-overview", args=[self.active_account.id])


class ProgressionOverview(
    LoginRequiredMixin, ProvideActiveAccountMixin, generic.list.ListView
):
    """CBV to display the list of all :class:`~penthouse.models.progression.Sample` instances.

    The list will be filtered by the currently active *account*.
    """

    model = Sample

    template_name = "penthouse/progression_overview.html"

    def get_active_account(self):
        """Fetch the currently active account.

        This is the implementation required by
        :class:`~penthouse.views.mixins.ProvideActiveAccountMixin`.
        """
        try:
            acc = Account.objects.filter_by_user(self.request.user).get(
                id=self.kwargs["account_id"]
            )
        except Account.DoesNotExist:
            raise ValueError(_("Could not identify parent Account object"))
        else:
            return acc

    def get_queryset(self):
        """Apply a filter to the queryset in order to limit the objects to the current account.

        The ``account_id`` is provided in the view's URL.
        """
        return super().get_queryset().filter(account=self.kwargs["account_id"])


class SampleCreateView(
    SampleBaseView, LoginRequiredMixin, ProvideActiveAccountMixin, generic.CreateView
):
    """CBV to create instances of :class:`~penthouse.models.progression.Sample`.

    This CBV uses the :class:`~penthouse.models.progression.SampleForm` and
    will inject the currently active :class:`~penthouse.models.account.Account`
    instance during the form validation process.
    """

    model = Sample

    form_class = SampleForm

    template_name = "penthouse/progression_sample_create.html"

    def get_active_account(self):
        """Fetch the currently active account.

        This is the implementation required by
        :class:`~penthouse.views.mixins.ProvideActiveAccountMixin`.
        """
        try:
            acc = Account.objects.filter_by_user(self.request.user).get(
                id=self.kwargs["account_id"]
            )
        except Account.DoesNotExist:
            raise ValueError(_("Could not identify parent Account object"))
        else:
            return acc

    def form_valid(self, form):
        """Inject the currently active :class:`~penthouse.models.account.Account`."""
        form.instance.account = self.active_account

        return super().form_valid(form)


class SampleDeleteView(
    SampleBaseView, LoginRequiredMixin, ProvideActiveAccountMixin, generic.DeleteView
):
    """CBV to delete instances of :class:`~penthouse.models.progression.Sample`."""

    model = Sample

    pk_url_kwarg = "sample_id"

    context_object_name = "sample"

    template_name = "penthouse/progression_sample_delete.html"


class SampleUpdateView(
    SampleBaseView, LoginRequiredMixin, ProvideActiveAccountMixin, generic.UpdateView
):
    """CBV to update instances of :class:`~penthouse.models.progression.Sample`.

    This CBV uses the :class:`~penthouse.models.progression.SampleForm` and
    will inject the currently active :class:`~penthouse.models.account.Account`
    instance during the form validation process.
    """

    model = Sample

    form_class = SampleForm

    template_name = "penthouse/progression_sample_update.html"

    pk_url_kwarg = "sample_id"

    def form_valid(self, form):
        """Inject the currently active :class:`~penthouse.models.account.Account`."""
        form.instance.account = self.active_account

        return super().form_valid(form)
