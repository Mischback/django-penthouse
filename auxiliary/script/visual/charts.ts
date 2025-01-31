import { getDomElement } from "../utility";

export function createLineChartFromTable(
  dataTableId: string,
  labelSelector: string,
  valueSelector: string,
  canvasId: string,
): void {
  /* grab the required elements from the DOM */
  const table = getDomElement(null, dataTableId);
  const canvas = getDomElement(null, canvasId);

  /* get the raw data from the table */
  for (let i = 1; i < table.rows.length; i++) {
    const tableRow = table.rows[i];
    const rowData = {};

    rowData["label"] = getDomElement(tableRow, labelSelector).innerHTML;
    /* console.log(getDomElement(tableRow, labelSelector)); */

    rowData["value"] = getDomElement(tableRow, valueSelector).innerHTML;
    /* console.log(getDomElement(tableRow, valueSelector)); */

    console.log(rowData);
  }

  /* create the actual chart */
}
