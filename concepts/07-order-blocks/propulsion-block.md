# Propulsion Block

**Category:** 07-order-blocks
**Aliases:** PB, propulsion candle, breakaway block
**ICT Confidence:** medium
**Year Introduced:** 2018
**Year Refined:** 2024
**Source IDs:** ICT-2018-BLOCKS, ICT-2024-PROPULSION-BLOCKS
**Tags:** order-block, propulsion, breakaway

## Definition

A propulsion block is a candle (or short candle cluster) that **launches an aggressive directional move with minimal pullback** — typically the candle that follows the order block and begins the displacement leg. Distinct from a regular OB, the propulsion block is the **takeoff** candle, not the absorption candle. ICT's 2024 mentorship modules included propulsion-block re-teaching as part of the block-vocabulary refinement. Less commonly traded as standalone entry; more often used as a **continuation reference** when price retests the propulsion zone.

## Formal Criteria

A propulsion block:

- Is a **wide-body candle** with same direction as the displacement.
- Sits at or near the OB; often the candle immediately after the OB.
- Has minimal opposing wick (≤ 20% of candle range).
- Often leaves an FVG inside it.
- Used as a **continuation entry zone** rather than a reversal/absorption zone.

## Formula / Math

```
is_propulsion_block(n) :=
    candle_n_body_size >= 1.5 * avg_body_size
    AND opposing_wick_pct <= 0.20
    AND directional_alignment_with_recent_displacement == true
    AND fvg_inside_or_after == true
```

## Machine-Readable

```json
{
  "id": "propulsion-block",
  "category": "07-order-blocks",
  "aliases": ["PB", "propulsion-candle", "breakaway-block"],
  "criteria": [
    {"id": "c1", "expr": "wide_body_with_minimal_opposing_wick == true"},
    {"id": "c2", "expr": "directional_with_recent_displacement == true"},
    {"id": "c3", "expr": "often_leaves_FVG == true"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "medium",
  "year_introduced": "2018",
  "year_refined": "2024",
  "related": ["bullish-order-block","bearish-order-block","order-block-criteria","displacement-definition","fair-value-gap","vacuum-block"],
  "sources": ["ICT-2018-BLOCKS","ICT-2024-PROPULSION-BLOCKS"]
}
```

## Visual Pattern

```
   bullish propulsion sequence:

   ▼  ← bullish OB (the absorption candle)
              ▲  ← propulsion block (wide green body, minimal lower wick)
              █▲
              █▲
              █▲   ← FVG inside / after this candle
              █
   On retest later, the propulsion-block body can serve as a
   continuation entry zone (price returns, reacts, continues up).
```

## Timeframes

M5–H4 most common.

## Examples

**Example 1 — bullish propulsion after OB:**
- Bullish OB candle 14:00 NY (small bearish body).
- 14:30 NY: 28-pip green candle, body covers 90% of range, leaves a 5-pip bullish FVG.
- → propulsion block at 14:30; body 1.0830–1.0858.
- On a future retracement to 1.0850, the propulsion block's body acts as continuation support; combined with the FVG inside, it's a confluence zone.

## Common Mistakes

- **Confusing PB with regular OB.** Propulsion is direction-aligned (same as displacement); OB is direction-opposite (absorption).
- **Treating PB as primary entry.** Less reliable than the OB itself; often used as continuation reference, not first-touch entry.
- **Vague qualification.** Without the wide-body + minimal-wick + FVG checks, you're calling normal trending candles "propulsion blocks."

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md), [order-block-criteria](order-block-criteria.md).
- [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [vacuum-block](vacuum-block.md).

## Citations

- `ICT-2018-BLOCKS` — propulsion block introduced.
- `ICT-2024-PROPULSION-BLOCKS` — re-teach in 2024 mentorship modules.

> Confidence is `medium` because propulsion-block usage varies across ICT community sources; less standardized than OB/FVG.
