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

---

## Phase 2 review fixes (2026-05-05)

- `quarterly-shift-theory.md`: day-quarter table conflated 6h wall-clock blocks with named ICT sessions; clarified they're independent. Added Common Mistake.
- `killzone-overview.md`: Asia-KZ midnight-wrap formula had `∪ [00:00, 00:00]` (empty set); replaced with prose.
- `asian-range-sweep.md`: Example 1 had a "Wait —" interjection that read like internal monologue; rewrote as clean ambiguity-resolution example.

---

## Phase 3 — PD Arrays Core (2026-05-05)

Wrote 33 concept files covering the conceptual heart of the library: PD arrays, premium/discount, equilibrium, fibonacci, OTE, and IPDA foundation.

**Added (33 files):**

`05-pd-arrays/` (9):
- pd-array-definition, premium-array, discount-array, dealing-range
- pd-array-hierarchy, pd-array-nesting, htf-pd-array-hierarchy
- pd-array-matrix, pd-array-confluence

`26-imbalance/` (5):
- imbalance-definition, inefficiency, imbalance-vs-fvg, imbalance-rebalance, volume-imbalance-detail

`27-equilibrium/` (4):
- equilibrium-definition, dealing-range-equilibrium, equilibrium-as-decision-point, mean-threshold

`28-fibonacci-levels/` (7):
- ict-fib-overview, fib-62, fib-705, fib-79
- standard-deviation-projections, symmetrical-price-projections, fib-vs-ote

`17-optimal-trade-entry/` (6):
- ote-overview, ote-62, ote-705, ote-79, ote-rules, ote-failure

`23-ipda/` (2 of 6 — foundation only):
- ipda-definition, ipda-data-ranges
- (per-window deep-dives ipda-20-day-lookback / ipda-40-day-lookback / ipda-60-day-lookback / ipda-reference-points deferred to Phase 7)

**Updated:**
- `INDEX.md` — replaced Phase-3 placeholders with 33 real entries (+ a note about Phase 7 IPDA deferred files).
- `TIMELINE.md` — backfilled 2017 (OTE + fib + PD-array vocabulary), 2018 (IPDA + volume-imbalance + symmetrical-projections), 2024 (PD-array nesting), and added 2025 nesting / confluence formalization entry.

**Forward refs that now resolve from earlier phases:**
- All references to `pd-array-definition`, `dealing-range`, `equilibrium-definition`, `consequent-encroachment` (FVG-CE), `fair-value-gap` (still pending Phase 4), `ote-overview`, `ipda-definition`, `htf-pd-array-hierarchy`, `pd-array-nesting`, `quarterly-shift-theory` (already from Phase 2).

**Phase 3 forward refs to Phases 4–6 still pending:**
- bullish-fvg, bearish-fvg, fair-value-gap, inversion-fvg, ce-as-primary-entry, immediate-rebalance-fvg, delayed-rebalance-fvg, fvg-mitigation (Phase 4)
- bullish-order-block, bearish-order-block, breaker-block, order-block-criteria (Phase 4)
- displacement-definition (Phase 4)
- htf-bias-framework, top-down-analysis (Phase 6)
- algorithmic-price-delivery (Phase 7)

**Cumulative: 96 / ~210 concept files = 46%.**

---

## Phase 3 review fixes (2026-05-05)

- `pd-array-confluence.md`: Formal Criteria said "high-confluence has 4+" but Formula/Math said "5-6 = high"; unified.
- `ote-overview.md` Example 1: bad math ("145 pips, R:R 9.7R" should be 220 pips, 14.7R); fixed.

---

## Phase 4 — FVG / OB / Breakers (2026-05-05)

Wrote 40 files across 6 directories — the largest single phase.

**Added (40 files):**

`06-fair-value-gaps/` (14):
- fair-value-gap, bullish-fvg, bearish-fvg, inversion-fvg
- consequent-encroachment, ce-as-primary-entry
- balanced-price-range, volume-imbalance
- immediate-rebalance-fvg, delayed-rebalance-fvg, fvg-classification-2025
- liquidity-void-vs-fvg, fvg-mitigation, nested-fvg

`07-order-blocks/` (10):
- order-block-criteria, bullish-order-block, bearish-order-block
- mitigated-order-block, unmitigated-order-block
- propulsion-block, vacuum-block
- reversal-order-block, continuation-order-block, order-block-vs-supply-demand

`08-breaker-blocks/` (6):
- breaker-block, bullish-breaker, bearish-breaker
- mitigation-block, breaker-vs-mitigation, failed-breaker

`18-mitigation/` (5):
- mitigation-definition, mitigation-of-ob, mitigation-of-fvg
- mitigation-of-breaker, partial-vs-full-mitigation

`19-rejection-blocks/` (3):
- rejection-block, bullish-rejection-block, bearish-rejection-block

`09-displacement/` (2 of 6 — foundation only):
- displacement-definition, displacement-and-fvg
- (4 remaining files deferred to Phase 7)

