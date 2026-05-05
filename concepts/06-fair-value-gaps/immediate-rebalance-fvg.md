# Immediate Rebalance FVG

**Category:** 06-fair-value-gaps
**Aliases:** immediate FVG, fast-fill FVG, continuation FVG
**ICT Confidence:** high
**Year Introduced:** 2024
**Year Refined:** 2025
**Source IDs:** ICT-2024-FVG-CLASSIFICATION
**Tags:** fvg, immediate-rebalance, classification, 2024-refinement

## Definition

An **immediate rebalance FVG** is one that gets **closed within 1–2 candles** of formation — price returns to the FVG zone almost as soon as it forms and fills it, then continues in the displacement direction. ICT teaches immediate rebalance as a **continuation signal**: the algorithm filled the imbalance quickly because intent is to continue, not consolidate. Counterpart: [delayed-rebalance-fvg](delayed-rebalance-fvg.md). The immediate-vs-delayed classification is part of the 2024 FVG refinement (`ICT-2024-FVG-CLASSIFICATION`).

## Formal Criteria

- An FVG forms at candle n (between n-1 and n+1).
- A subsequent candle (typically n+1, n+2, or n+3 — within the next 1–3 bars) revisits the FVG zone.
- Revisit reaches at least CE; often fills the FVG fully.
- Post-rebalance, price continues in the direction of the original displacement.
- The FVG is now considered "rebalanced" and structurally consumed.

## Formula / Math

```
immediate_rebalance(fvg) := exists candle k in {n+1, n+2, n+3}
                              such that price(k) reaches at least ce(fvg)
                              AND post-rebalance: price continues in
                                  original displacement direction
```

## Machine-Readable

```json
{
  "id": "immediate-rebalance-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["immediate-FVG", "fast-fill-FVG"],
  "criteria": [
    {"id": "c1", "expr": "FVG_revisited_within_1to3_bars == true"},
    {"id": "c2", "expr": "rebalance_reaches_at_least_CE == true"},
    {"id": "c3", "expr": "continuation_in_original_direction_after == true"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2024",
  "year_refined": "2025",
  "related": ["fair-value-gap","delayed-rebalance-fvg","fvg-classification-2025","consequent-encroachment","ce-as-primary-entry","imbalance-rebalance"],
  "sources": ["ICT-2024-FVG-CLASSIFICATION"]
}
```

## Visual Pattern

```
   immediate-rebalance bullish FVG:

   bar n-1: ─── small candle
   bar n:   ─── big bullish displacement (FVG forms below n+1)
   bar n+1: ─── pulls back, touches CE of FVG
   bar n+2: ─── continues up (FVG rebalanced + continuation)
```

## Timeframes

Most observable on M5–H4. On HTF, rebalance "within 1–3 bars" is a longer wall-clock window.

## Examples

**Example 1 — M5 immediate rebalance:**
- M5 bullish FVG forms at 1.0860–1.0866 on candle 09:30.
- 09:35 candle pulls back to 1.0863 (CE), prints a bullish wick reaction.
- 09:40 candle closes at 1.0875, continuing up.
- → immediate rebalance; FVG consumed; bullish bias confirmed for the next push.

## Common Mistakes

- **Treating immediate rebalance as a setup.** The CE-touch happens too fast for most live entries; it's more an *interpretation* signal (continuation incoming) than an entry trigger.
- **Confusing with delayed rebalance.** If the FVG goes ~10+ bars without a touch, it's delayed, not immediate.
- **Insisting on full fill.** Rebalance to CE qualifies; full fill is icing.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [delayed-rebalance-fvg](delayed-rebalance-fvg.md), [fvg-classification-2025](fvg-classification-2025.md), [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md), [imbalance-rebalance](../26-imbalance/imbalance-rebalance.md).

## Citations

- `ICT-2024-FVG-CLASSIFICATION`.
