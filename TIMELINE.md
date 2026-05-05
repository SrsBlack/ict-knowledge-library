# Timeline — ICT Concept Evolution (2016–2026)

Chronological record of when each concept was introduced or refined. Used for queries like "what changed in 2024?" or "when was IFVG formalized?"

Each year section is ready to receive entries. Concept files reference this timeline via their `Year Introduced` and `Year Refined` top-matter fields.

Format per entry: `- **<concept-id>** — <one-line note>. → [link](path)`

---

## 2016 — Foundational Mentorship

The original ICT mentorship year. Most foundational PD-array, killzone, and order-flow vocabulary originates here.

- **swing-high** — 3-bar pivot definition. → [swing-high](concepts/01-market-structure/swing-high.md)
- **swing-low** — 3-bar pivot definition. → [swing-low](concepts/01-market-structure/swing-low.md)
- **fair-value-gap (FVG)** — 3-candle wick imbalance introduced. → [fair-value-gap](concepts/06-fair-value-gaps/fair-value-gap.md), [bullish-fvg](concepts/06-fair-value-gaps/bullish-fvg.md), [bearish-fvg](concepts/06-fair-value-gaps/bearish-fvg.md)
- **order-block (OB)** — last opposite-color candle before displacement. → [order-block-criteria](concepts/07-order-blocks/order-block-criteria.md), [bullish-order-block](concepts/07-order-blocks/bullish-order-block.md), [bearish-order-block](concepts/07-order-blocks/bearish-order-block.md), [mitigated-order-block](concepts/07-order-blocks/mitigated-order-block.md), [unmitigated-order-block](concepts/07-order-blocks/unmitigated-order-block.md), [order-block-vs-supply-demand](concepts/07-order-blocks/order-block-vs-supply-demand.md)
- **power-of-three (PO3) / AMD doctrine** introduced. → [power-of-three](concepts/12-power-of-three/power-of-three.md), [accumulation-phase](concepts/12-power-of-three/accumulation-phase.md), [manipulation-phase](concepts/12-power-of-three/manipulation-phase.md), [distribution-phase](concepts/12-power-of-three/distribution-phase.md), [intraday-amd](concepts/12-power-of-three/intraday-amd.md), [htf-amd](concepts/12-power-of-three/htf-amd.md), [amd-cycle-overview](concepts/24-amd-cycle/amd-cycle-overview.md), [amd-on-htf](concepts/24-amd-cycle/amd-on-htf.md), [amd-on-intraday](concepts/24-amd-cycle/amd-on-intraday.md), [amd-vs-po3](concepts/24-amd-cycle/amd-vs-po3.md)
- **stop-run-definition** + variants. → [stop-run-definition](concepts/29-stop-runs/stop-run-definition.md), [stop-run-into-fvg](concepts/29-stop-runs/stop-run-into-fvg.md), [stop-run-into-ob](concepts/29-stop-runs/stop-run-into-ob.md), [stop-run-into-breaker](concepts/29-stop-runs/stop-run-into-breaker.md)
- **buy-side-liquidity (BSL)** — resting buy stops above swing highs. → [buy-side-liquidity](concepts/02-liquidity/buy-side-liquidity.md)
- **sell-side-liquidity (SSL)** — resting sell stops below swing lows. → [sell-side-liquidity](concepts/02-liquidity/sell-side-liquidity.md)
- **liquidity-pool** — umbrella term for stop clusters. → [liquidity-pool](concepts/02-liquidity/liquidity-pool.md)
- **session-overview** — six-session NY-time map. → [session-overview](concepts/15-sessions/session-overview.md)
- **asia-session** — accumulation window. → [asia-session](concepts/15-sessions/asia-session.md)
- **london-session** — manipulation + expansion window. → [london-session](concepts/15-sessions/london-session.md)
- **ny-am-session** — distribution window. → [ny-am-session](concepts/15-sessions/ny-am-session.md)
- **ny-pm-session** — secondary delivery / reversals. → [ny-pm-session](concepts/15-sessions/ny-pm-session.md)
- **london-close** — European unwind window. → [london-close](concepts/15-sessions/london-close.md)
- **session-overlaps** — overlap windows defined. → [session-overlaps](concepts/15-sessions/session-overlaps.md)
- **session-vs-killzone** — terminology distinction. → [session-vs-killzone](concepts/15-sessions/session-vs-killzone.md)
- **institutional-order-flow + algorithmic-price-delivery** — flow-reading framework. → [institutional-order-flow](concepts/03-order-flow/institutional-order-flow.md), [bullish-order-flow](concepts/03-order-flow/bullish-order-flow.md), [bearish-order-flow](concepts/03-order-flow/bearish-order-flow.md), [order-flow-shift](concepts/03-order-flow/order-flow-shift.md), [smart-money-footprint](concepts/03-order-flow/smart-money-footprint.md)

