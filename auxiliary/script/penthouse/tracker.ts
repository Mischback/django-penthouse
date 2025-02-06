// FIXME: Convert to direct imports for treeshaking
import Chart from "chart.js/auto";
import "chartjs-adapter-date-fns";

import { getDomElement, findNonZeroMin } from "../utility";
// import { createLineChart } from "../utility/charts";

/**
 * Create the visual representation of the run data.
 *
 * This function is closely tied to the app's view and template.
 */
export function createRunTrackerChart(): void {
  const table = <HTMLTableElement>getDomElement(null, "#tracker-data-table");
  const canvas = <HTMLCanvasElement>getDomElement(null, "#tracker-canvas");

  // grab raw data from the table
  let tableRow;
  const labels = [];
  const coinsRun = [];
  const coinsHour = [];
  const coinsRun5 = [];
  const coinsHour5 = [];

  for (let i = 1; i < table.rows.length; i++) {
    tableRow = table.rows[i];

    // the label is determined by the datapoints ``date``
    // @ts-expect-error TS2345: Will work or caught by ``getDomElement()``
    const thisLabel = getDomElement(tableRow, ".tracker-date-raw").innerHTML;
    const timestamp = parseInt(thisLabel, 10) * 1000;

    // we want coins/run
    const thisCoins = parseInt(
      getDomElement(
        // @ts-expect-error TS2345: Will work or caught by ``getDomElement()``
        tableRow,
        ".tracker-coins-run-raw",
      ).innerHTML,
      10,
    );

    // we want coins/h
    const thisCoinsH = parseInt(
      getDomElement(
        // @ts-expect-error TS2345: Will work or caught by ``getDomElement()``
        tableRow,
        ".tracker-coins-hour-raw",
      ).innerHTML,
      10,
    );

    // we want coins/run (Avg5)
    const thisCoins5 = parseInt(
      getDomElement(
        // @ts-expect-error TS2345: Will work or caught by ``getDomElement()``
        tableRow,
        ".tracker-coins-run-five-raw",
      ).innerHTML,
      10,
    );

    // we want coins/h (Avg5)
    const thisCoinsH5 = parseInt(
      getDomElement(
        // @ts-expect-error TS2345: Will work or caught by ``getDomElement()``
        tableRow,
        ".tracker-coins-hour-five-raw",
      ).innerHTML,
      10,
    );

    labels.push(timestamp);
    coinsRun.push(thisCoins);
    coinsHour.push(thisCoinsH);
    coinsRun5.push(thisCoins5);
    coinsHour5.push(thisCoinsH5);
  }

  // console.log(labels);
  // console.log(coinsRun);
  // console.log(coinsHour);
  // console.log(coinsRun5);
  // console.log(coinsHour5);

  // const minCoinsRun = Math.min(...coinsRun) * 0.9;
  // const maxCoinsRun = Math.max(...coinsRun) * 1.1;
  const minCoinsHour = findNonZeroMin(coinsHour);
  const maxCoinsHour = Math.max(...coinsHour);

  // console.log(minCoinsRun);
  // console.log(maxCoinsRun);
  // console.log(minCoinsHour);
  // console.log(maxCoinsHour);

  new Chart(canvas, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Coins/run",
          data: coinsRun,
          yAxisID: "y",
        },
        /* {
          label: "Coins/h",
          data: coinsHour,
          yAxisID: "y1",
        }, */
        {
          label: "Coins/run (Avg 5)",
          data: coinsRun5,
          yAxisID: "y",
          type: "line",
        },
        {
          label: "Coins/h (Avg 5)",
          data: coinsHour5,
          yAxisID: "y1",
          type: "line",
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          type: "linear",
          display: true,
          position: "left",
          // min: minCoinsRun,
          // max: maxCoinsRun,
        },
        y1: {
          type: "linear",
          display: true,
          position: "right",
          min: minCoinsHour,
          max: maxCoinsHour,
        },
      },
    },
  });
}

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
    // @ts-expect-error TS2345: Will work or caught by ``getDomElement()``
    const thisLabel = getDomElement(tableRow, ".meta-date-raw").innerHTML;
    const timestamp = parseInt(thisLabel, 10) * 1000;

    // we want LTC/LTS as datapoints
    // @ts-expect-error TS2345: Will work or caught by ``getDomElement()``
    const thisLtc = getDomElement(tableRow, ".meta-ltc-raw").innerHTML;
    // @ts-expect-error TS2345: Will work or caught by ``getDomElement()``
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
