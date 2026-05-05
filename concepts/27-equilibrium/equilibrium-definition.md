# Equilibrium — Definition

**Category:** 27-equilibrium
**Aliases:** EQ, equilibrium price, mid-range, fair price
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PD-ARRAYS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** equilibrium, eq, foundational

## Definition

Equilibrium (EQ) is the **50% midpoint of any reference range** — typically the current dealing range, but also FVGs (where it's called consequent encroachment / CE), individual swing legs, and any pair of price extremes. EQ is ICT's algorithmic "fair price": above EQ is premium (sell-side reference), below is discount (buy-side reference). EQ functions both as a level price often returns to and as a decision pivot for entry direction.

## Formal Criteria

For any reference range bounded by `top` and `bot`:

- `EQ = (top + bot) / 2` — the geometric midpoint.
- Premium half = `(EQ, top]`.
- Discount half = `[bot, EQ)`.
- A small tolerance `±ε` around EQ defines the equilibrium zone (~ a few pips on FX).

EQ is computed for:

- The current dealing range (most common usage).
- An individual swing leg (range from leg start to leg end).
- An FVG (where EQ = CE, the FVG's 50% midpoint).
- An OB (rarely; OB EQ is the body midpoint).

## Formula / Math

```
EQ(range) = (top(range) + bot(range)) / 2

dealing_range_EQ  = (LTH_ext + LTL_ext) / 2
swing_leg_EQ      = (leg_start + leg_end) / 2
FVG_EQ            = (FVG_high + FVG_low) / 2     # = consequent encroachment
```

## Machine-Readable

```json
{
  "id": "equilibrium-definition",
  "category": "27-equilibrium",
  "aliases": ["EQ", "equilibrium-price", "mid-range", "fair-price"],
  "criteria": [
    {"id": "c1", "expr": "EQ == (range_top + range_bot) / 2"},
    {"id": "c2", "expr": "applies_to_any_reference_range == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["dealing-range-equilibrium","equilibrium-as-decision-point","mean-threshold","pd-array-definition","premium-array","discount-array","dealing-range","consequent-encroachment"],
  "sources": ["ICT-2016-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   range_top ────────────  premium half
                █▒▒
                █▒▒  ← short PD arrays here
   ───────────────── EQ (50% midpoint)  ← decision pivot
                ░░
                ░░  ← long PD arrays here
   range_bot ────────────  discount half
```

## Timeframes

All TFs.

## Examples

**Example 1 — daily EQ as decision pivot:**
- Daily LTH 1.1000, LTL 1.0800. EQ = 1.0900.
- Current price 1.0855 → discount; bullish-bias setups valid here.
- If price rallies to 1.0905 → just above EQ; longs should already be in profit; short setups become valid only at deeper premium PD arrays (1.0945+).

## Common Mistakes

- **Using a stale range.** When external BOS occurs, the dealing range changes. EQ must be recomputed.
- **EQ-only entries.** EQ is a decision pivot, not a high-conviction entry by itself. Pair with a PD array (FVG / OB / breaker).
- **Ignoring scale.** Daily EQ on EURUSD might span 200 pips of range — a "tolerance" of 5 pips is fine. M5 EQ on the same pair might span 30 pips — tolerance scales accordingly.

## Related Concepts

- [dealing-range-equilibrium](dealing-range-equilibrium.md) — EQ within the primary reference frame.
- [equilibrium-as-decision-point](equilibrium-as-decision-point.md) — operational use as pivot.
- [mean-threshold](mean-threshold.md) — broader mean-reversion concept.
- [pd-array-definition](../05-pd-arrays/pd-array-definition.md), [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md), [dealing-range](../05-pd-arrays/dealing-range.md).
- [consequent-encroachment](../06-fair-value-gaps/consequent-encroachment.md) — FVG-scale EQ.

## Citations

- `ICT-2016-PD-ARRAYS`, `ICT-2022-MENTORSHIP-OVERVIEW`.
