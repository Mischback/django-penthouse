# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provide game-related constants for the app."""


# Django imports
from django.db.models import IntegerChoices, TextChoices


class TowerTiers(TextChoices):
    """The game's different tiers as a central constant."""

    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    T4 = "T4"
    T5 = "T5"
    T6 = "T6"
    T7 = "T7"
    T8 = "T8"
    T9 = "T9"
    T10 = "T10"
    T11 = "T11"
    T12 = "T12"
    T13 = "T13"
    T14 = "T14"
    T15 = "T15"
    T16 = "T16"
    T17 = "T17"
    T18 = "T18"


class TowerUnitSuffix(IntegerChoices):
    """The game's suffixes for number values.

    Actually there are even more. These are pre-defined until ``O``, which
    should be enough for all of this app's needs.
    """

    UNIT_K = 1000, "k"
    UNIT_M = 1000000, "M"
    UNIT_B = 1000000000, "B"
    UNIT_T = 1000000000000, "T"
    UNIT_Q_MIN = 1000000000000000, "q"
    UNIT_Q = 1000000000000000000, "Q"
    UNIT_S_MIN = 1000000000000000000000, "s"
    UNIT_S = 1000000000000000000000000, "S"
    UNIT_O = 1000000000000000000000000000, "O"
