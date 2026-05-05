# ICT Concept Index

Living table of contents. Concept entries are added as phases ship.

## Root Files

- [README.md](./README.md) — purpose, scope, file format conventions
- [TEMPLATE.md](./TEMPLATE.md) — required structure for every concept file
- [GLOSSARY.md](./GLOSSARY.md) — alphabetical abbreviation lookup
- [TIMELINE.md](./TIMELINE.md) — chronological 2016–2026 evolution
- [READING-ORDER.md](./READING-ORDER.md) — Beginner / Intermediate / Advanced learning tracks
- [SOURCES.md](./SOURCES.md) — canonical citation index (stable IDs)
- [CONTRIBUTING.md](./CONTRIBUTING.md) — rules for adding/editing concept files
- [CHANGELOG.md](./CHANGELOG.md) — phase-by-phase log

---

## Concepts

Format: `- [Concept Name](path) — one-line summary`

### 01 — Market Structure
- [swing-high](concepts/01-market-structure/swing-high.md) — local price peak; STH/ITH/LTH fractal hierarchy.
- [swing-low](concepts/01-market-structure/swing-low.md) — local price trough; STL/ITL/LTL fractal hierarchy.
- [internal-structure](concepts/01-market-structure/internal-structure.md) — swings inside the current dealing range.
- [external-structure](concepts/01-market-structure/external-structure.md) — LTH/LTL pair that bounds the range.
- [bos-bullish](concepts/01-market-structure/bos-bullish.md) — close above prior swing high in already-bullish trend (continuation).
- [bos-bearish](concepts/01-market-structure/bos-bearish.md) — close below prior swing low in already-bearish trend.
- [choch-bullish](concepts/01-market-structure/choch-bullish.md) — first close above swing high after bearish leg (reversal).
- [choch-bearish](concepts/01-market-structure/choch-bearish.md) — first close below swing low after bullish leg.
- [mss](concepts/01-market-structure/mss.md) — CHoCH with displacement + FVG.
- [mss-vs-choch](concepts/01-market-structure/mss-vs-choch.md) — disambiguation page.
- [range-expansion](concepts/01-market-structure/range-expansion.md) — momentum phase post-breakout.
- [range-contraction](concepts/01-market-structure/range-contraction.md) — accumulation/consolidation phase.

### 02 — Liquidity
- [buy-side-liquidity](concepts/02-liquidity/buy-side-liquidity.md) — resting buy stops above price (BSL).
- [sell-side-liquidity](concepts/02-liquidity/sell-side-liquidity.md) — resting sell stops below price (SSL).
- [equal-highs](concepts/02-liquidity/equal-highs.md) — densest BSL pool form (EQH).
- [equal-lows](concepts/02-liquidity/equal-lows.md) — densest SSL pool form (EQL).
- [trendline-liquidity](concepts/02-liquidity/trendline-liquidity.md) — sloped liquidity along retail trendlines.
- [liquidity-pool](concepts/02-liquidity/liquidity-pool.md) — umbrella concept for any concentrated stop cluster.
- [liquidity-void](concepts/02-liquidity/liquidity-void.md) — wide multi-bar expansion span with no two-sided trade.
- [liquidity-sweep](concepts/02-liquidity/liquidity-sweep.md) — wick-through-pool followed by close back inside.
- [liquidity-run](concepts/02-liquidity/liquidity-run.md) — full approach + sweep + resolution sequence.
- [internal-range-liquidity](concepts/02-liquidity/internal-range-liquidity.md) — liquidity inside the dealing range (IRL).
- [external-range-liquidity](concepts/02-liquidity/external-range-liquidity.md) — liquidity at/beyond range bounds (ERL).
- [draw-on-liquidity](concepts/02-liquidity/draw-on-liquidity.md) — the specific pool the algorithm targets next (DOL).
- [liquidity-matrix](concepts/02-liquidity/liquidity-matrix.md) — multi-TF map of all pools.
- [relative-equal-highs-lows](concepts/02-liquidity/relative-equal-highs-lows.md) — within-tolerance EQH/EQL (REH/REL).

### 03 — Order Flow
- (Phase 7)

