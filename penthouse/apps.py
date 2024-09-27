# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Application configuration as required by Django."""

# Django imports
from django.apps import AppConfig


class PenthouseConfig(AppConfig):
    """Application-specific configuration class, as required by Django.

    As of now, this doesn't really do anything and just provides meta
    information.
    """

    name = "penthouse"
    verbose_name = "Penthouse"

    def ready(self):
        """Apply app-specific stuff."""
        pass
