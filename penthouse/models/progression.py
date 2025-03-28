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
from django.db import models
from django.utils.translation import gettext_lazy as _

# app imports
from penthouse.exceptions import PenthouseModelException
from penthouse.models.account import Account


class SampleException(PenthouseModelException):
    """Base class for all exceptions related to :class:`~penthouse.models.progression.Sample`."""


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

    ltc = models.PositiveBigIntegerField(
        help_text=_("Current Lifetime Coins (LTC)"), verbose_name=_("LTC")
    )

    lts = models.PositiveIntegerField(
        help_text=_("Current Lifetime Stones (LTS)"), verbose_name=_("LTS")
    )

    notes = models.TextField(help_text=_("Additional notes"), verbose_name=_("Notes"))

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Sample")
        verbose_name_plural = _("Samples")
        ordering = ["date"]

    def __str__(self):  # noqa: D105
        return "{}: {} LTC, {} LTS ({})".format(
            self.date, self.ltc, self.lts, self.account.name
        )
