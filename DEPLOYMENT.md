# Future deployment — GitHub → Cloudflare Pages

**No deployment or DNS changes are part of this delivery.** These instructions are for a later authorised launch. The planned domain is `rapimotion.ismailstudio.my`; no `pages.dev` hostname or authoritative DNS provider is assumed.

## 1. Check the delivered repository

Open [ismailabs/rapi-motion](https://github.com/ismailabs/rapi-motion). The five page entry points must be at the root and in `about/`, `services/`, `projects/`, `contact/`, with `assets/` beside the root entry. Do not create another repository or add an enclosing website folder.

From the checkout:

```powershell
git status --short --branch
git remote -v
git log -1 --oneline
py scripts/verify_static.py
py scripts/configure_seo.py --mode staging --check
py scripts/serve.py
```

Open http://localhost:8000/ and test every route. Confirm the demo sends nothing. Stop with Ctrl+C. Keep staging SEO active during initial hosting review.

## 2. Create the Pages connection when authorised

Cloudflare dashboard → **Workers & Pages → Create application → Pages → Import an existing Git repository**. Select GitHub and grant the integration access to the existing `ismailabs/rapi-motion` repository. Select that exact repository and begin setup. Dashboard wording may change.

| Setting | Value |
|---|---|
| Production branch | `main` |
| Framework preset | None |
| Root directory | Repository root / blank |
| Build command | `exit 0` (no compilation) |
| Build output directory | `.` |
| Environment variables | None |

There is no `dist`, `build` or `public` output folder. The checked-in HTML is deployable directly. Cloudflare's [Static HTML guide](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/) describes a no-op build and a custom output directory containing the actual site files.

Review the settings, then deploy only under the later authorisation. Copy the exact assigned `*.pages.dev` URL from the dashboard. Visit `/`, `/about/`, `/services/`, `/projects/`, `/contact/` directly and after refresh. Check images, fonts, menu, filters, viewer and demo feedback. Inspect response headers for CSP and `X-Robots-Tag: noindex, follow`. `_headers` is processed by Pages, not embedded in HTML; the local helper only emulates this project's one global rule. See the [official header guide](https://developers.cloudflare.com/pages/configuration/headers/).

Git-connected Pages normally deploys subsequent pushes automatically. Review deployment triggers before future pushes once this connection exists.

## 3. Find the authoritative DNS provider

Being registered at Exabytes does not establish where DNS is hosted. Inspect the domain's nameservers in the registrar account, or run:

```powershell
nslookup -type=NS ismailstudio.my 1.1.1.1
```

Names ending in `ns.cloudflare.com` indicate Cloudflare nameservers. Otherwise identify the actual provider from the returned records and account. Do not switch nameservers merely to connect this subdomain, and do not alter existing apex-domain or unrelated service records.

## 4. Associate the custom subdomain when authorised

First open **the correct Pages project → Custom domains → Set up a domain** and enter `rapimotion.ismailstudio.my`. Associate it in Pages before configuring DNS. Cloudflare documents that a DNS record alone can fail to route correctly; see [Pages custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/).

If Cloudflare manages the zone, review the record proposed by Pages and avoid duplicates. If Exabytes or another provider is authoritative, create a CNAME in that provider's DNS interface:

| Field | Value |
|---|---|
| Type | CNAME |
| Name | `rapimotion` (or the FQDN if that interface requires it) |
| Target | The **actual assigned Pages hostname** |
| TTL | Provider default |

Do not invent the target or replace an existing record without checking its purpose. Avoid duplicate zone suffixes and conflicting A/AAAA records. Cloudflare supports an external-DNS subdomain CNAME; moving the parent zone is not required for this subdomain setup.

Check Pages' domain status and run `nslookup -type=CNAME rapimotion.ismailstudio.my 1.1.1.1`. Wait for DNS and certificate provisioning. Open the custom URL over HTTPS without certificate warnings. Verify all five routes and assets at that actual hostname. Certificate issuance, authoritative DNS and domain availability remain unverified until these steps occur.

## 5. Activate production SEO deliberately

Do this only after launch is authorised and the intended HTTPS custom hostname works. From the repository root:

```powershell
py scripts/configure_seo.py --mode production --origin https://rapimotion.ismailstudio.my
py scripts/configure_seo.py --mode production --origin https://rapimotion.ismailstudio.my --check
py scripts/verify_static.py
git diff
```

The script changes source only; it never commits, pushes, deploys or touches DNS. It updates eight files together:

- Five pages: `index, follow`, unique canonical and matching `og:url`, absolute Open Graph and Twitter image URLs.
- `sitemap.xml`: exactly the five canonical HTTPS routes.
- `robots.txt`: crawling allowed and the production sitemap advertised.
- `_headers`: staging's global `X-Robots-Tag` removed; all security restrictions retained.

Review and deliver those exact files through the then-authorised Git workflow. Check the published HTML and HTTP headers after deployment: no production `noindex`; correct canonical on each page; public social image; correct five-entry sitemap and robots declaration. Confirm `pages.dev` previews stay non-indexed through platform controls/headers; do not assume a production configuration protects every alternate hostname. If redirecting the production Pages hostname to the custom domain, configure and verify that separately after the custom domain works.

To restore staging source, use `py scripts/configure_seo.py --mode staging`, followed by `--check` and review. This restores page and header restrictions, removes canonicals/`og:url`, uses local social paths and empties the unadvertised sitemap. Crawling stays allowed so `noindex` can be read. No misleading LocalBusiness, reviews, address or opening-hours markup is included.

## 6. Launch verification

- Test all five routes in desktop and real mobile browsers, including direct nested-route refresh.
- Check zero missing assets, runtime errors and unwanted horizontal overflow.
- Verify navigation, focus indicators, gallery keyboard dismissal and demo validation.
- Confirm the fictional-business disclosures and genuine ISMAIL destination remain clear.
- Repeat accessibility and performance measurements on hosted HTTPS; local lab results do not prove field performance or WCAG conformance.
- Verify CSP, domain certificates, redirects, staging restrictions and final production SEO from actual responses.

Do not describe the site as deployed, indexed or domain-verified until those observations exist.
