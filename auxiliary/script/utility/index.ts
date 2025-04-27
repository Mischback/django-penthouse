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

/**
 * Parse a string into a number.
 *
 * This is meant to parse something, that is retrieved from the DOM, so it can
 * deal with ``string`` types (this is the intended use case), with ``null``
 * and ``undefined`` values.
 *
 * It will either return an actual ``number`` or ``undefined`` if the input
 * could not be parsed into a number.
 */
export function parseNumber(value: string | null | undefined) {
  if (!value) {
    return undefined;
  }

  const parsed = Number(value);
  return isNaN(parsed) ? undefined : parsed;
}

/**
 * Parse a string into a number or ``null``.
 *
 * uPlot uses ``null`` to indicate *missing datapoints* in a series.
 */
export function parseNumberOrNull(
  value: string | null | undefined,
): number | null {
  const parsed = parseNumber(value);

  if (parsed === undefined) {
    return null;
  }

  return parsed;
}
