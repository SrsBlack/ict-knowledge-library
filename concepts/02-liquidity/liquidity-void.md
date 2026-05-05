# Liquidity Void

**Category:** 02-liquidity
**Aliases:** void, price void, low-liquidity zone, vacuum zone
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, void, displacement, gap

## Definition

A liquidity void is a wide, fast-traversed price region produced by displacement that left no two-sided trade behind it — essentially a price corridor with no rest, where the algorithm raced through without filling orders in either direction. Distinct from a [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) (which is a 3-candle inefficiency); a liquidity void is a *larger structural concept* covering a multi-candle expansion span. Voids tend to get re-filled later because price seeks to re-test the unworked zone.

## Formal Criteria

- A multi-candle expansion has produced a wide directional move with minimal counter-trend pullback.
- The covered span contains few or no opposing wicks (i.e., no two-sided auction).
- One or more FVGs are typically nested inside the void.
- The span is identified visually as a "wall" of mostly-one-color candles with empty space inside.

## Formula / Math

```
expansion_span(start, end) := price range covered by displacement from bar start to bar end

void := expansion_span where:
  - directional_close_pct >= 0.8      [80%+ closes in same direction]
  - max_pullback_within_span <= 0.3 * expansion_size
  - contains_at_least_one_FVG == true
```

## Machine-Readable

```json
{
  "id": "liquidity-void",
  "category": "02-liquidity",
  "aliases": ["void", "price-void", "vacuum-zone"],
  "criteria": [
    {"id": "c1", "expr": "directional_close_pct >= 0.8"},
    {"id": "c2", "expr": "max_pullback_within_span <= 0.3 * expansion_size"},
    {"id": "c3", "expr": "contains_fvg == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["fair-value-gap","liquidity-void-vs-fvg","displacement-definition","range-expansion","vacuum-block"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   ▲
   █ ←  start of void: wide candle, body fills almost entire range
   █
   █
   █ ←  3-5 bars of one-color expansion
   █
   █
   █  ←  end of void: still no real pullback
   ▼

   inside the void: 1-3 nested FVGs that price is expected
   to revisit and rebalance.
```

## Timeframes

Most useful M15+ — voids on M1 are noise. HTF voids (H4, D) are major draws when they remain unrebalanced.

## Examples

**Example 1 — H1 bearish void:**
- During NFP release, EURUSD prints six consecutive red H1 candles, total range 80 pips, max pullback 12 pips.
- → liquidity void. The void contains 2 nested SIBI FVGs.
- Subsequent days often retrace into the void to rebalance the FVGs.

## Common Mistakes

- **Confusing void with FVG.** FVG is a specific 3-candle pattern; void is a multi-candle structural span. See [liquidity-void-vs-fvg](../06-fair-value-gaps/liquidity-void-vs-fvg.md) for the disambiguation.
- **Expecting full retrace.** Voids often partially rebalance (CE of internal FVGs is enough); insisting on full void fill is too literal.
- **Counting choppy moves as voids.** A move with substantial pullback within the span doesn't qualify even if the net travel is large.

## Related Concepts

- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) — smaller-scale inefficiency nested inside voids.
- [liquidity-void-vs-fvg](../06-fair-value-gaps/liquidity-void-vs-fvg.md) — disambiguation.
- [displacement-definition](../09-displacement/displacement-definition.md) — what creates a void.
- [range-expansion](../01-market-structure/range-expansion.md) — phase that produces voids.
- [vacuum-block](../07-order-blocks/vacuum-block.md) — related "no rest" concept.

## Citations

- `ICT-2017-DISPLACEMENT` — displacement leaving voids.
- `ICT-2022-MENTORSHIP-OVERVIEW` — void as a draw concept.
