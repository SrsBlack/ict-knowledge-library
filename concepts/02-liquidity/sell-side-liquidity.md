# Sell-Side Liquidity (SSL)

**Category:** 02-liquidity
**Aliases:** SSL, sellstops, resting sell orders, liquidity below
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, sellside, stops, foundational

## Definition

Sell-side liquidity is the set of resting sell orders sitting below price — primarily stop-losses from long positions and stop-entry orders from breakdown sellers. The mirror of [buy-side-liquidity](buy-side-liquidity.md). Algorithmic price delivery is drawn toward SSL pools when bearish intent is being expressed.

## Formal Criteria

SSL accumulates at:

- The low of any prior swing low (STL, ITL, LTL).
- Equal lows ([equal-lows](equal-lows.md)).
- Ascending trendline lows (retail support trendlines).
- Session lows (Asia low, London low, NY AM low, prior day low, prior week low).
- Round-number levels (00, 50) below price.

SSL is "taken" when price trades through the level.

## Formula / Math

```
SSL_levels(t) = { all unswept swing lows and equal-lows below current price at time t }
                ∪ { unswept session lows below current price }

SSL_swept(level) := low(any future bar) < level
```

## Machine-Readable

```json
{
  "id": "sell-side-liquidity",
  "category": "02-liquidity",
  "aliases": ["SSL", "sellstops", "liquidity-below"],
  "criteria": [
    {"id": "c1", "expr": "level == prior_swing_low OR level == equal_lows OR level == session_low"},
    {"id": "c2", "expr": "level < current_price"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["buy-side-liquidity","equal-lows","liquidity-sweep","liquidity-pool","draw-on-liquidity","swing-low"],
  "sources": ["ICT-2016-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
    \      /  ← current price approaching from above
     \    /
      \  /
       \/        ← prior swing low
   ─────────────
              SSL ←  sell stops + breakdown sell orders rest here
```

Every unswept swing low below price is an SSL pool.

## Timeframes

All TFs. HTF SSL (PDL, PWL, PML) is heavier than LTF SSL.

## Examples

**Example 1 — Equal-lows SSL pool:**
- M15 prints two equal lows at 1.0850.
- A later bar wicks to 1.0848, closes at 1.0860.
- → SSL swept; the equal-lows pool is now "claimed."

**Example 2 — Daily SSL stack:**
- PWL at 1.0700, PDL at 1.0750, current STL at 1.0780.
- Bearish bias targets the 1.0780 → 1.0750 → 1.0700 ladder.

## Common Mistakes

- **Pixel-perfect lows.** Equal lows don't need to match to the tick — within a few pips on FX, a few ticks on indices, ICT considers them equal.
- **Ignoring sweep direction.** A wick through SSL with a strong reversal close = liquidity raid. A close below SSL with displacement = bearish BOS, not a sweep.
- **One-sided analysis.** Always look at both BSL and SSL relative to current price; the algorithm's draw is whichever is the more attractive target given HTF bias and session.

## Related Concepts

- [buy-side-liquidity](buy-side-liquidity.md) — mirror.
- [equal-lows](equal-lows.md) — concentrated SSL pools.
- [liquidity-sweep](liquidity-sweep.md) — sweep behavior.
- [liquidity-pool](liquidity-pool.md) — broader concept.
- [draw-on-liquidity](draw-on-liquidity.md) — SSL as a DOL option.
- [swing-low](../01-market-structure/swing-low.md) — primary SSL location.

## Citations

- `ICT-2016-LIQUIDITY` — SSL introduced.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational framing.
