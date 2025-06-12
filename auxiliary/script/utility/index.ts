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
 * Provide the in-game magnitudes as flat list.
 *
 * Required by ``convertNumberForDisplay()``.
 */
const TOWER_NUMBER_MAGNITUDES = [
  "",
  "k",
  "M",
  "B",
  "T",
  "q",
  "Q",
  "s",
  "S",
  "O",
  "N",
];

/**
 * Provide the default magnitude of numbers.
 *
 * Required by ``convertNumberForDisplay()``.
 */
const TOWER_DEFAULT_MAGNITUDE = "T";

/**
 * Convert the internal representation of a number into the expected notation.
 *
 * This is the JS/TS implementation of ``convertNumberForDisplay()`` in
 * ``penthouse/utility.py``.
 */
export function convertNumberForDisplay(
  num: number,
  suffix: string = TOWER_DEFAULT_MAGNITUDE,
  precision: number = 2,
): string {
  if (num <= 0) {
    return "0";
  }

  const currentMag = TOWER_NUMBER_MAGNITUDES.indexOf(suffix);

  if (num < 1) {
    return convertNumberForDisplay(
      num * 1000,
      TOWER_NUMBER_MAGNITUDES[currentMag - 1],
    );
  }

  if (num >= 1000) {
    return convertNumberForDisplay(
      num / 1000,
      TOWER_NUMBER_MAGNITUDES[currentMag + 1],
    );
  }

  const precisionMod = Math.pow(10, precision);
  return `${Math.round((num + Number.EPSILON) * precisionMod) / precisionMod}${suffix}`;
}

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

export function parseNumberOrZero(value: string | null | undefined): number {
  const parsed = parseNumber(value);

  if (parsed === undefined) {
    return 0;
  }

  return parsed;
}
