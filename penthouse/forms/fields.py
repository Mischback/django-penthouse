# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific fields."""


# Django imports
from django.forms.fields import ChoiceField, FloatField, MultiValueField

# app imports
from penthouse.forms.widgets import GameNumberWidget
from penthouse.game_constants import TowerUnitSuffix


class GameNumberField(MultiValueField):
    """Provide the required input fields for ingame numbers.

    The Tower tends to not use actual numbers, but shortens them using a
    *decimal unit prefix*, like ``k``, ``M`` or ``T``.
    """

    widget = GameNumberWidget

    def __init__(self, *args, **kwargs):
        self.value_field = FloatField()
        self.suffix_field = ChoiceField(choices=TowerUnitSuffix)

        fields = (self.value_field, self.suffix_field)

        super().__init__(*args, fields=fields, **kwargs)

    def compress(self, data_list):
        """Compress the values of multiple fields into one object for the ORM layer.

        The ``GameNumberWidget`` renders two form fields, one for the actual
        numeral and one for the suffix. To get to the actual value, those have
        to be multiplied and returned as an integer value.

        Notes
        -----
        See the corresponding method in :meth:`penthouse.forms.widgets.GameNumberWidget.decompress`
        method.
        """
        if data_list:
            # ``data_list`` contains the values of both widgets:
            #   - first value is the actual number
            #   - second value is the suffix's multiplier
            # print("[GameNumberField.compress()] {}".format(data_list))
            # print("[GameNumberField.compress()] {}".format(int(data_list[0]*int(data_list[1]))))
            return int(data_list[0] * int(data_list[1]))
        return None
