// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

import uPlot from "uplot";
import { createCollapsibleContainer } from "../utility/collapsible";
import {
  convertNumberForDisplay,
  parseNumberOrNull,
  parseNumberOrZero,
} from "../utility";

type uPlotDate = number;
type uPlotData = number | null;

const LTC_CHANGE_HEADER_OFFSET = 2;
const LTC_CHANGE_DATA_OFFSET = 3;

function replaceOutliersByNull(data: uPlotData[]): uPlotData[] {
  const dataSum = data.reduce((acc, cur) => {
    if (cur === null) {
      return acc;
    } else {
      //@ts-expect-error TS18047
      return acc + cur;
    }
  }, 0);

  // @ts-expect-error TS18047 This will never be ``null``
  const dataMean = dataSum / data.length;

  const dataStdDev = Math.sqrt(
    // @ts-expect-error TS2531 This object should not be ``null``
    data
      .map((x) => {
        if (x === null) {
          return x;
        } else {
          return Math.pow(x - dataMean, 2);
        }
      })
      .reduce((acc, cur) => {
        if (cur === null) {
          return acc;
        } else {
          //@ts-expect-error TS18047
          return acc + cur;
        }
      }, 0) /
      (data.length - 1),
  );

  const upper = dataMean + dataStdDev;
  const lower = dataMean - dataStdDev;

  const result: uPlotData[] = [];
  data.forEach((cur) => {
    if (cur === null) {
      result.push(null);
    }

    //@ts-expect-error TS18047
    if (cur >= lower && cur <= upper) {
      result.push(cur);
    } else {
      result.push(null);
    }
  });

  console.log(result);
  return result;
}

export function addRelativeChange(): void {
  const sampleContainer = document.querySelector(
    "#progression-overview-samples",
  );
  if (sampleContainer === null) {
    console.error("Could not find sample container!");
    return;
  }

  const dataRows = sampleContainer.querySelectorAll(".data-list tr");

  let lastDateTimestamp = 0;
  let lastLTC = 0;
  let thisDateTimestamp = 0;
  let thisDateDiffDays = 0;
  let thisLTC = 0;
  let thisLTCDiffTotal = 0;
  // let thisLTCDiffPerDay = 0;
  let thisLTCDiffRelativeChange = 0;
  let thisLTCDiffRelativeChangePerDay = 0;
  let tmpCell;
  dataRows.forEach((row, index) => {
    if (index === 0) {
      console.debug("Assuming this is the header row!");
      tmpCell = (row as HTMLTableRowElement).insertCell(
        LTC_CHANGE_HEADER_OFFSET,
      );
      tmpCell.textContent = "LTC change per day";
    }

    if (index > 0) {
      thisDateTimestamp = parseNumberOrZero(
        row.querySelector(".ph-progression-date")?.textContent,
      );
      // The input from the backend is just a default UNIX timestamp, specified
      // in seconds, not in microseconds, which is the default in JS.
      thisDateDiffDays = Math.ceil(
        (thisDateTimestamp - lastDateTimestamp) / (24 * 60 * 60),
      );

      thisLTC = parseNumberOrZero(
        row.querySelector(".ph-progression-ltc")?.textContent,
      );
      thisLTCDiffTotal = thisLTC - lastLTC;

      // FIXME: Currently not displayed and not in use!
      // if (thisDateDiffDays === 0) {
      //   thisLTCDiffPerDay = 0;
      // } else {
      //   thisLTCDiffPerDay = thisLTCDiffTotal / thisDateDiffDays;
      // }

      if (lastLTC === 0) {
        thisLTCDiffRelativeChange = 100;
      } else {
        thisLTCDiffRelativeChange = (thisLTCDiffTotal / lastLTC) * 100;
      }

      if (thisDateDiffDays === 0) {
        thisLTCDiffRelativeChangePerDay = 0;
      } else {
        thisLTCDiffRelativeChangePerDay =
          thisLTCDiffRelativeChange / thisDateDiffDays;
      }

      // Actually provide additional fields
      tmpCell = (row as HTMLTableRowElement).insertCell(LTC_CHANGE_DATA_OFFSET);
      tmpCell.classList.add("ph-progression-ltc-change", "number-value");
      tmpCell.textContent = (
        Math.round((thisLTCDiffRelativeChangePerDay + Number.EPSILON) * 100) /
        100
      ).toString();

      // save the current values for the next iteration
      lastDateTimestamp = thisDateTimestamp;
      lastLTC = thisLTC;
    }
  });
}

