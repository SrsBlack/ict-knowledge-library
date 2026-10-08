# Liquidity Pool

**Category:** 02-liquidity
**Aliases:** none confirmed in corpus
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY-POOLS, ICT-2016-ELEMENTS-OF-A-TRADE-SETUP, ICT-2016-MMT-TRENDLINE, ICT-2017-OTE-USDCAD-REVIEW, ICT-2017-OTE-NYO-FIBER-LONG, ICT-2022-MENTORSHIP-EP02, ICT-2022-MENTORSHIP-EP18
**Tags:** liquidity, pool, foundational

## Definition

A liquidity pool is any concentration of resting orders at or near a discrete price level — stops, breakout entries, limit orders. ICT: "Liquidity is the open interest of buyers and sellers in the market and can be further defined by those entities at or near specific price levels" (`ICT-2016-LIQUIDITY-POOLS`, 00:50–00:56); "above old highs, there's a pool or a collection of orders that traders will build up around" (04:26); "the liquidity pools just above an old high and just below an old low" (`ICT-2016-ELEMENTS-OF-A-TRADE-SETUP`, 16:13). Pools are the destinations toward which algorithmic price delivery is drawn: "the market's being driven higher and the algorithm's going to attack that buy stock liquidity pool" (`ICT-2022-MENTORSHIP-EP02`, 21:32); "that gives you liquidity pools that you can attack" (`ICT-2022-MENTORSHIP-EP18`, 19:08).

## Formal Criteria

A liquidity pool exists wherever:

- A swing high or swing low has formed (creates pool above / below).
- Two or more [equal highs or lows](equal-highs.md) are visible (ICT: "seeking the sell stops below these relative equal lows," `ICT-2016-LIQUIDITY-POOLS`, 17:59).
- A retail trendline — the drawing is retail's, not ICT's (library convention); ICT's own trigger is specifically the **third** touch: "when that third touch of that uptrend line is seen in price action, many times I get dialed in" (`ICT-2016-MMT-TRENDLINE`, 07:58); the liquidity source is framed as "the influx of weak-handed or less informed money at an area or price level" (07:35).
- A session high/low, prior day, or prior week extreme formed — "highlight the previous day's highs and lows… that gives you liquidity pools" (`ICT-2022-MENTORSHIP-EP18`, 19:08).
- A round number / major figure is visible — "institutions use round numbers for their orders because it makes it easy to put in large blocks of orders" (`ICT-2017-OTE-USDCAD-REVIEW`, 10:09); "the liquidity resting above the 118 big figure" (`ICT-2017-OTE-NYO-FIBER-LONG`, 00:33).

**Option strike** pools are not in either corpus (0 hits for "option strike"; "strike" hits are bond/futures contexts unrelated to liquidity) and should not be presented as an ICT-sourced pool type.

The "size" of the pool is qualitative — it scales with how many retail traders would have placed orders at the level.

## Formula / Math

```
pool(level, type) := {
  source: prior_swing_high | prior_swing_low | EQH | EQL | trendline(3rd touch) | session_extreme | round_number,
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
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "level identifies as one of: swing, EQ-pair, trendline(3rd touch), session-extreme, round-number"},
    {"id": "c2", "expr": "level not yet swept"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["buy-side-liquidity","sell-side-liquidity","equal-highs","equal-lows","trendline-liquidity","liquidity-sweep","draw-on-liquidity"],
  "sources": ["ICT-2016-LIQUIDITY-POOLS","ICT-2016-ELEMENTS-OF-A-TRADE-SETUP","ICT-2016-MMT-TRENDLINE","ICT-2017-OTE-USDCAD-REVIEW","ICT-2017-OTE-NYO-FIBER-LONG","ICT-2022-MENTORSHIP-EP02","ICT-2022-MENTORSHIP-EP18"]
}
```

## Visual Pattern

Pools are not a unique pattern — they are an interpretation overlay on existing structural and session features. Examples:

```
   swing-high pool          EQH pool          trendline pool (3rd touch)
        /\               ─────┴────┴────         x
       /  \                                       \
      /    \                                        x
                                                     \
                                                      x  ← 3rd touch triggers
                                                       \    ICT's attention
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
- **Citing "option strike" as an ICT pool type.** Not in the corpus — drop it or label it explicitly unverified.

## Related Concepts

- [buy-side-liquidity](buy-side-liquidity.md) / [sell-side-liquidity](sell-side-liquidity.md) — pool-side specifics.
- [equal-highs](equal-highs.md) / [equal-lows](equal-lows.md) — densest pool form.
- [trendline-liquidity](trendline-liquidity.md) — sloped pools.
- [liquidity-sweep](liquidity-sweep.md) — what taking a pool looks like.
- [draw-on-liquidity](draw-on-liquidity.md) — pool selection as the algorithmic target.

## Citations

- `ICT-2016-LIQUIDITY-POOLS` (00:50–00:56) "liquidity is the open interest of buyers and sellers… at or near specific price levels"; (04:26) "above old highs, there's a pool or a collection of orders"; (17:19) "we're going to be looking for buy stops above these equal highs"; (17:59) "seeking the sell stops below these relative equal lows."
- `ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` (16:13) "the liquidity pools just above an old high and just below an old low."
- `ICT-2016-MMT-TRENDLINE` (07:35) "the influx of weak-handed or less informed money at an area or price level provides liquidity for the market maker"; (07:58) "when that third touch of that uptrend line is seen in price action, many times I get dialed in."
- `ICT-2017-OTE-USDCAD-REVIEW` (10:09) "institutions use round numbers for their orders because it makes it easy to put in large blocks of orders."
- `ICT-2017-OTE-NYO-FIBER-LONG` (00:33) "the liquidity resting above the 118 big figure."
- `ICT-2022-MENTORSHIP-EP02` (21:32) "the market's being driven higher and the algorithm's going to attack that buy stock liquidity pool."
- `ICT-2022-MENTORSHIP-EP18` (19:08) "highlight the previous day's highs and lows… that gives you liquidity pools that you can attack."
