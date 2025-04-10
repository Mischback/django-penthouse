# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provide utility functions used in several places throughout the application."""

# app imports
from penthouse.game_constants import TowerNumberMagnitudes

NUMBER_MAGNITUDES = TowerNumberMagnitudes.get_ss_list()
"""This module requires the in game-specific number magnitudes as a flat list."""

NUMBER_DEFAULT_MAGNITUDE = TowerNumberMagnitudes.TRILLION.value[2]
"""Throughout the app, large numbers are internally stored in *trillions*."""


def convertNumberForDisplay(num, suffix=NUMBER_DEFAULT_MAGNITUDE, precision=2):
    """Convert the internal representation of a number into the expected display value.

    The game deal with rather large number internally, but the user gets an
    abstracted representation. This function takes a number and converts it
    into the expected display notation (1-3 integral digits, 0-2 fractional
    digits with a suffix).
    """
    if num <= 0:
        return 0, NUMBER_MAGNITUDES[0]

    current_mag = NUMBER_MAGNITUDES.index(suffix)

    if num < 1:
        return convertNumberForDisplay(num * 1000, NUMBER_MAGNITUDES[current_mag - 1])

    if num >= 1000:
        return convertNumberForDisplay(num / 1000, NUMBER_MAGNITUDES[current_mag + 1])

    return round(num, precision), suffix
