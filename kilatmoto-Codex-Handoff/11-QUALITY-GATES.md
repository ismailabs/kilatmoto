# Definition of Done — measurable and honest

## P0: no-go until satisfied, unless explicitly marked blocked externally
- [ ] Brand is **KILAT MOTORWORKS** on all customer-visible surfaces; technical slug exactly `kilatmoto` in GitHub, Worker, and hostname.
- [ ] Five route paths preserved, direct navigation and refresh work, no broken assets/links.
- [ ] All six exact service names and source IDs preserved; useful descriptions improved, no missing services.
- [ ] Six distinct conceptual projects remain discoverable and readable without JS; filter and viewer function with JS.
- [ ] Explicit fictional disclosure above fold, on About/Projects and Contact; no real booking, stored personal data, sent enquiry or fabricated business contact claims.
- [ ] At least one clear correct ISMAIL business CTA per major journey; verify its destination, distinguish it from demo action.
- [ ] Run source checks `py scripts/verify_static.py`, JS syntax check, HTTP route checks; fix all introduced P0 failures.
- [ ] Browser keyboard menu, project filter, viewer, contact demo validation and no-submit behaviour tested in real browser, no production JS exceptions.
- [ ] Mobile widths 320/375/390/430 with no horizontal overflow, keyboard focus visible, all CTA copy legible; tablet/desktop 768/1024/1440/1920 reviewed.
- [ ] Verified new GitHub repo `ismailabs/kilatmoto`, preserved history, correct branch/release SHA, no force push or secret leak.
- [ ] Verified actual Cloudflare Worker `kilatmoto` (not Pages by assumption), deployed domain `https://kilatmoto.ismailstudio.my`, HTTPS and all five routes/content/assets.
- [ ] Production indexable **both meta + actual headers**, accurate canonical/sitemap/social; no misleading LocalBusiness claims.
- [ ] Old domain has **no redirect to new domain**; unrelated services not changed.
- [ ] Final release report includes actual test commands/results, screenshots, diff/commit/deploy IDs, blockers and actual status.

## P1: desirable and documented
- [ ] Editorial visual design matches precise mockup composition semantically; no flattened mockup masquerading as implementation.
- [ ] Responsive local image assets optimized; clear loading priorities, no unexpected large CLS.
- [ ] WCAG 2.2 AA intended; axe and manual keyboard/contrast/reduced-motion/zoom checks, note limited evidence where applicable.
- [ ] Lighthouse mobile + desktop lab checks on local and if possible production, record real values, environment and no measured improvement claims without baseline.
- [ ] Stable SEO/social preview, 200 responses, sitemap valid; check hosted security headers and CSP.
- [ ] Source docs, asset provenance and maintenance notes updated.

## Status labels
- `DONE — PRODUCTION VERIFIED`: all P0 criteria actually verified on intended live domain and GitHub/Worker.
- `IMPLEMENTED — PRODUCTION BLOCKED`: site passed local/staging but specific external auth/hosting/domain step blocked (name blocker and exact next user action).
- `PARTIAL — QUALITY GATES FAILED`: one or more implemented P0 failures remain; list failing criteria and recovery steps.

Do not call static audit, AI illustration or conceptual UI boards a measured benchmark. Do not claim 100 Lighthouse or certified accessibility without applicable evidence.
