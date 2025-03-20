# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific account.

In fact, these objects represent an ingame account, thus, a single tower. Each
user of the Django project can have multiple accounts.
"""

# Django imports
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# app imports
from penthouse.exceptions import PenthouseModelException


class AccountException(PenthouseModelException):
    """Base class for all exceptions related to :class:`~penthouse.models.account.Account`."""


class AccountManager(models.Manager):
    """Custom manager for :class:`~penthouse.models.account.Account` model."""

    def filter_by_user(self, user=None):
        """Filter objects by their owner.

        This method is intended to be used in combination with the ``request.user``
        of the actual HTTP request. It's a first layer of user verification/
        permission checking.
        """
        if user is None:
            raise AccountException("No user specified!")

        return self.get_queryset().filter(owner=user)


class Account(models.Model):
    """An ``Account`` represents one game account of The Tower."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Account")
    )
    """Reference to the project's ``User`` model.

    Notes
    -----
    This is implemented as a :class:`~django.db.models.ForeignKey` with
    ``on_delete=CASCADE``, meaning: if the referenced ``User`` object is deleted,
    the referencing ``Account`` instance is discarded aswell.

    To keep this application as pluggable as possible, the referenced class is
    dependent on :setting:`AUTH_USER_MODEL`. With this implementation, the
    project may substitute the :class:`~django.contrib.auth.models.User` model
    provided by Django without breaking any functionality in ``penthouse`` (see
    :djangodoc:`Reusable Apps and AUTH_USER_MODEL <topics/auth/customizing#reusable-apps-and-auth-user-model>`).
    """

    name = models.CharField(
        help_text=_("Name associated with this account"),
        verbose_name=_("Name"),
        max_length=150,
    )
    """Just a name to make different accounts of a ``User`` distinguishable."""

    objects = AccountManager()
    """Apply a custom manager.

    This should not interfere with Django's default inner mechanics, the custom
    manager does not replace any default functions, it just provides additional
    methods.
    """

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Account")
        verbose_name_plural = _("Account")

    def __str__(self):  # noqa: D105
        return "{} ({})".format(self.name, self.owner)
