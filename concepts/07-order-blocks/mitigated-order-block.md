# Mitigated Order Block

**Category:** 07-order-blocks
**Aliases:** mitigated OB, tested OB, used OB
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-OB-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, mitigated, state

## Definition

A mitigated order block is an OB that has been **tested by price** — price has returned to the OB body (typically reaching at least MT) since the OB formed. Mitigated OBs lose their **fresh-entry conviction**: they may still produce reactions, but the high-probability initial setup has been consumed. ICT teaches that fresh OBs are preferred for new entries; mitigated OBs serve as secondary references only.

## Formal Criteria

An OB is mitigated when:

- Price has returned and **reached at least the OB's MT** since the OB formed.
- Some practitioners use **full body fill** (price reaches the far edge: low for bullish OB, high for bearish OB) as the mitigation threshold; ICT's common framing uses MT.
- Once mitigated, the OB is no longer "fresh."

## Formula / Math

```
default_mitigation_threshold := mt(ob)    # body midpoint

is_mitigated(ob) := exists candle k after ob.formed_bar
                     such that price(k) reaches mt(ob)

# Stricter version:
is_fully_mitigated(ob) := price(k) reaches far_edge(ob)
```

## Machine-Readable

```json
{
  "id": "mitigated-order-block",
  "category": "07-order-blocks",
  "aliases": ["mitigated-OB", "tested-OB", "used-OB"],
  "criteria": [
    {"id": "c1", "expr": "price_returned_and_reached_at_least_MT == true"},
    {"id": "c2", "expr": "OB_no_longer_fresh == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bullish-order-block","bearish-order-block","unmitigated-order-block","mean-threshold","mitigation-of-ob","fvg-mitigation"],
  "sources": ["ICT-2016-OB-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB lifecycle:

   bar n: ▼  ← OB formed
   bar n+1..n+5: ▲▲▲▲▲ displacement away
   bar n+12: price returns
   bar n+13: price reaches MT     ← MITIGATED here (default threshold)
   bar n+14: price reaches OB low ← FULLY MITIGATED
```

## Timeframes

All TFs M5+.

## Examples

**Example 1 — M15 bullish OB mitigation lifecycle:**
- 14:00 NY: bullish OB body at 1.0820–1.0830, MT 1.0825.
- 14:30: bullish displacement moves price to 1.0860.
- Hours later, price retraces to 1.0825 → OB is **mitigated** (default).
- If price continues to 1.0820 (OB low) → **fully mitigated**.
- Subsequent retests have lower conviction; look for fresh structure.

## Common Mistakes

- **Treating mitigated OBs as fresh entries.** The first touch is the high-conviction one; subsequent retests are progressively weaker.
- **Inconsistent thresholds.** Pick MT-mitigated OR full-fill-mitigated and apply consistently.
- **Forgetting wick mitigation.** A wick that touches MT and bounces still counts as mitigated under most ICT frameworks (price was *there*, regardless of close).

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md), [unmitigated-order-block](unmitigated-order-block.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [mitigation-of-ob](../18-mitigation/mitigation-of-ob.md), [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md).

## Citations

- `ICT-2016-OB-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
