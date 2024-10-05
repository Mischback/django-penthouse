# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific widgets."""

# Django imports
from django.forms.widgets import MultiWidget, NumberInput, Select

# app imports
from penthouse.game_constants import TowerUnitSuffix


class GameNumberWidget(MultiWidget):
    """Widget to render the app-specific ``GameNumberField``."""

    def __init__(self, *args, **kwargs):

        self.value_widget = NumberInput()
        self.suffix_widget = Select(choices=TowerUnitSuffix)
        widgets = (self.value_widget, self.suffix_widget)

        super().__init__(*args, widgets=widgets, **kwargs)

    def decompress(self, value):
        """Decompress the received value to render its components in dedicated widgets.

        Notes
        -----
        See the corresponding method in :meth:`penthouse.forms.fields.GameNumberField.compress`
        method.
        """
        if value:
            print("[GameNumberWidget.decompress()] {}".format(value))

        return [None, None]
