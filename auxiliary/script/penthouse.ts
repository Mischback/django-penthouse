// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

import { applyProgressiveEnhancement } from "./utility";
import { initializeCollapsible } from "./utility/collapsible";

/* Add a global event listener to apply the app-specific scripts. */
document.addEventListener("DOMContentLoaded", () => {
  console.debug("performing the progressive enhancement");

  // account-create
  if (document.getElementById("ph-account-create")) {
    applyProgressiveEnhancement(
      ".collapsible-container",
      initializeCollapsible,
    );
  }

  // account-list
  if (document.getElementById("ph-account-list")) {
    applyProgressiveEnhancement(
      ".collapsible-container",
      initializeCollapsible,
    );
  }

  // progression-overview
  if (document.getElementById("ph-progression-overview")) {
    applyProgressiveEnhancement(
      ".collapsible-container",
      initializeCollapsible,
    );
  }

  // progression-sample-create
  if (document.getElementById("ph-progression-sample-create")) {
    applyProgressiveEnhancement(
      ".collapsible-container",
      initializeCollapsible,
    );
  }
});
