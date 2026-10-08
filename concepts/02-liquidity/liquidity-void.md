# Liquidity Void

**Category:** 02-liquidity
**Aliases:** void, price void
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY-VOIDS, ICT-2016-FVG-REINFORCED, ICT-2016-FAIR-VALUATION, ICT-2016-TIMEFRAME-SELECTION, ICT-2022-MENTORSHIP-EP38
**Tags:** liquidity, void, displacement, gap

> ⚠ **Re-dated 2026-10-08.** Previously `Year Introduced: 2017` cited only to the placeholder `ICT-2017-DISPLACEMENT`. The term and full lecture are Dec 2016 (`ICT-2016-LIQUIDITY-VOIDS`); earlier uses exist as far back as Sep–Nov 2016. See citations.

## Definition

A liquidity void is a wide, fast-traversed price region produced by displacement that left no two-sided trade behind it. ICT: "a liquidity void is a range in price delivery where one side of the market liquidity is shown in wide or long one-sided ranges or candles" (`ICT-2016-LIQUIDITY-VOIDS`, 00:57); "this causes a price imbalance, or as we call it, displacement" (01:54); "long bodied candles where price has only been delivered on the downside" (03:08). Whether a void gets re-filled is **ERA-SPLIT**, not a settled rule: 2016 — "price typically will want to revisit this porous range or void of contrarian liquidity" (01:09); 2022 — "I don't teach that… I'm not trying to insist that these imbalances completely rebalance" (`ICT-2022-MENTORSHIP-EP38`, 04:56–05:26). See Common Mistakes for both quotes in full.

## Formal Criteria

- A multi-candle expansion has produced a wide directional move with minimal counter-trend pullback: "long or wide one-sided ranges or candles" (`ICT-2016-LIQUIDITY-VOIDS`, 00:57).
- ICT presents the void as the **same imbalance viewed on a lower timeframe**, not a separate structural class from a [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md): "on a lower timeframe, it would many times appear as a liquidity void, where it's multiple candles that create that open space of range" (`ICT-2016-FVG-REINFORCED`, 05:26); he teaches "the overlap of liquidity voids and fair value gaps" directly (09:43). Treat "distinct structural concept" as an overstatement — the multi-candle description is correct, the claim of a separate class is not.
- No fixed directional-close percentage, pullback fraction, or FVG-containment rule is given — see Formula / Math.

## Formula / Math

ICT gives **no quantitative threshold** for a liquidity void. Searched "80 percent"/"eighty percent," "0.3," and "pullback" near "void" in both corpora (153 2016-17/2020-21 packets, 41 2022 episodes): all "80%" hits are position-sizing or audience-share contexts, unrelated to voids. The library's prior thresholds are **invented**:

```
# ICT gives no number for this:
directional_close_pct >= 0.8
max_pullback_within_span <= 0.3 * expansion_size
contains_at_least_one_FVG == true
```

ICT's own description is qualitative: wide/long one-sided candles, minimal opposing wicks, displacement present.

## Machine-Readable

```json
{
  "id": "liquidity-void",
  "category": "02-liquidity",
  "aliases": ["void", "price-void"],
  "criteria": [
    {"id": "c1", "expr": "wide, long one-sided candles with minimal opposing wicks (qualitative — ICT gives no numeric threshold)"},
    {"id": "c2", "expr": "displacement present"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["fair-value-gap","liquidity-void-vs-fvg","displacement-definition","range-expansion","vacuum-block"],
  "sources": ["ICT-2016-LIQUIDITY-VOIDS","ICT-2016-FVG-REINFORCED","ICT-2016-FAIR-VALUATION","ICT-2016-TIMEFRAME-SELECTION","ICT-2022-MENTORSHIP-EP38"]
}
```

## Visual Pattern

```
   ▲
   █ ←  start of void: wide candle, body fills almost entire range
   █
   █
   █ ←  one-color expansion, minimal opposing wicks
   █
   █
   █
   ▼

   ICT's defining example is drawn on a one-minute chart:
   "this is a one minute chart because the one minute chart is going
   to give me the opportunity to show you how there are pockets in
   these big rooms" (ICT-2016-LIQUIDITY-VOIDS, 03:23).
```

## Timeframes

All TFs — ICT's own defining example is **M1**, not M15+. Do not present "voids on M1 are noise" as ICT's position.

## Examples

**Example 1 — H1 bearish void:**
- During a news release, EURUSD prints six consecutive red H1 candles with minimal opposing wicks.
- → liquidity void, by ICT's qualitative description (wide one-sided candles, displacement present).

## Common Mistakes

- **Treating void and FVG as separate structural classes.** ICT presents the void as the same imbalance seen on a different timeframe, with voids and FVGs overlapping — not a strict "void is bigger than FVG" hierarchy.
- **Inventing numeric thresholds.** No 80%-close, 0.3-pullback, or FVG-containment rule is in the corpus.
- **"Voids always get re-filled" stated without era label.** This is **ERA-SPLIT**: 2016 says they typically get revisited, with no time limit — "price typically will want to revisit this porous range or void of contrarian liquidity" (`ICT-2016-LIQUIDITY-VOIDS`, 01:09); "there's no specific time limit on how long it's going to take for these voids to close in… they can stay open for months" (02:19–02:43). 2022 explicitly rejects full-refill teaching, naming "chris laurie" [Chris Lori]'s void-refill claim and distancing from it: "he talks about liquidity voids where he teaches how the market wants to come back down and fill all that area in — as you probably noticed, I don't teach that… I'm not trying to insist that these imbalances completely rebalance" (`ICT-2022-MENTORSHIP-EP38`, 04:56–05:26). State both eras explicitly when discussing refill expectations; do not collapse them into one claim.
- **"Most useful M15+."** Contradicted in emphasis — ICT's own teaching example is M1.

## Related Concepts

- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) — the same imbalance, often the lower-timeframe view of a void.
- [liquidity-void-vs-fvg](../06-fair-value-gaps/liquidity-void-vs-fvg.md) — disambiguation.
- [displacement-definition](../09-displacement/displacement-definition.md) — what creates a void.
- [range-expansion](../01-market-structure/range-expansion.md) — phase that produces voids.
- [vacuum-block](../07-order-blocks/vacuum-block.md) — related "no rest" concept.

## Citations

- `ICT-2016-LIQUIDITY-VOIDS` (00:57) "a liquidity void is a range in price delivery where one side of the market liquidity is shown in wide or long one-sided ranges or candles"; (01:09) "price typically will want to revisit this porous range or void of contrarian liquidity"; (01:54) "this causes a price imbalance, or as we call it, displacement"; (02:19–02:43) no time limit, can stay open for months; (03:08) "long bodied candles where price has only been delivered on the downside"; (03:23) the one-minute-chart defining example.
- `ICT-2016-FVG-REINFORCED` (05:26) "on a lower timeframe, it would many times appear as a liquidity void"; (09:43) "the overlap of liquidity voids and fair value gaps."
- `ICT-2016-FAIR-VALUATION` (24:40) "those areas of liquidity voids and liquidity pools above old highs."
- `ICT-2016-TIMEFRAME-SELECTION` (46:57) "you'll trade in liquidity voids."
- `ICT-2022-MENTORSHIP-EP38` (04:56–05:26) rejects "chris laurie" [Chris Lori]'s full-refill teaching: "I don't teach that… I'm not trying to insist that these imbalances completely rebalance."
