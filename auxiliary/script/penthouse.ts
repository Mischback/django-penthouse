import { createLineChartFromTable } from "./visual/charts";

/* Add a global event listener to apply the app-specific scripts. */
document.addEventListener("DOMContentLoaded", () => {
  /* Meta Tracker */
  if (document.getElementById("penthouse-meta")) {
    createLineChartFromTable(
      "#meta-data-table",
      ".meta-date-raw",
      ".meta-ltc-raw",
      "#meta-data-canvas",
    );
  }
});
