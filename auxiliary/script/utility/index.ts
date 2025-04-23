// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

export type setupFunc = (element: HTMLElement) => void;

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
