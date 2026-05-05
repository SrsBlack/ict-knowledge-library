# FVG Classification (2025 Framing)

**Category:** 06-fair-value-gaps
**Aliases:** FVG classification, immediate vs delayed rebalance, FVG taxonomy
**ICT Confidence:** high
**Year Introduced:** 2024
**Year Refined:** 2025
**Source IDs:** ICT-2024-FVG-CLASSIFICATION, ICT-2025-CE-PRIMARY-ENTRY
**Tags:** fvg, classification, 2024-refinement, 2025-refinement

## Definition

In 2024–2025 ICT formalized a binary FVG classification — **immediate rebalance** vs **delayed rebalance** — based on how quickly price returns to fill the gap. Combined with the 2025 elevation of CE to the primary entry zone, this produces a more disciplined FVG-based setup framework. The classification matters because the two types signal different intent: immediate = continuation, delayed = pending revisit setup.

## Formal Criteria

The 2024–2025 framework:

| Type | Time-to-fill | Implication | Setup style |
|---|---|---|---|
| Immediate | Within 1–3 bars after formation | Continuation in displacement direction | Reading signal, not entry |
| Delayed | Stays unfilled for 5+ bars | Future revisit target | Plan and wait for retest |

When entering a delayed FVG on its eventual revisit, the **CE-as-primary-entry** rule applies: default to CE.

## Formula / Math

```
classify_fvg(fvg, current_bar):
  if fvg.formed_bar + 3 >= current_bar AND fvg has been touched:
    return "immediate"
  elif fvg.formed_bar + 5 <= current_bar AND not touched yet:
    return "delayed"
  else:
    return "transitional"     # 4-5 bars old, untouched
```

## Machine-Readable

```json
{
  "id": "fvg-classification-2025",
  "category": "06-fair-value-gaps",
  "aliases": ["FVG-classification", "immediate-vs-delayed-rebalance"],
  "criteria": [
    {"id": "c1", "expr": "binary_classification: immediate | delayed"},
    {"id": "c2", "expr": "immediate == fill_within_1to3_bars"},
    {"id": "c3", "expr": "delayed == unfilled_for_5plus_bars"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2024",
  "year_refined": "2025",
  "related": ["fair-value-gap","immediate-rebalance-fvg","delayed-rebalance-fvg","ce-as-primary-entry","consequent-encroachment"],
  "sources": ["ICT-2024-FVG-CLASSIFICATION","ICT-2025-CE-PRIMARY-ENTRY"]
}
```

## Visual Pattern

```
   Immediate FVG:                       Delayed FVG:

   ───── ──── ──── ───── ─────         ───── ──── ──── ──── ──── ──── ──── ──── ─────
       formed   filled                       formed                          filled
       (bar n)  (bar n+2)                    (bar n)                         (bar n+12)
       continuation continues                FVG sat as planned setup
```

## Timeframes

All TFs.

## Examples

**Example 1 — classifying a freshly-formed FVG:**
- M15 bullish FVG forms at 14:30; size 6 pips.
- 14:45: price returns to CE → immediate rebalance (filled within ~1 bar).
- → continuation signal; the FVG is consumed; look for next FVG / structure.

**Example 2:**
- M15 bullish FVG forms at 14:30.
- Through 16:30 (8 bars later), price has not touched the FVG.
- → classified as delayed; mark the level; plan entry on eventual revisit at CE.

## Common Mistakes

- **Mid-classification action.** A 4-bar-old untouched FVG is in transition — don't force a category.
- **Trading immediate FVGs as setups.** Immediate fills happen too fast for live entries; treat them as signal interpretation.
- **Letting delayed FVGs drift indefinitely.** A "delayed" FVG that hasn't filled in 50+ bars and has been superseded by structure is effectively irrelevant.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [immediate-rebalance-fvg](immediate-rebalance-fvg.md), [delayed-rebalance-fvg](delayed-rebalance-fvg.md), [ce-as-primary-entry](ce-as-primary-entry.md), [consequent-encroachment](consequent-encroachment.md).

## Citations

- `ICT-2024-FVG-CLASSIFICATION`, `ICT-2025-CE-PRIMARY-ENTRY`.
