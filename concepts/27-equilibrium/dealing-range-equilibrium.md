# Dealing Range Equilibrium

**Category:** 27-equilibrium
**Aliases:** range EQ, DR EQ, primary equilibrium
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PD-ARRAYS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** equilibrium, dealing-range, primary

## Definition

Dealing range equilibrium is **THE** primary EQ in ICT's framework — the 50% midpoint of the current dealing range bounded by LTH_ext and LTL_ext on the analysis timeframe. When ICT says "above equilibrium" or "below equilibrium" without qualification, this is the EQ being referenced. Most premium/discount classification of PD arrays uses dealing-range EQ as the reference.

## Formal Criteria

- The reference dealing range is defined ([dealing-range](../05-pd-arrays/dealing-range.md)).
- EQ = midpoint of LTH_ext and LTL_ext.
- A new dealing range begins when external BOS occurs; EQ is recomputed.

## Formula / Math

```
DR_EQ = (LTH_ext + LTL_ext) / 2
```

## Machine-Readable

```json
{
  "id": "dealing-range-equilibrium",
  "category": "27-equilibrium",
  "aliases": ["range-eq", "DR-EQ", "primary-equilibrium"],
  "criteria": [
    {"id": "c1", "expr": "EQ == midpoint of LTH_ext and LTL_ext on reference TF"}
  ],
  "timeframes": ["M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["equilibrium-definition","dealing-range","equilibrium-as-decision-point","premium-array","discount-array","external-structure"],
  "sources": ["ICT-2016-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   LTH_ext ──────────  ← top of dealing range
            premium half
   ──────── DR_EQ ──── ← primary equilibrium
            discount half
   LTL_ext ──────────  ← bottom of dealing range
```

## Timeframes

H1+ produces meaningful DR ranges. M5/M15 ranges drift too quickly to make DR_EQ stable.

## Examples

**Example 1 — D1 dealing range with EQ:**
- D1 LTH 1.1000, LTL 1.0800.
- D1 DR_EQ = 1.0900.
- Current price 1.0855 = D1 discount → long setups consistent with HTF bullish bias valid.
- A bullish OB at 1.0820 sits at depth 0.8 into discount → high-conviction long zone.

## Common Mistakes

- **Stale range = stale EQ.** Update both when an external BOS occurs.
- **TF mismatch.** State which TF's DR_EQ you're using; H4 and D EQ values often differ by ~50–150 pips.
- **Dual-EQ confusion.** Don't blend DR_EQ with FVG-EQ (CE) — they're different scales of the same concept.

## Related Concepts

- [equilibrium-definition](equilibrium-definition.md) — broader concept.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the range whose midpoint this is.
- [equilibrium-as-decision-point](equilibrium-as-decision-point.md) — operational use.
- [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md).
- [external-structure](../01-market-structure/external-structure.md).

## Citations

- `ICT-2016-PD-ARRAYS`, `ICT-2022-MENTORSHIP-OVERVIEW`.
