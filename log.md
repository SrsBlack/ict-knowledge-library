# Log

Chronological, append-only record of activity on this wiki — ingests, queries, lint passes, structural changes. Each entry starts with `## [YYYY-MM-DD] <kind> | <short title>` so the log is parseable with `grep "^## \[" log.md | tail -10` for the last 10 entries.

Per the Karpathy LLM Wiki pattern, this file complements [`INDEX.md`](INDEX.md) (content-oriented, alphabetical-ish catalog) — `log.md` is **time-oriented**, the wiki's history.

---

## [2026-05-05] structural | initial scaffold

Repo initialized. Created concept directory tree (33 directories), `TEMPLATE.md`, `README.md`, `INDEX.md` skeleton.

→ commit `e78acd4`

## [2026-05-05] structural | phase 0 meta scaffolding

Built out the 6 root cross-cutting files: `GLOSSARY.md`, `TIMELINE.md`, `READING-ORDER.md`, `SOURCES.md`, `CONTRIBUTING.md`, `CHANGELOG.md`. Refined `TEMPLATE.md` with required top-matter fields + machine-readable JSON block + ICT vs Community section.

→ commit `6086c0e` (+ review fixes `c930bd8`)

## [2026-05-05] ingest | phase 1 — foundations

Wrote 35 concept files: `01-market-structure/` (12) + `02-liquidity/` (14) + `15-sessions/` (9). All Phase 1 files validated: 10 sections, JSON parse, id-match. Updated INDEX, TIMELINE backfill 2016/2017/2018/2021/2022.

→ commit `bb22e31` (+ review fixes `c0a65ee`)

## [2026-05-05] ingest | phase 2 — time & sessions

Wrote 28 files: `04-time-cycles/` (10) + `10-killzones/` (8) + `14-asian-range/` (6) + `13-judas-swing/` (4). Cumulative: 63 files.

→ commit `f68c7a5` (+ review fixes `b4aa89d`)

## [2026-05-05] ingest | phase 3 — PD arrays core

Wrote 33 files across 6 dirs (PD arrays, imbalance, equilibrium, fib levels, OTE, IPDA foundation). Cumulative: 96 files.

→ commit `8a71931` (+ review fixes `2933468`)

## [2026-05-05] ingest | phase 4 — FVG / OB / breakers

Largest single phase: 40 files (FVG 14 + OB 10 + breakers 6 + mitigation 5 + rejection 3 + displacement foundation 2). Cumulative: 136 files.

→ commit `c25affa` (+ review fix `cd866cd`)

## [2026-05-05] ingest | phase 5 — models & strategies

Wrote 30 files (silver-bullet 7 + PO3 6 + AMD 4 + turtle-soup 4 + SMT 5 + stop-runs 4). Cumulative: 166 files.

→ commit `ffecbe4` (+ review fix `3df3b6d`)

## [2026-05-05] ingest | phase 6 — bias, named models, risk

Wrote 28 files (htf-bias 7 + 14 named models including Venom + Zircon + risk 7). Cumulative: 194 files.

→ commit `d9327be`

## [2026-05-05] ingest | phase 7 — final content

Wrote 32 files (CRT 4 + quarterly-theory 9 + news-driven 5 + order-flow 6 + displacement remainder 4 + IPDA lookbacks 4). Cumulative: 226 files. **Library content-complete.**

→ commit `b4bc7d7`

## [2026-05-05] lint | phase 8 — final audit

Verification-only pass. Closed 20 timeline gaps. Confirmed: 226 files validated (10 sections, JSON parse, id-match), 0 broken cross-links, 0 orphan source citations, INDEX↔disk fully aligned, TIMELINE 100% coverage. **Library declared ship-ready.**

→ commit `b543976`

## [2026-05-05] lint | final polish

Cleared 4 stale `(pending)` markers in TIMELINE (Phase 7 had left two on shipped 2025 entries; 2019/2020 sections clarified as no-additions years). Replaced `(Phase 8)` placeholder in INDEX 99-glossary section with explanatory note pointing to root `GLOSSARY.md`. All audit checks still pass.

→ commit `8622ceb`

## [2026-05-05] structural | adapt to Karpathy LLM Wiki pattern

Added `log.md` (this file) and `AGENTS.md` schema following the [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern. The library was already 90% aligned with the pattern — `INDEX.md` was already content-oriented per the design — so the adaptation was incremental: explicit log + explicit ingest/query/lint schema for future LLM sessions.

→ commit `abc69ea`

## [2026-05-05] lint | SMC alias coverage

Added Smart Money Concepts (SMC) vocabulary aliases to 4 existing concept files for grep-discoverability. SMC is a community rebrand of ICT material, not its own framework — adding aliases lets SMC users find the right ICT files without claiming ICT authored the SMC framework.

- `bullish-order-block.md` += `demand zone (SMC)`, `demand block (SMC)`
- `bearish-order-block.md` += `supply zone (SMC)`, `supply block (SMC)`
- `liquidity-sweep.md` += `liquidity grab (SMC)`
- `turtle-soup.md` += `fakeout (SMC)`, `swing failure (SMC)`

Both top-matter `**Aliases:**` fields and JSON `aliases[]` arrays updated.

Also extended `GLOSSARY.md` with an "SMC Vocabulary Cross-Reference" section — full mapping table of SMC terms ↔ ICT equivalents + flagged terms that are SMC-only (engulfing block, Wyckoff spring/upthrust) as out-of-scope.

→ this commit