### 04 — Time Cycles
- [90-minute-cycle](concepts/04-time-cycles/90-minute-cycle.md) — smallest fractal-time unit; 4 mini-quarters of A/M/D/X.
- [macro-time-0050-0110](concepts/04-time-cycles/macro-time-0050-0110.md) — pre-London early macro.
- [macro-time-0250-0310](concepts/04-time-cycles/macro-time-0250-0310.md) — London open macro (canonical Judas).
- [macro-time-0950-1010](concepts/04-time-cycles/macro-time-0950-1010.md) — NY pre-open macro.
- [macro-time-1350-1410](concepts/04-time-cycles/macro-time-1350-1410.md) — NY first afternoon macro.
- [macro-time-1450-1510](concepts/04-time-cycles/macro-time-1450-1510.md) — NY mid-afternoon macro (last).
- [macro-times-overview](concepts/04-time-cycles/macro-times-overview.md) — five canonical 20-min programmed-delivery windows.
- [quarterly-shift-theory](concepts/04-time-cycles/quarterly-shift-theory.md) — fractal time hierarchy + 2024–2025 IPDA quarterly rotation.
- [time-of-day-pivots](concepts/04-time-cycles/time-of-day-pivots.md) — TDO, 08:30, 09:30, PDH/PDL etc.
- [dst-handling](concepts/04-time-cycles/dst-handling.md) — DST mismatch + canonical NY-clock anchoring.

### 05 — PD Arrays
- [pd-array-definition](concepts/05-pd-arrays/pd-array-definition.md) — umbrella concept for institutional price levels.
- [premium-array](concepts/05-pd-arrays/premium-array.md) — PD arrays above EQ; sell-side references.
- [discount-array](concepts/05-pd-arrays/discount-array.md) — PD arrays below EQ; buy-side references.
- [dealing-range](concepts/05-pd-arrays/dealing-range.md) — LTH/LTL-bounded reference frame for premium/discount.
- [pd-array-hierarchy](concepts/05-pd-arrays/pd-array-hierarchy.md) — type-by-type conviction ranking.
- [pd-array-nesting](concepts/05-pd-arrays/pd-array-nesting.md) — overlapping arrays produce stronger zones (2024–2025 strengthening principle).
- [htf-pd-array-hierarchy](concepts/05-pd-arrays/htf-pd-array-hierarchy.md) — multi-TF top-down array prioritization.
- [pd-array-matrix](concepts/05-pd-arrays/pd-array-matrix.md) — pre-trade tabular map of PD arrays across TFs.
- [pd-array-confluence](concepts/05-pd-arrays/pd-array-confluence.md) — multi-factor alignment scoring.

### 06 — Fair Value Gaps
- [fair-value-gap](concepts/06-fair-value-gaps/fair-value-gap.md) — canonical 3-candle imbalance.
- [bullish-fvg](concepts/06-fair-value-gaps/bullish-fvg.md) — BISI variant.
- [bearish-fvg](concepts/06-fair-value-gaps/bearish-fvg.md) — SIBI variant.
- [inversion-fvg](concepts/06-fair-value-gaps/inversion-fvg.md) — IFVG; polarity-flip after break.
- [consequent-encroachment](concepts/06-fair-value-gaps/consequent-encroachment.md) — CE; FVG midpoint.
- [ce-as-primary-entry](concepts/06-fair-value-gaps/ce-as-primary-entry.md) — 2025: CE elevated to default entry.
- [balanced-price-range](concepts/06-fair-value-gaps/balanced-price-range.md) — BPR; overlapping bull+bear FVGs.
- [volume-imbalance](concepts/06-fair-value-gaps/volume-imbalance.md) — body-vs-body gap.
- [immediate-rebalance-fvg](concepts/06-fair-value-gaps/immediate-rebalance-fvg.md) — fills within 1-3 bars.
- [delayed-rebalance-fvg](concepts/06-fair-value-gaps/delayed-rebalance-fvg.md) — stays unfilled 5+ bars.
- [fvg-classification-2025](concepts/06-fair-value-gaps/fvg-classification-2025.md) — immediate/delayed taxonomy.
- [liquidity-void-vs-fvg](concepts/06-fair-value-gaps/liquidity-void-vs-fvg.md) — disambiguation.
- [fvg-mitigation](concepts/06-fair-value-gaps/fvg-mitigation.md) — fresh/partial/mitigated state.
- [nested-fvg](concepts/06-fair-value-gaps/nested-fvg.md) — multi-TF FVG nesting.

