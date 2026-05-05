# Liquidity Pool

**Category:** 02-liquidity
**Aliases:** stop pool, order pool, liquidity cluster
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, pool, foundational

## Definition

A liquidity pool is any concentration of resting orders at or near a discrete price level — stops, breakout entries, limit orders. ICT uses "pool" as the umbrella term for any of: BSL/SSL at swing highs/lows, EQH/EQL pools, trendline liquidity, session highs/lows, and round-number levels. Pools are the destinations toward which algorithmic price delivery is drawn.

## Formal Criteria

A liquidity pool exists wherever:

- A swing high or swing low has formed (creates pool above / below).
- Two or more equal highs or lows are visible (densest concentration).
- A retail trendline has 2+ touches (sloped pool).
- A session high / low formed (Asia, London, NY, prior day, prior week).
- A round number / major figure / option strike is visible.

The "size" of the pool is qualitative — it scales with how many retail traders would have placed orders at the level.

## Formula / Math

```
pool(level, type) := {
  source: prior_swing_high | prior_swing_low | EQH | EQL | trendline | session_extreme | round_number,
  side:   buy_side | sell_side,
  size:   qualitative (depends on how obvious the level is to retail)
}
```

Pools have a `swept` boolean that flips true once price trades through the level.

## Machine-Readable

```json
{
  "id": "liquidity-pool",
  "category": "02-liquidity",
  "aliases": ["stop-pool", "order-pool", "liquidity-cluster"],
  "criteria": [
    {"id": "c1", "expr": "level identifies as one of: swing, EQ-pair, trendline, session-extreme, round-number"},
    {"id": "c2", "expr": "level not yet swept"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["buy-side-liquidity","sell-side-liquidity","equal-highs","equal-lows","trendline-liquidity","liquidity-sweep","draw-on-liquidity"],
  "sources": ["ICT-2016-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

Pools are not a unique pattern — they are an interpretation overlay on existing structural and session features. Examples:

```
   swing-high pool          EQH pool          trendline pool
        /\               ─────┴────┴────         x
       /  \                                       \
      /    \                                        x
                                                     \
                                                      x
                                                       \
   ─── BSL ───            ─── BSL ───              ──────  BSL line
```

## Timeframes

Every TF. ICT analysis routinely lists pools across TFs ("M5 SSL at 1.0850, H1 EQL at 1.0830, D1 PWL at 1.0750") to identify the next algorithmic draw.

## Examples

**Example 1 — Stacked bullish pools:**
- Above current price: nearest swing high BSL at 1.0900, EQH pool at 1.0925, prior week high BSL at 1.0950.
- Bullish bias → algorithm likely targets pools in order; each is an interim target before the next.

## Common Mistakes

- **Counting noise as pools.** Tiny M1 pivots have technical pools but rarely matter; filter by structural significance.
- **Ignoring already-swept pools.** Once a pool is taken, it stops being a draw target. New pools form as new structure prints.
- **Single-side analysis.** Always identify pools on both sides; the bias decides which side is the next target.

## Related Concepts

- [buy-side-liquidity](buy-side-liquidity.md) / [sell-side-liquidity](sell-side-liquidity.md) — pool-side specifics.
- [equal-highs](equal-highs.md) / [equal-lows](equal-lows.md) — densest pool form.
- [trendline-liquidity](trendline-liquidity.md) — sloped pools.
- [liquidity-sweep](liquidity-sweep.md) — what taking a pool looks like.
- [draw-on-liquidity](draw-on-liquidity.md) — pool selection as the algorithmic target.

## Citations

- `ICT-2016-LIQUIDITY` — pool terminology introduced.
- `ICT-2022-MENTORSHIP-OVERVIEW` — taxonomy refined.
