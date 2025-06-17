# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provide app-specific widgets."""


# Django imports
from django.forms.widgets import MultiWidget, NumberInput, Select

# app imports
from penthouse.utility import NUMBER_MAGNITUDES, convertNumberForDisplay

LARGE_NUMBER_SUFFIX_CHOICES = [(e, e) for e in NUMBER_MAGNITUDES]


class LargeNumberWidget(MultiWidget):
    """Provide the custom inputs for large values.

    See :class:`~penthouse.forms.fields.LargeNumberField` for the corresponding
    field implementation.
    """

    def __init__(self, *args, **kwargs):

        self.num_widget = NumberInput()
        self.suffix_widget = Select(choices=LARGE_NUMBER_SUFFIX_CHOICES)

        super().__init__(*args, widgets=(self.num_widget, self.suffix_widget), **kwargs)

    def decompress(self, value):
        """Decompress the single value from the ORM layer for display in multiple fields.

        Notes
        -----
        See the corresponding :meth:`~penthouse.forms.fields.LargeNumberField.compress`
        method.

        The internal implementation relies on
        :func:`~penthouse.utility.convertNumberForDisplay`.
        """
        if value:
            num, suffix = convertNumberForDisplay(value)

            return [num, suffix]

        return [None, None]
