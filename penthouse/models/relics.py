# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific user profile."""

# Django imports
from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _

# app imports
from penthouse.exceptions import PenthouseModelException
from penthouse.game_constants import RelicBonusType, RelicRarity, RelicSource


class RelicModelException(PenthouseModelException):
    """Base class for all exceptions related to :class:`~penthouse.models.relics.Relic`."""


class Relic(models.Model):
    """A single in-game relic."""

    name = models.CharField(
        max_length=200, help_text=_("Name of the Relic"), verbose_name=_("Name")
    )
    """The actual name of the relic."""

    rarity = models.CharField(
        max_length=6,
        help_text=_("The rarity of the relic"),
        verbose_name=_("Relic Rarity"),
        choices=RelicRarity,
    )

    bonus_type = models.CharField(
        max_length=6,
        help_text=_("The stat to be modified"),
        verbose_name=_("Bonus Type"),
        choices=RelicBonusType,
    )

    bonus_value = models.FloatField(
        help_text=_("Bonus value, specified in percent"), verbose_name=_("Bonus Value")
    )

    source = models.CharField(
        max_length=1,
        help_text=_("Source of the relic"),
        verbose_name=_("Source"),
        choices=RelicSource,
    )

    condition = models.CharField(
        max_length=200,
        help_text=_("Condition to obtain the relic"),
        verbose_name=_("Condition"),
    )

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Relic")
        verbose_name_plural = _("Relics")

    def __str__(self):  # noqa: D105
        return "[{}] {} ({} {})".format(
            self.get_rarity_display(),
            self.name,
            self.bonus_value,
            self.get_bonus_type_display(),
        )


class RelicForm(forms.ModelForm):
    """Used to validate input for creating and updating ``Relic`` instances."""

    class Meta:  # noqa: D106
        model = Relic
        fields = "__all__"
