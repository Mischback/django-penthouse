# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from penthouse.views import profile, tracker

app_name = "penthouse"

urlpatterns = [
    path("profile/delete/", profile.ProfileDeleteView.as_view(), name="profile-delete"),
    path("profile/update/", profile.ProfileUpdateView.as_view(), name="profile-update"),
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
