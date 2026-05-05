# Draw On Liquidity (DOL)

**Category:** 02-liquidity
**Aliases:** DOL, draw, liquidity draw, algorithmic draw, target liquidity
**ICT Confidence:** high
**Year Introduced:** 2021
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, dol, draw, foundational

## Definition

Draw On Liquidity is the specific liquidity pool that the algorithm is currently drawn toward — the next target price is intended to reach. DOL is the **directional anchor** of any trade hypothesis: if you cannot identify which liquidity pool price is going to take, you do not have a setup. ICT teaches that price is always traveling toward a draw; the analyst's job is to identify which pool is the draw and confirm with PD-array confluence.

## Formal Criteria

A DOL must be:

- An identifiable, unswept [liquidity-pool](liquidity-pool.md) — BSL, SSL, EQH/EQL, trendline, or session/day/week high/low.
- Consistent with HTF bias: if the HTF bias is bullish, DOL is upside (BSL); if bearish, DOL is downside (SSL).
- Reachable within the timeframe horizon of the trade (intra-day setup → intra-day pool).

ICT distinguishes:

- **Intermediate DOL** — partial / scaling target (often IRL).
- **Terminal DOL** — full-delivery destination (often ERL).

## Formula / Math

```
DOL(t) := select pool from { BSL, SSL, EQH, EQL, trendline, session_extremes, PWH/PWL, PDH/PDL }
            where:
              - aligns_with_HTF_bias(pool) == true
              - not_yet_swept(pool) == true
              - within_horizon(pool, trade_TF) == true
```

The selection is qualitative; ICT teaches it through repeated examples rather than a fixed scoring formula.

## Machine-Readable

```json
{
  "id": "draw-on-liquidity",
  "category": "02-liquidity",
  "aliases": ["DOL", "draw", "liquidity-draw", "algorithmic-draw"],
  "criteria": [
    {"id": "c1", "expr": "pool_aligns_with_HTF_bias == true"},
    {"id": "c2", "expr": "pool_unswept == true"},
    {"id": "c3", "expr": "pool_reachable_within_trade_horizon == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2021",
  "year_refined": "2022",
  "related": ["liquidity-pool","internal-range-liquidity","external-range-liquidity","htf-bias-framework","liquidity-matrix"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   HTF bullish bias

   ─── PWH BSL ERL ───   ← terminal DOL
        ↑
   ─── EQH IRL  ───      ← intermediate DOL
        ↑
   ─── current price
```

## Timeframes

Every TF M5+. ICT's standard procedure: identify HTF DOL (D / H4), then look for LTF entries that align with reaching it.

## Examples

**Example 1 — H4 bullish DOL hierarchy:**
- HTF (D) bias bullish.
- H4 DOL ladder: nearest BSL = swing high at 1.0900 (intermediate), next = EQH at 1.0925 (intermediate), terminal = PWH at 1.0950 (ERL).
- Intra-day setups (M15 / M5) target 1.0900 first, then 1.0925, then 1.0950.

## Common Mistakes

- **Trading without identifying DOL.** Setups taken without a clear pool target are speculation; the trade has no intended destination.
- **Choosing DOL against HTF bias.** A short setup with an upside DOL is incoherent — the analysis has the direction wrong.
- **Stale DOL.** Once a pool is swept, it is no longer the draw; the next unswept pool in the bias direction takes over.

## Related Concepts

- [liquidity-pool](liquidity-pool.md) — what DOL selects from.
- [internal-range-liquidity](internal-range-liquidity.md) / [external-range-liquidity](external-range-liquidity.md) — DOL classification.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md) — bias filter that picks the side.
- [liquidity-matrix](liquidity-matrix.md) — cross-TF DOL view.

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW` — DOL terminology formalized.
