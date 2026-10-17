# KILAT MOTORWORKS — release report

**DONE — PRODUCTION VERIFIED**

Verified 2026-10-17T01:16:24+00:00 / 2026-10-17T09:16:24+08:00 (Asia/Kuala_Lumpur). Original handoff documents 00–15 are retained as preparation records; this report records the completed implementation.

## Release identity

- Visitor brand: **KILAT MOTORWORKS**.
- Repository: https://github.com/ismailabs/kilatmoto — renamed in place; repository ID **1420850462**, original history preserved.
- Deployed application Git SHA: **`d4c7faacfb01a25b08b4e3b147d59ca841a83d5b`** on `main`.
- Original baseline ancestor: `d47f3eafff97f0c8fa6ee026e013e1430c70b9fd`.
- GitHub rename was completed before the repository connection update at 2026-10-17T00:39:14.410Z; the final name, ID, homepage, refs and Pages-disabled state were independently verified at 2026-10-17T01:13:27.801457+00:00. The exact rename mutation second was not separately captured.
- Worker service: **`kilatmoto`**, Static Assets, not Cloudflare Pages.
- Worker version: **`5f88b0d4-8ac0-4605-bcff-7640e2739a2c`** at 100% traffic.
- Deployment ID: `bfeed9fc-20d8-46b3-a93b-2ea4f552c18d`.
- Build ID: `348b3329-dc9e-4cff-8548-fd006beddcaf` — successful, exact source SHA above.
- Production: **https://kilatmoto.ismailstudio.my/**.
- Deployed: **2026-10-17T01:12:01.540795+00:00 UTC / 2026-10-17T09:12:01.540795+08:00 MYT**.
- Public `/release.json` and `X-Release-SHA` agree with that clean source commit. A subsequent evidence/documentation commit changes only files excluded from website publication; it does not change this deployed application identity.

## Protected content and safety

All five routes return direct HTTP 200: `/`, `/about/`, `/services/`, `/projects/`, `/contact/`.

All **6/6 exact service names and IDs** are preserved: Signature Exterior Detail (`exterior`), Interior Reset (`interior`), Paint Correction (`paint`), Ceramic Protection (`ceramic`), Wheel & Glass Care (`wheels`), Maintenance Detail (`maintenance`). All six service-to-demo query mappings passed browser tests.

All **6/6 concepts and associations** remain: The city reset. (`urban`, exterior); The executive edit. (`executive`, refinement); Room for real life. (`family`, interior); The weekend ritual. (`coupe`, refinement); The everyday rhythm. (`daily`, maintenance); The quiet arrival. (`electric`, protection). Filters produce 1/1/2/1/1/6 results, with announcements. Original-image links work without JavaScript.

The fictional disclosure appears at the top of every page and in page/footer context. AI imagery is labelled illustrative. No invented customers, statistics, address, phone, opening hours, prices, warranty, certification, tuning or completed-work claims were added. The genuine ISMAIL destination is **https://www.ismailstudio.my/**, verified HTTP 200; the apex redirects there.

The demo has no HTML form, endpoint, sending code or persistence. Empty, invalid and valid interactions passed; the browser recorded **zero network requests** during the demo window and no localStorage/sessionStorage/cookies. Final confirmation: “No enquiry was sent, submitted, booked or saved.” CSP retains `connect-src 'none'` and `form-action 'none'`.

## Actual verification

