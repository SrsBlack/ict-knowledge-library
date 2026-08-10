# Draw On Liquidity (DOL)

**Category:** 02-liquidity
**Aliases:** DOL, draw, liquidity draw, algorithmic draw, target liquidity
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-IPDA-DATA-RANGES, ICT-2017-OPEN-FLOAT, ICT-2020-OTE-VOL17
**Tags:** liquidity, dol, draw, foundational

## Definition

Draw On Liquidity is the specific liquidity pool that the algorithm is currently drawn toward — the next target price is intended to reach. DOL is the **directional anchor** of any trade hypothesis: if you cannot identify which liquidity pool price is going to take, you do not have a setup. ICT teaches that price is always traveling toward a draw; the analyst's job is to identify which pool is the draw and confirm with PD-array confluence.

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2021` while citing
only `ICT-2022-MENTORSHIP-OVERVIEW` — a claimed year *earlier* than its own sole source. Both ends
were wrong. The substance is taught in the **Jan-2017** mentorship: "you're going to look for price
to be **drawn to** one of those two price points ... it gives you **directional bias**"
(`ICT-2017-IPDA-DATA-RANGES`, 33:52–34:03) and "it's going to be drawn to a level, or it's going to
repel from a level ... **it's seeking large fund liquidity**" [41:12–41:17]; the same month's open-float
lesson states it against a pool outright — "the market was drawn to the buy stops on the fund level
at those July highs" (`ICT-2017-OPEN-FLOAT`, 03:25). The **name** arrives later: the earliest located
use of the phrase "draw on liquidity" is the 2020 OTE Pattern Recognition Series, where ICT coins it
on air — "it just needs to draw towards it; that's the reason why I call it a draw on liquidity"
(`ICT-2020-OTE-VOL17`, 00:45–00:50). Re-dated to 2017 for the concept; see the citations for the
naming. Searched all 153 corpus packets for "draw on liquidity" (4 hits, all 2020–2021), "drawn to"
(7 core-content hits, earliest Oct 2016) and "magnet" (3 hits); the one 2016 hit — "where do you
think the market's going to be drawn to?" (Month 02, *Growing Small Accounts*, 20:39) — is a
profit-target aside, not a taught concept, and was rejected as too weak to date the page to 2016.

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
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["liquidity-pool","internal-range-liquidity","external-range-liquidity","htf-bias-framework","liquidity-matrix"],
  "sources": ["ICT-2017-IPDA-DATA-RANGES","ICT-2017-OPEN-FLOAT","ICT-2020-OTE-VOL17"]
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

- `ICT-2017-IPDA-DATA-RANGES` — the concept without the name: price "drawn to one of those two price
  points ... it gives you directional bias" [33:52–34:03]; "drawn to a level, or ... repel from a
  level ... it's seeking large fund liquidity" [41:12–41:17].
- `ICT-2017-OPEN-FLOAT` — the draw stated against an explicit pool: "the market was drawn to the buy
  stops on the fund level at those July highs" [03:25].
- `ICT-2020-OTE-VOL17` — ICT names the concept: "it just needs to draw towards it; that's the reason
  why I call it a draw on liquidity" [00:45–00:50]. Also establishes that price need not *reach* the
  pool for the draw to be valid — the bias is directional, not a required touch.
