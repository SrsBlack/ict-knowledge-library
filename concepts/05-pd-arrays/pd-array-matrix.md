# PD Array Matrix

**Category:** 05-pd-arrays
**Aliases:** PDA matrix, PD array map, multi-TF PDA grid
**ICT Confidence:** medium
**Year Introduced:** 2022
**Year Refined:** 2024
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW, ICT-2024-MENTORSHIP-MODULE-LIST
**Tags:** pd-array, matrix, mapping

## Definition

The PD array matrix is the **PDA-side counterpart of the [liquidity-matrix](../02-liquidity/liquidity-matrix.md)**: a structured pre-trade tabulation of every relevant PD array across multiple timeframes, sorted by price, listing TF / array type / depth (premium or discount with its depth value) / freshness / direction. It is a working document the analyst maintains during the session — adding new arrays as they form, marking arrays as "tested" or "mitigated" once price interacts with them.

## Formal Criteria

A complete matrix lists, for the current symbol:

- Above and below current price, every PD array on M15 / H1 / H4 / D / W.
- For each array: TF, type (OB / FVG / breaker / etc.), price range, premium-or-discount + depth, freshness (unmitigated / partially / fully mitigated), polarity (bullish / bearish).
- Sorted by price for navigation.
- Optional: HTF-LTF nesting indicators (which arrays nest inside others).

## Formula / Math

```
matrix(t) = sort_by_price([
  { tf: M15 | H1 | H4 | D | W,
    type: OB | FVG | breaker | mitigation | rejection | propulsion | vacuum | EQ,
    price_range: [low, high],
    side: premium | discount,
    depth: float in [0, 1],
    polarity: bullish | bearish,
    fresh: bool,
    nested_with: [list of other matrix entries it overlaps]
  }
  for every identified array
])
```

## Machine-Readable

```json
{
  "id": "pd-array-matrix",
  "category": "05-pd-arrays",
  "aliases": ["PDA-matrix", "PDA-map"],
  "criteria": [
    {"id": "c1", "expr": "every_array_listed_with_tf_type_depth == true"},
    {"id": "c2", "expr": "matrix_sorted_by_price == true"}
  ],
  "timeframes": ["M15","H1","H4","D","W"],
  "confidence": "medium",
  "year_introduced": "2022",
  "year_refined": "2024",
  "related": ["pd-array-definition","pd-array-hierarchy","pd-array-nesting","pd-array-confluence","htf-pd-array-hierarchy","liquidity-matrix"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW","ICT-2024-MENTORSHIP-MODULE-LIST"]
}
```

## Visual Pattern

A tabular view, not a chart pattern. Sample matrix for a bullish-bias EURUSD intraday session:

```
TF   Type      Range            Side    Depth  Polarity  Fresh  Nest
──   ───────   ──────────────   ──────  ─────  ────────  ─────  ────
W    OB        1.0950–1.0970    premium 0.71   bear      yes    -
D    FVG       1.0935–1.0945    premium 0.40   bear      yes    nested in W OB
D    EQ        1.0900           --      0.50   --        --     -
H4   OB        1.0840–1.0850    discount 0.50  bull      yes    -
H4   FVG       1.0825–1.0835    discount 0.71  bull      yes    -
H1   OB        1.0820–1.0830    discount 0.78  bull      yes    nested in H4 FVG
─── current price 1.0855 ───
H1   FVG       1.0808–1.0815    discount 0.92  bull      yes    -
D    OB        1.0790–1.0800    discount 0.95  bull      yes    -
```

## Timeframes

The matrix is multi-TF by definition. Don't include arrays from below your minimum entry TF (clutter).

## Examples

**Example 1 — using the matrix:**
- HTF (D, W) bullish bias.
- Matrix shows nested H4-FVG / H1-OB at 1.0820–1.0835 (deep discount, fresh).
- Pre-trade plan: long entry on retest of 1.0820–1.0830 with SL below H1 OB (1.0815), TP1 at D EQ (1.0900), TP2 at D FVG (1.0935), final at W OB premium (1.0970).

## Common Mistakes

- **Listing everything.** Too many entries make the matrix unusable. Cap by TF (M15+) and by freshness (unmitigated only).
- **Static matrix.** Refresh as price interacts with arrays — once an array is mitigated or invalidated by a BOS, mark it as such.
- **Skipping nesting markers.** Nested arrays often produce the strongest setups; explicitly note which arrays overlap.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [pd-array-hierarchy](pd-array-hierarchy.md), [pd-array-nesting](pd-array-nesting.md), [pd-array-confluence](pd-array-confluence.md), [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md).
- [liquidity-matrix](../02-liquidity/liquidity-matrix.md) — analogous tool for liquidity pools.

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2024-MENTORSHIP-MODULE-LIST`.

> Confidence is `medium` because the term "PD array matrix" is community-popularized; ICT's own usage emphasizes the discipline rather than the specific tabular format.
