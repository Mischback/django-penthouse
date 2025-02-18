/**
 * Sort a HTML table by a given column.
 */
export function sortTableByColumn(
  table: HTMLTableElement,
  columnId: number,
  isDescending: boolean = false,
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
      return isDescending ? valB.localeCompare(valA) : valA.localeCompare(valB);
    }

    return isDescending
      ? Number(valB) - Number(valA)
      : Number(valA) - Number(valB);
  });

  const tbody = table.querySelector("tbody") as HTMLTableSectionElement;
  tbody.innerHTML = "";
  rows.forEach((row) => tbody.appendChild(row));
}
