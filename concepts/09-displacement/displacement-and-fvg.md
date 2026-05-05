# Displacement and FVG

**Category:** 09-displacement
**Aliases:** displacement-FVG link, FVG-as-displacement-test, displacement signature
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** displacement, fvg, foundational

## Definition

The relationship between displacement and FVG is fundamental to ICT structure analysis: **a real displacement candle almost always leaves an FVG inside or directly after it**. ICT teaches the FVG as the **operational test** for whether a candle qualifies as displacement. Conversely, an FVG without a displacement candle behind it is structurally weak. The two concepts validate each other.

## Formal Criteria

The link works in both directions:

- **Displacement → FVG:** when a candle moves with sufficient force (wide body, minimal opposing wick), it physically cannot have its wick overlap both n-1's wick and n+1's wick simultaneously — an FVG appears.
- **FVG → displacement:** if you see a 3-candle FVG, the middle candle is by geometry a displacement candle.

The principle: **no displacement = no FVG; no FVG = candle wasn't real displacement**.

## Formula / Math

```
# If candle n is true displacement:
#   range_n is large
#   body_n covers most of range
#   wick rebalance can't happen because algorithm moved too fast
#   → either H_{n-1} stays below L_{n+1} (bullish FVG) or H_{n+1} below L_{n-1} (bearish)

displacement_implies_fvg := P(fvg_present | true_displacement) ≈ 0.95+
fvg_implies_displacement := P(displacement | fvg_present) ≈ 0.95+
```

The implication is approximate (some edge cases exist) but operationally near-1.

## Machine-Readable

```json
{
  "id": "displacement-and-fvg",
  "category": "09-displacement",
  "aliases": ["displacement-FVG-link", "FVG-as-displacement-test"],
  "criteria": [
    {"id": "c1", "expr": "displacement_candle_typically_leaves_FVG == true"},
    {"id": "c2", "expr": "FVG_implies_middle_candle_was_displacement == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["displacement-definition","fair-value-gap","bullish-fvg","bearish-fvg","mss","order-block-criteria"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   displacement creates an FVG by geometry:

   candle n-1: ▲  (small, normal candle)
                    
   candle n:   ▲  ← wide green body, opens near low_{n-1}
               ██   covers most of its range
               ██   travels far up
               ██
                ▲  closes near high
   
   candle n+1: ▲   opens above H_{n-1} → low_{n+1} > high_{n-1}
                   → bullish FVG between them
```

## Timeframes

All TFs M5+.

## Examples

**Example 1 — testing displacement with FVG:**
- M15 candle 14:00 NY: body 22 pips, range 24 pips, lower wick 1 pip, upper wick 1 pip — body/range 92%.
- Candle n-1 high = 1.0860; candle n+1 low = 1.0865 → bullish FVG of 5 pips.
- → both displacement-criteria-met AND FVG present. Strong setup.

**Example 2 — displacement without FVG (rare edge case):**
- A candle has wide body but candle n+1's wick reaches back through to overlap candle n-1.
- → no FVG (wicks overlap). The displacement was real but post-candle reaction reabsorbed the inefficiency immediately. Lower-quality setup; treat with reduced conviction.

## Common Mistakes

- **Insisting on every FVG having displacement.** Most do; some are tight 3-bar gaps in low-volatility chop with weak displacement. Filter the FVG by displacement quality.
- **Skipping the FVG test for displacement.** A "looks-like" displacement candle without an FVG is a yellow flag — re-evaluate.
- **Using only one direction of the implication.** Both directions matter for setup quality assessment.

## Related Concepts

- [displacement-definition](displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [bullish-fvg](../06-fair-value-gaps/bullish-fvg.md), [bearish-fvg](../06-fair-value-gaps/bearish-fvg.md), [mss](../01-market-structure/mss.md), [order-block-criteria](../07-order-blocks/order-block-criteria.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.
