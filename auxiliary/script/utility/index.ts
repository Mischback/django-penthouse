// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

/**
 * Type definition for a setup function.
 *
 * This function is called on the elements and should do all necessary setup
 * and initialization steps.
 */
export type setupFunc = (element: HTMLElement) => void;

/**
 * Apply a setup function to HTML elements.
 *
 * The elements are identified by a *query* and the ``setupFunc`` is called on
 * each of them.
 */
export function applyProgressiveEnhancement(
  query: string,
  setupFunc: setupFunc,
): void {
  const elements: NodeListOf<HTMLElement> = document.querySelectorAll(query);

  if (elements.length <= 0) {
    console.debug(`No elements for '${query}' found!`);
    return;
  }

  elements.forEach(setupFunc);
}
