# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Integrates the app's models into Django's admin interface."""

# Django imports
from django.contrib import admin

# app imports
from penthouse.models.profile import Profile
from penthouse.models.tracker import Run


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):  # noqa: D101
    pass
