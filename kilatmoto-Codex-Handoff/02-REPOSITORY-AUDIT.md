# GitHub source audit — factual baseline, 17 October 2026

**Source:** connected GitHub repo `ismailabs/rapi-motion`, default branch `main`, public. Inspected root listing and the README, deployment, QA, asset manifest, home, services, projects and current SEO markers. This is **source inspection**, not an independent local browser run or exhaustive line-by-line code audit.

## Actual structure (source)
- Five static HTML pages: `/`, `/about/`, `/services/`, `/projects/`, `/contact/`.
- Site-level `assets/css/styles.css`, `assets/js/main.js`, `assets/images`, `assets/icons`, `assets/fonts`, `favicon.svg`, `og-image.webp`.
- `scripts/serve.py`, `scripts/verify_static.py`, `scripts/configure_seo.py`; `preview.cmd`; `_headers`, `robots.txt`, `sitemap.xml`.
- No source repository package manager, build system, CMS, API, real bookings or outgoing enquiry flow needed for regular browsing.
- The README documents **six services** and **six fictional projects**; `services/index.html` confirms names: Signature Exterior Detail; Interior Reset; Paint Correction; Ceramic Protection; Wheel & Glass Care; Maintenance Detail.
- Projects headings: “The city reset.”, “The executive edit.”, “Room for real life.”, “The weekend ritual.”, “The everyday rhythm.”, “The quiet arrival.” Verify exact card titles/IDs against current source before editing.
- Existing contact enquiry is **local-only validation**, not a submitted email: no real external form endpoint or storage. Protect that truthfully disclosed safety boundary.
- Existing gallery/filter mobile nav and disclosure controls reportedly supported per source QA. `QA.md` records historical Chromium/Edge checks and Lighthouse lab results, **not tests of KILAT MOTORWORKS**.
- Home head contains `<meta name="robots" content="noindex, follow">`, and `robots.txt` states staging policy. Existing SEO utility explicitly supports staging/production conversion, but must adapt origin to `https://kilatmoto.ismailstudio.my` and verify Worker-level response headers (not assume Pages `_headers` applies).

## Strengths to retain
- No-framework, fast-to-maintain static architecture; five distinct pages, semantic content and responsive patterns.
- Original generated local artwork (some useful reference imagery) and explicit fictional-project notices.
- Structural verification script, SEO transition script, QA evidence directory, reduced-motion and keyboard affordances.
- Services currently navigate via IDs and CTA query strings; project category filters use data-category matching.

## Opportunities / risks
1. **Identity mismatch:** RAPI MOTION titles, headings, logo, social assets, domain references and local source metadata need an exhaustive rebrand sweep.
2. **Creative differentiation:** existing charcoal/lime design is a foundation; demand a more singular editorial grid, strong typography, tuned photography, meaningful spacing, and non-template modules rather than just a colour swap.
3. **Commercial funnel:** make ISMAIL authorship and conversion path feel part of portfolio framing, not an intrusive or deceptive fake automotive booking flow.
4. **SEO:** preserve user-selected indexability while staying explicit about fiction; update original noindex directives, canonical, sitemap, social preview, Worker response headers and alternate-host behaviour.
5. **Hosting mismatch:** README's future Cloudflare **Pages** instructions are inconsistent with **current connected Cloudflare** inventory, which shows `rapimotion` as a live-bound **Worker**. Codex must inspect the real Wrangler/Worker integration before applying any deployment procedure.
6. **Access:** no production browser checks were run here; treat old published QA as historical and run new evidence-gathering tests after implementation.
7. **Naming:** slug `kilatmoto` is **not** customer-facing brand `KILAT MOTO`; two alternate visual boards mistakenly render `KILAT MOTO` and must not supply source copy or branding.

## Verify on Codex startup
Read complete current files, `git status`, `git remote -v`, current main HEAD and hosting integration; review existing CSS/JS and full six service/project contracts, scan all links and image metadata, take actual source and live browser screenshots where accessible. Do not trust this static source audit as complete.
