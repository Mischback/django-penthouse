# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific fields."""


# Django imports
from django.forms.fields import ChoiceField, FloatField, IntegerField, MultiValueField

# app imports
from penthouse.forms.widgets import GameDurationWidget, GameNumberWidget
from penthouse.game_constants import TowerUnitSuffix


class GameDurationField(MultiValueField):
    """Provide the required input field for durations."""

    widget = GameDurationWidget

    def __init__(self, *args, **kwargs):
        self.hour_field = IntegerField(min_value=0, step_size=1)
        self.minute_field = IntegerField(min_value=0, max_value=59, step_size=1)
        self.second_field = IntegerField(min_value=0, max_value=59, step_size=1)

        super().__init__(
            *args,
            fields=(self.hour_field, self.minute_field, self.second_field),
            **kwargs
        )

    def compress(self, data_list):
        """Compress the values of multiple fields into one object for the ORM layer.

        The ``GameDurationWidget`` renders three form fields (hours, minutes
        and seconds). To get to the actual value, those have to be converted
        into raw seconds.

        Notes
        -----
        See the corresponding method in :meth:`penthouse.forms.widgets.GameDurationWidget.decompress`
        method.
        """
        return int(
            int(data_list[0]) * 3600 + int(data_list[1]) * 60 + int(data_list[2])
        )


class GameNumberField(MultiValueField):
    """Provide the required input fields for ingame numbers.

    The Tower tends to not use actual numbers, but shortens them using a
    *decimal unit prefix*, like ``k``, ``M`` or ``T``.
    """

    widget = GameNumberWidget

    def __init__(self, *args, **kwargs):
        self.value_field = FloatField()
        self.suffix_field = ChoiceField(choices=TowerUnitSuffix)

        super().__init__(*args, fields=(self.value_field, self.suffix_field), **kwargs)

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
