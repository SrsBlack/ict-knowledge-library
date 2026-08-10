# Liquidity Matrix

**Category:** 02-liquidity
**Aliases:** liquidity map, pool matrix, multi-TF liquidity grid
**ICT Confidence:** medium
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-PD-ARRAY-MATRIX, ICT-2017-TOPDOWN-SHORT-TERM
**Tags:** liquidity, matrix, multi-tf, mapping

## Definition

A liquidity matrix is the analyst's organized view of every relevant liquidity pool across multiple timeframes — a cross-TF map of BSL/SSL/EQH/EQL/session-extremes/PWH-PDH/PWL-PDL stacked above and below current price. ICT teaches the matrix as a **pre-trade preparation tool**: before any setup, list every pool, identify which are likely DOL, and use that map to select entries and targets.

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2021` while citing
only `ICT-2022-MENTORSHIP-OVERVIEW` — a claimed year *earlier* than its own sole source. **The exact
phrase "liquidity matrix" appears zero times across all 153 corpus packets.** What ICT does teach,
and names, is the **PD array matrix**, and he defines it in the **Feb-2017** mentorship: "This is the
PD array matrix. And every array **above** market price is the premium spectrum. And every array
**below** current market action is the discount spectrum" (`ICT-2017-PD-ARRAY-MATRIX`, 04:21–04:27).
The multi-timeframe pre-trade routine this page describes is stated outright in the **Aug-2017**
top-down lecture: "I go through the daily and work my way through the four hour doing the PD array
matrix. **Note all the discount and premium arrays** ... knowing what's above us in terms of where
price may reach and what's below us in terms of where price may reach, we calibrate those levels"
(`ICT-2017-TOPDOWN-SHORT-TERM`, 23:53–24:48). Re-dated to 2017. ⚠ Two caveats: "liquidity matrix" is
a **community label**, not ICT's; and ICT's matrix inventories *all* PD arrays (order blocks, FVGs,
breakers, mitigation blocks, liquidity voids) alongside liquidity pools, where this page describes
the liquidity-pool-only subset. Searched all 153 packets for "liquidity matrix" (0 hits), "matrix"
(31 packets, **all 2017, none in the Sep-2016 → Jan-2017 Months 1–05**; every one of the ~90
occurrences is "PD array matrix" — or a whisper mangling of it, or an elided back-reference such as
"the discount matrix"), and "liquidity map" (0 hits).

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
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["draw-on-liquidity","liquidity-pool","internal-range-liquidity","external-range-liquidity","htf-bias-framework"],
  "sources": ["ICT-2017-PD-ARRAY-MATRIX","ICT-2017-TOPDOWN-SHORT-TERM"]
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

- `ICT-2017-PD-ARRAY-MATRIX` — defines the matrix and its two spectra: "This is the PD array matrix.
  And every array above market price is the premium spectrum. And every array below current market
  action is the discount spectrum" [04:21–04:27]; the per-array checklist to run inside a defined
  range — mitigation blocks, breakers, liquidity voids, fair value gaps, order blocks [17:26–17:44].
- `ICT-2017-TOPDOWN-SHORT-TERM` — the multi-TF pre-trade routine: daily then four-hour, "note all the
  discount and premium arrays ... the ones that are there, you highlight them" [23:53–24:13], then
  "knowing what's above us in terms of where price may reach and what's below us ... we calibrate
  those levels to the nearest 10 or nearest 5 level" [24:36–24:49].

> Confidence is `medium` because "liquidity matrix" is a community label that does not appear anywhere in the ICT corpus; ICT's own name is the **PD array matrix**, and his usage emphasizes the discipline more than the specific name.