**Updated:**
- `INDEX.md` — replaced Phase-4 placeholders with 40 entries.
- `TIMELINE.md` — added FVG/OB to 2016, displacement/BPR/blocks/CE/IFVG to 2017-2018, FVG-classification/IFVG-formalized/propulsion re-teach to 2024.

**Phase 1-3 forward refs that now resolve:**
- All references to `fair-value-gap`, `bullish-fvg`, `bearish-fvg`, `inversion-fvg`, `consequent-encroachment`, `ce-as-primary-entry`, `balanced-price-range`, `volume-imbalance`, `immediate-rebalance-fvg`, `delayed-rebalance-fvg`, `fvg-classification-2025`, `liquidity-void-vs-fvg`, `fvg-mitigation`, `nested-fvg`, all OB files, all breaker files, all mitigation files, all rejection-block files, `displacement-definition`, `displacement-and-fvg`.

**Phase 4 forward refs to Phases 5-7 still pending:**
- power-of-three / accumulation/manipulation/distribution-phase / silver-bullet (Phase 5)
- htf-bias-framework, top-down-analysis (Phase 6)
- turtle-soup, stop-run-definition (Phase 5)
- algorithmic-price-delivery (Phase 7)
- ndog / nwog / sunday-open-gap (Phase 6)
- bullish/bearish-displacement, displacement-strength-criteria, gap-classification (Phase 7)
- ipda-20/40/60-day-lookback, ipda-reference-points (Phase 7)

**Cumulative: 136 / ~210 concept files = 65%.**

---

## Phase 4 review fix (2026-05-05)

- GLOSSARY: stripped `(pending)` from 26 entries whose target files have shipped (BB, BISI, BOS, BPR, BSL, CE, CHoCH, DOL, EQH/EQL/ERL, FVG, IFVG, IPDA, IRL, MSS, OB, OTE, PD, PDH/PMH/PWH, SD, SIBI, SSL). Remaining 16 correctly point to Phase 5–7 deferred files.

---

## Phase 5 — Models & Strategies (2026-05-05)

Wrote 30 files across 6 directories — the named-models / setup-strategies layer.

**Added (30 files):**

`11-silver-bullet/` (7):
- silver-bullet-overview, silver-bullet-london, silver-bullet-ny-am, silver-bullet-ny-pm
- silver-bullet-rules, silver-bullet-formalized-2025, silver-bullet-failure-modes

`12-power-of-three/` (6):
- power-of-three, accumulation-phase, manipulation-phase, distribution-phase
- intraday-amd, htf-amd

`24-amd-cycle/` (4):
- amd-cycle-overview, amd-on-htf, amd-on-intraday, amd-vs-po3

`20-turtle-soup/` (4):
- turtle-soup, bullish-turtle-soup, bearish-turtle-soup, stop-hunt-pattern

`16-smt-divergence/` (5):
- smt-divergence, correlated-pairs-smt, index-smt, smt-confirmation, smt-failure

`29-stop-runs/` (4):
- stop-run-definition, stop-run-into-fvg, stop-run-into-ob, stop-run-into-breaker
- (stop-hunt-pattern lives in `20-turtle-soup`; cross-linked from `29-stop-runs`)

**Updated:**
- `INDEX.md` — replaced 6 placeholders with 30 entries.
- `TIMELINE.md` — backfill pending in commit; add 2016 (PO3, AMD) + 2018 (turtle-soup, SMT) + 2022 (silver bullet formalized) + 2025 (SB precision update).

**Phase 5 forward refs that now resolve:**
- All earlier-phase references to `silver-bullet-*`, `power-of-three`, `accumulation-phase`, `manipulation-phase`, `distribution-phase`, `intraday-amd`, `htf-amd`, `turtle-soup`, `bullish/bearish-turtle-soup`, `stop-hunt-pattern`, `smt-divergence`, `stop-run-definition`, `stop-run-into-*`, `amd-cycle-overview`, `amd-vs-po3`, etc.

**Phase 5 forward refs to Phase 6/7 still pending:**
- htf-bias-framework, top-down-analysis, monthly/weekly/daily-bias (Phase 6)
- algorithmic-price-delivery (Phase 7)
- ndog / nwog / sunday-open-gap, london-close-reversal, ny-pm-reversal (Phase 6)
- bullish/bearish-displacement, displacement-strength-criteria, gap-classification (Phase 7)
- ipda-20/40/60-day-lookback, ipda-reference-points (Phase 7)
- candle-range-theory + CRT files (Phase 7, community-attributed)

**Cumulative: 166 / ~210 concept files = 79%.**

---

## Phase 5 review fix (2026-05-05)

- `correlated-pairs-smt.md` Common Mistakes: said "EURUSD vs USDJPY (sometimes inverse) correlation; SMT logic inverts" — but parent `smt-divergence.md` correctly distinguishes weak (unreliable) from strong-negative (inverse SMT applies, e.g. EURUSD vs DXY). Reworded.

---

## Phase 6 — Bias, Named Models, Risk (2026-05-05)

