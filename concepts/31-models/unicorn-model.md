# Unicorn Model

**Category:** 31-models
**Aliases:** ICT Unicorn, the Unicorn, unicorn setup
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-UNICORN
**Tags:** model, unicorn, 2023

## Definition

The **Unicorn Model** is a high-conviction multi-confluence ICT setup — named for its rarity. The Unicorn requires the simultaneous presence of: a breaker block, an FVG inside the breaker, alignment with HTF bias, AND a clean liquidity sweep before the breaker formed. When all four conditions stack at the same level, the setup is the closest ICT publishes to "an A++ trade." Unicorns are infrequent but among the highest-probability ICT entries.

## Formal Criteria

A Unicorn requires ALL of:

1. **Breaker block** has formed (failed OB whose polarity has flipped).
2. **FVG nested inside the breaker zone** (same direction as the breaker's new polarity).
3. **HTF bias agrees** with the breaker direction (bullish breaker requires bullish HTF; mirror).
4. **Liquidity sweep** preceded the breaker formation (typically the sweep that triggered the original CHoCH/MSS).

When all four align at the same price zone, the setup is "Unicorn-grade."

## Formula / Math

```
unicorn(zone):
    breaker_block_present(zone)
    AND fvg_nested_inside_breaker(zone)
    AND htf_bias_matches_breaker_direction
    AND prior_liquidity_sweep_triggered_breaker
```

## Machine-Readable

```json
{
  "id": "unicorn-model",
  "category": "31-models",
  "aliases": ["ICT-Unicorn", "the-Unicorn", "unicorn-setup"],
  "criteria": [
    {"id": "c1", "expr": "breaker_block + nested_FVG + HTF_bias + prior_sweep"},
    {"id": "c2", "expr": "all 4 confluence layers required"}
  ],
  "timeframes": ["M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["ict-2022-model","ict-2023-model","breaker-block","fair-value-gap","nested-fvg","htf-bias-framework","liquidity-sweep","pd-array-confluence"],
  "sources": ["ICT-2023-UNICORN"]
}
```

## Visual Pattern

```
   bullish Unicorn:

   prior bearish leg ↓
        sweep at SSL (manipulation)  → triggers CHoCH up
        bearish OB at swing low → flipped to bullish breaker
        FVG forms inside the breaker zone (same bullish direction)
        HTF (D, W) bullish

   → all 4 conditions align at the breaker-FVG zone.
   → high-conviction long entry on FVG CE retest with SL beyond breaker invalidation.
```

## Timeframes

M15+. HTF Unicorns (H4, D) are the most-cited variant.

## Examples

**Example 1 — H1 bullish Unicorn:**
- Prior: H1 bearish leg, swept SSL at 1.0820 (trigger).
- H1 CHoCH up; the H1 swing-high bearish OB at 1.0840-1.0850 flipped to bullish breaker.
- Inside the breaker body, an H1 bullish FVG at 1.0843-1.0847.
- HTF (D, W) bullish ✓.
- All 4 Unicorn conditions met at 1.0843–1.0850.
- Long entry at FVG CE 1.0845; SL below breaker invalidation 1.0838; risk 7 pips.
- Target HTF DOL: 1.0925 (PDH BSL). 80 pips reward → ~11R.

## Common Mistakes

- **Calling 3-of-4 setups "Unicorn."** The hallmark is **all 4** conditions. 3-of-4 is a strong setup but not a Unicorn.
- **Forcing Unicorn classification.** Unicorns are deliberately rare — most setups are 2022/2023 models, not Unicorns.
- **Ignoring HTF bias.** A "Unicorn" against HTF bias is just a confluence cluster that will likely fail.

## Related Concepts

- [ict-2022-model](ict-2022-model.md), [ict-2023-model](ict-2023-model.md), [breaker-block](../08-breaker-blocks/breaker-block.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [nested-fvg](../06-fair-value-gaps/nested-fvg.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [pd-array-confluence](../05-pd-arrays/pd-array-confluence.md).

## Citations

- `ICT-2023-UNICORN`.
