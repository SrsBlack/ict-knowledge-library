# Sell-Side Liquidity (SSL)

**Category:** 02-liquidity
**Aliases:** SSL, sellstops, resting sell orders, liquidity below, old low (as a target)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY-RUNS, ICT-2016-MMT-FALSE-BREAKOUT, ICT-2016-LIQUIDITY-POOLS, ICT-2017-QUARTERLY-SHIFTS, ICT-2022-MENTORSHIP-EP16
**Tags:** liquidity, sellside, stops, foundational

## Definition

Sell-side liquidity is the set of resting sell orders sitting below price — primarily stop-losses from long positions and stop-entry orders from breakdown sellers. The mirror of [buy-side-liquidity](buy-side-liquidity.md). ICT: "below the lows, there would be sell stops for long traders and sell stops for short breakout traders" (`ICT-2016-MMT-FALSE-BREAKOUT`, 03:34); "the low that is under the current market price will typically have a trailed sell stop under it for long traders. Once sell stops for traders who wish to trade on a breakout lower in price for a short position also reside below old lows" (`ICT-2016-LIQUIDITY-POOLS`, 09:13–09:24); "every short-term low is going to have sell side liquidity or sell stops below that" (`ICT-2017-QUARTERLY-SHIFTS`, 34:00). Algorithmic price delivery is drawn toward SSL pools when bearish intent is being expressed.

## Formal Criteria

SSL accumulates at:

- The low of any prior swing low (STL, ITL, LTL) — "we see that as sell liquidity" (`ICT-2016-LIQUIDITY-RUNS`, 03:36).
- Equal lows ([equal-lows](equal-lows.md)).
- Ascending trendline lows (retail support trendlines).
- Session lows (Asia low, London low, NY AM low, prior day low, prior week low).
- Round-number levels below price.

SSL is "taken" when price trades through the level: "validation of this setup or condition is when the low is violated" (`ICT-2016-LIQUIDITY-POOLS`, 09:33).

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
  "sources": ["ICT-2016-LIQUIDITY-RUNS","ICT-2016-MMT-FALSE-BREAKOUT","ICT-2016-LIQUIDITY-POOLS","ICT-2017-QUARTERLY-SHIFTS","ICT-2022-MENTORSHIP-EP16"]
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
- A later bar wicks to 1.0848, reverses back above 1.0860.
- → SSL swept; the equal-lows pool is now "claimed."

**Example 2 — Daily SSL stack:**
- PWL at 1.0700, PDL at 1.0750, current STL at 1.0780.
- Bearish bias targets the 1.0780 → 1.0750 → 1.0700 ladder.

## Common Mistakes

- **Inventing a pip/tick tolerance for "equal."** ICT's own standard for equal lows is "close proximity" / "relatively equal, not exactly" (`ICT-2022-MENTORSHIP-EP16`, 04:13), not a specific pip or tick count — see [equal-lows](equal-lows.md). Do not present a fixed figure as ICT's rule.
- **Asserting a close-based rule for sweep vs. continuation.** "A close below SSL with displacement = bearish BOS, not a sweep" is not in the corpus. ICT's actual split is *sweep* (reverses) vs. *run* ("runs right over top of it and it just doesn't look back") — see [liquidity-sweep](liquidity-sweep.md) and [liquidity-run](liquidity-run.md).
- **One-sided analysis.** Always look at both BSL and SSL relative to current price; the algorithm's draw is whichever is the more attractive target given HTF bias and session.

## Related Concepts

- [buy-side-liquidity](buy-side-liquidity.md) — mirror.
- [equal-lows](equal-lows.md) — concentrated SSL pools.
- [liquidity-sweep](liquidity-sweep.md) — sweep behavior.
- [liquidity-pool](liquidity-pool.md) — broader concept.
- [draw-on-liquidity](draw-on-liquidity.md) — SSL as a DOL option.
- [swing-low](../01-market-structure/swing-low.md) — primary SSL location.

## Citations

- `ICT-2016-LIQUIDITY-RUNS` (03:36) "we see that as sell liquidity."
- `ICT-2016-MMT-FALSE-BREAKOUT` (03:34) "below the lows, there would be sell stops for long traders and sell stops for short breakout traders."
- `ICT-2016-LIQUIDITY-POOLS` (09:13–09:24) trailed sell stops for long traders and breakout-short sell stops below old lows; (09:33) the validation/take condition.
- `ICT-2017-QUARTERLY-SHIFTS` (34:00) "every short-term low is going to have sell side liquidity or sell stops below that."
- `ICT-2022-MENTORSHIP-EP16` (04:13) "relatively equal, not exactly — that's why I named them relatively equal lows."
