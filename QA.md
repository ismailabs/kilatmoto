# RAPI MOTION — verification record

**15 October 2026.** Five-page fictional automotive portfolio, implemented and tested locally. No Cloudflare deployment, DNS edit or domain activation was performed. These results replace the previous package's isolated-document test claims.

## Audit and visual direction

The supplied site was already at the project root. Its `/assets/` paths worked over HTTP; opening `index.html` through `file://` explained the apparent missing styling. Its pale/blue presentation, oversized capital headings and pill controls differed substantially from the approved RAPI reference. All five pages now use charcoal, lime, white, compact typography, rectangular controls, considered imagery and restrained borders.

The five-page RAPI composite was the primary visual reference; the unrelated PRIME hero provided secondary automotive mood context. Actual browser captures were visually compared for palette, hierarchy, imagery, section rhythm and card density. About's worker crop, the interior service image and mobile typography were refined after rendering. This was a qualitative comparison: the small composite cannot support a reliable pixel-difference fidelity score. No reference image is presented as implemented output.

## Structural and HTTP checks

```powershell
py scripts/serve.py --port 8001
py scripts/verify_static.py --base-url http://127.0.0.1:8001
py scripts/configure_seo.py --mode staging --check
node --check assets/js/main.js
```

**PASS: five pages, 165 references and 25 actual HTTP targets.** The checker validates distinct titles/descriptions, heading hierarchy, IDs, internal paths/anchors/srcsets, image alt text/dimensions, disclosures, ISMAIL links, sitemap XML, consistent SEO mode and the frontend-only safety boundary. All checked HTTP resources returned nonempty 200 responses. JavaScript syntax passed.

The real ISMAIL destination remains `https://www.ismailstudio.my/`; a direct HTTPS HEAD request returned **200**. No analytics, booking endpoint, remote font, map embed or runtime image hotlink was added.

## Real browser coverage

Delivered HTML was navigated through local HTTP at ports 8000 and 8001 in Codex's in-app Chromium. Port 8001 emulated the global security headers. CSS, JavaScript, font and images loaded normally. There was no `set_content`, resource embedding or simulated execution.

All five routes passed at requested viewports **320×740, 375×812, 430×932, 768×1024, 1024×768, 1440×1000 and 1920×1080**: **35 combinations** without horizontal document overflow. Classic scrollbars sometimes reduce content width by 15px; evidence records actual client width. Final Home/About/Contact checks used a 375px content width, followed by a narrow 320px requested-width regression on all five pages after the final line-break adjustment.

All five desktop navigation links were clicked successfully. Final website warning/error logs were empty. Separate automation-tool telemetry errors were not site requests or website console errors.

**19 functional assertions passed:** keyboard mobile menu opening/focus/Escape/navigation; six project filters with counts 1/1/2/1/1/6; keyboard image opening, Tab containment and Escape focus restoration; service-query selection; empty and invalid-email focus/feedback; valid demo response/status focus; keyboard FAQ expansion. The first gallery test exposed Tab leaving its single control; that defect was fixed and retested.

The enquiry has no HTML form, action, endpoint, fetch/XHR/beacon or persistence code. Header policies `connect-src 'none'` and `form-action 'none'` reinforce that boundary. The browser verified the explicit unsent/unsaved demo response. A resource-timing counter was unavailable in the automation scope; an instrumented zero-request measurement is **not** claimed.

No-JavaScript navigation, visible projects, ordinary gallery links and native disclosures are supported by source design and inspection; a separately configured browser session with JavaScript disabled was unavailable. Reduced-motion CSS is present; OS preference emulation was not performed.

## Accessibility and performance

**Lighthouse 13.5.0**, CLI, installed headless Microsoft Edge, actual local HTTP. Mobile used default simulated mobile throttling; desktop used its desktop preset. Inner pages were audited for accessibility and best practices. Results are local lab measurements, not certification or field data.

