# Scoped GitHub + Cloudflare Workers migration (NOT Cloudflare Pages)

## Fixed production identifiers
- Source repo: `ismailabs/rapi-motion` → target **`ismailabs/kilatmoto`**.
- Source Worker service: `rapimotion` → target **`kilatmoto`**.
- Current Worker custom-domain binding: `rapimotion.ismailstudio.my` → service `rapimotion` (read-only inspected 17 Oct 2026).
- New Worker custom domain: **`kilatmoto.ismailstudio.my`** → service `kilatmoto`.
- Customer display brand: **KILAT MOTORWORKS** (do not abbreviate to `KILAT MOTO` in website).
- User selected **no redirect from old automotive hostname**.

## Read-only preflight — do not skip
1. Obtain current GitHub HEAD, branch protection, workflows/build hooks, local clean/dirty state and repo settings. Use authenticated tools as available, never assume admin permissions are present in Codex environment.
2. Inspect Cloudflare Worker `rapimotion` script/Static Assets bindings, compat settings, account Worker Builds/Git integration, custom domain mapping, associated DNS and deployments. Confirm actual live HTTP status or report inability.
3. Confirm `kilatmoto` repo/Worker/domain names are available. Recheck if resources changed; do not replace an unrelated project that now owns any target name.
4. Record original production state and rollback path (restore prior Worker configuration or rebind original domain if necessary). Do not expose secrets or download unrelated account data.
5. Determine whether public old Worker must stay live. Since **no redirect requested**, prefer non-disruptive coexistence until new domain passes verification, then document old-host outcome. No old-host redirection rules.

## Implementation and staging
1. Build and verify redesign locally from existing `rapi-motion` repo. Preserve source history and working state.
2. Prepare `kilatmoto` Worker config / Wrangler Static Assets, e.g. appropriate `assets.directory` pointing at repository root or controlled static output folder **actually containing** five HTML routes. Do not assume Pages `_headers` is executed by Workers; verify Worker response headers explicitly.
3. For staging, keep `noindex` on previews and alternate hosts until domain verified; avoid promoting a real-looking fictional business as a live service.
4. Deploy tested new Worker `kilatmoto` via authenticated sanctioned tooling; inspect its actual assets and any Git build integration. Verify at staging/assigned Workers URL without modifying old domain.
5. Attach Worker **custom domain** `kilatmoto.ismailstudio.my` via the real Cloudflare mechanism. It may handle its own DNS record; avoid manually inventing a Pages CNAME. Verify TLS, DNS, content, route refresh and security headers.
6. Update GitHub repository display name to `kilatmoto` (keep history), change local origin URL, and update Worker Builds integration/triggers to point at renamed repo if necessary. Be mindful renaming while auto-deploy is active; sequence with backup/rollback and real source SHA verification.
7. Switch to production SEO only once intended host is live; publish five canonicals, sitemap, index/follow instructions and social URLs. Hosted Worker headers must not send `X-Robots-Tag: noindex` inadvertently.
8. Preserve unrelated DNS/Workers. Do **not** set a redirect from `rapimotion.ismailstudio.my` to new host. Record the old hostname's behaviour and whether previous Worker remains published.

## Checks required on **actual** production
- `https://kilatmoto.ismailstudio.my/`, `/about/`, `/services/`, `/projects/`, `/contact/` all HTTP 200 with correct HTML after direct navigation/refresh.
- Valid HTTPS chain, correct Worker/custom domain, responsive assets and JS.
- Exact protected labels, functional nav, accessible menu, working filter/gallery, unsent demo confirmation and ISMAIL CTA.
- HTTP headers not falsely staging/noindex; unique canonical URLs; indexable robots/sitemap; truthful metadata.
- Verify old hostname is **not** redirected to `kilatmoto`, as requested. No accidental changes to other sites.
- Record Git SHA, Worker deployment identifier and a time-stamped production verification matrix.

## Official docs
- Cloudflare Workers Static Assets/Configuration: https://developers.cloudflare.com/workers/wrangler/configuration/
- Cloudflare Static Assets binding: https://developers.cloudflare.com/workers/static-assets/binding/
- GitHub repository rename: https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository
- Google indexing and canonical references in `15-REFERENCES.md`.

**Autonomy:** User authorises scoped repo, Worker, DNS and deployment actions. This does **not** grant missing external access or permit destructive unrelated operations. If auth or platform permissions block an action, complete the safe remainder, log the exact blocker and requested one-off user action.
