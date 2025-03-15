// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

import {
  createMetaDataChart,
  createRunTrackerChart,
} from "./penthouse/tracker";
import { initializeEditModeToggles } from "./penthouse/progress";
import { initializeCollapsibles } from "./utility/collapsible";
import { sortTableByColumn, thClickHandler } from "./utility/sortable";

/* Add a global event listener to apply the app-specific scripts. */
document.addEventListener("DOMContentLoaded", () => {
  /* Run Tracker */
  if (document.getElementById("penthouse-tracker")) {
    createRunTrackerChart();
    initializeCollapsibles();

    // Apply the click handlers to sort the table by columns
    const defaultSortingColumn = document.getElementById(
      "tracker-data-date",
    ) as HTMLTableCellElement;
    defaultSortingColumn.addEventListener("click", (e) => {
      thClickHandler(e.currentTarget as HTMLTableCellElement);
    });

    document
      .getElementById("tracker-data-coins")
      .addEventListener("click", (e) => {
        thClickHandler(e.currentTarget as HTMLTableCellElement);
      });

    document
      .getElementById("tracker-data-coins-h")
      .addEventListener("click", (e) => {
        thClickHandler(e.currentTarget as HTMLTableCellElement);
      });

    // apply a default sorting to the overall table
    thClickHandler(defaultSortingColumn);
  }

  /* Meta Tracker */
  if (document.getElementById("penthouse-meta")) {
    createMetaDataChart();
    initializeCollapsibles();

    // apply a default sorting to the overall table
    sortTableByColumn(
      document.getElementById("meta-data-table") as HTMLTableElement,
      1,
      true,
    );
  }

  /* Relic Tracker */
  if (document.getElementById("penthouse-relics")) {
    initializeCollapsibles();

    document
      .getElementById("relic-data-bonus")
      .addEventListener("click", (e) => {
        thClickHandler(e.currentTarget as HTMLTableCellElement);
      });

    document
      .getElementById("relic-data-rarity")
      .addEventListener("click", (e) => {
        thClickHandler(e.currentTarget as HTMLTableCellElement);
      });

    document
      .getElementById("relic-data-obtained")
      .addEventListener("click", (e) => {
        thClickHandler(e.currentTarget as HTMLTableCellElement);
      });
  }

  /* Progress Planning */
  if (document.getElementById("penthouse-progress")) {
    initializeCollapsibles();
    initializeEditModeToggles();
  }
});
