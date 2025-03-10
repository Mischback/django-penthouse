# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Integrates the app's models into Django's admin interface."""

# Django imports
from django.contrib import admin

# app imports
from penthouse.models.profile import Profile
from penthouse.models.progress import Milestone, MilestoneSection, MilestoneStep
from penthouse.models.relics import Relic
from penthouse.models.tracker import MetaData, Run


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(MilestoneSection)
class MilestoneSectionAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(MilestoneStep)
class MilestoneStepAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(MetaData)
class MetaAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Relic)
class RelicAdmin(admin.ModelAdmin):  # noqa: D101
    pass