## 2017 — Charter Year

Refinements of FVG and OB definitions; introduction of OTE and Fibonacci levels; structure terminology formalized.

- **STH/ITH/LTH and STL/ITL/LTL fractal hierarchy** added to swing definitions. → [swing-high](concepts/01-market-structure/swing-high.md), [swing-low](concepts/01-market-structure/swing-low.md)
- **internal-structure** vs **external-structure** distinction. → [internal-structure](concepts/01-market-structure/internal-structure.md), [external-structure](concepts/01-market-structure/external-structure.md)
- **bos-bullish** / **bos-bearish** — BOS terminology. → [bos-bullish](concepts/01-market-structure/bos-bullish.md), [bos-bearish](concepts/01-market-structure/bos-bearish.md)
- **choch-bullish** / **choch-bearish** — CHoCH reversal terminology. → [choch-bullish](concepts/01-market-structure/choch-bullish.md), [choch-bearish](concepts/01-market-structure/choch-bearish.md)
- **mss** — Market Structure Shift formalized as displacement-driven CHoCH. → [mss](concepts/01-market-structure/mss.md)
- **mss-vs-choch** — disambiguation. → [mss-vs-choch](concepts/01-market-structure/mss-vs-choch.md)
- **equal-highs / equal-lows** terminology refined. → [equal-highs](concepts/02-liquidity/equal-highs.md), [equal-lows](concepts/02-liquidity/equal-lows.md)
- **trendline-liquidity** — sloped liquidity recognized. → [trendline-liquidity](concepts/02-liquidity/trendline-liquidity.md)
- **liquidity-void** — wide expansion-span concept. → [liquidity-void](concepts/02-liquidity/liquidity-void.md)
- **liquidity-sweep** / **liquidity-run** — sweep and run-on-liquidity terminology. → [liquidity-sweep](concepts/02-liquidity/liquidity-sweep.md), [liquidity-run](concepts/02-liquidity/liquidity-run.md)
- **ny-lunch** — dead-session designation. → [ny-lunch](concepts/15-sessions/ny-lunch.md)
- **OTE methodology + ICT fib levels** introduced (0.62 / 0.705 / 0.79 retracement; -1.5/-2.0/-2.5/-4.0 projection). → [ote-overview](concepts/17-optimal-trade-entry/ote-overview.md), [ote-62](concepts/17-optimal-trade-entry/ote-62.md), [ote-705](concepts/17-optimal-trade-entry/ote-705.md), [ote-79](concepts/17-optimal-trade-entry/ote-79.md), [ote-rules](concepts/17-optimal-trade-entry/ote-rules.md), [ote-failure](concepts/17-optimal-trade-entry/ote-failure.md), [ict-fib-overview](concepts/28-fibonacci-levels/ict-fib-overview.md), [fib-62](concepts/28-fibonacci-levels/fib-62.md), [fib-705](concepts/28-fibonacci-levels/fib-705.md), [fib-79](concepts/28-fibonacci-levels/fib-79.md), [standard-deviation-projections](concepts/28-fibonacci-levels/standard-deviation-projections.md), [fib-vs-ote](concepts/28-fibonacci-levels/fib-vs-ote.md)
- **HTF bias framework** introduced (top-down + per-TF reads + invalidation rules). → [htf-bias-framework](concepts/25-htf-bias/htf-bias-framework.md), [monthly-bias](concepts/25-htf-bias/monthly-bias.md), [weekly-bias](concepts/25-htf-bias/weekly-bias.md), [daily-bias](concepts/25-htf-bias/daily-bias.md), [bias-confluence](concepts/25-htf-bias/bias-confluence.md), [bias-invalidation](concepts/25-htf-bias/bias-invalidation.md), [top-down-analysis](concepts/25-htf-bias/top-down-analysis.md)
- **Risk management** discipline (R-multiple, position sizing, structural SL, partial takes, correlation risk). → [risk-per-trade](concepts/32-risk-management/risk-per-trade.md), [r-multiple](concepts/32-risk-management/r-multiple.md), [position-sizing](concepts/32-risk-management/position-sizing.md), [stop-placement-by-pd-array](concepts/32-risk-management/stop-placement-by-pd-array.md), [partial-takes](concepts/32-risk-management/partial-takes.md), [correlation-risk](concepts/32-risk-management/correlation-risk.md)
- **displacement** introduced as ICT's algorithmic-intent signature. → [displacement-definition](concepts/09-displacement/displacement-definition.md), [displacement-and-fvg](concepts/09-displacement/displacement-and-fvg.md), [bullish-displacement](concepts/09-displacement/bullish-displacement.md), [bearish-displacement](concepts/09-displacement/bearish-displacement.md), [displacement-strength-criteria](concepts/09-displacement/displacement-strength-criteria.md)
- **News-driven trading discipline** — three-posture protocol + per-news rules. → [news-driven-overview](concepts/30-news-driven/news-driven-overview.md), [nfp-protocol](concepts/30-news-driven/nfp-protocol.md), [news-blackout-rules](concepts/30-news-driven/news-blackout-rules.md)
- **balanced-price-range (BPR)** introduced. → [balanced-price-range](concepts/06-fair-value-gaps/balanced-price-range.md)
- **reversal-order-block** vs **continuation-order-block** distinction (refined 2023). → [reversal-order-block](concepts/07-order-blocks/reversal-order-block.md), [continuation-order-block](concepts/07-order-blocks/continuation-order-block.md)
- **breaker-block** introduced; **mitigation-block** distinct concept. → [breaker-block](concepts/08-breaker-blocks/breaker-block.md), [bullish-breaker](concepts/08-breaker-blocks/bullish-breaker.md), [bearish-breaker](concepts/08-breaker-blocks/bearish-breaker.md), [breaker-vs-mitigation](concepts/08-breaker-blocks/breaker-vs-mitigation.md), [failed-breaker](concepts/08-breaker-blocks/failed-breaker.md)
- **mitigation** as a state concept. → [mitigation-definition](concepts/18-mitigation/mitigation-definition.md), [mitigation-of-ob](concepts/18-mitigation/mitigation-of-ob.md), [mitigation-of-fvg](concepts/18-mitigation/mitigation-of-fvg.md), [mitigation-of-breaker](concepts/18-mitigation/mitigation-of-breaker.md), [partial-vs-full-mitigation](concepts/18-mitigation/partial-vs-full-mitigation.md)
- **fvg-mitigation** as state lifecycle, **liquidity-void-vs-fvg** disambiguation, **nested-fvg** confluence. → [fvg-mitigation](concepts/06-fair-value-gaps/fvg-mitigation.md), [liquidity-void-vs-fvg](concepts/06-fair-value-gaps/liquidity-void-vs-fvg.md), [nested-fvg](concepts/06-fair-value-gaps/nested-fvg.md)
- **PD array** vocabulary refined (premium / discount / hierarchy / dealing-range EQ). → [pd-array-definition](concepts/05-pd-arrays/pd-array-definition.md), [premium-array](concepts/05-pd-arrays/premium-array.md), [discount-array](concepts/05-pd-arrays/discount-array.md), [pd-array-hierarchy](concepts/05-pd-arrays/pd-array-hierarchy.md), [dealing-range](concepts/05-pd-arrays/dealing-range.md), [equilibrium-definition](concepts/27-equilibrium/equilibrium-definition.md), [dealing-range-equilibrium](concepts/27-equilibrium/dealing-range-equilibrium.md), [equilibrium-as-decision-point](concepts/27-equilibrium/equilibrium-as-decision-point.md), [mean-threshold](concepts/27-equilibrium/mean-threshold.md)

