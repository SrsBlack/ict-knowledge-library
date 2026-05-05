# Discount Array

**Category:** 05-pd-arrays
**Aliases:** discount PD array, discount level, buy-side array
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PD-ARRAYS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** pd-array, discount, buy-side

## Definition

A discount array is any PD array sitting **below the equilibrium** of a reference dealing range. Discount arrays are the institutional buy-side references. ICT's discipline: long setups originate at discount PD arrays.

## Formal Criteria

- Reference dealing range with bounds LTH_ext, LTL_ext.
- EQ = (LTH_ext + LTL_ext) / 2.
- A PD array `A` is discount iff `price(A) < EQ`.
- Deep discount = closer to LTL_ext; shallow discount = just below EQ.

## Formula / Math

```
EQ = (LTH_ext + LTL_ext) / 2

is_discount_array(level) := level < EQ

depth_into_discount(level) := (EQ - level) / (EQ - LTL_ext)
                              # 0 = at EQ, 1 = at LTL_ext
```

`depth_into_discount = 0.79` corresponds to OTE 0.79 long-side entry zone.

## Machine-Readable

```json
{
  "id": "discount-array",
  "category": "05-pd-arrays",
  "aliases": ["discount-PD-array", "buy-side-array"],
  "criteria": [
    {"id": "c1", "expr": "level < EQ_of_reference_range"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["pd-array-definition","premium-array","equilibrium-definition","dealing-range","ote-overview","ote-79","bullish-order-block","bullish-fvg"],
  "sources": ["ICT-2016-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   LTH_ext ───────────── (premium above)
   ────────────────────── EQ
   ──────────────────────  shallow-discount boundary
                ░░░  ← deep discount (depth ~0.7–0.9)
                ░░░    bullish OB / FVG here = high-conviction long
                ░░░
   LTL_ext ───────────── ← bottom of dealing range
```

## Timeframes

All TFs.

## Examples

**Example 1 — bullish setup at discount OB:**
- H4 dealing range: LTH 1.1000, LTL 1.0800. EQ = 1.0900.
- HTF bullish.
- H4 bullish OB at 1.0820–1.0830 → depth_into_discount = (1.0900 − 1.0825) / 100 = 0.75 (deep discount).
- Long setup: enter on retest, target EQ (1.0900) first, then LTH ERL (1.1000).

## Common Mistakes

- **Selling at discount.** ICT says no — short setups belong at premium arrays.
- **Shallow vs deep confusion.** A discount array just below EQ is much weaker than one at depth 0.79. Conviction scales with depth.
- **Reference-range drift.** Refresh the reference range when external BOS occurs; the old discount classification may flip.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [premium-array](premium-array.md), [equilibrium-definition](../27-equilibrium/equilibrium-definition.md), [dealing-range](dealing-range.md).
- [ote-overview](../17-optimal-trade-entry/ote-overview.md), [ote-79](../17-optimal-trade-entry/ote-79.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bullish-fvg](../06-fair-value-gaps/bullish-fvg.md).

## Citations

- `ICT-2016-PD-ARRAYS`, `ICT-2022-MENTORSHIP-OVERVIEW`.
