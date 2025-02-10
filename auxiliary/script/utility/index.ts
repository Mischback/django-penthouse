/**
 * Get a DOM element by a given query.
 *
 * This is a thin wrapper around ``querySelector()``, which throws an ``Error``
 * if no element could be found.
 */
export function getDomElement(
  root: Element | Document | null,
  query: string,
): HTMLElement {
  // Start at ``document``, if ``root`` is unspecified
  if (root === null) {
    root = document;
  }

  const tmp = root.querySelector(query);
  if (tmp === null) {
    throw new Error(`Missing required DOM element with query '${query}'`);
  }

  return tmp as HTMLElement;
}

/**
 * Find the lowest non-zero number in an array of numbers.
 */
export function findNonZeroMin(input: number[]): number {
  return Math.min.apply(null, input);
}

/**
 * Apply the game-specific number formatting.
 *
 * The base implementation was provided by ChatGPT, adjusted to match the
 * actual in-game number conventions.
 */
export function formatLargeNumber(num: number, precision: number = 2): string {
  const suffixes = ["", "k", "M", "B", "T", "q", "Q", "s", "S", "O", "N"];
  const sign = num < 0 ? "-" : ""; // Handle negative numbers
  num = Math.abs(num); // Work with absolute value

  if (num < 1000) return sign + num.toString(); // No formatting needed for numbers less than 1000

  let magnitude = Math.floor(Math.log10(num) / 3); // Determine the magnitude (thousands, millions, etc.)

  // Ensure we don't exceed the available suffixes (i.e., handle up to 1Q)
  if (magnitude >= suffixes.length) magnitude = suffixes.length - 1;

  // Scale down the number by the appropriate power of 1000 and add the suffix
  const scaledNumber = (num / Math.pow(1000, magnitude)).toFixed(precision);
  return sign + scaledNumber + suffixes[magnitude];
}
