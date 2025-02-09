import {
  createMetaDataChart,
  createRunTrackerChart,
} from "./penthouse/tracker";
import { initializeCollapsibles } from "./utility/collapsible";

/* Add a global event listener to apply the app-specific scripts. */
document.addEventListener("DOMContentLoaded", () => {
  /* Run Tracker */
  if (document.getElementById("penthouse-tracker")) {
    createRunTrackerChart();
    initializeCollapsibles();
  }

  /* Meta Tracker */
  if (document.getElementById("penthouse-meta")) {
    createMetaDataChart();
  }
});
