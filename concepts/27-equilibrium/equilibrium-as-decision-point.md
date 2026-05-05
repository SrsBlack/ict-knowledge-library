# Equilibrium as Decision Point

**Category:** 27-equilibrium
**Aliases:** EQ pivot, EQ decision, EQ as gate
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** equilibrium, decision, pivot, operational

## Definition

Equilibrium-as-decision-point is the operational use of EQ as a **pivot for setup-side selection** — the place where the analyst decides whether the current price action is a long-bias environment or a short-bias environment. ICT's discipline: at EQ, hesitate; well below EQ in discount, look only for longs; well above EQ in premium, look only for shorts. The further from EQ, the higher the conviction of the side.

## Formal Criteria

The decision rule:

- If `price < DR_EQ - small_buffer`: **discount mode** — only long setups valid.
- If `price > DR_EQ + small_buffer`: **premium mode** — only short setups valid.
- If `|price - DR_EQ| < small_buffer`: **EQ zone** — wait, no fresh entries; finalize existing positions.
- Buffer typically 5–15% of half-range (calibrate by TF and instrument).

Reinforcement modifiers:

- HTF bias must agree with the side suggested by EQ position.
- A PD array (FVG / OB / breaker) at the suggested side is required for actual entry.
- A liquidity sweep / Judas swing is preferred before commitment.

## Formula / Math

```
half_range = (LTH_ext - LTL_ext) / 2
buffer     = 0.10 * half_range     # 10% buffer; tune per TF/instrument

mode := "discount" if price < DR_EQ - buffer
       "premium"  if price > DR_EQ + buffer
       "eq_zone"  otherwise
```

## Machine-Readable

```json
{
  "id": "equilibrium-as-decision-point",
  "category": "27-equilibrium",
  "aliases": ["EQ-pivot", "EQ-decision-gate"],
  "criteria": [
    {"id": "c1", "expr": "price_position_vs_EQ_dictates_setup_side == true"},
    {"id": "c2", "expr": "EQ_zone_means_no_fresh_entries == true"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["equilibrium-definition","dealing-range-equilibrium","mean-threshold","premium-array","discount-array","htf-bias-framework"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   range_top ─────  full premium → high-conviction shorts only

       short zone (PD arrays here)

   ─── EQ + buffer ─────  shallow premium boundary
   ─── EQ ────────────── decision pivot (no fresh entries)
   ─── EQ - buffer ─────  shallow discount boundary

       long zone (PD arrays here)

   range_bot ─────  full discount → high-conviction longs only
```

## Timeframes

Same as dealing-range-EQ (H1+ for stable EQ).

## Examples

**Example 1 — bullish bias + price in discount:**
- D1 LTH 1.1000, LTL 1.0800. EQ = 1.0900.
- Buffer ~10 pips → discount mode below 1.0890, premium mode above 1.0910.
- Current price 1.0855 = discount → only long setups.
- HTF bullish + bullish OB at 1.0820 = entry zone.

**Example 2 — price at EQ zone:**
- Same range. Current price 1.0903.
- |1.0903 − 1.0900| = 3 pips, well within buffer.
- → EQ zone; no fresh entries. Existing positions get reviewed for partial-take or invalidation.

## Common Mistakes

- **Trading both directions equally regardless of EQ.** Selling at deep discount or buying at deep premium is fading the algorithmic intent.
- **No buffer.** Pixel-precise EQ entries flop both ways constantly. Use a buffer matched to the instrument.
- **Skipping HTF bias check.** EQ tells you which side has higher base-rate conviction in the current range; HTF bias overrides if there's a conflict (e.g. range about to break).

## Related Concepts

- [equilibrium-definition](equilibrium-definition.md), [dealing-range-equilibrium](dealing-range-equilibrium.md), [mean-threshold](mean-threshold.md).
- [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md).
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
