import {
  createMetaDataChart,
  createRunTrackerChart,
} from "./penthouse/tracker";
import { initializeCollapsibles } from "./utility/collapsible";
import { sortTableByColumn } from "./utility/sortable";

/* Add a global event listener to apply the app-specific scripts. */
document.addEventListener("DOMContentLoaded", () => {
  /* Run Tracker */
  if (document.getElementById("penthouse-tracker")) {
    createRunTrackerChart();
    initializeCollapsibles();

    // apply a default sorting to the overall table
    sortTableByColumn(
      document.getElementById("tracker-data-table") as HTMLTableElement,
      1,
      true,
    );
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
  }
});
