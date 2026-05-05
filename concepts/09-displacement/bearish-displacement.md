# Bearish Displacement

**Category:** 09-displacement
**Aliases:** bearish expansion candle, down-displacement
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** displacement, bearish

## Definition

Bearish displacement is a **wide-bodied red candle with strong directional intent down** — minimal upper wick, body covering most of the range, typically leaving a bearish FVG. Mirror of [bullish-displacement](bullish-displacement.md). Confirms bearish entries when forming after a sweep at HTF premium.

## Formal Criteria

A bearish displacement candle:

- **Body**: >= 1.5× recent average body size.
- **Body / range**: >= 0.70.
- **Upper wick**: <= 20% of range.
- **Direction**: close in bottom half.
- **FVG signature**: typically `H_{n+1} < L_{n-1}` (bearish FVG forms).

## Formula / Math

```
range_n = high(n) - low(n)
body_n  = open(n) - close(n)        # positive for bearish
upper_wick_n = high(n) - open(n)    # for bearish: open is upper body bound
lower_wick_n = close(n) - low(n)

bearish_displacement(n) :=
    body_n >= 1.5 * avg_body_recent
    AND body_n / range_n >= 0.70
    AND upper_wick_n / range_n <= 0.20
    AND close(n) <= midpoint(low, high)
    AND ideally H_{n+1} < L_{n-1}
```

## Machine-Readable

```json
{
  "id": "bearish-displacement",
  "category": "09-displacement",
  "aliases": ["bearish-expansion-candle", "down-displacement"],
  "criteria": [
    {"id": "c1", "expr": "body >= 1.5 * avg_body_recent"},
    {"id": "c2", "expr": "body/range >= 0.70"},
    {"id": "c3", "expr": "upper_wick/range <= 0.20"},
    {"id": "c4", "expr": "close in bottom half"},
    {"id": "c5", "expr": "ideally leaves bearish FVG"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["displacement-definition","bullish-displacement","displacement-strength-criteria","displacement-and-fvg","bearish-fvg","fair-value-gap","range-expansion"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bearish displacement candle:
   
        ▼   ← tiny lower wick
       ▼▼   
       ██   
       ██   
       ██   ← wide red body (70%+ of range)
       ██   
       ██   
        ▼   ← tiny upper wick
   
   close in bottom half, often near low.
   FVG forms below.
```

## Timeframes

M5–D.

## Examples

**Example 1 — H1 bearish displacement:**
- avg H1 body = 8 pips.
- Candle: O=1.0958, C=1.0930, L=1.0928, H=1.0960.
- body=28, range=32, body/range=0.875, upper_wick=2 (6%), lower_wick=2 (6%).
- → strong bearish displacement; FVG forms.

## Common Mistakes

- **No HTF context.** Bearish displacement against a clearly bullish HTF often fails to follow through.
- **Wide-but-not-clean candles.** A wide red candle with a 50% upper wick is not clean displacement.

## Related Concepts

- [displacement-definition](displacement-definition.md), [bullish-displacement](bullish-displacement.md), [displacement-strength-criteria](displacement-strength-criteria.md), [displacement-and-fvg](displacement-and-fvg.md), [bearish-fvg](../06-fair-value-gaps/bearish-fvg.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [range-expansion](../01-market-structure/range-expansion.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.
