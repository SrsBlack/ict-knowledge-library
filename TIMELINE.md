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
- **stop-run-definition** + the FVG and OB variants. → [stop-run-definition](concepts/29-stop-runs/stop-run-definition.md), [stop-run-into-fvg](concepts/29-stop-runs/stop-run-into-fvg.md), [stop-run-into-ob](concepts/29-stop-runs/stop-run-into-ob.md)
  ⚠ **[stop-run-into-breaker](concepts/29-stop-runs/stop-run-into-breaker.md) is deliberately NOT in this group** — it stays **2018**, because it depends on breaker vocabulary that does not exist until then (`ICT-2018-BLOCKS`). It was listed here alongside its siblings when all four were mis-dated; the 2026-08-10 pass moved the other three to 2016 on evidence and left this one, which is correctly dated. See the 2018 section.
- **turtle-soup** — ⚠ *re-dated 2018 → 2016 on 2026-08-10.* "Turtle soup is a false breakout pattern" (`ICT-2016-EQUILIBRIUM-DISCOUNT` [32:30], Sep 2016); both directional forms named in one sentence in the following session (`ICT-2016-EQUILIBRIUM-PREMIUM` [07:16–07:21]). **Not ICT-original** — he credits Raschke and Connors' *Street Smarts* outright ([30:19], [32:53] of `ICT-2017-INTRADAY-TOP-DOWN`) and adds the requirement that the raid land in a pre-identified HTF discount array. → [turtle-soup](concepts/20-turtle-soup/turtle-soup.md), [bullish-turtle-soup](concepts/20-turtle-soup/bullish-turtle-soup.md), [bearish-turtle-soup](concepts/20-turtle-soup/bearish-turtle-soup.md), [stop-hunt-pattern](concepts/20-turtle-soup/stop-hunt-pattern.md)
- **SMT divergence** — ⚠ *re-dated 2018 → 2016.* The definitional lecture is Nov 2016: "SMT … stands for smart money tool or smart money technique and we're going to be looking for a divergence between closely correlated or inversely correlated assets" (`ICT-2016-USDX-SMT` [02:21]). → [smt-divergence](concepts/16-smt-divergence/smt-divergence.md), [correlated-pairs-smt](concepts/16-smt-divergence/correlated-pairs-smt.md), [smt-confirmation](concepts/16-smt-divergence/smt-confirmation.md)
- **relative-equal-highs-lows (REH/REL)** — ⚠ *re-dated 2018 → 2016.* Dec 2016: "relatively equal highs" and the buy stops parked above them (`ICT-2016-DOUBLE-TOP-BOTTOM` [00:52, 04:27]); the exact term "relative equal lows" at `ICT-2016-LIQUIDITY-POOLS` [17:59]. → [relative-equal-highs-lows](concepts/02-liquidity/relative-equal-highs-lows.md)
- **Gap classification** taxonomy (FVG vs VI vs liquidity-void) and **volume-imbalance** — ⚠ *re-dated 2018 → 2016.* All three Dec-2016 lectures: the two-candle body gap named a "common gap" (`ICT-2016-LIQUIDITY-VOIDS` [12:23–12:37]), the same gap taught in `ICT-2016-FVG-REINFORCED` [12:26–13:33], and the breakaway/exhaustion roles in `ICT-2016-VACUUM-BLOCK` [12:48, 02:57–03:06]. → [gap-classification](concepts/09-displacement/gap-classification.md), [volume-imbalance](concepts/06-fair-value-gaps/volume-imbalance.md), [volume-imbalance-detail](concepts/26-imbalance/volume-imbalance-detail.md)
- **symmetrical-price-projections** — ⚠ *re-dated 2018 → 2016.* Equal-distance projection taught Oct 2016: "the second leg in price higher is equal to that first one" (`ICT-2016-MMT-FALSE-BREAKOUT` [17:23]). → [symmetrical-price-projections](concepts/28-fibonacci-levels/symmetrical-price-projections.md)
- **buy-side-liquidity (BSL)** — resting buy stops above swing highs. → [buy-side-liquidity](concepts/02-liquidity/buy-side-liquidity.md)
- **sell-side-liquidity (SSL)** — resting sell stops below swing lows. → [sell-side-liquidity](concepts/02-liquidity/sell-side-liquidity.md)
- **liquidity-pool** — umbrella term for stop clusters. → [liquidity-pool](concepts/02-liquidity/liquidity-pool.md)
- **market-efficiency-paradigm** — markets are efficient FOR smart money; everyone else is the liquidity. → [market-efficiency-paradigm](concepts/03-order-flow/market-efficiency-paradigm.md)
- **reclaimed-order-block** — reinforcing order-block theory; opposing-leg blocks re-used as entries. → [reclaimed-order-block](concepts/07-order-blocks/reclaimed-order-block.md)
- **timeframe-selection** — timeframe-to-style map (monthly=position, weekly=swing, daily=short-term, H4-and-below=day trading); five trader models; ICT's own three setups. → [timeframe-selection](concepts/25-htf-bias/timeframe-selection.md)
- **macro-to-micro-framework** — a 3–6 month currency outlook from the 30-year bond and 10-year note against the dollar index; 10Y-vs-30Y internal SMT divergence; cascade to pairs. → [macro-to-micro-framework](concepts/03-order-flow/macro-to-micro-framework.md)
- **market-protraction** — a small counter-directional impulse swing at 20:00 / 00:00 / 07:00 NY; the parent concept of the Judas swing. ⚠ Its use of the term "Judas swing" re-dates [judas-swing](concepts/13-judas-swing/judas-swing.md) and [london-judas-swing](concepts/13-judas-swing/london-judas-swing.md) from 2018 to 2016. → [market-protraction](concepts/13-judas-swing/market-protraction.md)
- **market-maker-trap** — classical retail patterns (flag, breakout, trendline, head & shoulders) printed against HTF order flow; four lectures, one page. Also re-dates [trendline-liquidity](concepts/02-liquidity/trendline-liquidity.md) from 2017 to 2016. → [market-maker-trap](concepts/31-models/market-maker-trap.md)
- **anticipatory-setup-development** — two monthly candles define the range; the armed one is an order block and the other the objective. → [anticipatory-setup-development](concepts/25-htf-bias/anticipatory-setup-development.md)
- **interest-rate-triad** — 30-year / 10-year / 5-year read against each other; a failure swing in one validates a dollar-index PD array, and its absence is a pass rule. → [interest-rate-triad](concepts/03-order-flow/interest-rate-triad.md)
- **session-overview** — six-session NY-time map. → [session-overview](concepts/15-sessions/session-overview.md)
- **asia-session** — accumulation window. → [asia-session](concepts/15-sessions/asia-session.md)
- **london-session** — manipulation + expansion window. → [london-session](concepts/15-sessions/london-session.md)
- **ny-am-session** — distribution window. → [ny-am-session](concepts/15-sessions/ny-am-session.md)
- **ny-pm-session** — secondary delivery / reversals. → [ny-pm-session](concepts/15-sessions/ny-pm-session.md)
- **london-close** — European unwind window. → [london-close](concepts/15-sessions/london-close.md)
- **session-overlaps** — overlap windows defined. → [session-overlaps](concepts/15-sessions/session-overlaps.md)
- **session-vs-killzone** — terminology distinction. → [session-vs-killzone](concepts/15-sessions/session-vs-killzone.md)
- **institutional-order-flow** — base flow-reading concept. → [institutional-order-flow](concepts/03-order-flow/institutional-order-flow.md)
- **dst-handling** — NY-clock anchoring discipline established. → [dst-handling](concepts/04-time-cycles/dst-handling.md)
- **All 5 killzones + supporting files**. → [killzone-overview](concepts/10-killzones/killzone-overview.md), [asia-killzone](concepts/10-killzones/asia-killzone.md), [london-open-killzone](concepts/10-killzones/london-open-killzone.md), [ny-am-killzone](concepts/10-killzones/ny-am-killzone.md), [london-close-killzone](concepts/10-killzones/london-close-killzone.md), [ny-pm-killzone](concepts/10-killzones/ny-pm-killzone.md), [killzone-times-table](concepts/10-killzones/killzone-times-table.md), [killzone-vs-session](concepts/10-killzones/killzone-vs-session.md)
- **Asian range** + bounds. → [asian-range](concepts/14-asian-range/asian-range.md), [asian-range-high](concepts/14-asian-range/asian-range-high.md), [asian-range-low](concepts/14-asian-range/asian-range-low.md)
- **Imbalance umbrella** vocabulary. → [imbalance-definition](concepts/26-imbalance/imbalance-definition.md), [inefficiency](concepts/26-imbalance/inefficiency.md), [imbalance-vs-fvg](concepts/26-imbalance/imbalance-vs-fvg.md)

