# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from penthouse.views.account import (
    AccountCreateView,
    AccountListView,
    AccountOverview,
    AccountUpdateView,
)

app_name = "penthouse"

urlpatterns = [
    # Account-related views
    path("account/add/", AccountCreateView.as_view(), name="account-create"),
    path(
        "account/<int:account_id>/update/",
        AccountUpdateView.as_view(),
        name="account-update",
    ),
    # path("account/<int:account_id>/delete/", name="account-delete"),
    path("account/list/", AccountListView.as_view(), name="account-list"),
    path("<int:account_id>/", AccountOverview.as_view(), name="account-overview"),
]
