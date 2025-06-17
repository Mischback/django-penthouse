// SPDX-FileCopyrightText: 2025 Mischback
// SPDX-License-Identifier: MIT
// SPDX-FileType: SOURCE

/**
 * Type definition for CollapsibleContainer
 *
 * In the HTML templates, the containers are actually ``<div>`` elements. To
 * make this module work, they should have a CSS ``classList`` and the element's
 * ``id`` attribute should be set.
 */
export interface CollapsibleContainer extends HTMLElement {
  id: string;
  classList: DOMTokenList;
}

const CSTATE_COLLAPSED = "col";
const CSTATE_EXPANDED = "exp";
const COLLAPSED_CSS_CLASS = "collapsed";

/**
 * Provide the actual key to access the localStorage.
 *
 * JavaScript/TypeScript is missing the equivalent of (e.g.) Python's
 * ``format()`` method for strings. The desired effect is, that the key to
 * access the localStorage is uniform and more error-proof.
 */
function collapsibleStorageKey(id: string): string {
  return `collapsible-${id}`;
}

/**
 * Setup the collapsible container.
 *
 * This function takes care of two things:
 * a) get the status of the specific container from the localStorage and
 *    restore the last state
 * b) add the click-handler to the container's header (which is just another
 *    ``<div>`` within the container
 */
export function initializeCollapsible(container: CollapsibleContainer): void {
  const header = container.querySelector<HTMLElement>(".collapsible-header");
  const id = container.id;

  const cState = localStorage.getItem(collapsibleStorageKey(id));
  if (cState === CSTATE_COLLAPSED) {
    container.classList.add(COLLAPSED_CSS_CLASS);
  } else {
    container.classList.remove(COLLAPSED_CSS_CLASS);
  }

  if (header) {
    header.addEventListener("click", () => toggleCollapsible(container, id));
  }
}

/**
 * Toggle the state of the collapsible container.
 *
 * This is the actual click-handler. It determines the current state *by
 * evaluating the CSS ``classList`` and then toggles this state between
 * *collapsed* and *expanded*. The new state is made persistant in the
 * localStorage.
 */
function toggleCollapsible(container: CollapsibleContainer, id: string): void {
  const isCollapsed = container.classList.contains(COLLAPSED_CSS_CLASS);

  if (isCollapsed) {
    container.classList.remove(COLLAPSED_CSS_CLASS);
    localStorage.setItem(collapsibleStorageKey(id), CSTATE_EXPANDED);
  } else {
    container.classList.add(COLLAPSED_CSS_CLASS);
    localStorage.setItem(collapsibleStorageKey(id), CSTATE_COLLAPSED);
  }
}

/**
 * Create a new collapsible container from template.
 *
 * The template can be found in ``penthouse/templates/penthouse/app_base.html``.
 */
export function createCollapsibleContainer(
  newID: string,
  newCaption: string,
  insertBeforeElem: HTMLElement | null,
): HTMLElement | null {
  if (insertBeforeElem === null || insertBeforeElem.parentElement === null) {
    console.error("Could not find element to insert before!");
    return null;
  }

  const template: HTMLTemplateElement | null = document.querySelector(
    "#tpl-collapsible-container",
  );
  if (template === null) {
    console.error("Could not find template!");
    return null;
  }

  const docFragment = document.importNode(template.content, true);

  const newCollapsible: HTMLElement = docFragment.querySelector("section")!;
  newCollapsible.id = newID;

  const caption: HTMLElement = newCollapsible.querySelector(
    ".collapsible-header h3",
  )!;
  caption.innerHTML = newCaption;

  insertBeforeElem.parentElement.insertBefore(newCollapsible, insertBeforeElem);

  return newCollapsible;
}
