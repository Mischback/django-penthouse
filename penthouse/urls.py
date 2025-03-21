# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from penthouse.views.account import AccountCreateView

app_name = "penthouse"

urlpatterns = [
    path("account/add/", AccountCreateView.as_view(), name="account-create"),
    # path("account/<int:account_id>/update/", name="account-update"),
    # path("account/<int:account_id>/delete/", name="account-delete"),
    # path("account/list/", name="account-list"),
    # path("<int:account_id>/", name="account-overview"),
]
