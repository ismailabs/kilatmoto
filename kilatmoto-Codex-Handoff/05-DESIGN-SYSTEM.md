# Implementation-ready visual system

## Foundational palette (proposed design tokens, adjustable for tested contrast)
| Token | Hex | Usage |
|---|---|---|
| `--canvas` | `#0A0D0C` | Page background |
| `--surface` | `#131716` | Card surfaces |
| `--surface-raised` | `#1A211D` | Overlays, focused components |
| `--ink` | `#F4F5F0` | Primary on-dark text |
| `--muted` | `#B1B9B0` | Muted content (verify WCAG contrast) |
| `--signal` | `#CDF228` | Primary action and small display accent |
| `--signal-dark` | `#263500` | Text on signal backgrounds, if contrast permits |
| `--bronze` | `#BD8B57` | Restrained warm editorial highlights, not primary body text |
| `--border` | `#39423C` | Delicate dividers |

Use semantic functional tokens for hover, focus, invalid, success and disabled states; verify actual contrast with the rendered background. Avoid relying only on lime colour for state.

## Typography
- Display: strong geometric condensed-feel sans with local licensed fallback; source already has a local Space Grotesk font and OFL licence. Codex may retain it or add a properly licensed and documented complementary display font. No external runtime font dependencies.
- H1 desktop 72–108px fluid clamp; mobile 42–56px fluid; paragraph 16–19px. Avoid fixed huge text at narrow widths and 200% zoom.
- Heading line-height approx 0.94–1.05 where safe; body 1.55–1.7. Visual hierarchy never depends on decorative uppercase tracking alone.

## Layout
- Content width 1240–1360px max with ~24–64px adaptive sides; use dynamic `clamp()` gutter; prevent text line width > ~75ch.
- Breakpoints are dictated by content rather than guessed devices. Validate 320, 375, 390, 430, 768, 1024, 1440, 1920 widths and 200% text enlargement.
- 12-column desktop grid; cards generally 3 across large desktop, 2 across tablet, 1 on narrow phones. Never let minimum widths force sideways scrolling.
- Hero: 64–85svh desktop, ~78–95svh mobile cap only when readable; avoid trapping CTA below fold on short landscape phones.
- Use 8px scale with visual rhythm (8, 12, 16, 24, 32, 48, 64, 96), but respect actual content lengths.

## Interactions
- Motion intensity: restrained premium. Image parallax only if performant and nonessential; fade/translate reveals 8–16px and 220–500ms; disable meaningful nonessential motion on prefers-reduced-motion.
- Native links with clear destinations; buttons only for actions. On mobile offer 44px-ish targets and clear current page state.
- Distinguish the **demo enquiry** from real ISMAIL business contact via explicit explanatory copy and no network send.
- Keyboard menu: aria-expanded, Escape close, focus restoration, logical Tab traversal and breakpoints. Gallery: proper dialog labeling, contained focus, Escape and return focus; no-JS linked full-size images.
- Project filters: user-operable buttons, selection status, count announcement, stable content order; progressive enhancement so all six concepts are visible with JS disabled.
- Service cards: visible link affordance and descriptive image alt; preserve deep links to source service IDs.

## Actual asset placement
- Hero desktop: `assets/photos/hero-vehicle-1600.webp` with responsive source and thoughtful crop. On mobile consider `hero-vehicle-mobile-900.webp`.
- Paint correction: `assets/photos/paint-correction-1200.webp`.
- Wheel and protective treatments: `assets/photos/wheel-detail-1200.webp`.
- Source existing six project images can stay if necessary, but confirm provenance and optimize.
- Logo candidates in `assets/brand/` are original local editable SVGs. Do not transform into third-party vehicle brand marks.

## Exact text on implementation-reference mockups
Accurate brand: `KILAT MOTORWORKS`. Service labels must match `data/six-service-contract.json`; avoid invented 100% satisfaction and 500+ projects. Narrative samples are concept copy, not real business claims.