## 2018 — Block Vocabulary Expansion

Mitigation, propulsion, rejection, vacuum block taxonomy; IFVG and CE introduced. Judas-swing terminology refined.

- **relative-equal-highs-lows (REH/REL)** — within-tolerance equality recognized. → [relative-equal-highs-lows](concepts/02-liquidity/relative-equal-highs-lows.md)
- **judas-swing** terminology refined into a named ICT concept. → [judas-swing](concepts/13-judas-swing/judas-swing.md), [london-judas-swing](concepts/13-judas-swing/london-judas-swing.md), [ny-judas-swing](concepts/13-judas-swing/ny-judas-swing.md), [judas-swing-failure](concepts/13-judas-swing/judas-swing-failure.md)
- **asian-range-projections** — extension-target framework. → [asian-range-projections](concepts/14-asian-range/asian-range-projections.md)
- **IPDA** introduced as the algorithm-name for institutional price delivery; 20/40/60-day lookback ranges established. → [ipda-definition](concepts/23-ipda/ipda-definition.md), [ipda-data-ranges](concepts/23-ipda/ipda-data-ranges.md), [ipda-20-day-lookback](concepts/23-ipda/ipda-20-day-lookback.md), [ipda-40-day-lookback](concepts/23-ipda/ipda-40-day-lookback.md), [ipda-60-day-lookback](concepts/23-ipda/ipda-60-day-lookback.md), [ipda-reference-points](concepts/23-ipda/ipda-reference-points.md)
- **Gap classification** taxonomy (FVG vs VI vs liquidity-void). → [gap-classification](concepts/09-displacement/gap-classification.md)
- **volume-imbalance** — body-vs-body imbalance distinction added. → [volume-imbalance-detail](concepts/26-imbalance/volume-imbalance-detail.md), [volume-imbalance](concepts/06-fair-value-gaps/volume-imbalance.md)
- **symmetrical-price-projections** — equal-distance projection method. → [symmetrical-price-projections](concepts/28-fibonacci-levels/symmetrical-price-projections.md)
- **inversion-fvg (IFVG)** introduced; **consequent-encroachment (CE)** introduced. → [inversion-fvg](concepts/06-fair-value-gaps/inversion-fvg.md), [consequent-encroachment](concepts/06-fair-value-gaps/consequent-encroachment.md)
- **turtle-soup** integrated into ICT framework (originally Connors 1998). → [turtle-soup](concepts/20-turtle-soup/turtle-soup.md), [bullish-turtle-soup](concepts/20-turtle-soup/bullish-turtle-soup.md), [bearish-turtle-soup](concepts/20-turtle-soup/bearish-turtle-soup.md), [stop-hunt-pattern](concepts/20-turtle-soup/stop-hunt-pattern.md)
- **SMT divergence** terminology refined into a named ICT confluence signal. → [smt-divergence](concepts/16-smt-divergence/smt-divergence.md), [correlated-pairs-smt](concepts/16-smt-divergence/correlated-pairs-smt.md), [index-smt](concepts/16-smt-divergence/index-smt.md), [smt-confirmation](concepts/16-smt-divergence/smt-confirmation.md), [smt-failure](concepts/16-smt-divergence/smt-failure.md)
- **propulsion-block, vacuum-block, rejection-block, mitigation-block** taxonomy. → [propulsion-block](concepts/07-order-blocks/propulsion-block.md), [vacuum-block](concepts/07-order-blocks/vacuum-block.md), [rejection-block](concepts/19-rejection-blocks/rejection-block.md), [bullish-rejection-block](concepts/19-rejection-blocks/bullish-rejection-block.md), [bearish-rejection-block](concepts/19-rejection-blocks/bearish-rejection-block.md), [mitigation-block](concepts/08-breaker-blocks/mitigation-block.md)

