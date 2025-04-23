// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

import { applyProgressiveEnhancement } from "./utility";
import { initializeCollapsible } from "./utility/collapsible";

/* Add a global event listener to apply the app-specific scripts. */
document.addEventListener("DOMContentLoaded", () => {
  console.debug("performing the progressive enhancement");

  if (document.getElementById("ph-progression-overview")) {
    applyProgressiveEnhancement(
      ".collapsible-container",
      initializeCollapsible,
    );
  }
});