### 07 — Order Blocks
- [bullish-order-block](concepts/07-order-blocks/bullish-order-block.md) — last bearish candle before bullish displacement+BOS.
- [bearish-order-block](concepts/07-order-blocks/bearish-order-block.md) — mirror.
- [order-block-criteria](concepts/07-order-blocks/order-block-criteria.md) — qualification rules.
- [mitigated-order-block](concepts/07-order-blocks/mitigated-order-block.md) — tested OB state.
- [unmitigated-order-block](concepts/07-order-blocks/unmitigated-order-block.md) — fresh OB, highest conviction.
- [propulsion-block](concepts/07-order-blocks/propulsion-block.md) — wide-body displacement candle as continuation reference.
- [vacuum-block](concepts/07-order-blocks/vacuum-block.md) — opening-gap candle.
- [reversal-order-block](concepts/07-order-blocks/reversal-order-block.md) — OB at CHoCH/MSS pivot.
- [continuation-order-block](concepts/07-order-blocks/continuation-order-block.md) — OB at BOS pivot in trend.
- [order-block-vs-supply-demand](concepts/07-order-blocks/order-block-vs-supply-demand.md) — disambiguation.

### 08 — Breaker Blocks
- [breaker-block](concepts/08-breaker-blocks/breaker-block.md) — failed OB whose polarity flips.
- [bullish-breaker](concepts/08-breaker-blocks/bullish-breaker.md) — failed bearish OB → support.
- [bearish-breaker](concepts/08-breaker-blocks/bearish-breaker.md) — failed bullish OB → resistance.
- [mitigation-block](concepts/08-breaker-blocks/mitigation-block.md) — violated OB without polarity flip (BOS context).
- [breaker-vs-mitigation](concepts/08-breaker-blocks/breaker-vs-mitigation.md) — disambiguation.
- [failed-breaker](concepts/08-breaker-blocks/failed-breaker.md) — breaker that fails on retest.

### 09 — Displacement
- [displacement-definition](concepts/09-displacement/displacement-definition.md) — wide-body force candle.
- [displacement-and-fvg](concepts/09-displacement/displacement-and-fvg.md) — displacement ↔ FVG mutual implication.
- (per-direction + classification + gap-classification deferred to Phase 7)

### 10 — Killzones
- [killzone-overview](concepts/10-killzones/killzone-overview.md) — five canonical KZs in NY time.
- [asia-killzone](concepts/10-killzones/asia-killzone.md) — 20:00–00:00 NY; Asian range formation.
- [london-open-killzone](concepts/10-killzones/london-open-killzone.md) — 02:00–05:00 NY; Judas-swing window.
- [ny-am-killzone](concepts/10-killzones/ny-am-killzone.md) — 08:00–11:00 NY; highest-volume KZ.
- [london-close-killzone](concepts/10-killzones/london-close-killzone.md) — 10:00–12:00 NY; overlaps NY AM.
- [ny-pm-killzone](concepts/10-killzones/ny-pm-killzone.md) — 13:30–16:00 NY; secondary delivery.
- [killzone-times-table](concepts/10-killzones/killzone-times-table.md) — quick-reference card.
- [killzone-vs-session](concepts/10-killzones/killzone-vs-session.md) — disambiguation (mirror).

### 11 — Silver Bullet
- [silver-bullet-overview](concepts/11-silver-bullet/silver-bullet-overview.md) — three SB windows, sweep+displacement+FVG framework.
- [silver-bullet-london](concepts/11-silver-bullet/silver-bullet-london.md) — 03:00–04:00 NY.
- [silver-bullet-ny-am](concepts/11-silver-bullet/silver-bullet-ny-am.md) — 10:00–11:00 NY (highest probability).
- [silver-bullet-ny-pm](concepts/11-silver-bullet/silver-bullet-ny-pm.md) — 14:00–15:00 NY (lowest).
- [silver-bullet-rules](concepts/11-silver-bullet/silver-bullet-rules.md) — 8-point checklist.
- [silver-bullet-formalized-2025](concepts/11-silver-bullet/silver-bullet-formalized-2025.md) — 2025 micro-execution refinements.
- [silver-bullet-failure-modes](concepts/11-silver-bullet/silver-bullet-failure-modes.md) — four common failure patterns.

