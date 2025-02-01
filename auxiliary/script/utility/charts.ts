// FIXME: Convert to direct imports for treeshaking
import Chart from "chart.js/auto";

import { getDomElement } from "../utility";

export function createLineChart(
  canvasId: string,
  labelList: string[],
  dataList: number[],
): void {
  /* grab the required elements from the DOM */
  const canvas = getDomElement(null, canvasId);

  return new Chart(canvas, {
    type: "line",
    data: {
      labels: labelList,
      datasets: [
        {
          label: "foo",
          data: dataList,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  });
}
