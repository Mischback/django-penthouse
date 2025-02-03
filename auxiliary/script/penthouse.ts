import {
  createMetaDataChart,
  createRunTrackerChart,
} from "./penthouse/tracker";

/* Add a global event listener to apply the app-specific scripts. */
document.addEventListener("DOMContentLoaded", () => {
  /* Run Tracker */
  if (document.getElementById("penthouse-tracker")) {
    createRunTrackerChart();
  }

  /* Meta Tracker */
  if (document.getElementById("penthouse-meta")) {
    createMetaDataChart();
  }
});
