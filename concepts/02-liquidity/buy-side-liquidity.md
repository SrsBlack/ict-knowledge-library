# Buy-Side Liquidity (BSL)

**Category:** 02-liquidity
**Aliases:** BSL, buystops, resting buy orders, liquidity above
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, buyside, stops, foundational

## Definition

Buy-side liquidity is the set of resting buy orders sitting above price — primarily stop-losses from short positions and stop-entry orders from breakout buyers. ICT teaches that price is algorithmically drawn toward these pools because executing them provides the counter-flow institutional positions need to fill in size. BSL is the primary upside [draw-on-liquidity](draw-on-liquidity.md) target.

## Formal Criteria

BSL accumulates at:

- The high of any prior swing high (especially STH, ITH, LTH).
- Equal highs ([equal-highs](equal-highs.md) — two or more swing highs at the same price).
- Trendline highs (descending series of lower highs that retail traders draw a trendline against).
- Session highs (Asia high, London high, NY AM high, prior day high, prior week high).
- Round-number levels (00, 50) and major figures.

A BSL pool is "taken" when price trades through the level — typically swept with a wick and then reversed (a [liquidity-sweep](liquidity-sweep.md)) or broken through cleanly on a continuation BOS.

## Formula / Math

```
BSL_levels(t) = { all unswept swing highs and equal-highs above current price at time t }
                ∪ { unswept session highs above current price }

BSL_swept(level) := high(any future bar) > level
```

The set is dynamic: levels enter when a swing high forms; levels leave when they are swept.

## Machine-Readable

```json
{
  "id": "buy-side-liquidity",
  "category": "02-liquidity",
  "aliases": ["BSL", "buystops", "liquidity-above"],
  "criteria": [
    {"id": "c1", "expr": "level == prior_swing_high OR level == equal_highs OR level == session_high"},
    {"id": "c2", "expr": "level > current_price"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["sell-side-liquidity","equal-highs","liquidity-sweep","liquidity-pool","draw-on-liquidity","swing-high"],
  "sources": ["ICT-2016-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
              BSL ←  buy stops + breakout buy orders rest here
   ─────────────
       /\        ← prior swing high
      /  \
     /    \
    /      \   ← current price approaching from below
```

Every unswept swing high above price is a BSL pool.

## Timeframes

Every TF. HTF BSL (daily / weekly highs, prior week high) is structurally heavier than LTF BSL (M5 swing high). ICT bias often comes from identifying which BSL or SSL pool is the next algorithmic draw.

## Examples

**Example 1 — Asian range BSL:**
- During Asia, EURUSD prints a session high at 1.0875.
- London opens; price rallies to 1.0876, wicks to 1.0879, closes back at 1.0872.
- → Asian BSL was swept. The sweep often signals the actual day's direction is the opposite (Judas swing).

**Example 2 — Daily BSL stack:**
- Prior week high at 1.1100, prior day high at 1.1080, current swing high at 1.1060.
- A bullish bias targets the 1.1060 → 1.1080 → 1.1100 BSL ladder.

## Common Mistakes

- **Treating any high as BSL.** Tiny noise highs on M1 are technically BSL but rarely meaningful as targets. Filter by structural significance and TF.
- **Assuming sweep = reversal.** A BSL sweep can either reverse (liquidity raid) or be a step in continuation (the BSL was the "fuel" needed for the next leg up). Read the displacement that follows.
- **Forgetting the sell-side mirror.** BSL above and SSL below interact; ICT analyses often pair them ("price is between PWH BSL and PWL SSL").

## Related Concepts

- [sell-side-liquidity](sell-side-liquidity.md) — mirror.
- [equal-highs](equal-highs.md) — concentrated BSL pools.
- [liquidity-sweep](liquidity-sweep.md) — what happens when BSL is taken.
- [liquidity-pool](liquidity-pool.md) — broader concept.
- [draw-on-liquidity](draw-on-liquidity.md) — BSL is one of the two DOL options.
- [swing-high](../01-market-structure/swing-high.md) — primary BSL location.

## Citations

- `ICT-2016-LIQUIDITY` — BSL/SSL terminology introduced in 2016 mentorship.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational framing as algorithmic draw.
