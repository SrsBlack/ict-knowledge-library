# Diamond Pattern

**Category:** 31-models
**Aliases:** ICT Diamond, diamond top/bottom, double-sweep diamond
**ICT Confidence:** medium
**Year Introduced:** 2023
**Year Refined:** 2024
**Source IDs:** ICT-2023-DIAMOND
**Tags:** model, diamond, double-sweep

## Definition

The **Diamond Pattern** is a consolidation pattern bounded by **two-sided liquidity sweeps before a directional resolution**. Named for the symmetrical "diamond" shape that forms when both BSL and SSL get swept inside the same consolidation window. ICT teaches the diamond as a high-conviction setup because both sides of the trapped liquidity are gone before the directional move — meaning few stops remain to cause a counter-move during the breakout.

## Formal Criteria

A Diamond requires:

1. **Initial consolidation** — price ranging in a defined area.
2. **Sweep of upper bound (BSL)** — wick takes BSL, closes back inside.
3. **Sweep of lower bound (SSL)** — wick takes SSL, closes back inside.
4. **Directional resolution** — break with displacement in HTF-bias direction.
5. **Visual diamond shape** — the sweeps form symmetrical extremes around the consolidation midpoint.

The order of the BSL/SSL sweeps doesn't matter; what matters is that **both** are taken before the directional break.

## Formula / Math

```
diamond_pattern(zone):
    consolidation_period_present
    AND BSL_sweep_during_consolidation
    AND SSL_sweep_during_consolidation
    AND directional_break_after_both_sweeps_in_HTF_bias_direction
```

## Machine-Readable

```json
{
  "id": "diamond-pattern",
  "category": "31-models",
  "aliases": ["ICT-Diamond", "diamond-top", "diamond-bottom", "double-sweep-diamond"],
  "criteria": [
    {"id": "c1", "expr": "consolidation + BSL_sweep + SSL_sweep + directional_break"},
    {"id": "c2", "expr": "both_sides_swept_before_resolution"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2023",
  "year_refined": "2024",
  "related": ["ict-2023-model","liquidity-sweep","range-contraction","range-expansion","htf-bias-framework","balanced-price-range"],
  "sources": ["ICT-2023-DIAMOND"]
}
```

## Visual Pattern

```
   bullish Diamond:

         ╱▲╲          ← upper sweep (BSL taken first)
        ╱   ╲
       ╱  ╳  ╲        ← consolidation midpoint
        ╲   ╱
         ╲▼╱          ← lower sweep (SSL taken second)

   Then: bullish breakout with displacement up
   (HTF bias bullish; both sides swept; clean breakout).
```

## Timeframes

M15+. Daily diamonds are rare and high-conviction; intraday diamonds (M15-H1) are more common.

## Examples

**Example 1 — bullish Diamond on H1:**
- 02:00–07:00 NY: H1 consolidation 1.0820–1.0875.
- 03:00 NY: H1 wicks 1.0879 (BSL swept), closes 1.0865.
- 05:00 NY: H1 wicks 1.0815 (SSL swept), closes 1.0830.
- HTF bullish; 09:00 NY: H1 closes 1.0890 with bullish displacement (breaks consolidation high with both sides cleared).
- → Diamond pattern complete; long entry on retest of FVG inside the breakout.

## Common Mistakes

- **Single-sweep "diamonds."** A Diamond requires BOTH sides swept; one-sided sweep + breakout is just a Judas swing or Turtle Soup, not a Diamond.
- **Forcing diamond geometry.** The "diamond shape" is descriptive; what matters structurally is the two-sided sweep before resolution.

## Related Concepts

- [ict-2023-model](ict-2023-model.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [range-contraction](../01-market-structure/range-contraction.md), [range-expansion](../01-market-structure/range-expansion.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [balanced-price-range](../06-fair-value-gaps/balanced-price-range.md).

## Citations

- `ICT-2023-DIAMOND`.

> Confidence is `medium` because the Diamond pattern is taught with name variations across the ICT community; the underlying double-sweep mechanic is well-established but the specific "Diamond" label has informal usage.
