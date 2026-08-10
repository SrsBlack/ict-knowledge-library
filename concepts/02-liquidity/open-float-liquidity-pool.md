# Open Float Liquidity Pool

**Category:** 02-liquidity
**Aliases:** open float, float, large fund liquidity pool, fund-level liquidity
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-OPEN-FLOAT
**Tags:** liquidity, funds, lookback, projection, daily, pools

## Definition

Open float is the technique ICT uses to locate the liquidity pools **large funds**
target, as distinct from the intraday pools retail stops create. From a reference
date, the daily chart is measured **60 trading days back and 60 trading days
forward** — "60 days look back and 60 days cast forward, that is open float"
(`ICT-2017-OPEN-FLOAT`, 02:32). The **highest high and lowest low** across that span
mark the fund-level pools.

The practical asymmetry: the levels are *derived* from the lookback, then **cast
forward** as active reference levels across the following ~60 trading days. They
remain the draw until that horizon expires — "the point at which open float ends in
terms of time" (06:16).

## Formal Criteria

- Measured on the **daily** chart.
- Windows are **20 / 40 / 60 trading days**, taken both **before and after** a
  reference date (02:03–02:28). 60+60 = **120 trading days** of total open float (06:31).
- The pool levels are the **highest high and lowest low** between the two reference
  points in time (02:41).
- Shorter windows narrow the read: "when we look out 40 days, it gives us a little bit
  more of a short-term basis for defining the liquidity pools on the daily chart" (05:44).
- The pools sit **above old highs and below old lows** — the liquidity "that will be
  generally targeted" (01:03).
- Levels stay live until the forward horizon expires, then the float is re-measured.

⚠ **Not the same as [ipda-60-day-lookback](../23-ipda/ipda-60-day-lookback.md).** IPDA
windows are **trailing only**. Open float adds the forward cast and the expiry horizon.
The lookback halves coincide; the concepts do not.

## Formula / Math

```
# Reference date T, on the DAILY chart, in trading days:

lookback_high(n)  := max(high) over [T-n, T]        # n = 20, 40, 60
lookback_low(n)   := min(low)  over [T-n, T]

forward_high(n)   := max(high) over [T, T+n]        # study/backward-looking only
forward_low(n)    := min(low)  over [T, T+n]

open_float_high   := max(high) over [T-60, T+60]
open_float_low    := min(low)  over [T-60, T+60]
open_float_span   := 120 trading days

# In live use the lookback levels are projected forward as horizontal
# references and remain the draw until T+60.
```

## Machine-Readable

```json
{
  "id": "open-float-liquidity-pool",
  "category": "02-liquidity",
  "aliases": ["open-float", "large-fund-liquidity-pool"],
  "criteria": [
    {"id": "c1", "expr": "timeframe == daily"},
    {"id": "c2", "expr": "windows == [20, 40, 60] trading days, both directions"},
    {"id": "c3", "expr": "pool_levels == highest_high and lowest_low across the span"},
    {"id": "c4", "expr": "total_span == 120 trading days"},
    {"id": "c5", "expr": "levels_expire_at forward_horizon"},
    {"id": "c6", "expr": "distinct_from ipda_trailing_lookback == true"}
  ],
  "timeframes": ["D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["liquidity-pool", "buy-side-liquidity", "sell-side-liquidity", "draw-on-liquidity", "ipda-60-day-lookback"],
  "sources": ["ICT-2017-OPEN-FLOAT"]
}
```

## Visual Pattern

```
        <-- 60 trading days back --|-- 60 trading days forward -->
                                   T (reference date)

   high ─────────●───────────────────────────────────────  open float HIGH
                  ╲   ╱╲                                    (fund buy stops above)
                   ╲_╱  ╲    ╱╲
                          ╲_╱  ╲___
   low  ──────────────────────────●─────────────────────   open float LOW
                                                            (fund sell stops below)

   Levels are derived from the lookback and cast forward.
   They stay the draw until the forward horizon expires, then re-measure.
```

## Timeframes

Daily only. Open float describes fund-scale positioning horizons; it has no intraday form.

## Examples

**Example 1 — July 2016 highs raided in September (`ICT-2017-OPEN-FLOAT`, 03:05–03:25):**
- The lookback window's highs formed in the latter part of July 2016.
- Those levels are cast forward as open-float pools.
- During September the market traded up into them: "those highs… were in fact raided.
  So the market was drawn to the buy stops on the fund level at those July highs."

## Common Mistakes

- **Treating it as an IPDA window.** IPDA lookbacks are trailing; open float is
  symmetric and carries an expiry. Using one where the other is meant changes which
  levels are live.
- **Using an intraday chart.** The technique is daily-only.
- **Letting stale levels persist.** Once the forward horizon passes, the float must be
  re-measured; old levels stop being the fund-level draw.
- **Confusing fund pools with retail stop pools.** Open float locates *large fund*
  liquidity specifically; ordinary intraday pools are
  [liquidity-pool](liquidity-pool.md).

## Related Concepts

- [liquidity-pool](liquidity-pool.md) — the general concept; open float is the fund-scale case.
- [buy-side-liquidity](buy-side-liquidity.md), [sell-side-liquidity](sell-side-liquidity.md) — what sits at the float's high and low.
- [draw-on-liquidity](draw-on-liquidity.md) — the float levels act as the draw until expiry.
- [ipda-60-day-lookback](../23-ipda/ipda-60-day-lookback.md) — the trailing-only sibling; explicitly not a synonym.

## Citations

- `ICT-2017-OPEN-FLOAT` (00:08) — "lesson 1.4, Defining Open Float Liquidity Pools"; (00:44) "the liquidity pools for the large funds"; (01:03) "the liquidity that's above old highs or below old lows that will be generally targeted"; (02:03–02:28) the 20/40/60-day windows measured both before and after the reference date; (02:32) "60 days look back and 60 days cast forward, that is open float"; (02:41) "you want to find the highest high and the lowest low in between those two reference points and time"; (03:05–03:25) the July-2016 highs cast forward and raided in September — "the market was drawn to the buy stops on the fund level"; (05:44) 40 days as the shorter-term basis; (06:16) "the point at which open float ends in terms of time"; (06:31) "120 trading days of what we call open float."
