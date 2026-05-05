# Order Block — Criteria

**Category:** 07-order-blocks
**Aliases:** OB criteria, order block rules, OB qualification
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-OB-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, criteria, foundational

## Definition

An Order Block (OB) is the **last opposite-direction candle before a displacement move that breaks structure**. ICT teaches OBs as the candles where institutions absorbed the opposite-side flow before driving price in their intended direction. The qualifying candle's body acts as the algorithmic reference zone for re-entry. This page defines the canonical OB qualification rules; the bullish and bearish variants are deep-dived in [bullish-order-block](bullish-order-block.md) and [bearish-order-block](bearish-order-block.md).

## Formal Criteria

A candle qualifies as an OB if ALL of:

1. **Last opposite candle.** It is the last candle of opposite color before a displacement move (bullish OB = last down-close before bullish displacement; bearish OB = last up-close before bearish displacement).
2. **Displacement follows.** The next 1–3 candles produce a clear directional displacement (wide bodies, minimal opposing wicks, an FVG is typically left in the displacement).
3. **Breaks structure.** The displacement breaks a recent swing high/low (BOS or CHoCH/MSS).
4. **Anchored at a swing pivot.** Best-quality OBs sit at swing highs (bearish) or swing lows (bullish) — pivots that already had structural significance.
5. **Fresh.** Has not yet been mitigated.

## Formula / Math

```
ob_qualifies(candle_n) :=
    is_last_opposite_color_before_displacement(n)
    AND displacement_after_n_present
    AND structure_broken_by_displacement
    AND anchored_at_swing_pivot
    AND not_yet_mitigated

# Bullish OB body: open and close of the OB candle:
bullish_ob_high := open(n)       # since C < O for a bearish candle
bullish_ob_low  := close(n)
bullish_ob_mt   := (open(n) + close(n)) / 2     # mean threshold

# Bearish OB:
bearish_ob_high := close(n)      # since C > O for a bullish candle
bearish_ob_low  := open(n)
bearish_ob_mt   := (close(n) + open(n)) / 2
```

## Machine-Readable

```json
{
  "id": "order-block-criteria",
  "category": "07-order-blocks",
  "aliases": ["OB-criteria", "OB-rules", "OB-qualification"],
  "criteria": [
    {"id": "c1", "expr": "last_opposite_color_before_displacement == true"},
    {"id": "c2", "expr": "displacement_present == true"},
    {"id": "c3", "expr": "structure_broken == true"},
    {"id": "c4", "expr": "anchored_at_swing_pivot == true"},
    {"id": "c5", "expr": "fresh_not_mitigated == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bullish-order-block","bearish-order-block","mitigated-order-block","unmitigated-order-block","mean-threshold","displacement-definition","fair-value-gap","bos-bullish","bos-bearish"],
  "sources": ["ICT-2016-OB-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB qualification:

   ▼               ← last DOWN candle before displacement
   ▼               (this is the bullish OB)
                   ▲
                   ▲ ← displacement candle 1
                   ▲
                       ▲
                       ▲ ← displacement candle 2 (FVG forms)
                       ▲     +  swing high broken (BOS / CHoCH)
   bullish OB body = OPEN to CLOSE of the marked down candle.
   MT = body midpoint.
```

## Timeframes

All TFs M5+. M1 OBs are too noisy.

## Examples

**Example 1 — H1 bullish OB:**
- H1 bearish candle at 14:00 NY: open 1.0830, close 1.0820, low 1.0815, high 1.0832.
- H1 candle 15:00 NY: bullish 22-pip displacement, leaves bullish FVG, breaks the prior H1 swing high (BOS).
- → 14:00 candle qualifies as bullish OB.
- OB body: [1.0820, 1.0830]. MT = 1.0825.
- Long entry on retest at MT (1.0825) with SL below 1.0815 (OB low + 3-pip buffer). Risk = 13 pips.

## Common Mistakes

- **Calling any down-candle an OB.** Without displacement-and-BOS following, it's not an OB — just a normal candle.
- **Skipping the structure-break check.** A "displacement" that doesn't break structure isn't significant enough; many practitioners include the BOS check explicitly.
- **Treating bodies vs ranges inconsistently.** Use OB body (open/close) by default; range version (high/low) is broader but less precise.
- **Stale OBs.** Once mitigated (price returned and reacted), the OB stops being a fresh entry zone.

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md) — directional variants.
- [mitigated-order-block](mitigated-order-block.md), [unmitigated-order-block](unmitigated-order-block.md) — state.
- [mean-threshold](../27-equilibrium/mean-threshold.md) — MT entry depth.
- [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [bos-bullish](../01-market-structure/bos-bullish.md), [bos-bearish](../01-market-structure/bos-bearish.md).

## Citations

- `ICT-2016-OB-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
