import { createMetaDataChart } from "./penthouse/tracker";

/* Add a global event listener to apply the app-specific scripts. */
document.addEventListener("DOMContentLoaded", () => {
  /* Meta Tracker */
  if (document.getElementById("penthouse-meta")) {
    createMetaDataChart();
  }
});
