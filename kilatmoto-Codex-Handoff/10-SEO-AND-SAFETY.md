# Indexable fictional site: SEO and compliance rules

## Confirmed intent
The **production** KILAT MOTORWORKS website should be **eligible for search indexing** (user Q15A). This is not guaranteed inclusion in Google results. It must still be unmistakably fictional, not falsely appear to be an actual Malaysian workshop.

## Stage change checklist
1. Keep previews/staging noindex as appropriate. On production, remove `noindex` from all five HTML pages **and from actual Worker HTTP `X-Robots-Tag` headers**, not just historical `_headers` source files.
2. Unique title/meta description per page: brand + fictional portfolio concept context where helpful; actual copy from source and brand voice.
3. Five accurate absolute canonicals under `https://kilatmoto.ismailstudio.my/` corresponding to `/`, `/about/`, `/services/`, `/projects/`, `/contact/`.
4. `og:site_name`, `og:title`, `og:description`, `og:url`, `og:image` and Twitter image use verified host and actual images. Do not ship speculative nonexistent image paths.
5. `robots.txt` crawl-friendly and sitemap absolute five HTTPS links to canonical pages; XML valid UTF-8; avoid promoting old hostname.
6. Check old domain has **no redirect** by choice; avoid duplicate indexable copies where possible: if still available, use old host noindex rather than redirect when technically feasible and approved within migration, without breaking unrelated resources.
7. Use `Organization` / portfolio `CreativeWork` markup only if **accurately describing ISMAIL or an explicitly fictional project**, not falsely asserting KILAT is a real `AutomotiveBusiness` with physical address, reviews, employees, prices, telephone or opening hours.
8. Check mobile parity, alt text, internal links, response status, CSP, content type, sitemap and Search Console validation if genuinely connected.

## Data and claims
- Fictional service demonstrations only, no live quote processing or customer records.
- Do not publish fake driving performance gains, before/after results, guarantees or product certifications.
- Generated images should not imply documented real customer cars, trademark endorsement or actual business premises.
- No analytics/tracking integrations without new explicit approval. Genuine lead capture occurs via external ISMAIL portfolio if supported there.

## Verification hierarchy
Source static scan < local HTTP+browser < live Worker HTTPS headers+browser < search-console indexing confirmation. Report each level separately. Live indexing/clickthrough cannot be inferred from source code.