## 2019 — Quiet / Iteration

Mostly refinements; few new named concepts.

- (pending)

## 2020 — Free Tutoring Series

Public YouTube re-teach of foundations. PO3 / AMD codified for free audience.

- (pending)

## 2021 — DOL & Liquidity Matrix

Draw On Liquidity language; IRL/ERL distinction emerges.

- **draw-on-liquidity (DOL)** — algorithmic draw-target terminology. → [draw-on-liquidity](concepts/02-liquidity/draw-on-liquidity.md)
- **liquidity-matrix** — multi-TF pool mapping discipline. → [liquidity-matrix](concepts/02-liquidity/liquidity-matrix.md)

## 2022 — The 2022 Model Year

ICT 2022 Mentorship; silver bullet windows formalized; **macro times introduced**. Most foundational concepts received their final operational framing in this year.

- **internal-range-liquidity (IRL)** vs **external-range-liquidity (ERL)** distinction formalized. → [internal-range-liquidity](concepts/02-liquidity/internal-range-liquidity.md), [external-range-liquidity](concepts/02-liquidity/external-range-liquidity.md)
- **range-expansion** / **range-contraction** — phase terminology operationalized. → [range-expansion](concepts/01-market-structure/range-expansion.md), [range-contraction](concepts/01-market-structure/range-contraction.md)
- **macro-times-overview** — five canonical 20-min programmed-delivery windows introduced. → [macro-times-overview](concepts/04-time-cycles/macro-times-overview.md)
- **silver-bullet** three windows formalized in 2022 mentorship. → [silver-bullet-overview](concepts/11-silver-bullet/silver-bullet-overview.md), [silver-bullet-london](concepts/11-silver-bullet/silver-bullet-london.md), [silver-bullet-ny-am](concepts/11-silver-bullet/silver-bullet-ny-am.md), [silver-bullet-ny-pm](concepts/11-silver-bullet/silver-bullet-ny-pm.md), [silver-bullet-rules](concepts/11-silver-bullet/silver-bullet-rules.md), [silver-bullet-failure-modes](concepts/11-silver-bullet/silver-bullet-failure-modes.md)
- **ICT 2022 Model** — flagship multi-step framework. → [ict-2022-model](concepts/31-models/ict-2022-model.md), [ny-am-open-range-model](concepts/31-models/ny-am-open-range-model.md), [london-close-reversal](concepts/31-models/london-close-reversal.md), [ny-pm-reversal](concepts/31-models/ny-pm-reversal.md)
- Per-macro deep dives shipped: [macro-time-0050-0110](concepts/04-time-cycles/macro-time-0050-0110.md), [macro-time-0250-0310](concepts/04-time-cycles/macro-time-0250-0310.md), [macro-time-0950-1010](concepts/04-time-cycles/macro-time-0950-1010.md), [macro-time-1350-1410](concepts/04-time-cycles/macro-time-1350-1410.md), [macro-time-1450-1510](concepts/04-time-cycles/macro-time-1450-1510.md).
- All foundational structure / liquidity / session concepts (2016–2018 introductions) re-taught with refined operational rules in the 2022 mentorship. See `Year Refined: 2022` on most Phase-1 / Phase-2 files.

