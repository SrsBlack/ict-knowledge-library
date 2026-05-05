# Glossary — ICT Abbreviations

Single-page lookup for every abbreviation used in this library. Each entry links to the canonical concept file (file may not yet exist if its phase hasn't shipped — entries marked `(pending)` will be wired up as their phase lands).

Format: `**ABBR**` — full term — short note — link.

---

## A

- **AMD** — Accumulation, Manipulation, Distribution. The three-phase market-maker cycle. → [power-of-three](concepts/12-power-of-three/power-of-three.md)
- **APD** — Algorithmic Price Delivery. The notion that price is delivered by an algorithm, not random walk. → [algorithmic-price-delivery](concepts/03-order-flow/algorithmic-price-delivery.md) `(pending)`
- **ATH / ATL** — All-Time High / All-Time Low.

## B

- **BB** — Breaker Block. An order block whose extreme has been broken; flips polarity. → [breaker-block](concepts/08-breaker-blocks/breaker-block.md)
- **BISI** — Buy-side Imbalance / Sell-side Inefficiency. The bullish form of an FVG. → [bullish-fvg](concepts/06-fair-value-gaps/bullish-fvg.md)
- **BOS** — Break of Structure. Price making a new swing high (bullish) or low (bearish) in the current trend direction. → [bos-bullish](concepts/01-market-structure/bos-bullish.md) / [bos-bearish](concepts/01-market-structure/bos-bearish.md)
- **BPR** — Balanced Price Range. A range with overlapping bullish and bearish FVGs. → [balanced-price-range](concepts/06-fair-value-gaps/balanced-price-range.md)
- **BSL** — Buy-Side Liquidity. Resting buy-stops above swing highs / equal highs. → [buy-side-liquidity](concepts/02-liquidity/buy-side-liquidity.md)

## C

- **CE** — Consequent Encroachment. The 50% midpoint of an FVG. → [consequent-encroachment](concepts/06-fair-value-gaps/consequent-encroachment.md)
- **CHoCH** — Change of Character. A structural break in the opposite direction of the prior trend. → [choch-bullish](concepts/01-market-structure/choch-bullish.md) / [choch-bearish](concepts/01-market-structure/choch-bearish.md)
- **CRT** — Candle Range Theory. Community-attributed (Romeo, ~2024). NOT ICT-original. → [candle-range-theory](concepts/21-crt/candle-range-theory.md) `(pending)`

## D

- **DOL** — Draw On Liquidity. The targeted liquidity pool the algorithm is drawn toward. → [draw-on-liquidity](concepts/02-liquidity/draw-on-liquidity.md)
- **DST** — Daylight Saving Time. Critical for any time-of-day rule; ICT teaches in NY time. → [dst-handling](concepts/04-time-cycles/dst-handling.md)

## E

- **EQH** — Equal Highs. Two or more highs at the same price level — pool of liquidity. → [equal-highs](concepts/02-liquidity/equal-highs.md)
- **EQL** — Equal Lows. Mirror of EQH on the sell side. → [equal-lows](concepts/02-liquidity/equal-lows.md)
- **EQ** — Equilibrium. The 50% midpoint of a dealing range. → [equilibrium-definition](concepts/27-equilibrium/equilibrium-definition.md)
- **ERL** — External Range Liquidity. Liquidity outside the current dealing range. → [external-range-liquidity](concepts/02-liquidity/external-range-liquidity.md)

## F

- **FOMC** — Federal Open Market Committee. The macro event ICT's two-stage delivery model targets. → [fomc-two-stage-delivery](concepts/30-news-driven/fomc-two-stage-delivery.md) `(pending)`
- **FVG** — Fair Value Gap. Three-candle imbalance where the middle candle's range is not overlapped. → [fair-value-gap](concepts/06-fair-value-gaps/fair-value-gap.md)

## H

- **HH / HL / LH / LL** — Higher High / Higher Low / Lower High / Lower Low. The four basic structural relationships between consecutive swings. → [swing-high](concepts/01-market-structure/swing-high.md) / [swing-low](concepts/01-market-structure/swing-low.md)
- **HOD** — High of Day. Daily high; structural reference. → covered in `25-htf-bias`
- **HTF** — Higher Time Frame. Any TF used to set bias for a lower TF entry. → [htf-bias-framework](concepts/25-htf-bias/htf-bias-framework.md)

## I

- **IFVG** — Inversion FVG. A traded-through FVG whose role flips (support↔resistance). → [inversion-fvg](concepts/06-fair-value-gaps/inversion-fvg.md)
- **IPDA** — Interbank Price Delivery Algorithm. ICT's name for the institutional algorithm; uses 20/40/60-day lookbacks. → [ipda-definition](concepts/23-ipda/ipda-definition.md)
- **IRL** — Internal Range Liquidity. Liquidity inside the current dealing range (FVGs, OBs, internal swing points). → [internal-range-liquidity](concepts/02-liquidity/internal-range-liquidity.md)

## L

- **LOD** — Low of Day. Daily low; structural reference. → covered in `25-htf-bias`
- **LTF** — Lower Time Frame. Used for entry refinement.

## M

- **MMBM** — Market Maker Buy Model. AMD running to upside distribution. → [power-of-three](concepts/12-power-of-three/power-of-three.md)
- **MMSM** — Market Maker Sell Model. AMD running to downside distribution. → [power-of-three](concepts/12-power-of-three/power-of-three.md)
- **MSS** — Market Structure Shift. A specific form of CHoCH characterized by displacement through the prior structure level. → [mss](concepts/01-market-structure/mss.md)

## N

- **NDOG** — New Day Opening Gap. Gap between previous day's close and new day's open at midnight NY. → [ndog](concepts/31-models/ndog.md)
- **NFP** — Non-Farm Payrolls. Monthly US labor report; high-impact news. → [nfp-protocol](concepts/30-news-driven/nfp-protocol.md) `(pending)`
- **NWOG** — New Week Opening Gap. Gap between Friday close and Sunday/Monday open. → [nwog](concepts/31-models/nwog.md)
- **NY** — New York time. The canonical timezone for every time-of-day reference in this library (subject to DST). → [dst-handling](concepts/04-time-cycles/dst-handling.md)

## O

- **OB** — Order Block. Last opposite-direction candle before a displacement. → [bullish-order-block](concepts/07-order-blocks/bullish-order-block.md) / [bearish-order-block](concepts/07-order-blocks/bearish-order-block.md)
- **OTE** — Optimal Trade Entry. The 0.62–0.79 retracement zone, typically entered at 0.705. → [ote-overview](concepts/17-optimal-trade-entry/ote-overview.md)

## P

- **PD Array** — Premium / Discount Array. Any institutional price level (FVG, OB, breaker, equilibrium, etc.). → [pd-array-definition](concepts/05-pd-arrays/pd-array-definition.md)
- **PDH / PDL** — Previous Day High / Low. Liquidity reference levels for the current day. → covered in `02-liquidity` and `25-htf-bias`
- **PMH / PML** — Previous Month High / Low. Monthly liquidity reference. → covered in `25-htf-bias`
- **PO3** — Power of Three. Same as AMD. → [power-of-three](concepts/12-power-of-three/power-of-three.md)
- **PWH / PWL** — Previous Week High / Low. Weekly liquidity reference. → covered in `25-htf-bias`

## R

- **R** — R-multiple. Profit/loss measured in units of initial risk. → [r-multiple](concepts/32-risk-management/r-multiple.md)

## S

- **SD** — Standard Deviation (in ICT's projection tool). Used at -1.5, -2, -2.5, -4 SD targets. → [standard-deviation-projections](concepts/28-fibonacci-levels/standard-deviation-projections.md)
- **SIBI** — Sell-side Imbalance / Buy-side Inefficiency. The bearish form of an FVG. → [bearish-fvg](concepts/06-fair-value-gaps/bearish-fvg.md)
- **SMC** — Smart Money Concepts. Community rebrand of ICT material. Distinct from ICT-original.
- **SMT** — Smart Money Technique (divergence). Divergence between correlated assets. → [smt-divergence](concepts/16-smt-divergence/smt-divergence.md)
- **SSL** — Sell-Side Liquidity. Resting sell-stops below swing lows / equal lows. → [sell-side-liquidity](concepts/02-liquidity/sell-side-liquidity.md)

## T

- **TDO** — True Day Open. Midnight NY open of the daily candle. → [true-day-open](concepts/22-quarterly-theory/true-day-open.md) `(pending)`
- **TF** — Time Frame.
- **TWO** — True Week Open. Sunday 18:00 NY (or Monday 00:00 NY depending on broker). → [true-week-open](concepts/22-quarterly-theory/true-week-open.md) `(pending)`

---

## Timeframe Shorthand

Standard chart timeframe abbreviations used throughout the library:

- **M1** — 1-minute
- **M5** — 5-minute
- **M15** — 15-minute
- **M30** — 30-minute
- **H1** — 1-hour
- **H4** — 4-hour
- **D / D1** — Daily
- **W / W1** — Weekly
- **MN / MN1** — Monthly
