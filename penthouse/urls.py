# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from penthouse.views.account import (
    AccountCreateView,
    AccountDeleteView,
    AccountListView,
    AccountOverview,
    AccountUpdateView,
)
from penthouse.views.progression import ProgressionOverview, SampleCreateView

app_name = "penthouse"

urlpatterns = [
    # Account-related views
    path("account/add/", AccountCreateView.as_view(), name="account-create"),
    path(
        "account/<int:account_id>/update/",
        AccountUpdateView.as_view(),
        name="account-update",
    ),
    path(
        "account/<int:account_id>/delete/",
        AccountDeleteView.as_view(),
        name="account-delete",
    ),
    path("account/list/", AccountListView.as_view(), name="account-list"),
    path("<int:account_id>/", AccountOverview.as_view(), name="account-overview"),
    #
    # Progression-related views
    path(
        "<int:account_id>/progression/",
        ProgressionOverview.as_view(),
        name="progression-overview",
    ),
    path(
        "<int:account_id>/progression/sample/add/",
        SampleCreateView.as_view(),
        name="progression-sample-create",
    ),
    # path("progression/sample/<int:sample_id>/update/", name="progression-sample-update"),
    # path("progression/sample/<int:sample_id>/delete/", name="progression-sample-delete"),
]