## 2017 — Charter Year

Refinements of FVG and OB definitions; introduction of OTE and Fibonacci levels; structure terminology formalized.

- **fib-anchoring** — fib attaches to candle **bodies**, not wicks, because wicks are the broker-variable part of a candle. → [fib-anchoring](concepts/28-fibonacci-levels/fib-anchoring.md)
- **ny-judas-swing** and **judas-swing-failure** — ⚠ *re-dated 2018 → 2017 on 2026-08-10.* ICT enumerates **four** session Judas swings, not two: "the London open for Judas, the CME open for the New York Judas, and Asia it has its Judas at eight o'clock … and then you have it also in London close" (`ICT-2017-MARKET-REVERSALS` [28:07], May 2017). The NY variant is anchored to the **08:20 CME open** and faded into the 5-day ADR bound (`ICT-2017-BREAD-BUTTER-BUY` [19:12–19:35]). ⚠ The *failure* page is dated to its nearest antecedent only — the **delayed protraction** of `ICT-2017-INTRADAY-PROFILES` — since "Judas swing failure" is not a label ICT uses anywhere in the corpus. ⚠ **The Asia and London-close Judas swings are named in the corpus and remain undocumented in this library.** → [ny-judas-swing](concepts/13-judas-swing/ny-judas-swing.md), [judas-swing-failure](concepts/13-judas-swing/judas-swing-failure.md)
- **asian-range-projections** — ⚠ *re-dated 2018 → 2017.* The Asian range used as a standard-deviation unit: buy 1–2 SD below it coupled with a discount PD array, scale every 2 SD, 40-pip stop (`ICT-2017-DAYTRADE-HIGH-PROBABILITY` [07:48, 11:05–11:21, 14:49, 16:38], Apr 2017). → [asian-range-projections](concepts/14-asian-range/asian-range-projections.md)
- **index-smt** — ⚠ *re-dated 2018 → 2017.* Relative highs/lows compared across NASDAQ, Dow and E-mini S&P in a **05:00–09:30 NY** window; "one index will fail to confirm a lower low … that's your bullish confirmation" (`ICT-2017-INDEX-SMT-AM-TREND` [07:57–08:13], Jun 2017). → [index-smt](concepts/16-smt-divergence/index-smt.md)
- **The four-tier top-down protocol** (Aug 2017, Month 12) — monthly→weekly, weekly→daily, daily→H4, H4→M5, with each tier **replacing** the prior tier's inputs rather than repeating them. → [top-down-analysis](concepts/25-htf-bias/top-down-analysis.md), [monthly-bias](concepts/25-htf-bias/monthly-bias.md), [weekly-bias](concepts/25-htf-bias/weekly-bias.md), [daily-bias](concepts/25-htf-bias/daily-bias.md), [pd-array-matrix](concepts/05-pd-arrays/pd-array-matrix.md)
- **ict-core-patterns** — ICT's complete executable repertoire under a condition → stage → execution frame: **two patterns plus a contingency** — OTE, turtle soup, and the breaker when the turtle soup is missed. "A buy program, a sell program, and… if I get it wrong program" (`ICT-2017-INTRADAY-TOP-DOWN` [39:31]). → [ict-core-patterns](concepts/31-models/ict-core-patterns.md)
- **flout** — CBDR and Asian range combined; its standard deviation is **half** the range projected from the centre, with an **unbounded** deviation count against the Asian range's 1–2. → [flout](concepts/15-sessions/flout.md)
- **Futures session structure** (Jun 2017, Month 10) — bond opening range 08:00–09:00 and index 09:30–10:30 NY; the ZB split-session day map; AM trend 09:30–12:00 and PM trend 13:00–16:00. → [futures-opening-range](concepts/15-sessions/futures-opening-range.md), [bond-split-session-rules](concepts/15-sessions/bond-split-session-rules.md), [index-am-pm-trend](concepts/15-sessions/index-am-pm-trend.md), [bond-trending-and-consolidation-days](concepts/31-models/bond-trending-and-consolidation-days.md)
- **Multi-asset and relative-strength framework** — the four-asset-class regime read (coupling sets magnitude, not direction) and leader-vs-sympathetic ranking against the dollar index. → [multi-asset-analysis](concepts/03-order-flow/multi-asset-analysis.md), [relative-strength-analysis](concepts/03-order-flow/relative-strength-analysis.md), [stock-watchlist-construction](concepts/31-models/stock-watchlist-construction.md)
- **draw-on-liquidity (DOL)** and **liquidity-matrix** — ⚠ *re-dated 2021 → 2017.* The draw mechanic is taught unnamed in Jan 2017 — "it's going to be drawn to a level, or it's going to repel from a level … it's seeking large fund liquidity" (`ICT-2017-IPDA-DATA-RANGES` [41:12–41:17]) — and only **named** three years later (`ICT-2020-OTE-VOL17` [00:39–00:50]). The premium/discount matrix is defined in Feb 2017 (`ICT-2017-PD-ARRAY-MATRIX` [04:21–04:27]). → [draw-on-liquidity](concepts/02-liquidity/draw-on-liquidity.md), [liquidity-matrix](concepts/02-liquidity/liquidity-matrix.md)
- **seasonal-tendency** — recurring annual tendency; the *ideal* form is maximum opposition between a pair's seasonal chart and the US Dollar Index seasonal chart. → [seasonal-tendency](concepts/04-time-cycles/seasonal-tendency.md)
- **bond-yield-analysis** — the 10-year note against the dollar index; tandem movement = consolidation, inverse = trending; "crack in correlation" as an SMT divergence. → [bond-yield-analysis](concepts/03-order-flow/bond-yield-analysis.md)
- **explosive-market-selection** — the eight hallmarks of an explosive swing trade; also **refines** the COT zero line (recentred 12-month midpoint) and open interest (10–15 % gate). → [explosive-market-selection](concepts/31-models/explosive-market-selection.md), [commitment-of-traders](concepts/03-order-flow/commitment-of-traders.md), [open-interest](concepts/03-order-flow/open-interest.md)
- **ict-day-trading-model** — 65–70 % of the daily range, five-day ADR, Sunday-opening-price filter, day-of-week profiles; 0 GMT entries for HTF setups. → [ict-day-trading-model](concepts/31-models/ict-day-trading-model.md)
- **swing-trading-hallmarks** — seven cumulative checks for swing-trade validity; static rule filtering; also **refines** [r-multiple](concepts/32-risk-management/r-multiple.md) with the breakeven-accuracy arithmetic. → [swing-trading-hallmarks](concepts/31-models/swing-trading-hallmarks.md)
- **projected-range-objectives** — taxonomy of index-futures daily profiles across AM / lunch / PM; the PM continuation filter keys off the timeframe rank of the AM's reversal array. → [projected-range-objectives](concepts/31-models/projected-range-objectives.md)
- **equity-seasonal-windows** — three divisions of the stock year, the May–October low-magnitude period, and the month-by-month Dow tendency table. → [equity-seasonal-windows](concepts/04-time-cycles/equity-seasonal-windows.md)
- **sentiment-effect** — short-term sentiment is maximally opposed at the entry; Asian-range and midnight-NY-open day-trade conditions with a 10-period Williams %R on M15. → [sentiment-effect](concepts/31-models/sentiment-effect.md)
- **Swing risk discipline merged** into [risk-per-trade](concepts/32-risk-management/risk-per-trade.md) (3:1 leverage, H4 entries on monthly/weekly frames) and [r-multiple](concepts/32-risk-management/r-multiple.md) (200–500 pip ranges yielding up to 10R).
- **central-bank-dealers-range** — 2pm–8pm NY range, ideal <40 pips, standard deviations 1–4 frame the next day. → [central-bank-dealers-range](concepts/15-sessions/central-bank-dealers-range.md)
- **open-interest** — outstanding futures contracts; rising OI in a trend = sponsorship. → [open-interest](concepts/03-order-flow/open-interest.md)
- **dollar-index** — USDX/DXY as intermarket reference for FX, commodities and seasonals. → [dollar-index](concepts/03-order-flow/dollar-index.md)
- **commitment-of-traders** — weekly CFTC report; commercial net position above/below the zero line = buy/sell program. → [commitment-of-traders](concepts/03-order-flow/commitment-of-traders.md)
- **open-float-liquidity-pool** — 60 trading days back + 60 cast forward; highest high / lowest low = large-fund pools. → [open-float-liquidity-pool](concepts/02-liquidity/open-float-liquidity-pool.md)
- **interest-rate-differentials** — central-bank policy-rate spread as the start of the macro read. → [interest-rate-differentials](concepts/03-order-flow/interest-rate-differentials.md)
- **premium-vs-carrying-charge-market** — nearby vs next month out; no premium = carrying charge. → [premium-vs-carrying-charge-market](concepts/03-order-flow/premium-vs-carrying-charge-market.md)
- **mega-trade** — the one prolonged annual move per market; months-long, seasonally driven, sponsorship-verified. → [mega-trade](concepts/31-models/mega-trade.md)
- **filling-the-numbers** — the daily range fills ~four reference levels; zero-GMT pivot ladder. → [filling-the-numbers](concepts/04-time-cycles/filling-the-numbers.md)
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
- **time-of-day pivots** (TDO/PDH/PDL/session-extreme references). → [time-of-day-pivots](concepts/04-time-cycles/time-of-day-pivots.md)
- **Asian range sweep + Asian session bias** terminology. → [asian-range-sweep](concepts/14-asian-range/asian-range-sweep.md), [asian-session-bias](concepts/14-asian-range/asian-session-bias.md)
- **imbalance-rebalance** state lifecycle terminology. → [imbalance-rebalance](concepts/26-imbalance/imbalance-rebalance.md)
- **bullish/bearish-order-flow + order-flow-shift + smart-money-footprint** — directional flow + shift + multi-signature scoring. → [bullish-order-flow](concepts/03-order-flow/bullish-order-flow.md), [bearish-order-flow](concepts/03-order-flow/bearish-order-flow.md), [order-flow-shift](concepts/03-order-flow/order-flow-shift.md), [smart-money-footprint](concepts/03-order-flow/smart-money-footprint.md)
- **balanced-price-range (BPR)** introduced. → [balanced-price-range](concepts/06-fair-value-gaps/balanced-price-range.md)
- **reversal-order-block** vs **continuation-order-block** distinction (refined 2023). → [reversal-order-block](concepts/07-order-blocks/reversal-order-block.md), [continuation-order-block](concepts/07-order-blocks/continuation-order-block.md)
- **breaker-block** introduced; **mitigation-block** distinct concept. → [breaker-block](concepts/08-breaker-blocks/breaker-block.md), [bullish-breaker](concepts/08-breaker-blocks/bullish-breaker.md), [bearish-breaker](concepts/08-breaker-blocks/bearish-breaker.md), [breaker-vs-mitigation](concepts/08-breaker-blocks/breaker-vs-mitigation.md), [failed-breaker](concepts/08-breaker-blocks/failed-breaker.md)
- **mitigation** as a state concept. → [mitigation-definition](concepts/18-mitigation/mitigation-definition.md), [mitigation-of-ob](concepts/18-mitigation/mitigation-of-ob.md), [mitigation-of-fvg](concepts/18-mitigation/mitigation-of-fvg.md), [mitigation-of-breaker](concepts/18-mitigation/mitigation-of-breaker.md), [partial-vs-full-mitigation](concepts/18-mitigation/partial-vs-full-mitigation.md)
- **fvg-mitigation** as state lifecycle, **liquidity-void-vs-fvg** disambiguation, **nested-fvg** confluence. → [fvg-mitigation](concepts/06-fair-value-gaps/fvg-mitigation.md), [liquidity-void-vs-fvg](concepts/06-fair-value-gaps/liquidity-void-vs-fvg.md), [nested-fvg](concepts/06-fair-value-gaps/nested-fvg.md)
- **PD array** vocabulary refined (premium / discount / hierarchy / dealing-range EQ). → [pd-array-definition](concepts/05-pd-arrays/pd-array-definition.md), [premium-array](concepts/05-pd-arrays/premium-array.md), [discount-array](concepts/05-pd-arrays/discount-array.md), [pd-array-hierarchy](concepts/05-pd-arrays/pd-array-hierarchy.md), [dealing-range](concepts/05-pd-arrays/dealing-range.md), [equilibrium-definition](concepts/27-equilibrium/equilibrium-definition.md), [dealing-range-equilibrium](concepts/27-equilibrium/dealing-range-equilibrium.md), [equilibrium-as-decision-point](concepts/27-equilibrium/equilibrium-as-decision-point.md), [mean-threshold](concepts/27-equilibrium/mean-threshold.md)

