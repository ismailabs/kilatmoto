const { chromium, expect } = require("@playwright/test");
const { default: AxeBuilder } = require("@axe-core/playwright");
const fs = require("node:fs");
const base = process.env.QA_ORIGIN || "http://127.0.0.1:8000";
const prefix = base.startsWith("https:") ? "production" : "local";
const out = "qa-artifacts";
fs.mkdirSync(out, { recursive: true });
const routes = ["", "about", "services", "projects", "contact"];
const report = {
  origin: base,
  time: new Date().toISOString(),
  browser: "Microsoft Edge / Chromium",
  responsive: [],
  axe: [],
  checks: [],
  errors: [],
};
const check = (name, ok) => {
  report.checks.push({ name, pass: !!ok });
  if (!ok) throw Error(name);
};
async function load(p, url) {
  const r = await p.goto(base + url);
  check("HTTP 200 " + url, r.status() === 200);
  await p.evaluate(() => document.fonts.ready);
}
async function reveal(p) {
  await p.locator("img").evaluateAll(async (imgs) => {
    for (const img of imgs) {
      img.loading = "eager";
      if (img.src) await img.decode().catch(() => {});
    }
  });
}
(async () => {
  const browser = await chromium.launch({ channel: "msedge", headless: true });
  try {
    const context = await browser.newContext();
    const p = await context.newPage();
    p.on("pageerror", (e) => report.errors.push(e.message));
    p.on("console", (m) => {
      if (m.type() === "error") report.errors.push(m.text());
    });
    p.on("response", (r) => {
      if (r.status() >= 400) report.errors.push(`${r.status()} ${r.url()}`);
    });
    for (const width of [320, 375, 390, 430, 768, 1024, 1440, 1920]) {
      await p.setViewportSize({ width, height: width < 700 ? 844 : 1000 });
      for (const route of routes) {
        await load(p, "/" + (route ? route + "/" : ""));
        await reveal(p);
        const dims = await p.evaluate(() => ({
          client: document.documentElement.clientWidth,
          scroll: document.documentElement.scrollWidth,
        }));
        report.responsive.push({ route: "/" + route, width, ...dims });
        check(
          "No overflow " + route + " " + width,
          dims.scroll <= dims.client + 1,
        );
        check("One H1 " + route, (await p.locator("h1").count()) === 1);
        if ([390, 1440].includes(width)) {
          const originalViewport = p.viewportSize();
          // Expand only capture height so native content-visibility sections are painted.
          // Responsive and axe checks retain the original viewport below.
          const estimatedHeight = await p.evaluate(() => Math.ceil(document.body.getBoundingClientRect().height));
          await p.setViewportSize({width, height: estimatedHeight + 2000});
          await p.evaluate(() => new Promise(requestAnimationFrame));
          const paintedHeight = await p.evaluate(() => Math.ceil(document.body.getBoundingClientRect().height));
          await p.setViewportSize({width, height: paintedHeight});
          await p.evaluate(() => new Promise(requestAnimationFrame));
          await p.screenshot({
            path: `${out}/${prefix}-${route || "home"}-${width}.png`,
            fullPage: true,
          });
          await p.setViewportSize(originalViewport);
          const a = await new AxeBuilder({ page: p })
            .withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"])
            .analyze();
          report.axe.push({
            route,
            width,
            violations: a.violations.map((v) => ({
              id: v.id,
              impact: v.impact,
              nodes: v.nodes.map((n) => ({
                target: n.target,
                summary: n.failureSummary,
              })),
            })),
          });
        }
      }
    }
    await p.setViewportSize({ width: 390, height: 844 });
    await load(p, "/");
    const toggle = p.locator("#nav-toggle");
    await expect(toggle).toHaveAccessibleName("Open navigation menu");
    await toggle.focus();
    await p.keyboard.press("Enter");
    await expect(toggle).toHaveAttribute("aria-expanded", "true");
    await expect(p.locator('#primary-nav a[href="/"]')).toBeFocused();
    await p.keyboard.press("Escape");
    await expect(toggle).toBeFocused();
    await expect(toggle).toHaveAttribute("aria-expanded", "false");
    check("Keyboard menu open Escape focus restoration", true);
    await toggle.click();
    await p.locator('#primary-nav a[href="/services/"]').click();
    await expect(p).toHaveURL(base + "/services/");
    check("Mobile menu navigation", true);
    await p.setViewportSize({ width: 1440, height: 1000 });
    for (const route of routes) {
      await p
        .locator(`#primary-nav a[href="/${route ? route + "/" : ""}"]`)
        .click();
      await expect(p).toHaveURL(base + "/" + (route ? route + "/" : ""));
    }
    check("All desktop navigation links", true);
    await load(p, "/");
    await p.locator('.concept-strip a').click();
    await expect(p.locator('#creator h2')).toBeInViewport();
    check("Creator disclosure anchor lands in viewport", true);
    await load(p, "/projects/");
    for (const [filter, count] of [
      ["exterior", 1],
      ["interior", 1],
      ["refinement", 2],
      ["protection", 1],
      ["maintenance", 1],
      ["all", 6],
    ]) {
      const b = p.locator(`[data-filter="${filter}"]`);
      await b.focus();
      await p.keyboard.press("Enter");
      await expect(p.locator(".project-card:visible")).toHaveCount(count);
      await expect(p.locator("#filter-count")).toHaveText(
        `Showing ${count} of 6 concepts`,
      );
      check("Keyboard filter " + filter, true);
    }
    const opener = p.getByRole("link", {
      name: "Enlarge Urban Hatchback concept image",
    });
    await opener.focus();
    await p.keyboard.press("Enter");
    await expect(p.getByRole("dialog")).toBeVisible();
    const close = p.getByRole("button", { name: "Close image viewer" });
    await expect(close).toBeFocused();
    await p.keyboard.press("Tab");
    await expect(close).toBeFocused();
    await p.keyboard.press("Shift+Tab");
    await expect(close).toBeFocused();
    await p.keyboard.press("Escape");
    await expect(opener).toBeFocused();
    check("Gallery open Tab Shift+Tab Escape focus restoration", true);
    for (const id of [
      "exterior",
      "interior",
      "paint",
      "ceramic",
      "wheels",
      "maintenance",
    ]) {
      await load(p, "/contact/?service=" + id);
      await expect(p.locator("#demo-service")).toHaveValue(id);
    }
    check("All six query-string service mappings", true);
    await reveal(p);
    const requests = [];
    p.on("request", (r) =>
      requests.push({
        url: r.url(),
        method: r.method(),
        type: r.resourceType(),
      }),
    );
    await p.locator("#demo-submit").click();
    await expect(p.locator("#demo-name")).toBeFocused();
    await p.locator("#demo-name").fill("Sample Person");
    await p.locator("#demo-email").fill("invalid");
    await p.locator("#demo-submit").click();
    await expect(p.locator("#demo-email")).toBeFocused();
    await p.locator("#demo-email").fill("sample@example.com");
    await p.locator("#demo-vehicle").selectOption({ label: "Sedan" });
    await p
      .locator("#demo-message")
      .fill("Fictional sample enquiry for local validation.");
    await p.locator("#demo-submit").click();
    await expect(p.locator("#demo-status")).toContainText(
      "No enquiry was sent, submitted, booked or saved.",
    );
    await expect(p.locator("#demo-status")).toBeFocused();
    check("Empty invalid and valid demo validation", true);
    check(
      "Zero network requests during demo interaction",
      requests.length === 0,
    );
    check(
      "Zero storage/cookies after demo",
      await p.evaluate(
        () =>
          localStorage.length === 0 &&
          sessionStorage.length === 0 &&
          document.cookie === "",
      ),
    );
    // Snapshot only the demo window; later route-navigation requests are unrelated.
    report.demoRequests = requests.slice();
    const summary = p.getByText(
      "Does the enquiry demo send or save anything?",
      { exact: true },
    );
    await summary.focus();
    await p.keyboard.press("Enter");
    check(
      "Native FAQ keyboard expansion",
      await summary.evaluate((el) => el.parentElement.open),
    );
    for (const width of [640, 960]) {
      await p.setViewportSize({ width, height: 900 });
      for (const r of routes) {
        await load(p, "/" + (r ? r + "/" : ""));
        await p.evaluate(() => {
          document.documentElement.style.zoom = "2";
        });
        const ok = await p.evaluate(
          () =>
            document.documentElement.scrollWidth <=
            document.documentElement.clientWidth + 1,
        );
        check("200 percent zoom reflow " + r + " " + width, ok);
        await p.evaluate(() => (document.documentElement.style.zoom = ""));
      }
    }
    await p.emulateMedia({ reducedMotion: "reduce" });
    await load(p, "/");
    check(
      "Reduced motion disables smooth scrolling",
      await p.evaluate(
        () =>
          getComputedStyle(document.documentElement).scrollBehavior === "auto",
      ),
    );
    const nojs = await browser.newContext({
      javaScriptEnabled: false,
      viewport: { width: 390, height: 844 },
    });
    const n = await nojs.newPage();
    for (const r of routes) {
      await load(n, "/" + (r ? r + "/" : ""));
      await expect(
        n.locator('#primary-nav a[href="/services/"]'),
      ).toBeVisible();
      if (r === "projects") {
        await expect(n.locator(".project-card:visible")).toHaveCount(6);
        await expect(n.locator(".filter-bar")).toBeHidden();
        await expect(
          n.getByRole("link", {
            name: "Enlarge Urban Hatchback concept image",
          }),
        ).toHaveAttribute("href", "/assets/images/project-urban.webp");
      }
      if (r === "contact") await expect(n.locator("#demo-submit")).toBeHidden();
    }
    check(
      "No-JS five routes navigation all projects original links demo fallback",
      true,
    );
    await nojs.close();
    check("No browser JS console or HTTP errors", report.errors.length === 0);
    check(
      "Zero axe violations across 10 page/viewport audits",
      report.axe.every((a) => a.violations.length === 0),
    );
  } finally {
    await browser.close();
    fs.writeFileSync(
      `${out}/${prefix}-browser-evidence.json`,
      JSON.stringify(report, null, 2),
    );
    console.log(
      JSON.stringify({
        responsive: report.responsive.length,
        axe: report.axe.map((a) => ({
          route: a.route,
          width: a.width,
          violations: a.violations.length,
        })),
        checks: report.checks.length,
        errors: report.errors,
      }),
    );
  }
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
