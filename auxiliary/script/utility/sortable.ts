// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

import { findNextParent } from ".";

/**
 * Sort a HTML table by a given column.
 *
 * This function performs the actual sorting.
 */
export function sortTableByColumn(
  table: HTMLTableElement,
  columnId: number,
  sortDirDesc: boolean = false,
): void {
  const rows: HTMLTableRowElement[] = Array.from(
    table.querySelectorAll("tbody tr"),
  );

  rows.sort((rowA, rowB) => {
    const cellA = rowA.cells[columnId] as HTMLTableCellElement;
    const cellB = rowB.cells[columnId] as HTMLTableCellElement;

    let valA = cellA ? cellA.textContent?.trim() : "";
    if (valA === undefined) valA = "";

    let valB = cellB ? cellB.textContent?.trim() : "";
    if (valB === undefined) valB = "";

    if (isNaN(Number(valA)) || isNaN(Number(valB))) {
      return sortDirDesc ? valB.localeCompare(valA) : valA.localeCompare(valB);
    }

    return sortDirDesc
      ? Number(valB) - Number(valA)
      : Number(valA) - Number(valB);
  });

  const tbody = table.querySelector("tbody") as HTMLTableSectionElement;
  tbody.innerHTML = "";
  rows.forEach((row) => tbody.appendChild(row));
}

/**
 * Handle clicks on the table header cells.
 *
 * Clicks on the header will toggle between ascending and descending sorting
 * for that column.
 *
 * This function will handle the actual toggle and will remove/add CSS classes
 * for the styling.
 */
export function thClickHandler(thElement: HTMLTableCellElement): void {
  const classAsc = "sortable-ascending";
  const classDesc = "sortable-descending";
  const parentTable = findNextParent(thElement, "table");
  const sortingRaw = Number(thElement.dataset["raw"]);
  const isDescending = thElement.classList.contains(classDesc);

  // Remove all classes that indicate the sorting direction from all sortable
  // table header cells.
  parentTable.querySelectorAll("thead .sortable-column").forEach((item) => {
    item.classList.remove(...[classAsc, classDesc]);
  });

  // Apply the actual sorting and add a class to indicate the sorting direction
  if (isDescending) {
    sortTableByColumn(parentTable as HTMLTableElement, sortingRaw, false);
    thElement.classList.add(classAsc);
  } else {
    sortTableByColumn(parentTable as HTMLTableElement, sortingRaw, true);
    thElement.classList.add(classDesc);
  }
}