## 2018 — Block Vocabulary Expansion

Mitigation, propulsion, rejection, vacuum block taxonomy; IFVG and CE introduced.

⚠ **This section was substantially wrong until 2026-08-10.** It previously claimed eight further
concept groups for 2018 — relative equal highs/lows, the NY and failed Judas swings, Asian-range
projections, gap classification, volume imbalance, symmetrical price projections, turtle soup and
SMT divergence. None of them had a 2018 source: each cited only the placeholder pair
`ICT-2017-CHARTER-OVERVIEW` + `ICT-2022-MENTORSHIP-OVERVIEW`. A full corpus read re-dated all of
them to **2016–2017** and moved them into those sections. What remains below is the material that
genuinely traces to 2018.

- **IPDA** introduced as the algorithm-name for institutional price delivery; 20/40/60-day lookback ranges established. → [ipda-definition](concepts/23-ipda/ipda-definition.md), [ipda-data-ranges](concepts/23-ipda/ipda-data-ranges.md), [ipda-20-day-lookback](concepts/23-ipda/ipda-20-day-lookback.md), [ipda-40-day-lookback](concepts/23-ipda/ipda-40-day-lookback.md), [ipda-60-day-lookback](concepts/23-ipda/ipda-60-day-lookback.md), [ipda-reference-points](concepts/23-ipda/ipda-reference-points.md)
- **algorithmic-price-delivery (APD)** — meta-thesis introduced alongside IPDA. → [algorithmic-price-delivery](concepts/03-order-flow/algorithmic-price-delivery.md)
- **inversion-fvg (IFVG)** introduced; **consequent-encroachment (CE)** introduced. → [inversion-fvg](concepts/06-fair-value-gaps/inversion-fvg.md), [consequent-encroachment](concepts/06-fair-value-gaps/consequent-encroachment.md)
- **smt-failure** — ⚠ **retained here as an open question, not as a sourced 2018 introduction.** An enumeration of every SMT mention in the corpus (~90 mentions across 20 packets, all 153 searched) found no lecture teaching SMT *failure*; the page carries `medium` confidence and an unverified-dating warning. → [smt-failure](concepts/16-smt-divergence/smt-failure.md)
- **stop-run-into-breaker** — the breaker-targeted stop run; stays 2018 because breaker vocabulary begins here, unlike its three siblings which are evidenced to 2016. → [stop-run-into-breaker](concepts/29-stop-runs/stop-run-into-breaker.md)
- **propulsion-block, vacuum-block, rejection-block, mitigation-block** taxonomy. → [propulsion-block](concepts/07-order-blocks/propulsion-block.md), [vacuum-block](concepts/07-order-blocks/vacuum-block.md), [rejection-block](concepts/19-rejection-blocks/rejection-block.md), [bullish-rejection-block](concepts/19-rejection-blocks/bullish-rejection-block.md), [bearish-rejection-block](concepts/19-rejection-blocks/bearish-rejection-block.md), [mitigation-block](concepts/08-breaker-blocks/mitigation-block.md)

