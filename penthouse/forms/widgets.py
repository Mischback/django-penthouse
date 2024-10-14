# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific widgets."""

# Django imports
from django.forms.widgets import MultiWidget, NumberInput, Select

# app imports
from penthouse.game_constants import TowerUnitSuffix
from penthouse.utility import seconds_to_hms


class GameDurationWidget(MultiWidget):
    """Widget to render the app-specific ``GameDurationField``."""

    def __init__(self, *args, **kwargs):
        self.hour_widget = NumberInput()
        self.minute_widget = NumberInput()
        self.second_widget = NumberInput()

        super().__init__(
            *args,
            widgets=(self.hour_widget, self.minute_widget, self.second_widget),
            **kwargs
        )

    def decompress(self, value):
        """Decompress the received value to render its components in dedicated widgets.

        Notes
        -----
        See the corresponding method in :meth:`penthouse.forms.fields.GameDurationField.compress`
        method.
        """
        if value:
            # print("[GameDurationWidget.decompress()] {}".format(value))

            h, m, s = seconds_to_hms(value)
            return [h, m, s]

        return [None, None, None]


class GameNumberWidget(MultiWidget):
    """Widget to render the app-specific ``GameNumberField``."""

    def __init__(self, *args, **kwargs):
        self.value_widget = NumberInput()
        self.suffix_widget = Select(choices=TowerUnitSuffix)

        super().__init__(
            *args, widgets=(self.value_widget, self.suffix_widget), **kwargs
        )

    def decompress(self, value):
        """Decompress the received value to render its components in dedicated widgets.

        Notes
        -----
        See the corresponding method in :meth:`penthouse.forms.fields.GameNumberField.compress`
        method.
        """
        if value:
            # print("[GameNumberWidget.decompress()] {}".format(value))

            value = int(value)
            if value / TowerUnitSuffix.UNIT_O > 1:
                return [value / TowerUnitSuffix.UNIT_O, TowerUnitSuffix.UNIT_O]
            elif value / TowerUnitSuffix.UNIT_S > 1:
                return [value / TowerUnitSuffix.UNIT_S, TowerUnitSuffix.UNIT_S]
            elif value / TowerUnitSuffix.UNIT_S_MIN > 1:
                return [value / TowerUnitSuffix.UNIT_S_MIN, TowerUnitSuffix.UNIT_S_MIN]
            elif value / TowerUnitSuffix.UNIT_Q > 1:
                return [value / TowerUnitSuffix.UNIT_Q, TowerUnitSuffix.UNIT_Q]
            elif value / TowerUnitSuffix.UNIT_Q_MIN > 1:
                return [value / TowerUnitSuffix.UNIT_Q_MIN, TowerUnitSuffix.UNIT_Q_MIN]
            elif value / TowerUnitSuffix.UNIT_T > 1:
                return [value / TowerUnitSuffix.UNIT_T, TowerUnitSuffix.UNIT_T]
            elif value / TowerUnitSuffix.UNIT_B > 1:
                return [value / TowerUnitSuffix.UNIT_B, TowerUnitSuffix.UNIT_B]
            elif value / TowerUnitSuffix.UNIT_M > 1:
                return [value / TowerUnitSuffix.UNIT_M, TowerUnitSuffix.UNIT_M]
            elif value / TowerUnitSuffix.UNIT_K > 1:
                return [value / TowerUnitSuffix.UNIT_K, TowerUnitSuffix.UNIT_K]
            else:
                return [value, None]

        return [None, None]