### 12 — Power of Three
- [power-of-three](concepts/12-power-of-three/power-of-three.md) — PO3 / AMD doctrine.
- [accumulation-phase](concepts/12-power-of-three/accumulation-phase.md), [manipulation-phase](concepts/12-power-of-three/manipulation-phase.md), [distribution-phase](concepts/12-power-of-three/distribution-phase.md) — phases.
- [intraday-amd](concepts/12-power-of-three/intraday-amd.md) — daily-scale Asia-London-NY mapping.
- [htf-amd](concepts/12-power-of-three/htf-amd.md) — weekly/monthly/yearly AMD.

### 13 — Judas Swing
- [judas-swing](concepts/13-judas-swing/judas-swing.md) — session-open false-direction move + reversal.
- [london-judas-swing](concepts/13-judas-swing/london-judas-swing.md) — canonical LO-KZ Judas with Asian-range sweep.
- [ny-judas-swing](concepts/13-judas-swing/ny-judas-swing.md) — smaller-scale NY AM Judas.
- [judas-swing-failure](concepts/13-judas-swing/judas-swing-failure.md) — when no reversal happens.

### 14 — Asian Range
- [asian-range](concepts/14-asian-range/asian-range.md) — bounded engineered-liquidity range from Asia session.
- [asian-range-high](concepts/14-asian-range/asian-range-high.md) — BSL pool at the top.
- [asian-range-low](concepts/14-asian-range/asian-range-low.md) — SSL pool at the bottom.
- [asian-range-sweep](concepts/14-asian-range/asian-range-sweep.md) — London-driven sweep of one bound.
- [asian-session-bias](concepts/14-asian-range/asian-session-bias.md) — secondary directional read from Asia close.
- [asian-range-projections](concepts/14-asian-range/asian-range-projections.md) — 0.5×/1×/1.5×/2× extension targets.

### 15 — Sessions
- [session-overview](concepts/15-sessions/session-overview.md) — full NY-time session map.
- [asia-session](concepts/15-sessions/asia-session.md) — 18:00 prev → 03:00 NY; accumulation / range-building.
- [london-session](concepts/15-sessions/london-session.md) — 02:00 → 11:00 NY; manipulation + expansion.
- [ny-am-session](concepts/15-sessions/ny-am-session.md) — 08:00 → 12:00 NY; distribution / largest range.
- [ny-lunch](concepts/15-sessions/ny-lunch.md) — 12:00 → 13:30 NY; dead session, skip.
- [ny-pm-session](concepts/15-sessions/ny-pm-session.md) — 13:30 → 16:00 NY; secondary delivery, reversals.
- [london-close](concepts/15-sessions/london-close.md) — 10:00 → 12:00 NY; European unwind; overlaps NY AM.
- [session-overlaps](concepts/15-sessions/session-overlaps.md) — high-volume intersection windows.
- [session-vs-killzone](concepts/15-sessions/session-vs-killzone.md) — disambiguation page.

### 16 — SMT Divergence
- [smt-divergence](concepts/16-smt-divergence/smt-divergence.md) — Smart Money Technique divergence between correlated assets.
- [correlated-pairs-smt](concepts/16-smt-divergence/correlated-pairs-smt.md) — FX cross-pair SMT.
- [index-smt](concepts/16-smt-divergence/index-smt.md) — NQ/ES/YM/RTY SMT.
- [smt-confirmation](concepts/16-smt-divergence/smt-confirmation.md) — SMT as confluence factor.
- [smt-failure](concepts/16-smt-divergence/smt-failure.md) — when divergence closes.

### 17 — Optimal Trade Entry
- [ote-overview](concepts/17-optimal-trade-entry/ote-overview.md) — canonical 0.62-0.79 entry methodology.
- [ote-62](concepts/17-optimal-trade-entry/ote-62.md) — shallow OTE entry.
- [ote-705](concepts/17-optimal-trade-entry/ote-705.md) — optimal mid-point entry.
- [ote-79](concepts/17-optimal-trade-entry/ote-79.md) — deep OTE entry / invalidation reference.
- [ote-rules](concepts/17-optimal-trade-entry/ote-rules.md) — full setup checklist.
- [ote-failure](concepts/17-optimal-trade-entry/ote-failure.md) — invalidation & response.

