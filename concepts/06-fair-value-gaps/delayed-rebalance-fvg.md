# Delayed Rebalance FVG

**Category:** 06-fair-value-gaps
**Aliases:** delayed FVG, slow-fill FVG, persistent FVG
**ICT Confidence:** high
**Year Introduced:** 2024
**Year Refined:** 2025
**Source IDs:** ICT-2024-FVG-CLASSIFICATION
**Tags:** fvg, delayed-rebalance, classification, 2024-refinement

## Definition

A **delayed rebalance FVG** stays **open** for many bars after formation — the algorithm did not immediately fill it. ICT teaches delayed FVGs as **higher-probability entry setups** than immediate ones because the unfilled FVG remains on the chart as an explicit unworked zone the algorithm intends to revisit later. The delay creates time for the analyst to identify the FVG, plan the entry, and wait. Counterpart: [immediate-rebalance-fvg](immediate-rebalance-fvg.md). Part of the 2024 FVG classification refinement.

## Formal Criteria

- An FVG forms at candle n.
- The next 5–10+ bars do NOT revisit the FVG (no touch, no CE-fill).
- The FVG remains as a marked zone the analyst tracks as a future entry / target reference.
- Eventually price returns and fills (often hours, sometimes days later); the entry is taken on that revisit.

## Formula / Math

```
delayed_rebalance(fvg) := for k in [n+1, ..., n+10]:
                            no candle in this window reaches ce(fvg)
                          AND eventually price revisits later
```

## Machine-Readable

```json
{
  "id": "delayed-rebalance-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["delayed-FVG", "slow-fill-FVG", "persistent-FVG"],
  "criteria": [
    {"id": "c1", "expr": "FVG_unfilled_for_5plus_bars == true"},
    {"id": "c2", "expr": "future_revisit_expected == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2024",
  "year_refined": "2025",
  "related": ["fair-value-gap","immediate-rebalance-fvg","fvg-classification-2025","consequent-encroachment","ce-as-primary-entry","imbalance-rebalance"],
  "sources": ["ICT-2024-FVG-CLASSIFICATION"]
}
```

## Visual Pattern

```
   delayed-rebalance bullish FVG:

   bar n-1, n, n+1 → FVG forms at [1.0860, 1.0866]
   bars n+2 ... n+8: price stays above 1.0866 (no fill)
   bar n+12: pulls back, fills FVG to CE
                  ↑ this is the entry

   The FVG sat unfilled for many bars; entry happens on the eventual revisit.
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 delayed rebalance:**
- H1 bullish FVG forms 14:00 NY at 1.0860–1.0866.
- For the next 8 H1 candles (8 hours), price stays above 1.0870 — FVG unfilled.
- Next day's London open: M5 sweeps Asian SSL, displaces up, then H1 candle pulls back into FVG zone, hits CE 1.0863.
- Long entry on retest at CE (per [ce-as-primary-entry](ce-as-primary-entry.md)).
- The 8-hour delay gave time to plan; conviction is higher than chasing an immediate-rebalance fill.

## Common Mistakes

- **Forgetting the FVG.** Delayed FVGs require active tracking — a marked level on the chart that the analyst checks back to as price approaches.
- **Treating delayed = guaranteed.** Some delayed FVGs never fill and become structurally irrelevant when superseded by new structure.
- **Confusing with immediate rebalance.** The classification is by *time-to-fill* — within 1–3 bars = immediate, 5+ bars = delayed.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [immediate-rebalance-fvg](immediate-rebalance-fvg.md), [fvg-classification-2025](fvg-classification-2025.md), [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md), [imbalance-rebalance](../26-imbalance/imbalance-rebalance.md).

## Citations

- `ICT-2024-FVG-CLASSIFICATION`.
