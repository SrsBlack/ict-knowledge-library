# CE as Primary Entry (2025 Refinement)

**Category:** 06-fair-value-gaps
**Aliases:** CE primary entry, CE-as-default, the CE shift
**ICT Confidence:** high
**Year Introduced:** 2025
**Year Refined:** 2025
**Source IDs:** ICT-2025-CE-PRIMARY-ENTRY
**Tags:** ce, fvg, 2025-refinement, primary-entry

## Definition

In multiple 2025 videos and threads, ICT explicitly elevated **Consequent Encroachment (CE)** from "a useful zone within an FVG" to **the default primary entry zone** for FVG-based setups. Prior framing was ambiguous — entries could happen at near edge, CE, or far edge depending on context. The 2025 refinement clarifies: when entering an FVG, **default to CE unless a specific reason supports a different depth**. This reduces overshoot risk (entries at near edge get stopped on full fills) and avoids missed fills (entries at far edge often never fill).

## Formal Criteria

The 2025 CE-primary entry rule:

- The default entry inside an FVG is **CE** (50% midpoint).
- Reasons to enter shallower (near edge):
  - High-conviction HTF setup where CE may not be reached.
  - Time-pressure (killzone closing soon).
  - Tight-stop scalping context.
- Reasons to enter deeper (toward far edge):
  - Strong bias toward full rebalance (e.g., during an immediate-rebalance pattern).
  - Lower-TF FVG nested at the far edge of the HTF FVG.
- SL convention: just beyond the FVG's far edge (or the next structural level beyond).

## Formula / Math

```
default_entry_depth = ce
default_sl_distance = (far_edge - ce) + buffer
default_risk        = abs(default_entry_depth - default_sl_distance)
```

The discipline: pick CE first; deviate only with a reason.

## Machine-Readable

```json
{
  "id": "ce-as-primary-entry",
  "category": "06-fair-value-gaps",
  "aliases": ["CE-primary-entry", "CE-as-default"],
  "criteria": [
    {"id": "c1", "expr": "default_entry_inside_FVG == CE"},
    {"id": "c2", "expr": "deviation_requires_explicit_reason == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2025",
  "year_refined": "2025",
  "related": ["consequent-encroachment","fair-value-gap","bullish-fvg","bearish-fvg","fvg-classification-2025","immediate-rebalance-fvg","delayed-rebalance-fvg"],
  "sources": ["ICT-2025-CE-PRIMARY-ENTRY"]
}
```

## Visual Pattern

```
   default CE entry (bullish FVG):

   ─── FVG high (far edge) ─────  ← SL reference (just above)
       
   ─── CE ───────────────────  ← DEFAULT ENTRY
       
   ─── FVG low (near edge) ──────
```

## Timeframes

All TFs.

## Examples

**Example 1 — applying CE-primary on M15 bullish FVG:**
- FVG: low 1.0860, high 1.0866. CE = 1.0863.
- HTF bullish; bullish bias clear; no specific reason for shallower or deeper entry.
- → Default entry: 1.0863 (CE).
- SL: 1.0858 (FVG low - 2-pip buffer); risk = 5 pips.
- Compare to alternatives: near-edge entry at 1.0866 → SL = 1.0858, risk = 8 pips, worse R:R; far-edge entry at 1.0860 → may not fill at all.

## Common Mistakes

- **Pre-2025 habits.** Older ICT teaching tended to default to far-edge entries. The 2025 refinement explicitly steps back from that. Update mental model.
- **Going to CE without reaction.** CE without a confirming reaction candle on a lower TF is just a level. Wait for at least a bullish (or bearish) wick / engulf at CE.
- **Refusing CE on small FVGs.** Sub-3-pip FVG CEs are noisy; consider a wider FVG instead.

## Related Concepts

- [consequent-encroachment](consequent-encroachment.md), [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md).
- [fvg-classification-2025](fvg-classification-2025.md), [immediate-rebalance-fvg](immediate-rebalance-fvg.md), [delayed-rebalance-fvg](delayed-rebalance-fvg.md).

## Citations

- `ICT-2025-CE-PRIMARY-ENTRY` — multiple 2025 videos reinforcing CE as default.
