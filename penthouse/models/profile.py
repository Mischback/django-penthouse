# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific user profile."""

# Django imports
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """The app-specific profile.

    A profile represents one game account of The Tower.
    """

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Owner")
    )
    """Reference to a Django `User`.

    Notes
    -----
    This is implemented as a :class:`~django.db.models.OneToOneField` with
    ``on_delete=CASCADE``, meaning: if the referenced `User` object is deleted,
    the referencing `Profile` object is discarded aswell.

    To keep this application as pluggable as possible, the referenced class is
    dependent on :setting:`AUTH_USER_MODEL`. With this implementation, the
    project may substitute the :class:`~django.contrib.auth.models.User` model
    provided by Django without breaking any functionality in `calingen` (see
    :djangodoc:`Reusable Apps and AUTH_USER_MODEL <topics/auth/customizing/#reusable-apps-and-auth-user-model>`).
    """

    settings_tracker_threshold_top_coins = models.PositiveSmallIntegerField(
        default=90,
        help_text=_("Threshold for top coins/run, specified in percent"),
        verbose_name=_("Top threshold for coins/run"),
    )
    """Threshold for top coins/run, specified in percent.

    The field is actually only an Integer field, but it will be used like
    a percent value (value/100).
    """

    settings_tracker_threshold_top_coins_hour = models.PositiveSmallIntegerField(
        default=90,
        help_text=_("Threshold for top coins/h, specified in percent"),
        verbose_name=_("Top threshold for coins/h"),
    )
    """Threshold for top coins/h, specified in percent.

    The field is actually only an Integer field, but it will be used like
    a percent value (value/100).
    """

    settings_tracker_threshold_top_cells = models.PositiveSmallIntegerField(
        default=90,
        help_text=_("Threshold for top cells/run, specified in percent"),
        verbose_name=_("Top threshold for cells/run"),
    )
    """Threshold for top cells/run, specified in percent.

    The field is actually only an Integer field, but it will be used like
    a percent value (value/100).
    """

    settings_tracker_threshold_top_cells_hour = models.PositiveSmallIntegerField(
        default=90,
        help_text=_("Threshold for top cells/h, specified in percent"),
        verbose_name=_("Top threshold for cells/h"),
    )
    """Threshold for top cells/h, specified in percent.

    The field is actually only an Integer field, but it will be used like
    a percent value (value/100).
    """

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):  # noqa: D105
        return "[Profile] {}".format(self.owner)
