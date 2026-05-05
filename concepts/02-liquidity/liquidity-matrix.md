# Liquidity Matrix

**Category:** 02-liquidity
**Aliases:** liquidity map, pool matrix, multi-TF liquidity grid
**ICT Confidence:** medium
**Year Introduced:** 2021
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, matrix, multi-tf, mapping

## Definition

A liquidity matrix is the analyst's organized view of every relevant liquidity pool across multiple timeframes — a cross-TF map of BSL/SSL/EQH/EQL/session-extremes/PWH-PDH/PWL-PDL stacked above and below current price. ICT teaches the matrix as a **pre-trade preparation tool**: before any setup, list every pool, identify which are likely DOL, and use that map to select entries and targets.

## Formal Criteria

A complete matrix lists, for the current symbol:

- Above price: every unswept BSL pool from M15 / H1 / H4 / D / W, in price order.
- Below price: every unswept SSL pool from same TFs, in price order.
- For each pool: TF, type (swing high, EQH, session high, etc.), price, and qualitative size.
- Optional: most recent sweep history (which pools were taken in the last N hours) to track delivery direction.

## Formula / Math

```
matrix(t) = sort_by_price([
  { tf: M15 | H1 | H4 | D | W,
    side: buy | sell,
    type: swing | EQ-pair | session-extreme | PWH-PWL | round-number,
    price: float,
    swept: bool,
    significance: low | medium | high
  }
  for every identified pool
])
```

## Machine-Readable

```json
{
  "id": "liquidity-matrix",
  "category": "02-liquidity",
  "aliases": ["liquidity-map", "pool-matrix"],
  "criteria": [
    {"id": "c1", "expr": "every_pool_listed_with_tf_and_type == true"},
    {"id": "c2", "expr": "matrix_sorted_by_price == true"}
  ],
  "timeframes": ["M15","H1","H4","D","W"],
  "confidence": "medium",
  "year_introduced": "2021",
  "year_refined": "2022",
  "related": ["draw-on-liquidity","liquidity-pool","internal-range-liquidity","external-range-liquidity","htf-bias-framework"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

A textual / tabular concept rather than a chart pattern. Example matrix for EURUSD intra-day:

```
Side  TF   Type           Price    Swept  Note
────  ──   ──────────     ──────   ─────  ────────────────────────
buy   W    PWH            1.0975   no     terminal ERL
buy   D    PDH            1.0925   no     intermediate DOL
buy   H4   EQH x2         1.0900   no     dense BSL
buy   H1   swing high     1.0880   no     intermediate
─── current price 1.0855 ───
sell  H1   swing low      1.0830   no     intermediate
sell  H4   EQL x3         1.0815   no     dense SSL
sell  D    PDL            1.0790   no     intermediate DOL
sell  W    PWL            1.0750   no     terminal ERL
```

## Timeframes

The matrix is always multi-TF by definition. The instrument-specific TF set varies (intraday FX → M15/H1/H4/D/W; intra-day indices may include M5 and exclude W).

## Examples

**Example 1 — Building the matrix pre-London:**
- Before London open, write out the matrix above.
- HTF (D) bias bullish → focus on BSL stack as primary DOL.
- Identify nearest sell-side pool (H1 swing low at 1.0830) as the most likely Judas-swing sweep target before the rally.
- Plan: sweep H1 SSL → CHoCH/MSS → enter long → target H4 EQH BSL first, scale to PDH, hold for PWH if delivery extends.

## Common Mistakes

- **Building once, not maintaining.** The matrix decays as pools are swept; refresh whenever delivery resolves a level.
- **Overlisting noise.** M1/M5 micro-pools swamp the matrix without adding decision value. Cap at M15+.
- **Ignoring HTF bias when reading the matrix.** A perfect matrix without a bias is just a list; bias is what makes it actionable.

## Related Concepts

- [draw-on-liquidity](draw-on-liquidity.md) — selected from the matrix.
- [liquidity-pool](liquidity-pool.md) — building block.
- [internal-range-liquidity](internal-range-liquidity.md) / [external-range-liquidity](external-range-liquidity.md) — classification.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md) — directional filter applied to the matrix.

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW` — liquidity-mapping discipline taught in 2022 mentorship.

> Confidence is `medium` because the term "liquidity matrix" is used across the ICT community with slight variations; ICT's own usage emphasizes the discipline more than the specific name.
