# Stop Placement by PD Array

**Category:** 32-risk-management
**Aliases:** structural SL, PD-array SL, invalidation-based SL
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, sl, pd-array, foundational

## Definition

ICT teaches **structural SL placement**: the SL is set just beyond the **PD array's invalidation level**, not at an arbitrary fixed-pip distance. The principle: if the PD array is the entry's algorithmic anchor, then the SL should sit where that anchor would be **structurally invalidated** — beyond the OB low (for bullish OB) or beyond the FVG far edge (for bullish FVG) or beyond the breaker zone, etc. Structural SLs are tighter than fixed-pip SLs but stop-out only when the setup premise has actually failed.

## Formal Criteria

SL placement by structure type (with small 2-5 pip buffer):

| Structure | Bullish setup SL | Bearish setup SL |
|---|---|---|
| FVG | Below FVG low | Above FVG high |
| Bullish OB | Below OB low (or wick low) | — |
| Bearish OB | — | Above OB high (or wick high) |
| Bullish breaker | Below breaker zone low | — |
| Bearish breaker | — | Above breaker zone high |
| OTE entry | Below 0.79 of leg | Above 0.79 of leg |
| Liquidity sweep entry | Below sweep low | Above sweep high |

Always add a small buffer (2–5 pips on FX, 2–5 points on indices) to avoid wick-stops on noise.

## Formula / Math

```
sl_for_long = pd_array_invalidation_low - buffer
sl_for_short = pd_array_invalidation_high + buffer

# Example: bullish OB body 1.0820-1.0830, OB candle low 1.0815
# SL = 1.0815 - 3 pip buffer = 1.0812
```

## Machine-Readable

```json
{
  "id": "stop-placement-by-pd-array",
  "category": "32-risk-management",
  "aliases": ["structural-SL", "PD-array-SL", "invalidation-based-SL"],
  "criteria": [
    {"id": "c1", "expr": "SL = pd_array_invalidation +/- buffer"},
    {"id": "c2", "expr": "buffer 2-5 pips FX, 2-5 points indices"},
    {"id": "c3", "expr": "structural not arbitrary"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["risk-per-trade","r-multiple","position-sizing","fair-value-gap","bullish-order-block","breaker-block","mean-threshold","ce-as-primary-entry"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB SL placement:

   OB body  ─── 1.0830 (top, MT 1.0825)
            ─── 1.0820 (bottom of body)
            ─── 1.0815 (OB candle wick low) ← SL reference
                                              ↓
                                              SL = 1.0812 (3-pip buffer below wick low)
```

## Timeframes

All TFs.

## Examples

**Example 1 — structural SL on bullish OB:**
- Setup: bullish OB body 1.0820–1.0830, OB candle wick low 1.0815.
- Entry at MT 1.0825.
- SL: 1.0815 − 3 pips = 1.0812.
- Risk = 13 pips.

**Example 2 — structural SL on bullish FVG:**
- FVG 1.0860–1.0866, CE 1.0863.
- Entry at CE 1.0863.
- SL: 1.0860 − 2 pips = 1.0858.
- Risk = 5 pips.

## Common Mistakes

- **Fixed-pip SL ignoring structure.** "Always 20 pip SL" misses tight setups (5R+) and over-stops loose ones.
- **No buffer.** Pixel-precise SLs at exact PD-array invalidation get wicked out on routine noise.
- **Buffer too wide.** 10-pip buffer on a 15-pip setup destroys R:R. Use 2–5 pips.
- **Wrong invalidation reference.** Bullish FVG SL goes BELOW the FVG (FVG low), not below CE — CE is the entry, the LOW is the invalidation.

## Related Concepts

- [risk-per-trade](risk-per-trade.md), [r-multiple](r-multiple.md), [position-sizing](position-sizing.md).
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [breaker-block](../08-breaker-blocks/breaker-block.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
