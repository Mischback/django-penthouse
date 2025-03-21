# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provides all views associated with :class:`~penthouse.models.account.Account`."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# app imports
from penthouse.models.account import Account, AccountCreationForm


class AccountCreateView(LoginRequiredMixin, generic.CreateView):
    """CBV to create instances of :class:`~penthouse.models.account.Account`.

    This CBV uses the dedicated :class:`~penthouse.models.account.AccountCreationForm`
    and will inject the currently active user during the form validation
    process.
    """

    model = Account

    form_class = AccountCreationForm

    template_name = "account_create.html"

    def form_valid(self, form):
        """Inject the request's user while validating.

        :class:`~penthouse.models.account.Account` requires the ``owner`` as
        a mandatory attribute. It is injected here and derived from the current
        request.
        """
        form.instance.owner = self.request.user

        return super().form_valid(form)
