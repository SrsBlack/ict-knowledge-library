# Mitigation of FVG

**Category:** 18-mitigation
**Aliases:** FVG mitigation, FVG tested, FVG fill
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2025
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2025-CE-PRIMARY-ENTRY
**Tags:** mitigation, fvg, foundational

## Definition

FVG mitigation is the act of price returning to an FVG and **reaching at least CE**. Per the 2025 ICT framing ([ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md)), CE is the canonical mitigation threshold for FVGs. Once mitigated, the FVG is structurally tested; the first-touch entry at CE is the highest-conviction setup. See also [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md) for the FVG-side framing of the same event.

## Formal Criteria

- An FVG exists per [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) criteria.
- Price returns and reaches at least CE = (fvg_low + fvg_high) / 2.
- Wick touches count.
- Optionally: full mitigation requires price reaching the far edge.

## Formula / Math

```
ce(fvg) = (fvg_low + fvg_high) / 2

is_fvg_mitigated(fvg) := exists future candle k
                          such that
                            (bullish FVG) low(k) <= ce(fvg)
                            OR (bearish FVG) high(k) >= ce(fvg)
```

## Machine-Readable

```json
{
  "id": "mitigation-of-fvg",
  "category": "18-mitigation",
  "aliases": ["FVG-mitigation", "FVG-tested", "FVG-fill"],
  "criteria": [
    {"id": "c1", "expr": "price reaches CE of FVG (default 2025 framing)"},
    {"id": "c2", "expr": "wick touch counts"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2025",
  "related": ["mitigation-definition","fvg-mitigation","consequent-encroachment","ce-as-primary-entry","fair-value-gap","imbalance-rebalance","partial-vs-full-mitigation"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2025-CE-PRIMARY-ENTRY"]
}
```

## Visual Pattern

```
   bullish FVG mitigation:

   ─── FVG high (1.0866) ──── (far edge)
   ─── CE (1.0863) ────── ← mitigation threshold (default)
   ─── FVG low (1.0860) ──── (near edge)

   first touch reaching CE = mitigated.
```

## Timeframes

All TFs.

## Examples

**Example 1 — M15 FVG mitigation:**
- M15 bullish FVG: low 1.0860, high 1.0866, CE 1.0863.
- Price returns; M15 wicks 1.0863 → mitigation triggered.
- First-touch long entry valid at CE per 2025 default.

## Common Mistakes

- **Insisting on full fill before considering mitigation.** Prefer CE (default 2025) — wider rebalance criteria miss most setups.
- **Treating an unfilled FVG as mitigated due to a nearby touch.** "Near miss" doesn't count; price must reach CE.

## Related Concepts

- [mitigation-definition](mitigation-definition.md), [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md), [consequent-encroachment](../06-fair-value-gaps/consequent-encroachment.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [imbalance-rebalance](../26-imbalance/imbalance-rebalance.md), [partial-vs-full-mitigation](partial-vs-full-mitigation.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2025-CE-PRIMARY-ENTRY`.
