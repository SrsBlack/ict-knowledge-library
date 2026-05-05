# Displacement — Definition

**Category:** 09-displacement
**Aliases:** displacement, expansion candle, momentum candle, force candle
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** displacement, momentum, foundational

## Definition

Displacement is **a fast, forceful, directional price move** — typically a single candle (or a short cluster) with a wide range, dominant body, minimal opposing wick, and almost-pure directional close. ICT uses displacement as the visual signature of **algorithmic intent**: a displacement candle is when the algorithm "delivered" the move with conviction. Displacement is the **filter** that separates real OBs / FVGs / MSS events from noise — without displacement, the structural pattern is weaker.

## Formal Criteria

A displacement candle:

- **Wide body** — body size significantly larger than the recent average (often ≥ 1.5× recent average body).
- **Dominant body** — body covers most of the candle range (typically ≥ 70%).
- **Minimal opposing wick** — wick on the opposite side of intended direction is small (≤ 20% of range).
- **Directional close** — close in the direction of the displacement (top half for bullish, bottom half for bearish).
- Often **leaves an FVG** in its wake (this is the operational test ICT uses for displacement).

## Formula / Math

```
range_n   = high(n) - low(n)
body_n    = abs(close(n) - open(n))
upper_wick = high(n) - max(open(n), close(n))
lower_wick = min(open(n), close(n)) - low(n)

is_displacement(n) :=
    body_n >= 1.5 * avg_body_recent
    AND body_n / range_n >= 0.70
    AND opposing_wick / range_n <= 0.20
    AND close direction consistent

# Operational ICT shortcut:
is_displacement_simple(n) := leaves_fvg_inside_or_through(n)
```

## Machine-Readable

```json
{
  "id": "displacement-definition",
  "category": "09-displacement",
  "aliases": ["displacement", "expansion-candle", "momentum-candle", "force-candle"],
  "criteria": [
    {"id": "c1", "expr": "body >= 1.5 * avg_body_recent"},
    {"id": "c2", "expr": "body/range >= 0.70"},
    {"id": "c3", "expr": "opposing_wick/range <= 0.20"},
    {"id": "c4", "expr": "leaves_FVG (operational test)"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["displacement-and-fvg","fair-value-gap","mss","range-expansion","liquidity-void","order-block-criteria","propulsion-block"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish displacement candle:               bearish displacement candle:

        ▲                                          ▼
       ▲▲   ← tiny upper wick                     ▼▼▼  ← tiny lower wick
       ██                                          ██
       ██                                          ██
       ██   ← wide green body                      ██  ← wide red body
       ██   covers 70%+ of range                   ██  covers 70%+ of range
       ██                                          ██
       ██                                          ██
        ▲   ← tiny lower wick                      ▼   ← tiny upper wick
                                                   
   close in top half                          close in bottom half
   leaves FVG inside or after                 leaves FVG inside or after
```

## Timeframes

All TFs M5+. The character of displacement scales with TF — an H4 displacement candle's body might be 50–100 pips on EURUSD, an M5 displacement might be 8–15 pips.

## Examples

**Example 1 — H1 bullish displacement:**
- Average H1 body recent = 8 pips.
- Candle: open 1.0830, close 1.0858, low 1.0828, high 1.0860.
- Body = 28, range = 32, upper wick = 2, lower wick = 2.
- Body/range = 87%, upper wick = 6%, lower wick = 6%, body 28 vs avg 8 = 3.5× recent.
- → strong displacement; FVG forms inside (between candle n-1's high and candle n+1's low).

## Common Mistakes

- **Calling any wide candle "displacement."** Without the body-dominance and opposing-wick checks, wide candles in choppy markets aren't displacement.
- **Skipping the FVG test.** ICT's shortcut: real displacement leaves an FVG. If no FVG forms, the candle is unlikely to be true displacement.
- **Ignoring scale.** Displacement is relative to recent average — a candle that's "wide" in a quiet session might be normal in a volatile one.

## Related Concepts

- [displacement-and-fvg](displacement-and-fvg.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [mss](../01-market-structure/mss.md), [range-expansion](../01-market-structure/range-expansion.md), [liquidity-void](../02-liquidity/liquidity-void.md), [order-block-criteria](../07-order-blocks/order-block-criteria.md), [propulsion-block](../07-order-blocks/propulsion-block.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.
