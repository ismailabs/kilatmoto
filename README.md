# RAPI MOTION — Your Drive. Refined.

A five-page automotive detailing portfolio concept by [ISMAIL](https://www.ismailstudio.my/). RAPI MOTION is fictional: services, studio imagery, vehicle stories and enquiries are demonstrations. There is no operating workshop, booking service, price list or customer record.

Source repository: [ismailabs/rapi-motion](https://github.com/ismailabs/rapi-motion). Intended future domain: `https://rapimotion.ismailstudio.my/`. Hosting and DNS are not configured by this delivery.

## Preview on Windows

Double-click **`preview.cmd`**, then open **http://localhost:8000/**. Keep its terminal open; press Ctrl+C to stop. Python 3 is needed for local preview only.

Alternatively, open PowerShell in this folder and run:

```powershell
py scripts/serve.py
```

If `py` is unavailable, use `python scripts/serve.py`. If port 8000 is busy, use `py scripts/serve.py --port 8002` and open http://localhost:8002/. The included server serves the repository root regardless of your terminal directory, applies the site's global security headers, blocks dotfiles and directory listings, and binds only to this computer.

A basic fallback, **run from the project root**, is `py -m http.server 8000 --bind 127.0.0.1`. It serves the same pages but does not emulate Cloudflare headers. Double-clicking `index.html` is not supported: `/assets/` and clean page routes need an HTTP origin. No assets need to be downloaded during normal use.

## Pages and features

| Route | Content |
|---|---|
| `/` | Cinematic introduction, care philosophy, services, process, three project concepts, FAQs |
| `/about/` | Fictional studio philosophy, assessment principles and care workflow |
| `/services/` | Six services with inclusions, suitability, limitations, selection guidance and FAQs |
| `/projects/` | Six fictional studies, six focus filters, care disclosures and keyboard image viewer |
| `/contact/` | Local-only enquiry validation, location concept, FAQs and genuine ISMAIL link |

The mobile menu supports keyboard opening, Escape and focus restoration. FAQs and service details use native HTML disclosures. Gallery links open the image normally without JavaScript; supported browsers enhance them with a native modal. Filters appear only once active; all six projects remain available without JavaScript. Motion is restrained and reduced-motion preferences are respected.

The enquiry deliberately has **no `<form>`, submission endpoint, network call or browser storage**. Its button checks required values and email syntax in the current tab, focuses invalid fields, then announces: “No enquiry has been submitted, sent or saved.” Use sample information. Nothing is booked. The real business enquiry pathway is the separate ISMAIL portfolio link.

## Structure and editing

```text
index.html                 Home
about/index.html           About
services/index.html        Services
projects/index.html        Projects
contact/index.html         Contact demo
assets/css/styles.css      Shared tokens, components and responsive layouts
assets/js/main.js          Progressive navigation, filters, viewer and demo validation
assets/images/             Local WebP editorial artwork
assets/fonts/              Space Grotesk display font and OFL licence
assets/icons/              Identity artwork
favicon.svg, og-image.webp Brand and social assets
_headers                   Cloudflare security and staging indexing policy
robots.txt, sitemap.xml     Explicit SEO lifecycle outputs
preview.cmd                Beginner-friendly Windows preview
scripts/serve.py            Optional local preview helper
scripts/verify_static.py    Structural, safety, SEO and HTTP checks
scripts/configure_seo.py    Explicit staging/production source configuration
qa-screenshots/             Actual HTTP browser screenshots and compact evidence
```

Edit content directly in the five standalone HTML files. No generator or build is needed. Shared navigation and footer are intentionally materialised in each page; update all five together. Change palette, spacing and breakpoints in the CSS. Display type uses local Space Grotesk; body copy uses the system Arial/sans-serif stack. Change behaviour only in `main.js`.

Service IDs (`exterior`, `interior`, `paint`, `ceramic`, `wheels`, `maintenance`) must agree with contact select values and service CTA query strings. Project `data-category` values must agree with filter button values. Preserve the SEO marker comments in each document. Record any replacement image's rights and origin in [ASSET-MANIFEST.md](ASSET-MANIFEST.md).

## Verify and prepare for launch

```powershell
py scripts/verify_static.py
py scripts/verify_static.py --base-url http://127.0.0.1:8000
py scripts/configure_seo.py --mode staging --check
node --check assets/js/main.js
```

Node is optional for JavaScript syntax checking; it is not a production dependency. Python checks use only its standard library.

The delivered source is **staging / noindex**. Crawling is allowed so search engines can read the restriction. There are no production canonicals, no advertised sitemap and no claims that the intended hostname is active. The production transition writes unique canonicals, absolute social URLs, five sitemap entries and production robots/headers together. Follow [DEPLOYMENT.md](DEPLOYMENT.md) only after launch is authorised.

See [QA.md](QA.md) for actual measurements, browser coverage and limits. Physical devices, Safari/Firefox, screen-reader conformance, hosted headers, public indexing and field Core Web Vitals require later verification. No analytics or conversion rates are claimed. Future measurement could examine service exploration, filter use and ISMAIL click-through, subject to a separate privacy-conscious instrumentation decision; no tracking is installed.