### 18 — Mitigation
- [mitigation-definition](concepts/18-mitigation/mitigation-definition.md) — umbrella concept of zone "tested" state.
- [mitigation-of-ob](concepts/18-mitigation/mitigation-of-ob.md) — MT-threshold OB mitigation.
- [mitigation-of-fvg](concepts/18-mitigation/mitigation-of-fvg.md) — CE-threshold FVG mitigation (2025 default).
- [mitigation-of-breaker](concepts/18-mitigation/mitigation-of-breaker.md) — breaker retest mechanics.
- [partial-vs-full-mitigation](concepts/18-mitigation/partial-vs-full-mitigation.md) — fresh/partial/mitigated/fully-consumed lifecycle.

### 19 — Rejection Blocks
- [rejection-block](concepts/19-rejection-blocks/rejection-block.md) — long-wick rejection at key level.
- [bullish-rejection-block](concepts/19-rejection-blocks/bullish-rejection-block.md) — lower-wick variant.
- [bearish-rejection-block](concepts/19-rejection-blocks/bearish-rejection-block.md) — upper-wick variant.

### 20 — Turtle Soup
- [turtle-soup](concepts/20-turtle-soup/turtle-soup.md) — failed breakout pattern.
- [bullish-turtle-soup](concepts/20-turtle-soup/bullish-turtle-soup.md), [bearish-turtle-soup](concepts/20-turtle-soup/bearish-turtle-soup.md) — directional variants.
- [stop-hunt-pattern](concepts/20-turtle-soup/stop-hunt-pattern.md) — broader stop-hunt umbrella.

### 21 — CRT (community-attributed)
- (Phase 7)

### 22 — Quarterly Theory
- (Phase 7)

### 23 — IPDA
- [ipda-definition](concepts/23-ipda/ipda-definition.md) — Interbank Price Delivery Algorithm overview.
- [ipda-data-ranges](concepts/23-ipda/ipda-data-ranges.md) — 20/40/60-day lookback windows.
- (per-window deep dives shipped Phase 7: ipda-20-day-lookback, ipda-40-day-lookback, ipda-60-day-lookback, ipda-reference-points)

### 24 — AMD Cycle
- [amd-cycle-overview](concepts/24-amd-cycle/amd-cycle-overview.md) — cycle as repeating temporal pattern.
- [amd-on-htf](concepts/24-amd-cycle/amd-on-htf.md) — weekly/monthly cycle.
- [amd-on-intraday](concepts/24-amd-cycle/amd-on-intraday.md) — daily/90min cycle.
- [amd-vs-po3](concepts/24-amd-cycle/amd-vs-po3.md) — disambiguation (same cycle, two framings).

### 25 — HTF Bias
- [htf-bias-framework](concepts/25-htf-bias/htf-bias-framework.md) — top-down bias decision system.
- [monthly-bias](concepts/25-htf-bias/monthly-bias.md), [weekly-bias](concepts/25-htf-bias/weekly-bias.md), [daily-bias](concepts/25-htf-bias/daily-bias.md) — per-TF deep-dives.
- [bias-confluence](concepts/25-htf-bias/bias-confluence.md) — multi-TF alignment scoring.
- [bias-invalidation](concepts/25-htf-bias/bias-invalidation.md) — when bias must flip.
- [top-down-analysis](concepts/25-htf-bias/top-down-analysis.md) — prescribed analysis sequence.

### 26 — Imbalance
- [imbalance-definition](concepts/26-imbalance/imbalance-definition.md) — umbrella term for any unworked price region.
- [inefficiency](concepts/26-imbalance/inefficiency.md) — synonym (microstructure framing).
- [imbalance-vs-fvg](concepts/26-imbalance/imbalance-vs-fvg.md) — disambiguation; FVG ⊂ imbalance.
- [imbalance-rebalance](concepts/26-imbalance/imbalance-rebalance.md) — when price returns to fill the imbalance.
- [volume-imbalance-detail](concepts/26-imbalance/volume-imbalance-detail.md) — body-vs-body gap (not an FVG).

### 27 — Equilibrium
- [equilibrium-definition](concepts/27-equilibrium/equilibrium-definition.md) — 50% midpoint of any reference range.
- [dealing-range-equilibrium](concepts/27-equilibrium/dealing-range-equilibrium.md) — primary EQ in the dealing-range frame.
- [equilibrium-as-decision-point](concepts/27-equilibrium/equilibrium-as-decision-point.md) — operational EQ pivot rules.
- [mean-threshold](concepts/27-equilibrium/mean-threshold.md) — OB body midpoint (MT).

