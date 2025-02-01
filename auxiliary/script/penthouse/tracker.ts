import { getDomElement } from "../utility";
import { createLineChart } from "../utility/charts";

/**
 * Create the visual representation of the meta datapoints.
 *
 * This function is closely tied to the app's view and template.
 */
export function createMetaDataChart(): void {
  const table = getDomElement(null, "#meta-data-table");

  // grab raw data from the table
  let tableRow;
  const labels = [];
  const ltcData = [];
  const ltsData = [];
  for (let i = 1; i < table.rows.length; i++) {
    let thisLabel;
    let thisLtc;
    let thisLts;
    tableRow = table.rows[i];

    // the label is determined by the datapoints ``date``
    thisLabel = getDomElement(tableRow, ".meta-date-raw").innerHTML;

    // we want LTC/LTS as datapoints
    thisLtc = getDomElement(tableRow, ".meta-ltc-raw").innerHTML;
    thisLts = getDomElement(tableRow, ".meta-lts-raw").innerHTML;

    labels.push(thisLabel);
    ltcData.push(thisLtc);
    ltsData.push(thisLts);
  }

  console.log(labels);
  console.log(ltcData);
  console.log(ltsData);

  const chart = createLineChart("#meta-data-canvas", labels, ltcData);
}
