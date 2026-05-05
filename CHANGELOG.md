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

---

## Phase 1 review fixes (2026-05-05)

- Sessions DST notation simplified (canonical NY anchors + pointer to dst-handling.md).
- README.md gained a `## Cross-Links During Build` note clarifying that forward refs to later phases are intentional, not bugs.

---

## Phase 2 — Time & Sessions (2026-05-05)

Wrote 28 concept files covering the time-domain layer of the library.

**Added (28 files):**

`04-time-cycles/` (10):
- 90-minute-cycle, macro-times-overview
- macro-time-0050-0110, macro-time-0250-0310, macro-time-0950-1010, macro-time-1350-1410, macro-time-1450-1510
- quarterly-shift-theory, time-of-day-pivots, dst-handling

`10-killzones/` (8):
- killzone-overview, asia-killzone, london-open-killzone, ny-am-killzone, london-close-killzone, ny-pm-killzone
- killzone-times-table, killzone-vs-session

`14-asian-range/` (6):
- asian-range, asian-range-high, asian-range-low, asian-range-sweep, asian-session-bias, asian-range-projections

`13-judas-swing/` (4):
- judas-swing, london-judas-swing, ny-judas-swing, judas-swing-failure

**Updated:**
- `INDEX.md` — replaced Phase-2 placeholders with 28 real entries.
- `TIMELINE.md` — backfilled 2018, 2022, 2023 sections; added 2025 macro/QT refinement entries.

**Phase 1 forward refs that now resolve:**
- All session files' references to `dst-handling`, `killzone-overview`, `asia-killzone`, etc.
- All liquidity files' references to `judas-swing`, `asian-range`.

**Phase 2 forward refs to Phases 3–6 still pending:**
- silver-bullet-* (Phase 5), power-of-three / accumulation/manipulation/distribution-phase (Phase 5)
- bullish-fvg / bearish-fvg / fair-value-gap (Phase 4)
- ipda-definition (Phase 3), htf-bias-framework (Phase 6)
- ote-overview (Phase 3), pd-array-* (Phase 3)
- london-close-reversal / ny-pm-reversal (Phase 6)

**Cumulative: 63 / ~210 concept files = 30%.**
