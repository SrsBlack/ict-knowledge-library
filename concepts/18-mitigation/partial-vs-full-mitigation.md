# Partial vs Full Mitigation — Disambiguation

**Category:** 18-mitigation
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2025
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2025-CE-PRIMARY-ENTRY
**Tags:** mitigation, disambiguation, partial, full

## Definition

When a structure (OB, FVG, breaker) is being mitigated, two thresholds are commonly distinguished:

- **Partial mitigation** — price has touched the structure but has NOT reached its midpoint (CE for FVG, MT for OB).
- **Full mitigation** — price has reached at least the midpoint (the standard "mitigated" state per most ICT framings).

Some practitioners further distinguish a third state — **completely consumed** — when price has reached the **far edge** of the structure. The library uses **partial / mitigated / fully consumed** as the canonical 3-state lifecycle.

## Formal Criteria

For any structure with `near_edge`, `midpoint` (CE or MT), `far_edge`:

- **Fresh:** price has not touched the structure since formation.
- **Partial:** price has reached at most `near_edge` but not yet `midpoint`.
- **Mitigated** (default "tested" state): price has reached at least `midpoint`.
- **Fully consumed:** price has reached at least `far_edge`.

## Formula / Math

```
state(structure, current_price_history):
  if no touch yet:                            "fresh"
  elif touched_near_edge but not midpoint:    "partial"
  elif reached_midpoint but not far_edge:     "mitigated"
  elif reached_far_edge:                       "fully_consumed"
```

## Machine-Readable

```json
{
  "id": "partial-vs-full-mitigation",
  "category": "18-mitigation",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "states: fresh | partial | mitigated | fully_consumed"},
    {"id": "c2", "expr": "transition driven by deepest_price_into_structure"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2025",
  "related": ["mitigation-definition","mitigation-of-ob","mitigation-of-fvg","mitigation-of-breaker","fvg-mitigation","mitigated-order-block","unmitigated-order-block"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2025-CE-PRIMARY-ENTRY"]
}
```

## Visual Pattern

```
   structure lifecycle (bullish FVG example):

   1.0866 ─── far edge (FVG high)        ← fully consumed when reached
                                           
   1.0863 ─── midpoint (CE)              ← MITIGATED when reached (default)
                                           
   1.0860 ─── near edge (FVG low)        ← PARTIAL when first touched
   
   No touch                              ← FRESH
```

## Timeframes

All TFs.

## Examples

**Example 1 — lifecycle of a bullish FVG:**
- t0: FVG forms. State: **fresh**.
- t1: price wicks 1.0865 (above near edge but below CE). State: **partial**.
- t2: price wicks 1.0863 (CE). State: **mitigated** — first-touch entry triggered.
- t3: price wicks 1.0860 (far edge). State: **fully consumed**.

## Common Mistakes

- **Treating partial as mitigation.** A wick that touches the near edge but doesn't reach CE is not yet mitigated under default ICT framing.
- **Treating mitigation as full fill.** The 2025 default elevates CE to the mitigation threshold; "full fill" is a stricter condition (fully-consumed state).
- **Mid-state ambiguity.** Pick a default state-machine and apply consistently; mixing definitions across files / strategies produces inconsistent backtests.

## Related Concepts

- [mitigation-definition](mitigation-definition.md), [mitigation-of-ob](mitigation-of-ob.md), [mitigation-of-fvg](mitigation-of-fvg.md), [mitigation-of-breaker](mitigation-of-breaker.md), [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md), [mitigated-order-block](../07-order-blocks/mitigated-order-block.md), [unmitigated-order-block](../07-order-blocks/unmitigated-order-block.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2025-CE-PRIMARY-ENTRY`.
