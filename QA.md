# KILAT MOTORWORKS — measured verification

17 October 2026. Latest release identity and production verdict are recorded in `kilatmoto-Codex-Handoff/16-RELEASE-REPORT.md`. Historical RAPI MOTION results are available through Git; they are not KILAT evidence.

## Implemented design and comparison

The precise 1440px/390px Home and Services references and primary concept board guided the cinematic dark car, warm lighting, lime/graphite palette, stacked brand, three-line Home headline, rectangular actions and six-service grid. No reference board is rendered as webpage content. Wrong KILAT MOTO names, invented metrics and fictitious business contacts were excluded.

Actual local HTTP screenshots under `qa-artifacts/local-*.png` were inspected. Desktop Home preserves the split hero and four-part value strip; mobile uses the supplied portrait crop, stacked actions and single-column service cards. Services preserves all six names with fuller descriptions, suitability, care limitations and demo links, making it longer than the reference overview. Its interior illustration depicts a cabin, rather than copying the mockup's mismatched polishing image. About, Projects and Contact share the tested system. The creator section is a deliberate lime editorial interval with a distinct genuine ISMAIL CTA.

Initial too-early top captures showed lazy-image placeholders; final full-page captures force decoding and the Services top capture was replaced after decoding. These are screenshot timing artifacts, not evidence that empty placeholders are intended design.

## Structural, HTTP and safety

`py scripts/verify_static.py --base-url http://127.0.0.1:8000` passed: five pages, 179 references, 26 actual HTTP targets, exact service names/IDs and demo mappings, six baseline project/filter associations, six concept titles, semantic structure, links, image alt/dimensions and SEO consistency. `node --check assets/js/main.js` passed. Handoff asset validation passed using the bundled Python/Pillow runtime; system Python lacks Pillow.

The enquiry has no form, send endpoint, fetch/XHR/beacon, cookies or storage. Browser instrumentation observed **zero network requests** during empty, invalid and valid demo interactions and no localStorage/sessionStorage/cookies. `connect-src 'none'` and `form-action 'none'` reinforce this boundary. ISMAIL's apex redirects to https://www.ismailstudio.my/ and returns HTTP 200 with the expected portfolio title; site CTAs use that final destination.

## Actual browser and accessibility

Microsoft Edge/Chromium via Playwright, real HTTP pages. `qa-artifacts/local-browser-evidence.json` records **175 successful checks**, **40 route/viewport combinations** at 320/375/390/430/768/1024/1440/1920px, **zero browser errors**, and **zero axe violations across ten audits** (all five routes at 390px and 1440px, WCAG 2 A/AA, 2.1 AA and 2.2 AA rule tags).

Coverage includes desktop navigation; mobile keyboard menu opening, first-link focus, Escape and focus restoration; all six filters and result counts; gallery opening, Tab/Shift+Tab containment and Escape return; all six service query mappings; empty/invalid-email/valid demo feedback and focus; native FAQ keyboard expansion; no-JavaScript five-route navigation, all projects, original-image links and unavailable demo fallback; reduced-motion emulation; 200% CSS zoom/reflow at 640px and 960px windows on all five routes. The enlargement check exposed intrinsic overflow in headings and the value strip; safeguards fixed it before the successful run. CSS zoom is a reflow stress test, not a claim of a physical-browser toolbar zoom audit.

Automated zero violations are not WCAG certification. Physical phones, Safari, Firefox, screen readers and real touch ergonomics were not tested. Screenshots cover desktop/mobile; performance is lab data, not field Core Web Vitals.

## Local performance

Lighthouse **13.5.0** with installed headless Edge. Mobile uses default simulated mobile throttling; desktop uses the recorded desktop settings. `qa-artifacts/local-performance-summary.json` contains actual timestamps, settings/results and failed-audit explanations. Measured Home mobile: performance **81**, accessibility **100**, best practices **100**, SEO **58**, LCP **2.229s**, CLS **0.07324**, TBT **615.84ms**. Desktop: **95/100/100/58**, LCP **0.729s**, CLS **0**, TBT **0ms**. These staging runs overlapped browser QA; CPU contention may affect results. No causal improvement claim is made.

Staging SEO is deliberately noindex. Lighthouse's robots.txt audit also encounters the restrictive connect-src policy. Direct HTTP/source robots checks pass; the security policy was not weakened for an audit score. Final production lab measurements and indexability checks belong in the release report.

## Publication safeguards

A feature branch retains the original commit ancestry. New Worker config targets only `kilatmoto` and its named custom domain. Builds copy only public files into an ignored `dist/` output; a Wrangler dry run passed with 63 files and no bindings. The old main-branch Worker build trigger was replaced with a trigger on the new Worker before publication. The original Worker and domain remain live, without a new redirect. Custom staged secret-pattern/path/whitespace scanning is recorded separately; it is not Gitleaks.



## Final hosted release — 17 October 2026

The corrected final application source is `d4c7faacfb01a25b08b4e3b147d59ca841a83d5b`, served at https://kilatmoto.ismailstudio.my/ by Worker `kilatmoto`, version `5f88b0d4-8ac0-4605-bcff-7640e2739a2c`. Final production verification passed **77 HTTPS/content/SEO checks** and **175 browser checks**, including 40 responsive combinations, ten axe audits with zero violations, zero console errors and zero demo requests. The additional mobile skip-link, creator-anchor and editorial-scroll checks passed. Deployed HTML/assets match committed blobs. The original hostname remains its original noindex site with no redirect in a normal browser.

An experimental off-screen layout change measured 95 locally but 78/75 on the host and broke a hosted creator-anchor check. It was removed, and the corrected layout passes the permanent anchor regression. Those experiment measurements remain separate from final-release data. Final hosted Lighthouse measured mobile **82** (LCP **3.023s**, CLS **0.07428**, TBT **415ms**) and desktop **100** (LCP **0.595s**, CLS **0**, TBT **0ms**). The mobile run reported a cache-clear timeout, so no cold-cache guarantee is claimed. Mobile blocking time remains a P1 limitation. Accessibility/best-practices measured 100 and SEO 92. The robots audit hit the preserved connect-src policy; independent actual HTTPS robots/sitemap/indexability checks passed.

See `kilatmoto-Codex-Handoff/16-RELEASE-REPORT.md` for the complete matrix, migration decisions, repaired failures, provenance, limitations and rollback. All final evidence is in `qa-artifacts/`. Physical-device/Safari/Firefox/screen-reader coverage and actual search-engine inclusion are not claimed.
