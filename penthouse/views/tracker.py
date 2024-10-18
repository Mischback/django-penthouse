# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Views related to the run tracker functions."""

# Python imports
import re
from collections import defaultdict, deque
from statistics import mean

# Django imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# app imports
from penthouse.models.profile import Profile
from penthouse.models.tracker import Run, RunForm
from penthouse.views.mixins import ProfileIDMixin, RestrictToUserMixin


def _get_deque5():
    """Provide a default size ``collections.deque`` instance."""
    return deque(maxlen=5)


def natural_sort_key(s, _nsre=re.compile(r"(\d+)")):
    """Provide natural sorting of strings.

    E.g. ["T12", "T1"] will sort to ["T1", "T12"].

    See https://stackoverflow.com/a/16090640
    """
    return [int(text) if text.isdigit() else text.lower for text in _nsre.split(s)]


class RunData:
    """A temporary data class to apply additional evaluation to ``Run`` instances."""

    def __init__(self, id, date, tier, waves, duration, coins, cells, notes):
        self.id = id
        self.date = date
        self.tier = tier
        self.waves = waves
        self.duration = duration
        self.coins = coins
        self.cells = cells
        self.notes = notes

        self.coins_hour = int(coins / (duration / 3600))
        self.coins_wave = int(coins / waves)
        self.cells_hour = int(cells / (duration / 3600))
        self.cells_wave = int(cells / waves)

        self.pb_coins = False
        self.pb_cells = False
        self.pb_coins_hour = False
        self.pb_cells_hour = False

        self.coins_avg5 = 0
        self.coins_hour_avg5 = 0
        self.cells_avg5 = 0
        self.cells_hour_avg5 = 0


class TierData:
    """A temporary data class to provide the last 5 runs by tier."""

    def __init__(self):
        self._entries = defaultdict(_get_deque5)

    def add(self, entry):
        """Add an entry to the class."""
        if entry is None:
            raise Exception("An entry is required")

        self._entries[entry.tier].append(entry)

    def get_results(self):
        """Evaluate the results."""
        results = {}
        for k in self._entries:
            results[k] = {}

            tmp = [e.waves for e in self._entries[k]]
            results[k]["waves_min"] = min(tmp)
            results[k]["waves_avg"] = mean(tmp)
            results[k]["waves_max"] = max(tmp)

            tmp = [e.coins for e in self._entries[k]]
            results[k]["coins_min"] = min(tmp)
            results[k]["coins_avg"] = mean(tmp)
            results[k]["coins_max"] = max(tmp)

            tmp = [e.coins_hour for e in self._entries[k]]
            results[k]["coins_hour_min"] = min(tmp)
            results[k]["coins_hour_avg"] = mean(tmp)
            results[k]["coins_hour_max"] = max(tmp)

            tmp = [e.cells for e in self._entries[k]]
            results[k]["cells_min"] = min(tmp)
            results[k]["cells_avg"] = mean(tmp)
            results[k]["cells_max"] = max(tmp)

            tmp = [e.cells_hour for e in self._entries[k]]
            results[k]["cells_hour_min"] = min(tmp)
            results[k]["cells_hour_avg"] = mean(tmp)
            results[k]["cells_hour_max"] = max(tmp)

        return {
            key: results[key] for key in sorted(results.keys(), key=natural_sort_key)
        }


