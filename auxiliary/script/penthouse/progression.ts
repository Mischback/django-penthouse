// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

import uPlot from "uplot";
import { createCollapsibleContainer } from "../utility/collapsible";
import { parseNumber, parseNumberOrNull } from "../utility";

type uPlotDate = number;
type uPlotData = number | null;

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
  const lts_cells = sampleContainer.querySelectorAll(
    ".data-list .ph-progression-lts",
  );
  if (
    date_cells.length != ltc_cells.length ||
    date_cells.length != lts_cells.length
  ) {
    console.error("Error while fetching sample data! Lengths do not match!");
    return;
  }

  const date_list: uPlotDate[] = [];
  const ltc_list: uPlotData[] = [];
  const lts_list: uPlotData[] = [];

  date_cells.forEach((cell, index) => {
    // This is really defensive programming.
    //
    // The uPlotDate[] may only contain numbers, while the uPlotData[] *may*
    // use ``null`` values as padding.
    const this_date = parseNumber(cell.innerHTML);
    if (this_date === undefined) {
      date_list.push(0);
    } else {
      date_list.push(this_date);
    }
    ltc_list.push(parseNumberOrNull(ltc_cells[index]!.innerHTML));
    lts_list.push(parseNumberOrNull(lts_cells[index]!.innerHTML));
  });

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
        },
        {
          scale: "stones",
          stroke: settingsAxeCaptionColor, // --axe-caption-color
          side: 1,
        },
      ],
      scales: {
        coins: {
          distr: 3,
        },
        stones: {
          distr: 3,
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
    ],
    chartContainer.querySelector(".collapsible-content") as HTMLElement,
  );

  // cover the ESLint error
  //
  // TODO: It might be desirable to return the actual chart for future
  //       modifications, like adjusting the data.
  console.debug(progressionChart);
}
