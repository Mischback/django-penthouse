# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from penthouse.views import profile, progress, relics, tracker

app_name = "penthouse"

urlpatterns = [
    path("meta/", tracker.MetaDataListView.as_view(), name="meta-data-overview"),
    path("meta/add/", tracker.MetaDataCreateView.as_view(), name="meta-data-add"),
    path(
        "meta/<int:meta_id>/delete/",
        tracker.MetaDataDeleteView.as_view(),
        name="meta-data-delete",
    ),
    path(
        "meta/<int:meta_id>/update/",
        tracker.MetaDataUpdateView.as_view(),
        name="meta-data-update",
    ),
    path("profile/delete/", profile.ProfileDeleteView.as_view(), name="profile-delete"),
    path(
        "profile/settings/update/",
        profile.ProfileSettingsUpdateView.as_view(),
        name="profile-settings-update",
    ),
    path("progress/", progress.MilestoneListView.as_view(), name="progress-milestones"),
    path(
        "progress/milestone/add/",
        progress.MilestoneCreateView.as_view(),
        name="progress-milestone-add",
    ),
    path(
        "progress/section/add/<int:milestone_id>/",
        progress.MilestoneSectionCreateView.as_view(),
        name="progress-section-add",
    ),
    path(
        "progress/section/<int:section_id>/update/",
        progress.MilestoneSectionUpdateView.as_view(),
        name="progress-section-update",
    ),
    path(
        "progress/step/add/<int:milestonesection_id>/",
        progress.MilestoneStepCreateView.as_view(),
        name="progress-step-add",
    ),
    path(
        "progress/step/<int:step_id>/update",
        progress.MilestoneStepUpdateView.as_view(),
        name="progress-step-update",
    ),
    path(
        "progress/step/toggle/<int:step_id>/",
        progress.milestonestep_toggle,
        name="progress-step-toggle",
    ),
    path("relics/", relics.RelicListView.as_view(), name="relics-list"),
    path("relics/claim/<int:relic_id>/", relics.relic_claim, name="relics-claim"),
    path("relics/unclaim/<int:relic_id>/", relics.relic_unclaim, name="relics-unclaim"),
    path("tracker/", tracker.tracker_overview, name="tracker-overview"),
    path("tracker/run/add/", tracker.RunCreateView.as_view(), name="tracker-run-add"),
    path(
        "tracker/run/<int:run_id>/delete/",
        tracker.RunDeleteView.as_view(),
        name="tracker-run-delete",
    ),
    path(
        "tracker/run/<int:run_id>/update/",
        tracker.RunUpdateView.as_view(),
        name="tracker-run-update",
    ),
]
