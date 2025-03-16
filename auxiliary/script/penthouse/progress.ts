// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

export function initializeEditModeToggles(): void {
  const milestones = document.querySelectorAll(".progress-planning-milestone");

  milestones.forEach((m) => {
    const id = m.id;

    const toggle = m.querySelector(".toggle-button input");
    if (!toggle) return;

    // get the last state from localStorage and restore it
    const state = localStorage.getItem(`progress-edit-mode-state-${id}`);
    if (state === "active") {
      m.classList.remove("view-mode");
      toggle.checked = true;
    } else {
      m.classList.add("view-mode");
      toggle.checked = false;
    }

    // add the event listener to the toggle button
    toggle.addEventListener("click", () => toggleEditMode(m, id));
  });
}

function toggleEditMode(container: HTMLElement, id: string): void {
  const viewModeActive = container.classList.contains("view-mode");

  if (viewModeActive) {
    container.classList.remove("view-mode");
    localStorage.setItem(`progress-edit-mode-state-${id}`, "active");
  } else {
    container.classList.add("view-mode");
    localStorage.setItem(`progress-edit-mode-state-${id}`, "inactive");
  }
}