Wrote 28 files across 3 directories — the bias decision system, the named-models layer, and the risk-management discipline.

**Added (28 files):**

`25-htf-bias/` (7):
- htf-bias-framework, monthly-bias, weekly-bias, daily-bias
- bias-confluence, bias-invalidation, top-down-analysis

`31-models/` (14):
- ict-2022-model, ict-2023-model, ict-2024-model
- unicorn-model, bread-and-butter-setup, diamond-pattern
- ny-am-open-range-model, london-close-reversal, ny-pm-reversal
- ndog, nwog, sunday-open-gap
- venom-model (Apr 2025), zircon-model (Jan 2026 demo-stage)

`32-risk-management/` (7):
- risk-per-trade, r-multiple, position-sizing
- stop-placement-by-pd-array, partial-takes
- static-drawdown-2026, correlation-risk

**Updated:**
- `INDEX.md` — replaced 3 placeholders with 28 entries.
- `TIMELINE.md` — backfilled 2017 (HTF bias + risk discipline), 2022 (ICT 2022 Model + named openings/reversals), 2023 (ICT 2023 + Unicorn/B&B/Diamond + NDOG/NWOG/Sunday-gap), 2024 (ICT 2024 Model). Stripped (pending) markers from 2025 Venom and 2026 Zircon/static-DD entries.

**Phase 1-5 forward refs that now resolve:**
- All references to `htf-bias-framework`, `monthly-bias`, `weekly-bias`, `daily-bias`, `bias-confluence`, `bias-invalidation`, `top-down-analysis`, `ict-2022-model`, `ict-2023-model`, `ict-2024-model`, `unicorn-model`, `bread-and-butter-setup`, `diamond-pattern`, `ny-am-open-range-model`, `london-close-reversal`, `ny-pm-reversal`, `ndog`, `nwog`, `sunday-open-gap`, `venom-model`, `zircon-model`, `risk-per-trade`, `r-multiple`, `position-sizing`, `stop-placement-by-pd-array`, `partial-takes`, `static-drawdown-2026`, `correlation-risk`.

**Phase 6 forward refs to Phase 7/8 still pending:**
- algorithmic-price-delivery + 03-order-flow files (Phase 7)
- bullish/bearish-displacement, displacement-strength-criteria, gap-classification (Phase 7)
- ipda-20/40/60-day-lookback, ipda-reference-points (Phase 7)
- candle-range-theory + CRT files (Phase 7, community-attributed)
- 22-quarterly-theory dir extras: yearly/monthly/weekly/daily-quarters, 90-minute-quarters, true-week-open, true-day-open, quarterly-shift-2025 (Phase 7)
- 30-news-driven dir: news-driven-overview, fomc-two-stage-delivery, nfp-protocol, cpi-protocol, news-blackout-rules (Phase 7)

**Cumulative: 194 / ~210 concept files = 92%.**

---

## Phase 7 — Final Content (2026-05-05)

Wrote 32 files closing every remaining content directory. The library is content-complete.

**Added (32 files across 6 dirs):**

`21-crt/` (4 — all community-attributed):
- candle-range-theory, crt-rules, crt-vs-amd, ict-response-to-crt

`22-quarterly-theory/` (9):
- quarterly-theory-overview, yearly-quarters, monthly-quarters, weekly-quarters, daily-quarters
- 90-minute-quarters, true-day-open, true-week-open, quarterly-shift-2025

`30-news-driven/` (5):
- news-driven-overview, fomc-two-stage-delivery, nfp-protocol, cpi-protocol, news-blackout-rules

`03-order-flow/` (6):
- institutional-order-flow, algorithmic-price-delivery
- bullish-order-flow, bearish-order-flow, order-flow-shift, smart-money-footprint

`09-displacement/` (4 remaining):
- bullish-displacement, bearish-displacement, displacement-strength-criteria, gap-classification

`23-ipda/` (4 remaining):
- ipda-20-day-lookback, ipda-40-day-lookback, ipda-60-day-lookback, ipda-reference-points

**Updated:**
- `INDEX.md` — replaced 4 `(Phase 7)` placeholders + 1 `(deferred to Phase 7)` marker; all 33 concept directories now fully indexed.
- `TIMELINE.md` — backfilled 2017 (order-flow + displacement variants + news), 2018 (IPDA lookback expansion + gap-classification), 2023 (Quarterly Theory deep-dives), 2024 (CRT community-attributed), 2025 (Quarterly Shift + FOMC two-stage + CPI).
- `GLOSSARY.md` — stripped final concept-file `(pending)` markers; only the explanatory header reference remains.

**Cumulative: 226 concept files** (exceeded the original ~210 estimate; final count higher because each directory got fuller deep-dive coverage than initially estimated).

**Library content is COMPLETE.**

Phase 8 is the audit pass — no new content, just verification: full link-check, JSON-block consistency, source-citation completeness, INDEX line-by-line vs Glob, TIMELINE coverage. Per build plan §7.
