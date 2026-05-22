# Lint Report: 2026-05-21

**Type:** meta
**Scope:** full vault (228 markdown files: 226 concepts + 11 root + 1 `99-glossary/README.md`)
**Tooling:** `.lint-tmp/lint.py` (markdown-link resolver + header parser)
**Status:** developing

---

## Summary

| Check                       | Count | Severity      |
|-----------------------------|------:|---------------|
| Pages scanned               |   238 | —             |
| Orphan pages                |     0 | —             |
| Dead links                  |     1 | low (template) |
| Frontmatter gaps            |     0 | —             |
| Empty sections              |     9 | informational (structural pattern, not defects) |
| Stale-claim candidates      |   173 | informational |
| Cross-reference gaps        |     6 | review        |
| INDEX.md broken refs        |     0 | —             |
| GLOSSARY.md broken refs     |     0 | —             |
| Concepts missing from INDEX |     0 | —             |
| Address validation          |  skip | DragonScale not in use |
| Semantic tiling             |  skip | helper script not present |

Net assessment: the vault is in **strong** shape. The only true defect is one placeholder link in `TEMPLATE.md`. Everything else is either structurally intentional (empty-section false positives) or low-priority polish.

---

## Vault Layout Notes

This vault does NOT use the canonical `wiki/` structure assumed by the lint skill. It uses:

- Concept pages under `concepts/NN-topic/<slug>.md` (226 files).
- Root navigation files: `INDEX.md`, `GLOSSARY.md`, `TIMELINE.md`, `READING-ORDER.md`, `SOURCES.md`, `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `AGENTS.md`, `TEMPLATE.md`, `log.md`.
- Links are markdown relative links (`[text](../foo/bar.md)`), **not** `[[wikilinks]]`.
- Frontmatter is a bolded-key header block (`**Category:** ...`), **not** YAML.

The lint script was adapted to these conventions. Address validation (DragonScale Mechanism 2) and semantic tiling (Mechanism 3) are opt-in and skipped — no `.vault-meta/`, `scripts/allocate-address.sh`, or `tiling-check.py` present.

---

## Orphan Pages

**None.** Every concept page has at least one inbound markdown link from INDEX.md, a sibling concept, or a root file. The Karpathy LLM-Wiki pattern is holding.

---

## Dead Links

One dead link, in the template (intentional placeholder):

- `TEMPLATE.md` → `../<dir>/<file>.md` — placeholder text from the template's "Related Concepts" example. Not a real defect; this line documents the link format for contributors.

**Suggested action:** rewrite the placeholder so it doesn't parse as a link (e.g., backtick-quote it: `` `[Related Concept](../<dir>/<file>.md)` ``). Optional. Cosmetic.

---

## Frontmatter Gaps

**None.** All 226 concept files carry the required header block: `Category`, `Aliases`, `ICT Confidence`, `Year Introduced`, `Year Refined`, `Source IDs`, `Tags`. (`99-glossary/README.md` is a per-folder README and was excluded from the check.)

---

## Empty Sections

9 hits, all in `*-vs-*` disambiguation pages and all **structurally intentional false positives**:

| Page                                                              | Heading                  |
|-------------------------------------------------------------------|--------------------------|
| `concepts/01-market-structure/mss-vs-choch.md`                    | `## Formal Criteria`     |
| `concepts/06-fair-value-gaps/liquidity-void-vs-fvg.md`            | `## Formal Criteria`     |
| `concepts/07-order-blocks/order-block-vs-supply-demand.md`        | `## Formal Criteria`     |
| `concepts/08-breaker-blocks/breaker-vs-mitigation.md`             | `## Formal Criteria`     |
| `concepts/15-sessions/session-vs-killzone.md`                     | `## Formal Criteria`     |
| `concepts/21-crt/crt-vs-amd.md`                                   | `## Formal Criteria`     |
| `concepts/24-amd-cycle/amd-vs-po3.md`                             | `## Formal Criteria`     |
| `concepts/26-imbalance/imbalance-vs-fvg.md`                       | `## Formal Criteria`     |
| `concepts/28-fibonacci-levels/fib-vs-ote.md`                      | `## Formal Criteria`     |

Each `## Formal Criteria` has H3 subheadings underneath (e.g., `### CHoCH`, `### MSS`) that carry the content. The H2 itself is a container. The lint script considers a heading "empty" if no text sits between it and the next heading; this pattern is intentional for two-sided comparison pages.

**Suggested action:** none. Pattern is correct for disambiguation files. If you want to silence the linter, add a one-line lead-in under each `## Formal Criteria` ("The two definitions diverge as follows:") — purely cosmetic.

---

## Stale-Claim Candidates

173 concept pages have `Year Refined: 2022` or `2023`. This is **informational only** and **expected** — most ICT terminology was established in those years and has not been refined since. The 2024-2026 refinement layer is captured in a smaller set of dedicated pages (e.g., `silver-bullet-formalized-2025`, `quarterly-shift-2025`, `static-drawdown-2026`, `fomc-two-stage-delivery`, `zircon-model`).

