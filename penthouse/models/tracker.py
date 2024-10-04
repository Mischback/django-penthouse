# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""The models needed to track runs, that is, a single battle within the game."""

# Django imports
from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _

# app imports
from penthouse.exceptions import PenthouseModelException
from penthouse.game_constants import TowerTiers
from penthouse.models.profile import Profile


class RunModelException(PenthouseModelException):
    """Base class for all exceptions related to :class:`~penthouse.models.tracker.Run` model."""


class RunManager(models.Manager):
    """Custom manager for ``Run`` model."""

    def get_runs_by_user(self, user=None):
        """Filter the runs by the specified user."""
        if user is None:
            raise RunModelException("No user specified!")

        return self.get_queryset().filter(profile__owner=user)


class Run(models.Model):
    """A single run instance."""

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name=_("Profile")
    )
    """Reference to the associated profile."""

    date = models.DateTimeField(
        help_text=_("Date and time of the run"), verbose_name=_("Run Date")
    )
    """Date (and time) of the run."""

    tier = models.CharField(
        help_text=_("Tier of the run"),
        verbose_name=_("Tier"),
        choices=TowerTiers,
        max_length=3,
    )
    """The tier of the run."""

    waves = models.PositiveSmallIntegerField(
        help_text=_("End wave of the run"), verbose_name=_("End Wave")
    )
    """End wave counter of the run."""

    duration = models.PositiveIntegerField(
        help_text=_("Duration of the run (in seconds)"),
        verbose_name=_("Duration"),
        default=1,
    )
    """Duration of the run, specified in seconds."""

    coins = models.PositiveBigIntegerField(
        help_text=_("Total coins of the run"), verbose_name=_("Coins")
    )
    """Total coins of the run."""

    cells = models.PositiveIntegerField(
        help_text=_("Total cells of the run"), verbose_name=_("Cells")
    )
    """Total cells of the run."""

    notes = models.TextField(
        help_text=_("Additional notes for the run"), verbose_name=_("Notes"), blank=True
    )
    """Can store possible additional information about the run."""

    coins_hour = models.PositiveBigIntegerField(
        help_text=_("Coins per hour"), verbose_name=_("Coins/h"), default=0
    )
    """Coins per hour of the run.

    This field should be calculated automatically depending on ``coins`` and
    ``duration``.
    """

    coins_wave = models.PositiveBigIntegerField(
        help_text=_("Coins per wave"), verbose_name=_("Coins/Wave"), default=0
    )
    """Coins per wave of the run.

    This field should be calculated automatically depending on ``coins`` and
    ``waves``.
    """

    cells_hour = models.PositiveIntegerField(
        help_text=_("Cells per hour"), verbose_name=_("Cells/h"), default=0
    )
    """Cells per hour of the run.

    This field should be calculated automatically depending on ``cells`` and
    ``duration``.
    """

    cells_wave = models.PositiveIntegerField(
        help_text=_("Cells per wave"), verbose_name=_("Cells/Wave"), default=0
    )
    """Cells per wave of the run.

    This field should be calculated automatically depending on ``cells`` and
    ``waves``.
    """

    objects = RunManager()
    """Apply a custom manager.

    This should not interfere with Django's default inner mechanics, the
    custom manager does not replace any default functions, it just provides
    additional methods.
    """

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Run")
        verbose_name_plural = _("Runs")

    def __str__(self):  # noqa: D105
        return "[Run] ({}) {} {}-{}: {} / {}".format(
            self.profile, self.date, self.tier, self.waves, self.coins, self.cells
        )

    def save(self, **kwargs):
        """Implement ``save`` method to automatically calculate per hour/wave value."""
        self.coins_hour = self._calculate_coins_hour()
        self.coins_wave = self._calculate_coins_wave()
        self.cells_hour = self._calculate_cells_hour()
        self.cells_wave = self._calculate_cells_wave()

        if (update_fields := kwargs.get("update_fields")) is not None:
            kwargs["update_fields"] = {
                "coins_hour",
                "coins_wave",
                "cells_hour",
                "cells_wave",
            }.union(update_fields)

        print("[save]...")
        super().save(**kwargs)

    def _calculate_coins_hour(self):  # noqa: D105
        return self.coins / (self.duration / 3600)

    def _calculate_coins_wave(self):  # noqa: D105
        return self.coins / self.waves

    def _calculate_cells_hour(self):  # noqa: D105
        return self.cells / (self.duration / 3600)

    def _calculate_cells_wave(self):  # noqa: D105
        return self.cells / self.waves


class RunForm(forms.ModelForm):
    """Used to validate input for creating and updating ``Run`` instances."""

    duration_h = forms.IntegerField(min_value=0, step_size=1)
    duration_m = forms.IntegerField(min_value=0, max_value=59, step_size=1)
    duration_s = forms.IntegerField(min_value=0, max_value=59, step_size=1)

    class Meta:  # noqa: D106
        model = Run
        fields = [
            "date",
            "tier",
            "waves",
            "duration",
            "duration_h",
            "duration_m",
            "duration_s",
            "coins",
            "cells",
            "notes",
        ]
        widgets = {"duration": forms.HiddenInput()}

    def save(self, *args, **kwargs):
        """Calculate the actual duration from dedicated input fields."""
        dur_h = self.cleaned_data.get("duration_h")
        dur_m = self.cleaned_data.get("duration_m")
        dur_s = self.cleaned_data.get("duration_s")

        self.instance.duration = dur_h * 3600 + dur_m * 60 + dur_s

        return super().save(*args, **kwargs)
