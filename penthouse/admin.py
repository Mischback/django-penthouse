# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Integrates the app's models into Django's admin interface."""

# Django imports
from django.contrib import admin

# app imports
from penthouse.models.account import Account
from penthouse.models.progression import Sample


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):  # noqa: D101
    pass