@login_required
def tracker_overview(request):
    """Provide an overview over all runs."""
    runs_raw = (
        Run.objects.filter_by_user(user=request.user)
        .select_related("profile")
        .order_by("date")
    )

    runs = []
    runs_by_tier = TierData()
    pb_coins = None
    pb_cells = None
    pb_coins_hour = None
    pb_cells_hour = None
    run_i = 0
    for run in runs_raw.iterator():
        item = RunData(
            run.id,
            run.date,
            run.tier,
            run.waves,
            run.duration,
            run.coins,
            run.cells,
            run.notes,
        )
        runs_by_tier.add(item)

        try:
            if item.coins > pb_coins.coins:
                pb_coins = item
                item.pb_coins = True
        except AttributeError:
            pb_coins = item
            item.pb_coins = True

        try:
            if item.cells > pb_cells.cells:
                pb_cells = item
                item.pb_cells = True
        except AttributeError:
            pb_cells = item
            item.pb_cells = True

        try:
            if item.coins_hour > pb_coins_hour.coins_hour:
                pb_coins_hour = item
                item.pb_coins_hour = True
        except AttributeError:
            pb_coins_hour = item
            item.pb_coins_hour = True

        try:
            if item.cells_hour > pb_cells_hour.cells_hour:
                pb_cells_hour = item
                item.pb_cells_hour = True
        except AttributeError:
            pb_cells_hour = item
            item.pb_cells_hour = True

        if run_i > 3:
            item.coins_avg5 = int(
                (
                    runs[run_i - 4].coins
                    + runs[run_i - 3].coins
                    + runs[run_i - 2].coins
                    + runs[run_i - 1].coins
                    + item.coins
                )
                / 5
            )
            item.coins_hour_avg5 = int(
                (
                    runs[run_i - 4].coins_hour
                    + runs[run_i - 3].coins_hour
                    + runs[run_i - 2].coins_hour
                    + runs[run_i - 1].coins_hour
                    + item.coins_hour
                )
                / 5
            )
            item.cells_avg5 = int(
                (
                    runs[run_i - 4].cells
                    + runs[run_i - 3].cells
                    + runs[run_i - 2].cells
                    + runs[run_i - 1].cells
                    + item.cells
                )
                / 5
            )
            item.cells_hour_avg5 = int(
                (
                    runs[run_i - 4].cells_hour
                    + runs[run_i - 3].cells_hour
                    + runs[run_i - 2].cells_hour
                    + runs[run_i - 1].cells_hour
                    + item.cells_hour
                )
                / 5
            )

        runs.append(item)
        run_i = run_i + 1

    runs_by_tier.get_results()

    return render(
        request,
        "penthouse/tracker_overview.html",
        {
            "profile": run.profile,
            "runs": runs,
            "runs_by_tier": runs_by_tier.get_results(),
            "pb_coins": pb_coins,
            "pb_coins_hour": pb_coins_hour,
            "pb_cells": pb_cells,
            "pb_cells_hour": pb_cells_hour,
            "threshold_top_coins": pb_coins.coins
            * (run.profile.settings_tracker_threshold_top_coins / 100),
            "threshold_top_coins_hour": pb_coins_hour.coins_hour
            * (run.profile.settings_tracker_threshold_top_coins_hour / 100),
            "threshold_top_cells": pb_cells.cells
            * (run.profile.settings_tracker_threshold_top_cells / 100),
            "threshold_top_cells_hour": pb_cells_hour.cells_hour
            * (run.profile.settings_tracker_threshold_top_cells_hour / 100),
        },
    )


class RunCreateView(LoginRequiredMixin, ProfileIDMixin, generic.CreateView):
    """Generic class-based view implementation to add ``Run`` instances."""

    model = Run

    form_class = RunForm

    template_name_suffix = "_create"

    success_url = reverse_lazy("penthouse:tracker-overview")

    def form_valid(self, form):  # noqa: D102
        form.instance.profile = Profile.objects.get(owner=self.request.user)

        return super().form_valid(form)


class RunDeleteView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.DeleteView
):
    """Generic class-based view implementation to delete ``Run`` instances."""

    model = Run

    context_object_name = "run_item"

    pk_url_kwarg = "run_id"

    success_url = reverse_lazy("penthouse:tracker-overview")


class RunUpdateView(
    LoginRequiredMixin, RestrictToUserMixin, ProfileIDMixin, generic.UpdateView
):
    """Generic class-based view implementation to update ``Run`` instances."""

    model = Run

    form_class = RunForm

    template_name_suffix = "_update"

    pk_url_kwarg = "run_id"

    success_url = reverse_lazy("penthouse:tracker-overview")