## 2023 — Quarterly Theory Era

Quarterly Theory taught publicly; named models multiply (Unicorn, Diamond, Bread-and-Butter).

- **quarterly-shift-theory** — fractal time hierarchy taught publicly. → [quarterly-shift-theory](concepts/04-time-cycles/quarterly-shift-theory.md)
- **90-minute-cycle** — smallest fractal time unit operationalized within Quarterly Theory. → [90-minute-cycle](concepts/04-time-cycles/90-minute-cycle.md)
- **Quarterly Theory deep-dives** — per-level fractal expansion. → [quarterly-theory-overview](concepts/22-quarterly-theory/quarterly-theory-overview.md), [yearly-quarters](concepts/22-quarterly-theory/yearly-quarters.md), [monthly-quarters](concepts/22-quarterly-theory/monthly-quarters.md), [weekly-quarters](concepts/22-quarterly-theory/weekly-quarters.md), [daily-quarters](concepts/22-quarterly-theory/daily-quarters.md), [90-minute-quarters](concepts/22-quarterly-theory/90-minute-quarters.md), [true-day-open](concepts/22-quarterly-theory/true-day-open.md), [true-week-open](concepts/22-quarterly-theory/true-week-open.md)
- **ICT 2023 Model** — refines 2022 with QT + macro integration. → [ict-2023-model](concepts/31-models/ict-2023-model.md)
- **Unicorn / Bread-and-Butter / Diamond** named-model trio. → [unicorn-model](concepts/31-models/unicorn-model.md), [bread-and-butter-setup](concepts/31-models/bread-and-butter-setup.md), [diamond-pattern](concepts/31-models/diamond-pattern.md)
- **NDOG / NWOG / Sunday Open Gap** taught. → [ndog](concepts/31-models/ndog.md), [nwog](concepts/31-models/nwog.md), [sunday-open-gap](concepts/31-models/sunday-open-gap.md)

## 2024 — Refinement & Naming

IFVG formalized; immediate vs delayed rebalance distinction; propulsion block re-teach. PD-array nesting principle introduced; HTF top-down array hierarchy refined.

