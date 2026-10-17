# Codex technical implementation playbook

## First inspect
- Current local clone of `ismailabs/rapi-motion`; check `git status`, actual branch, HEAD, remotes, untracked/secret files, changed files, current deployment integration and references.
- Existing source is static multi-page HTML/CSS/vanilla JS with Python utilities; **prefer preserving this architecture** over adding React, Next.js, paid CMS or dependencies unless an evidence-based reason and comparable testing justify the change.
- Read every source route (`index.html`, `about`, `services`, `projects`, `contact`), `assets/css/styles.css`, `assets/js/main.js`, `scripts/verify_static.py`, `scripts/configure_seo.py`, `_headers`, `robots.txt`, `sitemap.xml`, and source QA history.

## Author actual website code, not mockup images
- Apply correct display brand and assets throughout nav, footer, title, OG, alt text, social share, manifest, QR if any, copy, SVGs and CSS selectors.
- Implement five responsive page layouts based on accurate mockups, while accommodating real source content lengths.
- Use local asset variants; maintain WebP responsive `srcset`, widths/heights and lazy-loading except critical hero.
- Use true semantic headings, anchors, buttons, dialog; keyboard and touch tests. Keep form local-only and demonstrate zero actual submission.
- If any code mechanism relies on regex string matching of RAPI MOTION, update carefully; don't broad search/replace unrelated factual source, provenance or historical archive.
- Ensure no external runtime fonts, analytics, payment processor, calls to fictitious APIs or storage introduced.

## Source-driven content contract
- `data/six-service-contract.json` protects the six names and ID mapping. Compare real source titles, IDs and labels on every page before modifying.
- `data/six-project-contract.json` holds source-observed concept titles for verification; actual cards may have related shorter title variants. Treat source HTML as authoritative where this static extraction is incomplete.
- Preserve all six cards / images / accessible interactions and service selection mappings, not just counts.

## Practical test setup
Current source README provides:
```
py scripts/serve.py
py scripts/verify_static.py
py scripts/verify_static.py --base-url http://127.0.0.1:8000
node --check assets/js/main.js
```
`py scripts/configure_seo.py --mode staging --check` verifies staging; before production, audit script options and run production mode with `--origin https://kilatmoto.ismailstudio.my` only once new hostname and release readiness are confirmed. The script may need adaptation if Worker headers/routing differ from historic Pages assumptions. Do not run direct `file://` preview as proof of the live site.

## QA evidence
- Browser screenshots for all five pages at narrow and desktop widths, with explicit reference comparison notes.
- Automated structural + HTTP route assertions, keyboard filters/dialog/menu, demo validation and real no-submit evidence.
- Accessibility WCAG 2.2 AA **goal**, axe plus manual keyboard and contrast checks; do not call automated zero violations certification.
- Lighthouse performance/local mobile lab metrics if feasible, plus hosted check; record versions and variability, not invented 100s.

## Change control
Use feature branch while developing if practical, run tests, review diff, protect existing data/history, merge/push to `main` only when ready and authorized. No force push, dropping commits, secret printing or unrelated repository edits. Follow any deployment pipeline triggers carefully to avoid premature production publication.
