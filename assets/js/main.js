/* Progressive enhancements. Core content and links work without JavaScript. */
(() => {
  "use strict";
  const doc = document;
  const toggle = doc.getElementById("nav-toggle");
  const nav = doc.getElementById("primary-nav");
  if (toggle && nav) {
    const close = (restoreFocus = false) => {
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Open navigation menu");
      nav.classList.remove("open");
      if (restoreFocus) toggle.focus();
    };
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") !== "true";
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute(
        "aria-label",
        open ? "Close navigation menu" : "Open navigation menu",
      );
      nav.classList.toggle("open", open);
      if (open) nav.querySelector("a")?.focus();
    });
    nav.addEventListener("click", (event) => {
      if (event.target.closest("a")) close();
    });
    doc.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && nav.classList.contains("open")) {
        event.preventDefault();
        close(true);
      }
    });
    doc.addEventListener("click", (event) => {
      if (!event.target.closest(".site-header")) close();
    });
    doc.addEventListener("focusin", (event) => {
      if (!event.target.closest(".site-header")) close();
    });
    matchMedia("(max-width: 800px)").addEventListener("change", () => close());
    doc.documentElement.classList.add("js-nav-ready");
  }
  const filters = [...doc.querySelectorAll(".filter-btn")];
  const projects = [...doc.querySelectorAll(".project-card")];
  if (filters.length && projects.length) {
    doc.querySelector(".filter-bar").hidden = false;
    filters.forEach((button) =>
      button.addEventListener("click", () => {
        filters.forEach((filter) =>
          filter.setAttribute("aria-pressed", String(filter === button)),
        );
        let visible = 0;
        projects.forEach((card) => {
          card.hidden =
            button.dataset.filter !== "all" &&
            card.dataset.category !== button.dataset.filter;
          if (!card.hidden) visible++;
        });
        doc.getElementById("filter-count").textContent =
          `Showing ${visible} of ${projects.length} concepts`;
      }),
    );
  }
  const dialog = doc.getElementById("project-lightbox");
  if (dialog && typeof dialog.showModal === "function") {
    let opener;
    const closeButton = doc.getElementById("lightbox-close");
    doc.querySelectorAll(".open-lightbox").forEach((link) =>
      link.addEventListener("click", (event) => {
        event.preventDefault();
        opener = link;
        const image = doc.getElementById("lightbox-image");
        image.src = link.getAttribute("href");
        image.alt = link.closest(".project-media").querySelector("img").alt;
        doc.getElementById("lightbox-heading").textContent = link.dataset.title;
        dialog.showModal();
        doc.body.classList.add("modal-open");
        closeButton.focus();
      }),
    );
    closeButton.addEventListener("click", () => dialog.close());
    dialog.addEventListener("keydown", (event) => {
      // The image viewer has one interactive control. Keep Tab on that control.
      if (event.key === "Tab") {
        event.preventDefault();
        closeButton.focus();
      }
    });
    dialog.addEventListener("click", (event) => {
      const box = dialog.getBoundingClientRect();
      if (
        event.clientX < box.left ||
        event.clientX > box.right ||
        event.clientY < box.top ||
        event.clientY > box.bottom
      )
        dialog.close();
    });
    dialog.addEventListener("close", () => {
      doc.body.classList.remove("modal-open");
      if (opener?.isConnected && !opener.closest("[hidden]")) opener.focus();
    });
  }
  // No form element, endpoint, network request, analytics or persistence.
  const demoButton = doc.getElementById("demo-submit");
  if (demoButton) {
    const status = doc.getElementById("demo-status");
    const fields = ["name", "email", "vehicle", "service", "message"].map(
      (key) => doc.getElementById(`demo-${key}`),
    );
    const showStatus = (message) => {
      status.textContent = message;
      status.classList.add("has-message");
    };
    fields.forEach((field) =>
      field.addEventListener("input", () =>
        field.removeAttribute("aria-invalid"),
      ),
    );
    demoButton.addEventListener("click", () => {
      fields.forEach((field) => field.removeAttribute("aria-invalid"));
      const invalid = fields.find(
        (field) => !field.checkValidity() || !field.value.trim(),
      );
      if (invalid) {
        invalid.setAttribute("aria-invalid", "true");
        const name = doc
          .querySelector(`label[for="${invalid.id}"]`)
          .textContent.replace("*", "")
          .trim();
        showStatus(
          `Please enter a valid ${name.toLowerCase()}. Nothing has been sent.`,
        );
        invalid.focus();
        return;
      }
      showStatus(
        "This is a fictional portfolio demo. No enquiry has been submitted, sent or saved.",
      );
      status.focus({ preventScroll: true });
    });
    const selected = new URLSearchParams(location.search).get("service");
    const select = doc.getElementById("demo-service");
    if ([...select.options].some((option) => option.value === selected))
      select.value = selected;
    demoButton.hidden = false;
  }
})();