| Page / run | Performance | Accessibility | Best practices | SEO |
|---|---:|---:|---:|---:|
| Home, mobile after image optimisation | **97** | **100** | **100** | 58 |
| Home, desktop earlier in this revision | **95** | **100** | **100** | 66 |
| About | Not measured | **100** | **100** | Not measured |
| Services, successful final rerun | Not measured | **100** | **100** | Not measured |
| Projects | Not measured | **100** | **100** | Not measured |
| Contact | Not measured | **100** | **100** | Not measured |

Final mobile Home: **LCP 2.40s, CLS 0.0605, TBT 32ms**. Earlier desktop Home: **LCP 0.83s, CLS 0, TBT 156ms**. Earlier mobile scores were 86–87; the final run followed smaller image derivatives and recompression. Machine load and lab variability also affect scores. A small mobile line-break fix followed these audits and received browser regression checks, not another performance audit. No INP or real-user Core Web Vitals were measured.

One initial Services audit encountered a transient local connection refusal. The asset returned 200 directly; the helper's concurrent request backlog was increased and the rerun passed at 100/100. A logo label/name discrepancy was corrected by deriving its accessible name from visible text.

SEO scores are deliberately limited by staging `noindex`. The headered run also reported “robots.txt is not valid” with the explanation **“Fetch of robots.txt failed … CSP violation”**, because `connect-src 'none'` blocked its audit fetch. Direct HTTP retrieval and structural robots validation passed. Security was not loosened to change the score.

## SEO and headers

Delivered source is **staging**: five meta directives and the global header say `noindex, follow`; robots allows crawling to read that directive; sitemap is valid, empty and unadvertised; no production canonical or `og:url` asserts an active hostname. Semantic content, descriptions and social artwork are complete.

The production transition was executed and checked in an isolated copy, then reversed there. It prepares five unique HTTPS canonicals, matching Open Graph URLs, absolute social images, a five-route sitemap, robots sitemap declaration and removal of the staging header while retaining security. Working source stays staging. The script never deploys or changes DNS.

The helper emulated this project's global `_headers` policy, including CSP, frame restrictions, content-type protection and staging indexing. Actual Cloudflare processing, HTTPS, CDN behaviour and public social previews require later launch verification.

## Evidence and publication

`qa-screenshots/evidence.json` contains responsive observations, the 19 assertions, navigation results and compact Lighthouse records with tool versions, timings and limitations. WebP screenshots were converted from actual HTTP JPEG captures without altering rendered content:

- `desktop-home.webp`, `desktop-about.webp`, `desktop-services.webp`, `desktop-projects.webp`, `desktop-contact.webp`: full pages at requested 1440×1000.
- `mobile-home.webp`, `mobile-about.webp`, `mobile-contact.webp`: full pages at 375×812. Native lazy images were brought into view before the final Home capture; initial too-fast captures were replaced.
- `home-preview.webp`: desktop Home viewport overview.

The folder initially lacked its own Git metadata and inherited an unrelated ancestor repository. An independent repository was initialised inside this project, leaving the ancestor untouched. The exact authorised GitHub destination existed, was writable and contained no refs before publication. No alternate repository or history rewrite was used. The staged 58-file package passed whitespace, forbidden-path and custom secret-pattern checks (private keys, common provider tokens, JWTs and assigned secret literals). Gitleaks was unavailable; this is not a claim of a Gitleaks audit. Credentials, caches and temporary generation/audit files are excluded. The completion report provides the verified pushed commit.

## Remaining limits

- No known blocking defect remains in tested flows. Automated coverage does not establish complete accessibility/browser conformance.
- Physical phones, Safari, Firefox, screen readers, browser text zoom and real touch ergonomics were not independently tested.
- No formal WCAG audit, hosted performance measurement, field data, conversion rate or indexing evidence exists.
- Vehicle stories and studio imagery are fictional; no real staff/customer claims, prices, address, hours or treatment guarantees exist.
- Real enquiry delivery, booking, payment and persistence are intentionally absent.
- Pages, authoritative DNS, the planned hostname, certificates and production indexing remain future work documented in `DEPLOYMENT.md`.
