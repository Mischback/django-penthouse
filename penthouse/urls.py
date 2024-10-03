# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from penthouse.views import tracker

app_name = "penthouse"

urlpatterns = [
    path("tracker/", tracker.tracker_overview, name="tracker-overview"),
    path("tracker/run/add/", tracker.RunCreateView.as_view(), name="tracker-run-add"),
]
