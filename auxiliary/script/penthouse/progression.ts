// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

import uPlot from "uplot";
import { createCollapsibleContainer } from "../utility/collapsible";
import { parseNumberOrNull } from "../utility";

type uPlotData = number | null;

export function createProgressionChart(): void {
  const sampleContainer = document.querySelector(
    "#progression-overview-samples",
  );
  if (sampleContainer === null) {
    console.error("Could not find sample container!");
    return;
  }

  const chartContainer = createCollapsibleContainer(
    "progression-overview-chart",
    "Chart",
    sampleContainer as HTMLElement,
  );
  if (chartContainer === null) {
    console.error("Could not create chart container!");
    return;
  }

  // BEGIN EXPERIMENTAL uPlot
  /* eslint-disable @typescript-eslint/no-unsafe-call */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-unused-vars */
  const opts = {
    id: "chart1",
    class: "ph-chart",
    width:
      document.querySelector("#progression-overview-chart .collapsible-content")
        .offsetWidth - 50,
    height: 300,
    series: [
      {},
      {
        // initial toggled state (optional)
        show: true,

        spanGaps: false,

        // in-legend display
        label: "RAM",
        value: (self, rawValue) =>
          rawValue == null ? "" : "$" + rawValue.toFixed(2),

        // series style
        stroke: "red",
        width: 1,
        fill: "rgba(255, 0, 0, 0.3)",
        dash: [10, 5],
      },
    ],
  };

  const data = [
    [1546300800, 1546387200], // x-values (timestamps)
    [35, 71], // y-values (series 1)
    [90, 15], // y-values (series 2)
  ];

  const uplot = new uPlot(
    opts,
    data,
    chartContainer.querySelector(".collapsible-content"),
  );
  /* eslint-enable @typescript-eslint/no-unsafe-call */
  /* eslint-enable @typescript-eslint/no-unsafe-member-access */
  /* eslint-enable @typescript-eslint/no-unused-vars */
  // END EXPERIMENTAL uPlot

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

  const date_list: uPlotData[] = [];
  const ltc_list: uPlotData[] = [];
  const lts_list: uPlotData[] = [];

  date_cells.forEach((cell, index) => {
    date_list.push(parseNumberOrNull(cell.innerHTML));
    ltc_list.push(parseNumberOrNull(ltc_cells[index]!.innerHTML));
    lts_list.push(parseNumberOrNull(lts_cells[index]!.innerHTML));
  });

  console.log(date_cells);
  console.log(ltc_cells);
  console.log(lts_cells);

  console.log(date_list);
  console.log(ltc_list);
  console.log(lts_list);
}
