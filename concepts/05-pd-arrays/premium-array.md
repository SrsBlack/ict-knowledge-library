# Premium Array

**Category:** 05-pd-arrays
**Aliases:** premium PD array, premium level, sell-side array
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PD-ARRAYS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** pd-array, premium, sell-side

## Definition

A premium array is any PD array (FVG, OB, breaker, etc.) sitting **above the equilibrium** of a reference dealing range. Premium arrays are the institutional sell-side references — the levels at which the algorithm distributes when traveling from a discount-side accumulation. ICT's discipline: short setups originate at premium PD arrays.

## Formal Criteria

- The reference dealing range has bounds LTH_ext (top) and LTL_ext (bottom).
- EQ = (LTH_ext + LTL_ext) / 2.
- A PD array `A` is premium iff `price(A) > EQ`.
- Stronger premium = closer to LTH_ext (deep premium); shallower premium = just above EQ.

## Formula / Math

```
EQ = (LTH_ext + LTL_ext) / 2

is_premium_array(level) := level > EQ

depth_into_premium(level) := (level - EQ) / (LTH_ext - EQ)
                              # 0 = at EQ, 1 = at LTH_ext
```

`depth_into_premium = 0.79` corresponds to the OTE 0.79 level (see [ote-79](../17-optimal-trade-entry/ote-79.md)) — a deep-premium short entry zone.

## Machine-Readable

```json
{
  "id": "premium-array",
  "category": "05-pd-arrays",
  "aliases": ["premium-PD-array", "sell-side-array"],
  "criteria": [
    {"id": "c1", "expr": "level > EQ_of_reference_range"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["pd-array-definition","discount-array","equilibrium-definition","dealing-range","ote-overview","ote-79","bearish-order-block","bearish-fvg"],
  "sources": ["ICT-2016-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   LTH_ext ─────────── ← top of dealing range
                ▒▒▒  ← deep premium (depth ~0.7-0.9)
                ▒▒▒    bearish OB / FVG here = high-conviction short
                ▒▒▒
   ──────────────────── ← shallow-premium boundary (EQ + buffer)
   ──────────────────── ← EQ
   (discount below)
   LTL_ext ─────────────
```

## Timeframes

All TFs.

## Examples

**Example 1 — bearish setup at premium FVG:**
- H4 dealing range: LTH 1.1000, LTL 1.0800. EQ = 1.0900.
- HTF (D) bias bearish.
- H4 bearish FVG at 1.0945–1.0960 → depth = (1.0950 − 1.0900) / 100 = 0.50 (mid-premium).
- Short setup: enter on retest of the bearish FVG, target EQ first (1.0900), then LTL ERL (1.0800).

## Common Mistakes

- **Buying at premium.** ICT discipline says no — long entries belong at discount arrays, not premium ones. A "bullish-looking" pattern at premium is suspect.
- **Skipping the depth check.** A premium array just above EQ is shallow and weaker than one near LTH_ext. Depth matters for conviction.
- **Wrong reference range.** Always state the reference TF's dealing range. Premium on H1 may be discount on H4.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [discount-array](discount-array.md), [equilibrium-definition](../27-equilibrium/equilibrium-definition.md), [dealing-range](dealing-range.md).
- [ote-overview](../17-optimal-trade-entry/ote-overview.md), [ote-79](../17-optimal-trade-entry/ote-79.md) — premium-side fib entries.
- [bearish-order-block](../07-order-blocks/bearish-order-block.md), [bearish-fvg](../06-fair-value-gaps/bearish-fvg.md) — premium-array examples.

## Citations

- `ICT-2016-PD-ARRAYS`, `ICT-2022-MENTORSHIP-OVERVIEW`.
