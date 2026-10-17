# KILAT MOTORWORKS → Codex handoff | Start here

**Deliverable:** actual design/audit/asset package, not the finished/deployed website. Prepared **17 October 2026**.

## The naming contract — never substitute
- **Customer-facing display brand:** `KILAT MOTORWORKS` (not “KILAT MOTO”).
- **GitHub:** rename the **existing** `ismailabs/rapi-motion` to **`ismailabs/kilatmoto`**, preserving Git history.
- **Cloudflare Worker:** new intended Worker/service name **`kilatmoto`**. Audit and migrate from currently connected `rapimotion` Worker, not a hypothetical Pages project.
- **Production domain:** **`https://kilatmoto.ismailstudio.my/`**.
- **Old domain:** `https://rapimotion.ismailstudio.my/`; user explicitly chose **no redirect**. Do not configure a redirect, and do not delete unrelated DNS. Document final old-host behaviour truthfully.
- **Real client-conversion destination:** `https://ismailstudio.my/` (verify actual working canonical destination); do not generate fake enquiries.

## Windows / Codex procedure
1. Obtain or use the EXISTING local Git clone of `https://github.com/ismailabs/rapi-motion` (do not initialize a new repository or overwrite files).
2. Extract this **entire** `kilatmoto-Codex-Handoff/` folder into the repository **beside** `index.html`, `.gitignore`, `services/`, and `assets/`. This folder is a brief, not a replacement website.
3. Open VS Code/Codex **in the repository root**. Open `kilatmoto-Codex-Handoff/PASTE-INTO-CODEX.txt` and paste it into Codex.
4. Codex reads all documents, references and images in this folder, implements actual site changes **in repository files outside the handoff**, tests, renames repo, migrates Cloudflare Worker/domain, and verifies production.
5. Give Codex connected GitHub/Cloudflare permissions when required. Autonomy means **no routine interruptions**, not bypassing authentication or platform-enforced permissions.

## Reading order
1. `01-REQUIREMENTS.md`, `02-REPOSITORY-AUDIT.md`, `03-INFRASTRUCTURE-STATE.md`
2. `04-ART-DIRECTION.md`, `05-DESIGN-SYSTEM.md`, `06-PAGE-SPECIFICATIONS.md`, `07-CONTENT-AND-CONVERSION.md`
3. Visual references `design/implementation-mockups/`, concept options `design/concept-boards/`, runtime-ready `assets/photos/` and `assets/brand/`
4. `08-IMPLEMENTATION.md`, `09-MIGRATION-RUNBOOK.md`, `10-SEO-AND-SAFETY.md`
5. `11-QUALITY-GATES.md`, `12-CODEX-GOAL-CONTRACT.md`, `16-RELEASE-REPORT.md`

## What is and isn't done
**Done here:** source repository read-only audit, connected Cloudflare read-only inventory, original AI-generated concept boards and photos, authored brand SVGs and accurate brand desktop/mobile implementation-reference mockups, detailed specs, acceptance checklist and ZIP validation. **Not done:** edits to website repository, GitHub rename, domain/DNS changes, Cloudflare Worker deployment, live production browser/a11y/performance QA. A URL lookup of `https://rapimotion.ismailstudio.my/` could not retrieve page content; do not claim the current public render was tested. Details in `14-EXECUTION-STATUS.md`.

**Do not copy visual-concept mockups' invented statistics, fake contact forms, slogans, service claims or alternate brand text.** The two experimental boards labelled `KILAT MOTO` are **non-authoritative** illustration references only. Use `KILAT MOTORWORKS` everywhere visible and the precise fixed route/content contract.