export function createProgressionChart(): void {
  const sampleContainer = document.querySelector(
    "#progression-overview-samples",
  );
  if (sampleContainer === null) {
    console.error("Could not find sample container!");
    return;
  }

  // Providing initial values for colors
  let settingsGridColor = "#000";
  let settingsAxeCaptionColor = "#000";
  let settingsDataset01Color = "#c00";
  let settingsDataset01Secondary = "#600";
  let settingsDataset02Color = "#0c0";

  // Create the actual collapsible container for the chart
  const chartContainer = createCollapsibleContainer(
    "progression-overview-chart",
    "Chart",
    sampleContainer as HTMLElement,
  );
  if (chartContainer === null) {
    console.error("Could not create chart container!");
    return;
  } else {
    // add another class to this container
    chartContainer.classList.add("ph-chart-container");

    // get color values
    settingsGridColor = getComputedStyle(chartContainer)
      .getPropertyValue("--grid-color")
      .trim();
    settingsAxeCaptionColor = getComputedStyle(chartContainer)
      .getPropertyValue("--axe-caption-color")
      .trim();
    settingsDataset01Color = getComputedStyle(chartContainer)
      .getPropertyValue("--dataset01-main")
      .trim();
    settingsDataset01Secondary = getComputedStyle(chartContainer)
      .getPropertyValue("--dataset01-secondary")
      .trim();
    settingsDataset02Color = getComputedStyle(chartContainer)
      .getPropertyValue("--dataset02-main")
      .trim();
  }

  // ``querySelectorAll()`` will return the elements in the order of the DOM,
  // so this should be pretty easy.
  //
  // This relies on the default ordering of the table, when it is initially
  // rendered, adjust the Django codebase accordingly if required.
  //
  // All other JS/TS shenanigans *must be applied later*.
  const date_cells = sampleContainer.querySelectorAll(
    ".data-list .ph-progression-date",
  );
  const ltc_cells = sampleContainer.querySelectorAll(
    ".data-list .ph-progression-ltc",
  );
  const ltc_change_cells = sampleContainer.querySelectorAll(
    ".data-list .ph-progression-ltc-change",
  );
  const lts_cells = sampleContainer.querySelectorAll(
    ".data-list .ph-progression-lts",
  );
  if (
    date_cells.length != ltc_cells.length ||
    date_cells.length != lts_cells.length ||
    date_cells.length != ltc_change_cells.length
  ) {
    console.error("Error while fetching sample data! Lengths do not match!");
    return;
  }

  const date_list: uPlotDate[] = [];
  const ltc_list: uPlotData[] = [];
  const ltc_change_list: uPlotData[] = [];
  const lts_list: uPlotData[] = [];

  date_cells.forEach((cell, index) => {
    // This is really defensive programming.
    //
    // The uPlotDate[] may only contain numbers, while the uPlotData[] *may*
    // use ``null`` values as padding.
    /*const this_date = parseNumber(cell.textContent);*/
    /*if (this_date === undefined) {*/
    /*date_list.push(0);*/
    /*} else {*/
    /*date_list.push(this_date);*/
    /*}*/
    date_list.push(parseNumberOrZero(cell.textContent));
    ltc_list.push(parseNumberOrNull(ltc_cells[index]!.textContent));
    ltc_change_list.push(
      parseNumberOrZero(ltc_change_cells[index]!.textContent),
    );
    lts_list.push(parseNumberOrNull(lts_cells[index]!.textContent));
  });

  const ltcChangeListNormalized = replaceOutliersByNull(ltc_change_list);

  const progressionChart = new uPlot(
    {
      // id: "progressionChart",
      class: "ph-chart",
      width:
        (
          document.querySelector(
            "#progression-overview-chart .collapsible-content",
          ) as HTMLElement
        ).offsetWidth - 50,
      height: 300,
      series: [
        {},
        {
          label: "LTC",
          stroke: settingsDataset01Color, // --dataset01-main
          scale: "coins",
          width: 2,
          points: {
            stroke: settingsDataset01Color,
            fill: settingsGridColor,
          },
          value: (_, raw) => {
            return convertNumberForDisplay(raw);
          },
        },
        {
          label: "LTS",
          stroke: settingsDataset02Color, // --dataset02-main
          scale: "stones",
          width: 2,
          points: {
            stroke: settingsDataset02Color,
            fill: settingsGridColor,
          },
        },
        {
          label: "LTC change",
          stroke: settingsDataset01Secondary, // --dataset01-secondary
          scale: "coins_change",
          width: 2,
          points: {
            stroke: settingsDataset01Secondary,
            fill: settingsGridColor,
          },
        },
      ],
      axes: [
        {
          stroke: settingsAxeCaptionColor, // --axe-caption-color
        },
        {
          scale: "coins",
          stroke: settingsAxeCaptionColor, // --axe-caption-color
          grid: {
            width: 1,
            stroke: settingsGridColor, // --grid-color
          },
          side: 1,
        },
        {
          show: false,
          scale: "stones",
          stroke: settingsAxeCaptionColor, // --axe-caption-color
          grid: {
            show: false,
          },
          side: 1,
        },
        {
          scale: "coins_change",
          stroke: settingsAxeCaptionColor, // --axe-caption-color
          grid: {
            show: false,
          },
          side: 3,
        },
      ],
      scales: {
        coins: {
          distr: 3,
        },
        stones: {
          distr: 3,
        },
        coins_change: {
          distr: 1,
        },
      },
      cursor: {
        points: {
          // use the points stroke color on hover
          fill: (u, sidx) => {
            // eslint-disable-next-line @typescript-eslint/no-unsafe-return
            return u?.series[sidx]?.stroke?.();
          },
        },
      },
    },
    [
      date_list, // x-values (timestamps)
      ltc_list, // y-values
      lts_list, // y-values
      ltcChangeListNormalized, // y-values
    ],
    chartContainer.querySelector(".collapsible-content") as HTMLElement,
  );

  // cover the ESLint error
  //
  // TODO: It might be desirable to return the actual chart for future
  //       modifications, like adjusting the data.
  console.debug(progressionChart);
}