- **pd-array-nesting** introduced (formalized 2025 in adv-liquidity series, but rooted in 2024 mentorship modules). → [pd-array-nesting](concepts/05-pd-arrays/pd-array-nesting.md)
- **htf-pd-array-hierarchy** — multi-TF top-down framework refined. → [htf-pd-array-hierarchy](concepts/05-pd-arrays/htf-pd-array-hierarchy.md)
- **pd-array-matrix** — pre-trade tabular discipline operationalized. → [pd-array-matrix](concepts/05-pd-arrays/pd-array-matrix.md)
- **FVG classification: immediate vs delayed rebalance** formalized. → [fvg-classification-2025](concepts/06-fair-value-gaps/fvg-classification-2025.md), [immediate-rebalance-fvg](concepts/06-fair-value-gaps/immediate-rebalance-fvg.md), [delayed-rebalance-fvg](concepts/06-fair-value-gaps/delayed-rebalance-fvg.md)
- **IFVG formalized** as a standardized ICT structural reference. → [inversion-fvg](concepts/06-fair-value-gaps/inversion-fvg.md)
- **propulsion-block** re-teach in 2024 mentorship module list. → [propulsion-block](concepts/07-order-blocks/propulsion-block.md)
- **ICT 2024 Model** — disciplined integration of 2024 vocabulary expansions. → [ict-2024-model](concepts/31-models/ict-2024-model.md)
- **CRT (Candle Range Theory)** popularized by Romeo / TTrades — community-attributed, not ICT-original. → [candle-range-theory](concepts/21-crt/candle-range-theory.md), [crt-rules](concepts/21-crt/crt-rules.md), [crt-vs-amd](concepts/21-crt/crt-vs-amd.md), [ict-response-to-crt](concepts/21-crt/ict-response-to-crt.md)

## 2025 — New Models & FOMC

- **Venom Model** — released April 2025. NQ/ES/YM 90-min intraday strategy. → [venom-model](concepts/31-models/venom-model.md)
- **Two-stage FOMC delivery** — Sept 2025. → [fomc-two-stage-delivery](concepts/30-news-driven/fomc-two-stage-delivery.md) `(pending)`
- **Advanced liquidity series** — Oct 2025. PD-array nesting strengthened. → [pd-array-nesting](concepts/05-pd-arrays/pd-array-nesting.md) `(pending)`
- **CE as primary entry** — reinforced through 2025. → [ce-as-primary-entry](concepts/06-fair-value-gaps/ce-as-primary-entry.md)
- **macro-times precision update** — `Year Refined: 2025` on all 6 macro files. → [macro-times-overview](concepts/04-time-cycles/macro-times-overview.md)
- **silver-bullet-formalized-2025** — micro-execution timing + CE-primary integration. → [silver-bullet-formalized-2025](concepts/11-silver-bullet/silver-bullet-formalized-2025.md)
- **quarterly-shift-theory IPDA rotation refinement** — added 3-4 month ERL↔IRL rotation. → [quarterly-shift-theory](concepts/04-time-cycles/quarterly-shift-theory.md)
- **pd-array-nesting + pd-array-confluence "strengthening principle"** formalized in October 2025 advanced-liquidity series. → [pd-array-nesting](concepts/05-pd-arrays/pd-array-nesting.md), [pd-array-confluence](concepts/05-pd-arrays/pd-array-confluence.md)
- **Two-stage FOMC delivery model** + **CPI protocol refinement**. → [fomc-two-stage-delivery](concepts/30-news-driven/fomc-two-stage-delivery.md), [cpi-protocol](concepts/30-news-driven/cpi-protocol.md)
- **Quarterly Shift 2025** — IPDA ERL/IRL rotation explicit. → [quarterly-shift-2025](concepts/22-quarterly-theory/quarterly-shift-2025.md)

## 2026 — Static Drawdown & Zircon

- **Zircon Model** — Jan 2026 silent demo (content withheld; flagged demo-stage). → [zircon-model](concepts/31-models/zircon-model.md)
- **Static drawdown adaptation** — prop-firm rule shift; OB hold-time guidance updated. → [static-drawdown-2026](concepts/32-risk-management/static-drawdown-2026.md)

---

## Community-Attributed (NOT ICT-original; flagged separately)

- **2024 — Candle Range Theory (CRT)** — Romeo / TTrades. ICT publicly acknowledged but did not author. → [candle-range-theory](concepts/21-crt/candle-range-theory.md), [crt-rules](concepts/21-crt/crt-rules.md), [crt-vs-amd](concepts/21-crt/crt-vs-amd.md), [ict-response-to-crt](concepts/21-crt/ict-response-to-crt.md)
