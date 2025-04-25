// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

import uPlot from "uplot";
import { createCollapsibleContainer } from "../utility/collapsible";

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
}
