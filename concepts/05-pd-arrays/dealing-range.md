# Dealing Range

**Category:** 05-pd-arrays
**Aliases:** trading range, range, swing range, reference range
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PD-ARRAYS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** range, dealing-range, foundational

## Definition

A dealing range is the price band bounded by the most recent confirmed long-term high (LTH) and long-term low (LTL) on the analysis timeframe — the **reference frame** for premium/discount classification, equilibrium, OTE, and PD-array depth measurements. ICT's analysis nearly always begins by identifying the current dealing range; without this frame, premium/discount cannot be defined and PD arrays have no reference.

## Formal Criteria

- The two most recent **unbroken** LTH and LTL on the reference TF define the bounds.
- An external BOS (close beyond either bound) ends the current range and starts a new one (the broken bound usually becomes the entry point of the next range).
- Inside the range: every price is either premium (above EQ), discount (below EQ), or at EQ.
- A dealing range exists at every TF; pick the TF that matches your trade horizon.

## Formula / Math

```
LTH_ext = highest unbroken LTH on TF
LTL_ext = lowest  unbroken LTL on TF

dealing_range = [LTL_ext, LTH_ext]
range_size    = LTH_ext - LTL_ext
EQ            = (LTH_ext + LTL_ext) / 2
```

## Machine-Readable

```json
{
  "id": "dealing-range",
  "category": "05-pd-arrays",
  "aliases": ["trading-range", "swing-range", "reference-range"],
  "criteria": [
    {"id": "c1", "expr": "bounds == [most_recent_unbroken_LTL, most_recent_unbroken_LTH]"},
    {"id": "c2", "expr": "current_price strictly_between bounds"}
  ],
  "timeframes": ["M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["pd-array-definition","premium-array","discount-array","equilibrium-definition","external-structure","internal-structure","internal-range-liquidity","external-range-liquidity"],
  "sources": ["ICT-2016-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   LTH_ext ──────────────────  ← upper bound (premium ceiling)
            (premium half)
   ──────────────────────────  ← EQ (50% midpoint)
            (discount half)
   LTL_ext ──────────────────  ← lower bound (discount floor)
```

## Timeframes

H1+ produces meaningful dealing ranges. M5/M15 ranges are too noisy and shift constantly. ICT analysis routinely names the dealing-range TF explicitly ("the daily dealing range is …").

## Examples

**Example 1 — daily dealing range:**
- Daily LTH 1.1000 (formed last week), LTL 1.0800 (formed two weeks ago).
- Daily dealing range = [1.0800, 1.1000], EQ = 1.0900.
- Until either bound is broken on a daily close, this is the reference for daily premium/discount.

**Example 2 — fractal contradiction resolved:**
- H4 dealing range: 1.0850–1.0925 (smaller, recent).
- D dealing range: 1.0800–1.1000 (larger, older).
- Current price 1.0890 = premium on H4 (above 1.0888 H4 EQ), but below D EQ (1.0900) = D discount.
- Resolution: state the reference TF when discussing premium/discount.

## Common Mistakes

- **Stale range.** An external BOS ends the current range. Failing to redefine the range produces wrong premium/discount labels.
- **Mixing TF references.** Premium/discount only makes sense relative to a stated TF range. Multi-TF analysis should label each.
- **Ignoring fractal hierarchy.** Long-term highs / lows that bound the range are themselves the most-recent ITH/ITL pair *that became LTH/LTL*. See [external-structure](../01-market-structure/external-structure.md).

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [premium-array](premium-array.md), [discount-array](discount-array.md), [equilibrium-definition](../27-equilibrium/equilibrium-definition.md).
- [external-structure](../01-market-structure/external-structure.md), [internal-structure](../01-market-structure/internal-structure.md).
- [internal-range-liquidity](../02-liquidity/internal-range-liquidity.md), [external-range-liquidity](../02-liquidity/external-range-liquidity.md).

## Citations

- `ICT-2016-PD-ARRAYS`, `ICT-2022-MENTORSHIP-OVERVIEW`.
