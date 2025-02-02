// FIXME: Convert to direct imports for treeshaking
import Chart from "chart.js/auto";
import "chartjs-adapter-date-fns";

import { getDomElement } from "../utility";
// import { createLineChart } from "../utility/charts";

/**
 * Create the visual representation of the meta datapoints.
 *
 * This function is closely tied to the app's view and template.
 */
export function createMetaDataChart(): void {
  const table = <HTMLTableElement>getDomElement(null, "#meta-data-table");
  const canvas = <HTMLCanvasElement>getDomElement(null, "#meta-data-canvas");

  // grab raw data from the table
  let tableRow;
  const labels = [];
  const ltcData = [];
  const ltsData = [];
  for (let i = 1; i < table.rows.length; i++) {
    tableRow = table.rows[i];

    // the label is determined by the datapoints ``date``
    // @ts-expect-error TS2345: Will work or catched by ``getDomElement()``
    const thisLabel = getDomElement(tableRow, ".meta-date-raw").innerHTML;
    const timestamp = parseInt(thisLabel, 10) * 1000;

    // we want LTC/LTS as datapoints
    // @ts-expect-error TS2345: Will work or catched by ``getDomElement()``
    const thisLtc = getDomElement(tableRow, ".meta-ltc-raw").innerHTML;
    // @ts-expect-error TS2345: Will work or catched by ``getDomElement()``
    const thisLts = getDomElement(tableRow, ".meta-lts-raw").innerHTML;

    labels.push(timestamp);
    ltcData.push(thisLtc);
    ltsData.push(thisLts);
  }

  // console.log(labels);
  // console.log(ltcData);
  // console.log(ltsData);

  // TODO: This still needs lots of work. Actually I would love to provide the
  //       overall and common configuration of all charts in a central place
  //       and only have the very specific bits here.
  new Chart(canvas, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "LTC",
          data: ltcData,
          yAxisID: "y",
        },
        {
          label: "LTS",
          data: ltsData,
          yAxisID: "y1",
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          type: "time",
          time: {
            unit: "day",
          },
        },
        y: {
          type: "logarithmic",
          display: true,
          position: "left",
        },
        y1: {
          type: "linear",
          display: true,
          position: "right",
        },
      },
    },
  });
}
