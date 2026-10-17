# KILAT MOTORWORKS

A five-page fictional Malaysian automotive detailing website by [ISMAIL](https://www.ismailstudio.my/). Editable HTML, CSS and vanilla JavaScript; no browser framework or third-party runtime requests.

- Source: https://github.com/ismailabs/kilatmoto (renamed in place, history retained).
- Verified production host: https://kilatmoto.ismailstudio.my/
- Hosting: Cloudflare Worker `kilatmoto` with Static Assets, not Pages.
- Release evidence: `kilatmoto-Codex-Handoff/16-RELEASE-REPORT.md` and `qa-artifacts/`.

## Preview and verify

Run `py scripts/serve.py` and open http://127.0.0.1:8000/. Use HTTP rather than opening index.html directly. Python is only a preview/verification dependency.

```powershell
npm ci
py scripts/verify_static.py --base-url http://127.0.0.1:8000
node --check assets/js/main.js
npm run test:browser
node scripts/performance-qa.mjs
npm run build
npx wrangler deploy --dry-run
```

Browser QA uses an installed Microsoft Edge. Set `QA_ORIGIN` to the public HTTPS origin to exercise production. The scripts save real screenshots and structured observations. Dev dependencies provide QA and publishing; the shipped website has no package dependency.

## Content and interactions

| Route | Purpose |
|---|---|
| `/` | Cinematic introduction, six services, care process, project previews, creator invitation and FAQ |
| `/about/` | Fictional brand principles, Malaysian driving context and hypothetical workflow |
| `/services/` | Six exact service labels/IDs, suitability, native disclosures, limitations and demo selection links |
| `/projects/` | Six preserved concepts and filter associations; keyboard-operable filters and modal image viewer |
| `/contact/` | Local validation only; fictional location context and distinct genuine ISMAIL destination |

Services: Signature Exterior Detail (`exterior`), Interior Reset (`interior`), Paint Correction (`paint`), Ceramic Protection (`ceramic`), Wheel & Glass Care (`wheels`), Maintenance Detail (`maintenance`).

No HTML form, submission endpoint, analytics, mail, booking, payment, cookies or browser storage is used. Use sample details only. The explicit response says no enquiry was sent, submitted, booked or saved. CSP forbids form actions and network connections. All six projects and navigation remain available without JavaScript; native disclosures and original-image links still work.

## Authoring and deployment

Edit the five HTML files, shared `assets/css/styles.css` and `assets/js/main.js` directly. Photo variants and editable SVG identity files live under `assets/photos/` and `assets/brand/`. The handoff is a reference package; it is never uploaded as website content.

`npm run build` copies only an allowlisted set of public files into `dist/`. It excludes Git metadata, the handoff, docs, node_modules, scripts and QA evidence. `release.json` and `X-Release-SHA` identify the source commit; `dirty` reports tracked local changes at build time. `wrangler.jsonc` deploys that directory to the named Worker/custom domain. See DEPLOYMENT.md for lifecycle and rollback.

Production is technically indexable with honest fictional-portfolio metadata. Search-engine inclusion is separate from technical indexability. See the release report for the actual verified state.
