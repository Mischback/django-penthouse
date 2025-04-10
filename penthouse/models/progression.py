# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Track meta progression in the game.

The progression is *account-specific*, so the samples are tied to an
:class:`~penthouse.models.account.Account` instance.

There are two main data points relevant for the meta progression throughout the
game: Lifetime Coins (LTC, all coins gathered) and Lifetime Stones (LTS). They
are *kind of* interdependent, but the relation between them will vary based on
spending habits (F2P vs. whaling).
"""

# Django imports
from django import forms
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

# app imports
from penthouse.exceptions import PenthouseModelException
from penthouse.models.account import Account
from penthouse.utility import convertNumberForDisplay


class SampleException(PenthouseModelException):
    """Base class for all exceptions related to :class:`~penthouse.models.progression.Sample`."""


class SampleManager(models.Manager):
    """Custom manager for :class:`~penthouse.models.progression.Sample` model."""

    def filter_by_user(self, user=None):
        """Filter objects by their owner.

        This method is intended to be used in combination with the ``request.user``
        of the actual HTTP request. It's a first layer of user verification/
        permission checking.
        """
        if user is None:
            raise SampleException("No user specified!")

        return self.get_queryset().filter(account__owner=user)

    def get_queryset(self):
        """Add ``Account`` to the query.

        Throughout the app, the :class:`~penthouse.models.account.Account`
        object is required to be available when working with ``Sample`` objects.
        """
        return super().get_queryset().select_related("account")


class Sample(models.Model):
    """A ``Sample`` is a single data point to track the meta progression."""

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="progression_samples",
        verbose_name=_("Account"),
    )
    """Reference to an app's :class:`~penthouse.models.account.Account` instance."""

    date = models.DateField(help_text=_("Date of this sample"), verbose_name=_("Date"))

    ltc = models.DecimalField(
        max_digits=36,
        decimal_places=12,
        help_text=_("Current Lifetime Coins (LTC)"),
        verbose_name=_("LTC"),
    )
    """Coin-related values are stored in *trillions* semantically.

    Those values can get really big, especially for this lifetime coins (LTC).
    The field in use is a ``DecimalField`` with 36 *overall digits*, of which
    12 can be used as decimal places.

    Notes
    -----
    :func:`~penthouse.utility.convertNumberForDisplay` can be used to provide
    an actual human-readable presentation of the value. This is wrapped in this
    class' ``ltc_display`` method.

    :const:`~penthouse.utility.NUMBER_DEFAULT_MAGNITUDE` should be used to
    control that throughout the app.
    """

    lts = models.PositiveIntegerField(
        help_text=_("Current Lifetime Stones (LTS)"), verbose_name=_("LTS")
    )

    notes = models.TextField(help_text=_("Additional notes"), verbose_name=_("Notes"))

    objects = SampleManager()
    """Apply a custom manager.

    This should not interfere with Django's default inner mechanics, the custom
    manager does not replace any default functions, it just provides additional
    methods.
    """

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Sample")
        verbose_name_plural = _("Samples")
        ordering = ["date"]

    def __str__(self):  # noqa: D105
        return "{}: {} LTC, {} LTS ({})".format(
            self.date, self.ltc, self.lts, self.account.name
        )

    @cached_property
    def ltc_display(self):
        """Provide the LTC value in a human readable format."""
        return "{}{}".format(*convertNumberForDisplay(self.ltc))


class SampleForm(forms.ModelForm):
    """Validate input while creating/updating :class:`~penthouse.models.progression.Sample` instances.

    This form works for both operations. It might be advisable to divide it
    into dedicated implementations later.
    """

    class Meta:  # noqa: D106
        model = Sample
        fields = ["date", "ltc", "lts", "notes"]
