# Bullish Displacement

**Category:** 09-displacement
**Aliases:** bullish expansion candle, up-displacement
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** displacement, bullish

## Definition

Bullish displacement is a **wide-bodied green candle (or short cluster) with strong directional intent up** — minimal lower wick, body covering most of the range, and typically leaving a bullish FVG in its wake. Mirror of [bullish-fvg](../06-fair-value-gaps/bullish-fvg.md)'s parent displacement event. Bullish displacement is the visual signature ICT teaches as the trigger for bullish entries: when a wide green displacement candle prints, especially after a sweep at HTF discount, the bullish setup is confirmed.

## Formal Criteria

A bullish displacement candle:

- **Body**: >= 1.5× recent average body size.
- **Body / range**: >= 0.70 (body dominates the candle).
- **Lower wick**: <= 20% of range (minimal opposing wick).
- **Direction**: close in top half, ideally near high.
- **FVG signature**: typically `L_{n+1} > H_{n-1}` (bullish FVG forms inside or after).

## Formula / Math

```
range_n = high(n) - low(n)
body_n  = close(n) - open(n)        # positive for bullish
lower_wick_n = open(n) - low(n)     # for bullish candle: open is lower body bound
upper_wick_n = high(n) - close(n)

bullish_displacement(n) :=
    body_n >= 1.5 * avg_body_recent
    AND body_n / range_n >= 0.70
    AND lower_wick_n / range_n <= 0.20
    AND close(n) >= midpoint(low, high)
    AND ideally L_{n+1} > H_{n-1}
```

## Machine-Readable

```json
{
  "id": "bullish-displacement",
  "category": "09-displacement",
  "aliases": ["bullish-expansion-candle", "up-displacement"],
  "criteria": [
    {"id": "c1", "expr": "body >= 1.5 * avg_body_recent"},
    {"id": "c2", "expr": "body/range >= 0.70"},
    {"id": "c3", "expr": "lower_wick/range <= 0.20"},
    {"id": "c4", "expr": "close in top half"},
    {"id": "c5", "expr": "ideally leaves bullish FVG"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["displacement-definition","bearish-displacement","displacement-strength-criteria","displacement-and-fvg","bullish-fvg","fair-value-gap","range-expansion"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish displacement candle:
   
        ▲   ← tiny upper wick
       ▲▲   
       ██   
       ██   
       ██   ← wide green body (70%+ of range)
       ██   
       ██   
        ▲   ← tiny lower wick
   
   close in top half, often near high.
   FVG forms above (between candle n-1's high and candle n+1's low).
```

## Timeframes

M5–D.

## Examples

**Example 1 — H1 bullish displacement:**
- Average H1 body recent = 8 pips.
- Candle: O=1.0830, C=1.0858, L=1.0828, H=1.0860.
- body=28, range=32, body/range=0.875, upper_wick=2 (6%), lower_wick=2 (6%).
- → strong bullish displacement; FVG forms.

## Common Mistakes

- **Treating wide candles in chop as displacement.** Without context (sweep before, structure break), wide candles aren't displacement — just volatility.
- **Skipping the FVG check.** Real displacement leaves FVG; absence is a yellow flag.

## Related Concepts

- [displacement-definition](displacement-definition.md), [bearish-displacement](bearish-displacement.md), [displacement-strength-criteria](displacement-strength-criteria.md), [displacement-and-fvg](displacement-and-fvg.md), [bullish-fvg](../06-fair-value-gaps/bullish-fvg.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [range-expansion](../01-market-structure/range-expansion.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.
