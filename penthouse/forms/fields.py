# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provide app-specific fields."""

# Django imports
from django.forms.fields import ChoiceField, FloatField, MultiValueField

# app imports
from penthouse.forms.widgets import LARGE_NUMBER_SUFFIX_CHOICES, LargeNumberWidget
from penthouse.utility import convert_large_number


class LargeNumberField(MultiValueField):
    """Provide inputs for large values.

    The game deals with rather large numbers internally, especially regarding
    coin values. The user usually only gets an abstracted representation,
    based on 1-3 integral digits, 0-2 fractional digits and a suffix based off
    the short scale number naming system (see
    https://en.wikipedia.org/wiki/Names_of_large_numbers#Standard_dictionary_numbers
    for reference.

    This field will provide the required inputs for form validation.
    :class:`~penthouse.forms.widgets.LargeNumberWidget` will handle the actual
    HTML presentation.
    """

    widget = LargeNumberWidget

    def __init__(self, *args, **kwargs):

        self.num_field = FloatField()
        self.suffix_field = ChoiceField(
            choices=LARGE_NUMBER_SUFFIX_CHOICES, required=False
        )

        super().__init__(*args, fields=(self.num_field, self.suffix_field), **kwargs)

    def compress(self, data_list):
        """Compress the values of multiple fields into one value for the ORM layer.

        Notes
        -----
        See the corresponding :meth:`~penthouse.forms.widgets.LargeNumberWidget.decompress`
        method.

        The internal implementation relies on
        :func:`~penthouse.utility.convert_large_number`.
        """
        if data_list:
            num, _ = convert_large_number(data_list[0], data_list[1])
            return round(num, 12)

        return None
