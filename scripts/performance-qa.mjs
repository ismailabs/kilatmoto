import lighthouse from "lighthouse";
import { launch } from "chrome-launcher";
import { writeFile, mkdir } from "node:fs/promises";
const origin = process.env.QA_ORIGIN || "http://127.0.0.1:8000";
const prefix = origin.startsWith("https:") ? "production" : "local";
await mkdir("qa-artifacts", { recursive: true });
const results = [];
for (const mode of ["mobile", "desktop"]) {
  const chrome = await launch({
    chromePath: "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    chromeFlags: ["--headless=new"],
  });
  try {
    const { lhr } = await lighthouse(origin + "/", {
      port: chrome.port,
      output: "json",
      logLevel: "error",
      onlyCategories: ["performance", "accessibility", "best-practices", "seo"],
      ...(mode === "desktop"
        ? {
            formFactor: "desktop",
            screenEmulation: {
              mobile: false,
              width: 1440,
              height: 1000,
              deviceScaleFactor: 1,
              disabled: false,
            },
            throttling: {
              rttMs: 40,
              throughputKbps: 10240,
              cpuSlowdownMultiplier: 1,
              requestLatencyMs: 0,
              downloadThroughputKbps: 0,
              uploadThroughputKbps: 0,
            },
          }
        : {}),
    });
    await writeFile(
      `qa-artifacts/lighthouse-${prefix}-${mode}.json`,
      JSON.stringify(lhr),
    );
    results.push({
      mode,
      version: lhr.lighthouseVersion,
      fetchTime: lhr.fetchTime,
      url: lhr.finalDisplayedUrl,
      categories: Object.fromEntries(
        Object.entries(lhr.categories).map(([k, v]) => [k, v.score]),
      ),
      metrics: Object.fromEntries(
        [
          "largest-contentful-paint",
          "cumulative-layout-shift",
          "total-blocking-time",
          "first-contentful-paint",
          "speed-index",
        ].map((k) => [k, lhr.audits[k].numericValue]),
      ),
      warnings: lhr.runWarnings,
      failedAudits: Object.entries(lhr.audits)
        .filter(([k, v]) => v.score !== null && v.score < 0.9)
        .map(([id, v]) => ({
          id,
          title: v.title,
          description: v.description,
          displayValue: v.displayValue,
        })),
    });
  } finally {
    await chrome.kill();
  }
}
await writeFile(
  `qa-artifacts/${prefix}-performance-summary.json`,
  JSON.stringify({ origin, results }, null, 2),
);
console.log(JSON.stringify(results));
