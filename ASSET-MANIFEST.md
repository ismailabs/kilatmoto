# RAPI MOTION — local asset record

All runtime assets are local. Automotive images are fictional generated editorial artwork, never evidence of actual staff, premises, customer work, treatment results or before/after transformations. No image hotlinks, manufacturer logos or external runtime fonts are required.

## New artwork, 15 October 2026

Created with the built-in OpenAI image-generation tool, inspected, then converted to WebP with Pillow. Large generated PNG sources remain outside the delivery; the deployable derivatives below are in the repository.

| Path under `assets/images/` | Prompt / art direction | Use |
|---|---|---|
| `studio-hero.webp`, `studio-hero-800.webp` | Wide premium Malaysian detailing studio; unbranded black sedan in front three-quarter view on the right; geometric white ceiling lights; neutral black/silver palette; dark space on the left; realistic anatomy; no logos, text or UI | Home hero, About studio illustration, Contact backdrop, closing editorial image |
| `care-studio.webp`, `care-studio-800.webp` | Adult Malaysian male in plain black polo and gloves, carefully wiping a glossy black hood with folded grey microfiber; natural skin and hands; neutral workshop lighting; no logos, badges, text or UI | About hero; CSS mirrors it to keep the person clear of the copy |
| `interior-care.webp` | Modern unbranded family-car cabin, black leather texture and stitching, center console and dashboard; soft daylight and white workshop lights; credible geometry; no people, logos or text | Interior Reset cards |

The hero is 1536 × 1024 with an 800px responsive derivative. About has matching width variants. The interior card image is reduced to 800px width. Exact dimensions are recorded in HTML; decorative CSS crops use stable section dimensions. New images are illustrative; the person is not represented as an employee.

`og-image.webp` is a 1200 × 630 social composition of the new studio artwork, the RAPI MOTION identity, tagline and explicit fictional-portfolio label. It was composed locally with the shipped display font. Staging uses a local path; the production SEO script writes absolute social URLs.

## Retained supplied artwork

The original package's manifest records OpenAI-generated artwork and Pillow crops. That provenance is inherited from the supplied project, not independently reconstructed from original generation records.

| Assets | Recorded origin / current role |
|---|---|
| `project-urban.webp`, `project-executive.webp`, `project-family.webp` | Crops from the supplied silver hatchback / dark sedan / olive SUV composite; fictional project collection |
| `project-coupe.webp`, `project-daily.webp`, `project-electric.webp` | Crops from the supplied red coupe / silver sedan / electric crossover composite; fictional project collection |
| `detail-protection.webp`, `detail-wheel.webp` | Supplied electric-crossover and wheel crops; service illustrations |
| `hero-rapi.webp`, `editorial-reflections.webp`, `detail-exterior.webp`, `detail-glass.webp`, `detail-maintenance.webp`, `detail-paint.webp` | Retained original source-package derivatives; currently unused by the runtime pages |

Hatchback and coupe artwork was recompressed for this revision. The Family SUV project image illustrates vehicle type; it is not a photograph of an interior treatment. New interior imagery is used on the actual Interior Reset service cards.

## Identity and typography

- `favicon.svg`: new original light `r` and lime point on charcoal, drawn in SVG.
- `assets/icons/wordmark-dark.svg`, `wordmark-light.svg`: original reusable identity lockups. The live header uses selectable HTML text and local display typography; these SVG variants are supporting assets using system Arial.
- `assets/icons/mark.svg`, `grid.svg`, `spark.svg`: retained supplied original vector artwork, currently unused.
- `assets/fonts/space-grotesk.ttf`: Space Grotesk 700, downloaded from Google's font service; distributed under SIL Open Font License 1.1. The accompanying `OFL.txt` was retrieved from [Google Fonts' Space Grotesk directory](https://github.com/google/fonts/tree/main/ofl/spacegrotesk). Body copy uses system Arial/Helvetica/sans-serif. No remote font request occurs when viewing the website.

## Evidence

`qa-screenshots/` contains captures of the implemented pages served over local HTTP. These are evidence, not runtime assets or design mockups. JPEG captures are converted to WebP without altering the rendered content. See `QA.md` for viewport dimensions, methods and remaining verification limits.

For future replacements, verify the source and usage rights, store the asset locally, update alt text and dimensions, and record its provenance here.
