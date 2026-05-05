# Vacuum Block

**Category:** 07-order-blocks
**Aliases:** vacuum, gap candle, no-rest block
**ICT Confidence:** medium
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2018-BLOCKS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, vacuum, gap, displacement

## Definition

A vacuum block is a candle that **opens with a gap from the prior close**, leaving an unworked region between the prior candle's close and the current candle's open — a "vacuum" of price. ICT teaches it as related to but distinct from FVG and volume imbalance: vacuum specifically refers to **opening gaps** (typically at session opens, weekly opens, or news releases). Vacuum blocks tend to act like FVGs structurally — algorithm seeks to revisit and rebalance.

## Formal Criteria

A vacuum block:

- Has an **opening gap** from the prior candle's close.
- Bullish vacuum: `open(n) > close(n-1)` with no overlap.
- Bearish vacuum: `open(n) < close(n-1)` with no overlap.
- The gap region is the vacuum.
- Often appears at:
  - Sunday open (weekly gap, see [nwog](../31-models/nwog.md)).
  - Midnight open (NDOG, see [ndog](../31-models/ndog.md)).
  - High-impact news release candles.

## Formula / Math

```
bullish_vacuum(n) := open(n) > close(n-1)
                      AND high(n-1) < open(n)     # strict gap, no wick overlap
vacuum_low  := close(n-1)
vacuum_high := open(n)
vacuum_size := vacuum_high - vacuum_low
```

## Machine-Readable

```json
{
  "id": "vacuum-block",
  "category": "07-order-blocks",
  "aliases": ["vacuum", "gap-candle", "no-rest-block"],
  "criteria": [
    {"id": "c1", "expr": "open(n) gaps from close(n-1)"},
    {"id": "c2", "expr": "no wick overlap between n-1 and n (strict gap)"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["fair-value-gap","volume-imbalance","liquidity-void","ndog","nwog","sunday-open-gap"],
  "sources": ["ICT-2018-BLOCKS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish vacuum block (Sunday open gap example):

   Friday close: 1.0850
   Sunday open:  1.0858

       ▲
       █  ← Sunday's first candle, opens at 1.0858
       █
       O_n = 1.0858
       ──────  ← vacuum: 8-pip gap region
       C_{n-1} = 1.0850
       █
       █  ← Friday's last candle (closed 1.0850)
       ▼

   No wick from either side covers [1.0850, 1.0858] = strict vacuum.
```

## Timeframes

M15+ generally; vacuum gaps on M1/M5 from feed jitter are noise.

## Examples

**Example 1 — bullish weekend vacuum on EURUSD:**
- Friday H1 close 1.0850.
- Sunday H1 open 1.0858.
- → 8-pip bullish vacuum block at [1.0850, 1.0858].
- Algorithm tendency: revisit to fill the vacuum (often within 1–3 days). Provides a discount-side reference for any bullish setup attempting to take HTF BSL.

## Common Mistakes

- **Confusing with FVG.** FVG is a 3-candle wick-non-overlap pattern within continuous trading. Vacuum is a 1-bar gap from prior close to current open — typically at session boundaries.
- **Tiny gaps.** Most opens have small (~1-pip) vacuums that are noise; filter by size.
- **Treating all gaps as fillable.** Strong-trend opens sometimes never fill the gap; the vacuum becomes a permanent structural offset.

## Related Concepts

- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [volume-imbalance](../06-fair-value-gaps/volume-imbalance.md), [liquidity-void](../02-liquidity/liquidity-void.md).
- [ndog](../31-models/ndog.md), [nwog](../31-models/nwog.md), [sunday-open-gap](../31-models/sunday-open-gap.md) — specific vacuum types.

## Citations

- `ICT-2018-BLOCKS`, `ICT-2022-MENTORSHIP-OVERVIEW`.

> Confidence is `medium` because the term "vacuum block" is used inconsistently across the ICT community; some teach it as a synonym for FVG, others reserve it for opening gaps as defined here.
