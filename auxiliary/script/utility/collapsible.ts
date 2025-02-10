interface CollapsibleContainer extends HTMLElement {
  classList: DOMTokenList;
  id: string;
}

/**
 * Find and setup collapsible containers.
 *
 * All collapsible containers have a dedicated class attached to them
 * (".collapsible-container") and provide a common internal DOM structure.
 * This function attaches an event listener to the header element. It will
 * make sure to initialize the state of the container depending on its "id".
 * The state is stored in the browser's "localStorage".
 */
export function initializeCollapsibles(): void {
  // Find all collapsible containers
  const containers = document.querySelectorAll<CollapsibleContainer>(
    ".collapsible-container",
  );

  containers.forEach((c) => {
    const header = c.querySelector<HTMLElement>(".collapsible-header");
    const id = c.id;

    const cState = localStorage.getItem(`collapsible-${id}`);
    if (cState === "collapsed") {
      c.classList.add("collapsed");
    } else {
      c.classList.remove("collapsed");
    }

    if (header) {
      header.addEventListener("click", () => toggleCollapsible(c, id));
    }
  });
}

/**
 * This is the actual event handler for "click" events.
 */
function toggleCollapsible(container: CollapsibleContainer, id: string): void {
  const isCollapsed = container.classList.contains("collapsed");

  if (isCollapsed) {
    container.classList.remove("collapsed");
    localStorage.setItem(`collapsible-${id}`, "expanded");
  } else {
    container.classList.add("collapsed");
    localStorage.setItem(`collapsible-${id}`, "collapsed");
  }
}