### 28 — Fibonacci Levels
- [ict-fib-overview](concepts/28-fibonacci-levels/ict-fib-overview.md) — ICT-specific fib retracement + projection set.
- [fib-62](concepts/28-fibonacci-levels/fib-62.md) — upper OTE bound (shallow).
- [fib-705](concepts/28-fibonacci-levels/fib-705.md) — OTE optimal entry mid-point.
- [fib-79](concepts/28-fibonacci-levels/fib-79.md) — deep OTE / invalidation reference.
- [standard-deviation-projections](concepts/28-fibonacci-levels/standard-deviation-projections.md) — extension targets (-1.5/-2.0/-2.5/-4.0).
- [symmetrical-price-projections](concepts/28-fibonacci-levels/symmetrical-price-projections.md) — equal-distance leg projection.
- [fib-vs-ote](concepts/28-fibonacci-levels/fib-vs-ote.md) — disambiguation (OTE ⊂ fib).

### 29 — Stop Runs
- [stop-run-definition](concepts/29-stop-runs/stop-run-definition.md) — algorithmic stop-targeting umbrella.
- [stop-run-into-fvg](concepts/29-stop-runs/stop-run-into-fvg.md) — sweep + displacement + FVG entry.
- [stop-run-into-ob](concepts/29-stop-runs/stop-run-into-ob.md) — sweep + OB entry at MT.
- [stop-run-into-breaker](concepts/29-stop-runs/stop-run-into-breaker.md) — sweep + breaker retest entry.
- (stop-hunt-pattern shipped in `20-turtle-soup`)

### 30 — News Driven
- (Phase 7)

### 31 — Models
- [ict-2022-model](concepts/31-models/ict-2022-model.md) — flagship multi-step setup framework.
- [ict-2023-model](concepts/31-models/ict-2023-model.md) — Quarterly Theory + macro integration refinements.
- [ict-2024-model](concepts/31-models/ict-2024-model.md) — FVG classification + IFVG + propulsion refinements.
- [unicorn-model](concepts/31-models/unicorn-model.md) — rare A++ confluence: breaker + nested FVG + bias + sweep.
- [bread-and-butter-setup](concepts/31-models/bread-and-butter-setup.md) — the recurring daily delivery sequence.
- [diamond-pattern](concepts/31-models/diamond-pattern.md) — double-sweep consolidation breakout.
- [ny-am-open-range-model](concepts/31-models/ny-am-open-range-model.md) — 08:00–08:30/09:00 NY OR sweep model.
- [london-close-reversal](concepts/31-models/london-close-reversal.md) — 10:00–12:00 NY morning-fade pattern.
- [ny-pm-reversal](concepts/31-models/ny-pm-reversal.md) — afternoon fade of AM trend.
- [ndog](concepts/31-models/ndog.md) — New Day Opening Gap (midnight NY).
- [nwog](concepts/31-models/nwog.md) — New Week Opening Gap (Sunday/Monday).
- [sunday-open-gap](concepts/31-models/sunday-open-gap.md) — 18:00 NY Sunday open event.
- [venom-model](concepts/31-models/venom-model.md) — Apr 2025; pre-cash-open range fake-breakout for US indices.
- [zircon-model](concepts/31-models/zircon-model.md) — Jan 2026 silent demo (demo-stage).

### 32 — Risk Management
- [risk-per-trade](concepts/32-risk-management/risk-per-trade.md) — per-trade % risk discipline.
- [r-multiple](concepts/32-risk-management/r-multiple.md) — R as universal trade-quality measure.
- [position-sizing](concepts/32-risk-management/position-sizing.md) — lot/contract calculation.
- [stop-placement-by-pd-array](concepts/32-risk-management/stop-placement-by-pd-array.md) — structural SL.
- [partial-takes](concepts/32-risk-management/partial-takes.md) — scaling-out ladder.
- [static-drawdown-2026](concepts/32-risk-management/static-drawdown-2026.md) — 2026 prop-firm rule shift adaptation.
- [correlation-risk](concepts/32-risk-management/correlation-risk.md) — cluster exposure tracking.

### 99 — Glossary (deep-dives)
- (Phase 8)