| Check | Command / method | Observed result | Evidence |
|---|---|---|---|
| Source and local HTTP | `py scripts/verify_static.py --base-url http://127.0.0.1:8000` | PASS: five pages, 179 references, 26 targets, protected contracts, links, semantics, safety and production SEO | `scripts/verify_static.py`, `QA.md` |
| JavaScript and build | `node --check assets/js/main.js`; `npm run build`; Wrangler 4.151.1 dry run | PASS; controlled 63-file output, no application bindings; docs, handoff, Git, scripts and packages excluded | `scripts/build.mjs`, `wrangler.jsonc` |
| Asset integrity | Bundled Python/Pillow, hashes, SVG parsing | PASS: all 11 supplied runtime assets match the manifest; social graphic 1200×630 | `../qa-artifacts/asset-integrity.json` |
| Local browser | Microsoft Edge via Playwright | PASS: 175 checks, 40 route/width combinations, zero errors | `../qa-artifacts/local-browser-evidence.json` |
| Production browser | `QA_ORIGIN=https://kilatmoto.ismailstudio.my` with `npm run test:browser` | PASS: 175 checks, 40 route/width combinations, zero errors; all five desktop/mobile routes | `../qa-artifacts/production-browser-evidence.json`, `production-*.png` |
| Keyboard and progressive enhancement | Menu, navigation, filters, viewer, native disclosures, demo focus, no-JS and reduced-motion emulation | PASS; menu Escape/return focus, modal Tab/Shift+Tab containment, six query mappings; all six concepts without JS | Browser JSON above; `../qa-artifacts/home-layout-keyboard.json` |
| Reflow | 320/375/390/430/768/1024/1440/1920px, plus 200% CSS zoom at 640/960 windows | PASS: no horizontal document overflow on all five routes | Browser JSON above |
| Axe | WCAG 2 A/AA, 2.1 AA, 2.2 AA rule tags | Zero violations in ten production audits: all pages at 390/1440px | Production browser JSON |
| HTTPS, bytes, headers, SEO and private paths | `py scripts/production-check.py --mode production --sha d4c7faacfb01a25b08b4e3b147d59ca841a83d5b` | **77/77 PASS**: trusted TLS 1.3, all five HTML files and 18 assets match committed blobs, release SHA, no injected script, secure headers, private/unknown paths 404 | `../qa-artifacts/production-http-evidence.json` |
| Worker/domain/DNS | Authenticated Cloudflare inventory and deployments | `kilatmoto.ismailstudio.my` → Worker `kilatmoto`, enabled; previews off; proxied managed AAAA `100::` | `../qa-artifacts/final-production-cloudflare-deployment.json`, `../qa-artifacts/infrastructure-final.json` |
| GitHub/history | Git, advertised remote and GitHub API | Stable repo ID, preserved ancestor, correct new remote; release HEAD/tracking/advertised SHA match | `../qa-artifacts/github-publication.json` |
| Former hostname | Actual browser navigation, redirect chain and meta/header inspection | HTTP 200, original RAPI MOTION, noindex; **zero redirects**, no new-host redirect | `old_host_browser` in production HTTP evidence |
| Unrelated resources | Compare baseline and final API snapshots | Pre-existing Worker modification times/tags, DNS records and custom-domain associations unchanged; original RUM rule unchanged | `../qa-artifacts/infrastructure-baseline.json`, `../qa-artifacts/infrastructure-final.json` |
| Publication scan | `py scripts/release-check.py` | Staged path, custom secret-pattern and whitespace checks passed; no force push | `scripts/release-check.py`; not a Gitleaks audit |

## Performance and visual comparison

Lighthouse **13.5.0**, installed headless Microsoft Edge; mobile simulated throttling, desktop settings recorded in the runner. Final audits ran separately from the browser suite.

| Final run | Performance | Accessibility | Best practices | SEO | LCP | CLS | TBT |
|---|---:|---:|---:|---:|---:|---:|---:|
| Production mobile | 82 | 100 | 100 | 92 | 3.023s | 0.07428 | 415.0ms |
| Production desktop | 100 | 100 | 100 | 92 | 0.595s | 0.00000 | 0.0ms |

Raw lab reports are local `qa-artifacts/lighthouse-production-*.json`; committed compact evidence is `../qa-artifacts/production-performance-summary.json`. Initial production mobile performance was 81 with 580.5ms TBT. An experimental layout-deferral trial measured 95 locally but 78/75 on the host and caused an additional native-anchor regression. It was removed. Its measurements are retained separately in `production-deferred-layout-performance-summary.json` and `production-recheck-performance-summary.json`; they are not final-release results. The final table above records the restored layout. Mobile blocking time remains a P1 performance limitation; no hosted performance improvement is claimed. No field INP, real-user Core Web Vitals or causal benchmark improvement is claimed.

