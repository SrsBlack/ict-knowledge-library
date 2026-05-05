# Displacement Strength Criteria

**Category:** 09-displacement
**Aliases:** displacement quality, displacement scoring, strong vs weak displacement
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2024
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** displacement, scoring, quality

## Definition

Displacement Strength Criteria are the **quality scoring** for displacement candles. Not all displacement is equal: a candle with body 90% of range and zero opposing wick is much stronger than one at 70% with a 15% wick. ICT teaches displacement scoring qualitatively as "weak / moderate / strong" — this file formalizes the criteria so setups can be calibrated by displacement quality.

## Formal Criteria

The 5-factor displacement scoring:

| Factor | Weak | Moderate | Strong |
|---|---|---|---|
| Body / range | 0.50–0.70 | 0.70–0.85 | 0.85+ |
| Opposing wick % | 20–30% | 10–20% | <10% |
| Body vs avg | 1.0–1.5× | 1.5–2× | 2×+ |
| FVG formed | small or absent | clear FVG | wide FVG inside |
| Follow-through | none | 1–2 candles continue | 3+ candles continue |

Score = sum of factor levels (1-3 each) → range 5-15.

- 5–8: weak (low conviction).
- 9–11: moderate (standard).
- 12–15: strong (highest conviction).

## Formula / Math

```
displacement_score(candle) = sum([
    body_range_score(0.50, 0.70, 0.85),
    opposing_wick_score(0.30, 0.20, 0.10),
    body_vs_avg_score(1.0, 1.5, 2.0),
    fvg_score(absent_or_small, clear, wide),
    followthrough_score(none, 1-2_candles, 3+_candles),
])

# returns 5-15
```

## Machine-Readable

```json
{
  "id": "displacement-strength-criteria",
  "category": "09-displacement",
  "aliases": ["displacement-quality", "displacement-scoring"],
  "criteria": [
    {"id": "c1", "expr": "5-factor scoring: body/range, opposing wick, body vs avg, FVG, follow-through"},
    {"id": "c2", "expr": "weak 5-8, moderate 9-11, strong 12-15"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2024",
  "related": ["displacement-definition","bullish-displacement","bearish-displacement","displacement-and-fvg","fair-value-gap"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Weak displacement:                Strong displacement:
   
        ▲                                ▲   ← tiny wick
       ▲▲                               ▲▲
       █▲▲   ← upper wick 25%           ██
       ██   ← body 60% of range         ██   ← body 90% of range
       ██                               ██
       █                                ██
        ▲   ← lower wick                 ▲
                                         (no opposing wick)
   small/no FVG                       clear wide FVG
   no follow-through                  3+ continuation candles
```

## Timeframes

M5–D.

## Examples

**Example 1 — strong displacement scoring:**
- Body 28/32 = 87% (strong → 3).
- Upper wick 2/32 = 6% (strong → 3).
- Body 28 vs avg 8 = 3.5× (strong → 3).
- Clear FVG formed (clear → 2 — wide would be 3).
- 4 follow-up candles continued (strong → 3).
- Score = 3+3+3+2+3 = 14 → strong displacement.

## Common Mistakes

- **Single-factor scoring.** Body/range alone doesn't capture displacement quality; use all 5 factors.
- **Treating wide-but-wicked candles as strong.** A 90%-body candle with 20% upper wick is moderate, not strong.
- **Ignoring follow-through.** A "strong" displacement that immediately reverses isn't really strong — follow-through is part of the signature.

## Related Concepts

- [displacement-definition](displacement-definition.md), [bullish-displacement](bullish-displacement.md), [bearish-displacement](bearish-displacement.md), [displacement-and-fvg](displacement-and-fvg.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.
