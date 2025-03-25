# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provides all views associated with :class:`~penthouse.models.account.Account`."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render
from django.views import generic

# app imports
from penthouse.models.account import Account, AccountCreationForm
from penthouse.views.mixins import RestrictToUserMixin


class AccountCreateView(LoginRequiredMixin, generic.CreateView):
    """CBV to create instances of :class:`~penthouse.models.account.Account`.

    This CBV uses the dedicated :class:`~penthouse.models.account.AccountCreationForm`
    and will inject the currently active user during the form validation
    process.
    """

    model = Account

    form_class = AccountCreationForm

    template_name = "penthouse/account_create.html"

    def form_valid(self, form):
        """Inject the request's user while validating.

        :class:`~penthouse.models.account.Account` requires the ``owner`` as
        a mandatory attribute. It is injected here and derived from the current
        request.
        """
        form.instance.owner = self.request.user

        try:
            return super().form_valid(form)
        except IntegrityError:
            return render(self.request, "penthouse/error.html")


class AccountOverview(
    LoginRequiredMixin, RestrictToUserMixin, generic.detail.DetailView
):
    """CBV to display a single instance of :class:`~penthouse.models.account.Account`.

    FIXME: The current implementation is just a stub. This view should fetch
    information from other components of the app and provide them in an
    "executive dashboard"-like manner.
    """

    model = Account

    pk_url_kwarg = "account_id"

    context_object_name = "account"

    template_name = "penthouse/account_overview.html"


class AccountListView(LoginRequiredMixin, RestrictToUserMixin, generic.list.ListView):
    """CBV to display a list of all instances of :class:`~penthouse.models.account.Account`.

    The list will be filtered by the current user.

    FIXME: This should display *some* information about the accounts, which will
    be fetched from oder components.
    """

    model = Account

    template_name = "penthouse/account_list.html"
