# FVG Mitigation

**Category:** 06-fair-value-gaps
**Aliases:** FVG mitigated, FVG fill, mitigated FVG state
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fvg, mitigation, rebalance, status

## Definition

FVG mitigation is the **state change** that occurs when price returns to an FVG and **fills it sufficiently** to be considered "no longer fresh." The exact threshold varies — some practitioners use CE-touch as the mitigation point, others use full fill (price reaching the far edge). ICT's 2025 framing leans toward CE as the operational mitigation marker (consistent with [ce-as-primary-entry](ce-as-primary-entry.md)). Once mitigated, the FVG is structurally consumed and stops acting as a fresh entry zone.

## Formal Criteria

Operational definitions (pick one and apply consistently):

- **CE mitigation** (recommended, 2025 framing): FVG is mitigated once price reaches CE.
- **Full mitigation**: FVG is mitigated only when price fills to the far edge.
- **Partial mitigation**: FVG is partially mitigated if touched but not yet at CE.

Once mitigated:
- The FVG is no longer a high-conviction fresh entry zone.
- A new FVG taking its place is the next reference.
- Mitigated FVGs can still serve as secondary references (especially for inversion-FVG analysis).

## Formula / Math

```
mitigation_threshold := ce_of_fvg     # default per 2025 framing

is_mitigated(fvg) := exists candle k after fvg.formed_bar
                       such that price(k) reaches mitigation_threshold

# Status states:
state := "fresh"     if not_yet_touched
       | "partial"   if touched but not_at_threshold
       | "mitigated" if touched_at_or_past_threshold
```

## Machine-Readable

```json
{
  "id": "fvg-mitigation",
  "category": "06-fair-value-gaps",
  "aliases": ["FVG-mitigated", "FVG-fill"],
  "criteria": [
    {"id": "c1", "expr": "default_mitigation_threshold == CE (2025 framing)"},
    {"id": "c2", "expr": "states: fresh | partial | mitigated"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["fair-value-gap","consequent-encroachment","ce-as-primary-entry","imbalance-rebalance","mitigation-of-fvg","inversion-fvg","mitigated-order-block"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Fresh → Partial → Mitigated lifecycle:

   FVG forms ─┬── (fresh)
              │
              ↓ price touches near edge
              │
          (partial — between near edge and CE)
              │
              ↓ price reaches CE
              │
          (mitigated per 2025 default)
              │
              ↓ price reaches far edge
              │
          (fully mitigated)
```

## Timeframes

All TFs.

## Examples

**Example 1 — partial → mitigated:**
- M15 bullish FVG forms at 1.0860–1.0866 (size 6 pips, CE 1.0863).
- 14:45: price touches 1.0865 (near edge); FVG is now "partial."
- 15:30: price reaches 1.0863 (CE); FVG is now "mitigated" per 2025 default.
- 15:45: price reaches 1.0860 (far edge); FVG is "fully mitigated."
- Beyond this point, the FVG is structurally consumed.

## Common Mistakes

- **Inconsistent mitigation thresholds.** Pick CE-mitigation OR full-mitigation and stick with it; mixing produces inconsistent backtests and live decisions.
- **Treating mitigated FVGs as still-fresh.** Once mitigated, the algorithmic anchor weakens; new entries should reference fresh structure.
- **Confusing FVG mitigation with OB mitigation.** They use the same word; the threshold rules differ. See [mitigation-of-fvg](../18-mitigation/mitigation-of-fvg.md) and [mitigation-of-ob](../18-mitigation/mitigation-of-ob.md).

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md).
- [imbalance-rebalance](../26-imbalance/imbalance-rebalance.md), [mitigation-of-fvg](../18-mitigation/mitigation-of-fvg.md), [inversion-fvg](inversion-fvg.md), [mitigated-order-block](../07-order-blocks/mitigated-order-block.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
