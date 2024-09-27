# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""A pluggable Django application with several tools for The Tower game."""

__author__ = "Mischback"
"""The current project owner."""

__app_name__ = "django-penthouse"
"""The name of the application."""

__version__ = "1.0.0"
"""The current version."""

default_app_config = "penthouse.apps.PenthouseConfig"
"""The path to the app's default configuration class.

Consider this *legacy code*. See
:djangoapi:`Django's documentation<applications/#configuring-applications>` for
details.
"""
