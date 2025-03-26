# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provides all views associated with :class:`~penthouse.models.account.Account`."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

# app imports
from penthouse.models.account import Account, AccountForm
from penthouse.views.mixins import RestrictToUserMixin


class AccountCreateView(LoginRequiredMixin, generic.CreateView):
    """CBV to create instances of :class:`~penthouse.models.account.Account`.

    This CBV uses the dedicated :class:`~penthouse.models.account.AccountCreationForm`
    and will inject the currently active user during the form validation
    process.
    """

    model = Account

    form_class = AccountForm

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


class AccountDeleteView(LoginRequiredMixin, RestrictToUserMixin, generic.DeleteView):
    """CBV to delete instances of :class:`~penthouse.models.account.Account`."""

    model = Account

    pk_url_kwarg = "account_id"

    context_object_name = "account"

    template_name = "penthouse/account_delete.html"

    success_url = reverse_lazy("penthouse:account-list")


class AccountListView(LoginRequiredMixin, RestrictToUserMixin, generic.list.ListView):
    """CBV to display a list of all instances of :class:`~penthouse.models.account.Account`.

    The list will be filtered by the current user.

    FIXME: This should display *some* information about the accounts, which will
    be fetched from oder components.
    """

    model = Account

    template_name = "penthouse/account_list.html"

    def render_to_response(self, context):
        """Check if there is actual *need* to display a list of accounts.

        If there is only one account, it will redirect to the corresponding
        :class:`~penthouse.views.account.AccountOverview`. If there is actually
        no :class:`~penthouse.models.account.Account`, it will redirect to the
        :class:`~penthouse.views.account.AccountCreateView`.

        There is an obvious *issue* with this approach: The view will actually
        execute a database query to determine the number of accounts. If there
        is only one account, the database will be hit again while processing the
        :class:`~penthouse.views.account.AccountOverview`. Meh.
        """
        qs = context["object_list"]
        cnt = qs.count()

        if cnt > 1:
            return super().render_to_response(context)
        elif cnt < 1:
            return redirect("penthouse:account-create")
        else:
            return redirect("penthouse:account-overview", qs.first().id)


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


class AccountUpdateView(LoginRequiredMixin, RestrictToUserMixin, generic.UpdateView):
    """CBV to update instances of :class:`~penthouse.models.account.Account`."""

    model = Account

    form_class = AccountForm

    pk_url_kwarg = "account_id"

    template_name = "penthouse/account_update.html"
