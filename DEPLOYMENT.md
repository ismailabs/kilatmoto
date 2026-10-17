# KILAT MOTORWORKS — Workers deployment

The existing repository was renamed from `ismailabs/rapi-motion` to `ismailabs/kilatmoto`, preserving repository ID 1420850462 and baseline commit d47f3eafff97f0c8fa6ee026e013e1430c70b9fd. The local folder name may remain `rapi-motion`.

## Actual infrastructure

The original site uses Worker `rapimotion`, Static Assets and custom domain `rapimotion.ismailstudio.my`. The account has zero Pages projects. The new release uses Worker `kilatmoto` and `kilatmoto.ismailstudio.my`. These are separate services. The original Worker/domain stays published with no new redirect, retaining its prior noindex policy.

A preflight inventory is saved in `qa-artifacts/infrastructure-baseline.json`. The old Worker version is `543c3245-7ab5-4e50-a867-9f2bf48b97a1` (deployment `142436c7-1f76-45ef-ad25-9dcd46dc4dc9`). No old-host DNS record was deleted.

The former main-branch build trigger was retired to prevent accidental deployment to the old Worker. Its successor targets the new Worker and the same stable GitHub repository ID. The repository connection name was updated to `kilatmoto`. The existing Cloudflare-managed build-token reference is retained; no token value is stored here. Consult the release report for build/deploy receipts.

## Controlled publication

1. Run source, browser, accessibility and performance checks; inspect screenshots.
2. Build using `npm run build`. Only the public allowlist enters `dist/`.
3. Use `npx wrangler deploy --dry-run` to validate config/output.
4. Publish a clean, reviewed commit using the authenticated Cloudflare Workers Builds connection or `npm run deploy` when local Wrangler is authenticated. Local `wrangler whoami` was unauthenticated during this release; the connected API is the authorized publication path.
5. Deploy staging/noindex first, then verify HTTPS and all five routes on the custom domain.
6. Run `py scripts/configure_seo.py --mode production --origin https://kilatmoto.ismailstudio.my`, verify with `--check`, review, commit and publish.
7. Independently compare local HEAD, origin/main, advertised Git remote, hosted release.json, X-Release-SHA and Worker deployment/version. Test actual response headers; source `_headers` alone is insufficient.

Cloudflare Workers Static Assets currently supports `_headers` on asset responses. This configuration is assets-only: no custom Worker fetch handler intercepts those responses. `workers_dev` and preview URLs are disabled, and only the intended custom domain is configured. No old-host redirect exists in the source or configuration. Custom-domain binding manages its own DNS; do not add a Pages CNAME.

## SEO and security

`configure_seo.py` manages meta robots, unique canonical/og:url, absolute social-image URLs, robots.txt and five-route sitemap. Staging is noindex; production is index/follow. It never deploys. Keep `connect-src 'none'`, `form-action 'none'`, frame restrictions and other security headers. Lighthouse's browser-side robots fetch may be blocked by this CSP; verify robots independently over HTTPS rather than weakening the demo's network boundary.

## Rollback

For a defective new release, use Cloudflare's Worker version/deployment history to restore the last verified `kilatmoto` version, then verify its release SHA and all routes. The previous `rapimotion` Worker remains independent and available. Do not redirect the old hostname, change unrelated DNS, force-push or delete history. To restore the original build trigger only if explicitly needed, recreate it against the saved original Worker tag/repository connection with original build command empty and deploy command `npx wrangler deploy`; do not let that old trigger consume the new `kilatmoto` config.

Completion requires the real evidence in `kilatmoto-Codex-Handoff/16-RELEASE-REPORT.md`; this runbook is not proof of deployment.

## Scoped production refinements

GitHub also had a legacy Pages publisher for this repository despite Cloudflare having no Pages projects. That duplicate repository-specific publisher was disabled and verified as absent through GitHub's Pages API. The repository homepage points to the Worker custom domain.

The zone's pre-existing automatic Cloudflare Web Analytics setup injected a beacon into the new site's HTML. The existing CSP blocked it. A proposed host-only RUM exclusion was rejected by the account's rule limit without changing the existing rules. The new Worker's own `_headers` therefore uses `Cache-Control: public, max-age=0, must-revalidate, no-transform`, the documented way to prevent automatic beacon injection. This is scoped to this site's responses; the zone-wide analytics setting and other hosts are untouched. Preserve this header and verify actual HTML has no injected beacon after future releases.

Reference: https://developers.cloudflare.com/web-analytics/faq/#my-website-is-proxied-through-cloudflare-but-web-analytics-automatic-setup-is-not-working