**Suggested action:** none for now. Reconsider only if you discover a specific 2025/2026 source that contradicts a 2022-dated page — then bump `Year Refined` and update the affected section. Examples worth a future audit pass:

- `concepts/06-fair-value-gaps/fvg-mitigation.md` (Year Refined 2022) — should it reflect the 2025 CE-as-primary-entry shift already captured in `ce-as-primary-entry.md` and `mitigation-of-fvg.md`?
- `concepts/07-order-blocks/order-block-criteria.md` (Year Refined 2022) — should it cross-reference the 2023 reversal/continuation OB distinction?
- `concepts/22-quarterly-theory/quarterly-theory-overview.md` (Year Refined 2023) — should it forward-pointer to `quarterly-shift-2025.md`?

These are not defects — they are candidates for a future "refresh pass," not for today's lint.

---

## Cross-Reference Gaps

Six concept-mention-without-link patterns were detected. Most are noise (the source page already links to a sibling or variant of the target). Reviewing case by case:

| Target page                                              | Mentioning-but-not-linking | Verdict |
|----------------------------------------------------------|---------------------------:|---------|
| `concepts/11-silver-bullet/silver-bullet-overview.md`    | 15 pages | likely false positive — pages link to specific SB variants (london/ny-am/ny-pm/rules) instead of overview |
| `concepts/14-asian-range/asian-range.md`                 | 11 pages | likely false positive — pages link to `asian-range-high`/`-low`/`-sweep` instead |
| `concepts/13-judas-swing/judas-swing.md`                 | 10 pages | likely false positive — pages link to `london-judas-swing` or `ny-judas-swing` instead |
| `concepts/07-order-blocks/order-block-criteria.md`       |  8 pages | likely false positive — pages link to `bullish-order-block`/`bearish-order-block` instead |
| `concepts/20-turtle-soup/turtle-soup.md`                 |  2 pages | review |
| `concepts/06-fair-value-gaps/fair-value-gap.md`          |  1 page  | review |

The 4 high-count rows reflect a deliberate linking pattern: pages link to the most specific variant rather than the umbrella concept. That's good practice; the lint heuristic just doesn't model it. The 2 low-count rows are worth a manual look:

- [`concepts/29-stop-runs/stop-run-into-fvg.md`](../concepts/29-stop-runs/stop-run-into-fvg.md) mentions "turtle soup" — consider adding `[turtle-soup](../20-turtle-soup/turtle-soup.md)` cross-link.
- [`concepts/31-models/diamond-pattern.md`](../concepts/31-models/diamond-pattern.md) mentions "turtle soup" — consider adding the same cross-link.
- [`concepts/13-judas-swing/judas-swing.md`](../concepts/13-judas-swing/judas-swing.md) mentions "fair value gap" — consider adding `[fair-value-gap](../06-fair-value-gaps/fair-value-gap.md)` cross-link.

**Suggested action:** ask before fixing. None of these are defects; they are link-density polish suggestions.

---

## INDEX / GLOSSARY Validation

- **INDEX.md:** 227 internal `(concepts/...)` references, **all resolve.** All 226 concept files are listed.
- **GLOSSARY.md:** 50 internal `(concepts/...)` references, **all resolve.**
- **No stale entries** pointing to renamed or deleted pages.
- **README.md** claims "226 concept files" — matches actual count (`find concepts -name "*.md" -not -name "README.md" | wc -l` → 226). Not stale.

---

## Naming Conventions

This vault uses kebab-case filenames (e.g., `silver-bullet-overview.md`), not the Title-Case-with-spaces convention referenced by the wiki-lint skill. The vault's chosen convention is **internally consistent** across all 226 concept files. Folder naming (`NN-topic-name`) is also consistent.

No mixed conventions detected. No rename needed.

---

## DragonScale Mechanisms (skipped)

- **Address Validation (Mechanism 2):** skipped — `scripts/allocate-address.sh` and `.vault-meta/address-counter.txt` absent. Vault has not adopted DragonScale addressing.
- **Semantic Tiling (Mechanism 3):** skipped — `scripts/tiling-check.py` absent. Not enabled.

These are opt-in features. Skipping them is the documented behavior.

---

## Before Auto-Fixing

**Nothing is safe to auto-fix without confirmation.** All findings are either:

1. Structural patterns the lint heuristic does not model (empty sections, xref gaps to variants).
2. Informational stats (stale-claim candidates).
3. A single intentional placeholder (template dead link).

If you want, I can:

- (a) Patch the `TEMPLATE.md` placeholder to be a code-fenced example (1 line edit).
- (b) Add the three specific cross-links flagged in the xref-gap "review" section (3 file edits).
- (c) Add one-line lead-ins under the 9 `## Formal Criteria` headings in disambiguation pages to silence the lint heuristic (9 file edits, purely cosmetic).

None of (a)/(b)/(c) is necessary. Vault is publication-ready as-is.
