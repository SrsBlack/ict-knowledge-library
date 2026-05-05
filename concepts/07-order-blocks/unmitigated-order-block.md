# Unmitigated Order Block

**Category:** 07-order-blocks
**Aliases:** unmitigated OB, fresh OB, virgin OB, untested OB
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-OB-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, unmitigated, fresh, foundational

## Definition

An unmitigated order block is one that has **not yet been tested** by price since formation. ICT teaches unmitigated OBs as the **highest-conviction entry zones** in the OB family: the algorithm has not yet consumed the institutional reference, so the next price visit carries the full setup probability. Counterpart to [mitigated-order-block](mitigated-order-block.md).

## Formal Criteria

- The OB qualifies per [order-block-criteria](order-block-criteria.md).
- Price has NOT returned to the OB body (or in the strict version, to the OB's MT) since formation.
- The OB still acts as the canonical entry zone for setups in its direction.

## Formula / Math

```
is_unmitigated(ob) := for all candles k after ob.formed_bar:
                       price(k) did NOT reach mt(ob)
```

## Machine-Readable

```json
{
  "id": "unmitigated-order-block",
  "category": "07-order-blocks",
  "aliases": ["unmitigated-OB", "fresh-OB", "virgin-OB", "untested-OB"],
  "criteria": [
    {"id": "c1", "expr": "no_price_return_to_OB_body_since_formation == true"},
    {"id": "c2", "expr": "still_fresh_high_conviction == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bullish-order-block","bearish-order-block","mitigated-order-block","mean-threshold","order-block-criteria"],
  "sources": ["ICT-2016-OB-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   unmitigated bullish OB:

   ▼  ← OB formed                ← Body still untouched
                ▲                ← displacement away
                ▲                
                ▲                
                ▲                ← price moves further away
                ▲ ▲ ▲            
                  ▼ ← pullback   ← but does NOT reach OB body
                ▲                  → unmitigated, fresh, high conviction
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 unmitigated bullish OB:**
- H1 bullish OB body 1.0820–1.0830 (MT 1.0825), formed 12 hours ago.
- Since formation, price has stayed above 1.0840 — never reached MT.
- → unmitigated. When price eventually returns and approaches 1.0825, this is a high-conviction long entry.
- If on retest price reaches MT and reacts strongly: classic OB-mitigation entry. The OB then transitions to mitigated for any future retest.

## Common Mistakes

- **Treating unmitigated as eternal.** The first retest mitigates the OB. Don't expect a second equally-strong reaction.
- **Mixing fresh with stale.** An "unmitigated" OB from many sessions ago that has been superseded by major structural shifts may no longer be operationally relevant — assess HTF context.
- **Wick-only "mitigation".** A wick brushing the OB body usually still counts as mitigation in the strict ICT framing (price was there).

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md), [mitigated-order-block](mitigated-order-block.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [order-block-criteria](order-block-criteria.md).

## Citations

- `ICT-2016-OB-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
