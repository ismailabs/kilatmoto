# Research references & evidence classification | 17 October 2026

## Direct connected-account evidence (read-only)
- GitHub connected repository `ismailabs/rapi-motion` default `main`, root listing, README, DEPLOYMENT.md, QA.md, ASSET-MANIFEST.md, route source files, `robots.txt` (retrieved 2026-10-17).
- Cloudflare `GET /accounts`, `/accounts/{account_id}/pages/projects`, `/accounts/{account_id}/workers/scripts`, `/zones?name=ismailstudio.my`, `/zones/{zone_id}/dns_records`, `/accounts/{account_id}/workers/domains`, `/zones/{zone_id}/workers/routes` (retrieved 2026-10-17). Sensitive account IDs and tokens intentionally **not** stored.
- Public `https://rapimotion.ismailstudio.my/` browser fetch **could not retrieve live page**; status of public HTML not independently established. Cloudflare binding presence is **not** a successful HTTP-response measurement.

## Primary technical documentation (checked 2026-10-17)
- GitHub repo rename and preserved redirects: https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository
- Cloudflare Workers Wrangler config, custom domain and assets: https://developers.cloudflare.com/workers/wrangler/configuration/
- Cloudflare Workers Static Assets: https://developers.cloudflare.com/workers/static-assets/binding/
- Cloudflare Pages custom domains (comparative only; not current deployment): https://developers.cloudflare.com/pages/configuration/custom-domains/
- Google noindex meta+header: https://developers.google.com/search/docs/crawling-indexing/block-indexing
- Google canonical: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Google sitemap: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Google structured data restrictions: https://developers.google.com/search/docs/appearance/structured-data/sd-policies

## Evidence vs recommendation
Source-observed: five pages, six services, six projects, noindex staging, existing Worker/domain. User-confirmed: new brand, technical slug, no old redirect, indexable final demo, autonomous Codex. Suggested (not approved as a rigid final UI): palette tokens, tagline copy, exact spacing, placement of images and typography details. All must be validated against actual rendering before production.

## Image provenance
Each generated source and derivative is recorded in `13-ASSET-PROVENANCE.md` and `data/asset-manifest.json`. Photos are original AI-generated fictional **illustrations**, not actual photographed work. Logo SVG files are produced specifically for this handoff. Avoid manufacturer badges/logos or documentary business claims.
