---
type: meta
title: "Hot Cache"
updated: 2026-05-21
---

# Recent Context

## Last Updated

2026-05-21. Vault adopted the `wiki` skill operations vocabulary by adding a thin `CLAUDE.md` mapping the existing layout (root files + `concepts/NN-topic/`) to the canonical scaffold (`wiki/index.md`, `wiki/log.md`, etc.). No content moved; the deviation is documented so external readers know `INDEX.md` ≡ `wiki/index.md` and `meta/hot.md` ≡ `wiki/hot.md`. A full lint pass ran the same day: 0 orphans, 0 dead links (except 1 intentional template placeholder), 0 frontmatter gaps, INDEX↔disk fully aligned.

## Key Recent Facts

- Vault is publication-ready. 226 concept files across 33 numbered domain folders, all conforming to TEMPLATE.md.
- Schema lives in [AGENTS.md](../AGENTS.md). The new [CLAUDE.md](../CLAUDE.md) is a thin pointer + skill-vocabulary map; do not duplicate the schema there.
- Lint pass recorded at [lint-report-2026-05-21.md](lint-report-2026-05-21.md). 9 "empty section" hits are structural false positives in `*-vs-*` disambiguation pages, not defects.
- Layout deviates from the canonical wiki-skill scaffold: kebab-case filenames, markdown relative links (no `[[wikilinks]]`), bold-key headers (no YAML frontmatter), no `wiki/` wrapper folder. Deliberate; documented in `CLAUDE.md`.
- 173 concept pages have `Year Refined: 2022` or `2023`. Informational only — ICT terminology mostly stabilised in those years; 2024-2026 refinements live in dedicated pages (`silver-bullet-formalized-2025`, `quarterly-shift-2025`, `static-drawdown-2026`, `fomc-two-stage-delivery`, `zircon-model`).

## Recent Changes

- Created: [CLAUDE.md](../CLAUDE.md) — wiki-skill operations map and layout-deviation note.
- Created: [meta/lint-report-2026-05-21.md](lint-report-2026-05-21.md) — full vault health check.
- Created: [meta/hot.md](hot.md) — this file. New `meta/` directory established for lint reports + hot cache.
- Unchanged: all 226 concept files, all root navigation files. Content has not been touched.

## Active Threads

- Decision pending: whether to point the `obsidian-vault` MCP server at this repo (currently it targets `C:/Users/User/claude-obsidian`).
- Optional polish flagged in lint report (none required): TEMPLATE.md placeholder code-fencing, 3 cross-link additions (turtle-soup × 2, fair-value-gap × 1), 9 cosmetic lead-ins under `## Formal Criteria` in disambiguation pages.
- Future refresh-pass candidates: `fvg-mitigation.md`, `order-block-criteria.md`, `quarterly-theory-overview.md` — would benefit from explicit forward-pointers to 2025 refinement pages.