The final mobile audit also reported a browser-cache-clear timeout; a cold-cache guarantee is not claimed.

Lighthouse's robots.txt audit is blocked by the deliberately restrictive page `connect-src` policy. Independent HTTPS checks verify the actual robots file, five-entry sitemap, index/follow meta, absence of noindex headers, absolute canonicals and social images. The policy was preserved. Search-engine inclusion and Search Console acceptance are not claimed.

The primary board and four precise Home/Services mockups guided the warm photography, graphite/lime palette, correct stacked brand, desktop split hero, mobile crop/actions and service grid. Actual local/production captures were visually reviewed. The catalogue is longer than the overview mockup because it includes meaningful suitability and limitations; the interior card correctly depicts a cabin. Alternate wrong-brand boards and fabricated claims were excluded. The site is editable HTML/CSS/JS, never flattened boards.

The final CSS uses the stable fully laid-out Home page. Experimental native off-screen deferral was removed after a hosted creator-anchor regression. The permanent browser suite now checks that the disclosure link lands on the creator heading. Additional skip-link and mobile scroll checks pass. Full-document captures expand only capture height for complete painting; responsive assertions and axe run at their original viewports. The standalone mobile editorial-scroll capture shows the normal scrolled view. No numerical pixel-fidelity score is claimed.

## Decisions, repaired failures and limits

- Existing static architecture retained. Node dependencies are development/QA/publishing only.
- New Worker created before cutover, with the original Worker kept published. Old build trigger retired; successor points to the renamed repository's stable ID and new Worker. Automatic building is configured/enabled; the measured releases used explicit exact-commit Cloudflare Builds requests. Local Wrangler authentication was absent, so the authenticated connector/build service was used successfully; no credential value was exposed or new login bypassed.
- A legacy **GitHub Pages** publisher on this same repository was discovered and disabled to avoid a duplicate public copy. Cloudflare Pages remained unused.
- A pre-existing zone Web Analytics beacon was detected by byte comparison. A host-specific exclusion attempt hit the account's rule limit and changed nothing. This site's `Cache-Control: public, max-age=0, must-revalidate, no-transform` prevents injection using [Cloudflare's documented mechanism](https://developers.cloudflare.com/web-analytics/faq/). Existing zone analytics and other hosts are unchanged. Final HTML contains only the local application script.
- Initial header-order consistency, a test locator whose accessible label changed, the HTTP helper's URL accessor, image dimensions, intrinsic zoom overflow and the experimental layout/anchor regression were corrected. Final source and hosted checks pass. The system Python lacked Pillow; asset validation succeeded with the bundled runtime.
- The old host returns 403 to urllib but 200 to a normal browser. Both observations are retained; the no-redirect/noindex conclusion uses the actual browser response and redirect chain.
- Accessibility evidence is automated plus keyboard/visual checks, not certification. Physical phones, Safari, Firefox, screen readers and browser-toolbar zoom were not tested. The 200% result is CSS zoom/reflow stress testing. Lab scores vary with environment; no commercial conversion or search-ranking claim is made.
- **Remaining P0 defects: none in the tested scope. Remaining P1: mobile lab blocking time/performance as recorded above. External access blockers: none for this release.**

## Rollback and maintenance

Keep the source history and no-transform/security headers. Re-run the supplied source/browser/HTTP checks after changes. Restore a prior verified `kilatmoto` Worker version through deployment history if required, then verify its manifest/SHA and routes. The pre-layout verified version `5261db3d-983b-4428-8a5e-9e0f9a9ca3a8` is available; the original independent `rapimotion` version remains `543c3245-7ab5-4e50-a867-9f2bf48b97a1`. Do not redirect the old hostname, alter unrelated DNS, force-push or replace history.

**Final verdict: DONE — PRODUCTION VERIFIED.**
