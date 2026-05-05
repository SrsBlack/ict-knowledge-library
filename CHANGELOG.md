# Changelog

Append-only log of phases shipped. Each phase = one commit, one entry here.

---

## Phase 0 — Meta scaffolding (2026-05-05)

Seeded all root cross-cutting files and refined the concept-file template.

**Added:**
- `GLOSSARY.md` — alphabetical abbreviation index (BSL, SSL, FVG, IFVG, CE, OB, BB, MSS, BOS, CHoCH, IPDA, OTE, PD, IRL, ERL, DOL, NDOG, NWOG, AMD, PO3, BPR, BISI, SIBI, EQH, EQL, SMT, CRT, FOMC, NFP, SD, SMC, MMBM, MMSM, TDO, TWO, HTF, LTF, HOD, LOD, R, DST, TF, APD).
- `TIMELINE.md` — year-by-year skeleton 2016 → 2026 with 2025 / 2026 entries pre-populated for known concepts (Venom, Zircon, FOMC two-stage, advanced liquidity, static drawdown).
- `READING-ORDER.md` — Beginner / Intermediate / Advanced tracks with full file ordering.
- `SOURCES.md` — canonical citation index with stable IDs (ICT-2016 → ICT-2026, X-ICT, community sources).
- `CONTRIBUTING.md` — hard rules, required fields, confidence-field guide.
- `CHANGELOG.md` — this file.

**Refined:**
- `TEMPLATE.md` — added required top-matter fields (`ICT Confidence`, `Year Introduced`, `Year Refined`, `Source IDs`); added `## Machine-Readable` JSON block section; added optional `## ICT vs Community` section.
- `INDEX.md` — referenced new root files; concept entries remain `(pending)` until Phase 1+.

**Deferred to later phases:**
- Concept-file content for all 33 topic directories (~210 files).
- 99-glossary deep-dive abbreviation files.
- TIMELINE.md backfill for 2016–2024 (filled per-phase as concepts are written).

---

## Phase 1 — Foundations (2026-05-05)

Wrote the 35 foundational concept files referenced by every later phase.

**Added (35 files):**

`01-market-structure/` (12):
- swing-high, swing-low, internal-structure, external-structure
- bos-bullish, bos-bearish, choch-bullish, choch-bearish
- mss, mss-vs-choch, range-expansion, range-contraction

`02-liquidity/` (14):
- buy-side-liquidity, sell-side-liquidity, equal-highs, equal-lows
- trendline-liquidity, liquidity-pool, liquidity-void
- liquidity-sweep, liquidity-run
- internal-range-liquidity, external-range-liquidity, draw-on-liquidity
- liquidity-matrix, relative-equal-highs-lows

`15-sessions/` (9):
- session-overview, asia-session, london-session, ny-am-session
- ny-lunch, ny-pm-session, london-close, session-overlaps, session-vs-killzone

**Updated:**
- `INDEX.md` — replaced Phase-1 placeholders with real entries (35 lines).
- `TIMELINE.md` — backfilled 2016, 2017, 2018, 2021, 2022 sections with concept references.

**Conventions established (will be followed by all later phases):**
- Every file has all required top-matter fields filled.
- Every file has the `## Machine-Readable` JSON block with `id` matching filename.
- Every file cites at least one SOURCES.md ID in `**Source IDs:**`.
- Every file's `## Related Concepts` section uses real `(../path/file.md)` links so Phase 8 link-check has real targets to verify.
- Disambiguation pages (`mss-vs-choch.md`, `session-vs-killzone.md`) use `## Definition` to state the containment relationship up front.
