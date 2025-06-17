# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provide game-related constants for the app.

Those constants are derived from the actual game.
"""

# Python imports
from enum import Enum


class TowerNumberMagnitudes(Enum):
    """Magnitudes and their representations for numbers.

    The game tends to deal with rather large numbers. Usually those are
    presented as a decimal with an integral part of 1-3 digits and a fractional
    part of 2 digits and a corresponding unit suffix, derived from the
    short scale number naming system (see
    https://en.wikipedia.org/wiki/Names_of_large_numbers#Standard_dictionary_numbers
    and
    https://en.wikipedia.org/wiki/Long_and_short_scales for reference).
    """

    RAW = (0, "raw", "")
    KILO = (3, "kilo", "k")
    MILLION = (6, "Million", "M")
    BILLION = (9, "Billion", "B")
    TRILLION = (12, "Trillion", "T")
    QUADRILLION = (15, "Quadrillion", "q")
    QUINTILLION = (18, "Quintillion", "Q")
    SEXTILLION = (21, "Sextillion", "s")
    SEPTILLION = (24, "Septillion", "S")
    OCTILLION = (27, "Octillion", "O")
    NONILLION = (30, "Nonillion", "N")

    @classmethod
    def get_ss_list(cls):
        """Return a list of the short-scale notation in order of declaration."""
        return [e.value[2] for e in cls]