## 2019 — Quiet / Iteration

Mostly refinements; few new named concepts. No concept files in this library trace to a 2019 introduction date; refinements from this period are folded into the 2018 / 2020 / 2022 entries.

## 2020 — Free Tutoring Series

Public YouTube re-teach of foundations. PO3 / AMD codified for free audience. Most concepts re-taught here were originally introduced in 2016 (PO3) or 2017–2018 (vocabulary expansions); no concept files have a 2020 introduction date. The 2020 contribution shows up in `Year Refined` fields and in 2022 mentorship operationalizations.

## 2021 — DOL & Liquidity Matrix

IRL/ERL distinction emerges.

⚠ **Both concepts formerly listed here were re-dated to 2017 on 2026-08-10** and moved to that
section: each claimed 2021 while citing only a 2022 source. The **name** "draw on liquidity" is
nonetheless a later coinage than the idea — ICT names it on air in Jun 2020 ("that's the reason why
I call it a draw on liquidity", `ICT-2020-OTE-VOL17` [00:39–00:50]) having taught the mechanic
unnamed in Jan 2017. The 2021 heading is retained because the *vocabulary* did consolidate in this
period, but no concept file now carries a 2021 introduction date.

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
- **Two-stage FOMC delivery** — Sept 2025. → [fomc-two-stage-delivery](concepts/30-news-driven/fomc-two-stage-delivery.md)
- **Advanced liquidity series** — Oct 2025. PD-array nesting strengthened. → [pd-array-nesting](concepts/05-pd-arrays/pd-array-nesting.md)
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
