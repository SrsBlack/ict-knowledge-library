# Trendline Liquidity

**Category:** 02-liquidity
**Aliases:** trendline stops, retail trendline liquidity, sloped liquidity
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, trendline, sloped, retail-trap

## Definition

Trendline liquidity is the cluster of stop orders that retail traders place against trendlines they draw across two or more swing points. ICT teaches that the algorithm is aware of these stops and frequently sweeps them in two directions: above descending highs (BSL trendline liquidity) and below ascending lows (SSL trendline liquidity). The trendline is not a real support/resistance level — it is a psychological convention whose chief function is to mark a stop cluster.

## Formal Criteria

A bullish-side (SSL) trendline:

- Two or more ascending swing lows can be connected by a straight line.
- Retail traders treat the line as support and place stops just below.
- The stop cluster runs along the line; it is **sloped**, not horizontal.

A bearish-side (BSL) trendline:

- Two or more descending swing highs can be connected by a straight line.
- Retail traders treat the line as resistance and place stops just above.

Trendline liquidity is most attractive when:

- The trendline has 3+ touches (the more touches, the more stops).
- Retail charting platforms have the line drawn in obvious places (round-number anchor points, session boundaries).

## Formula / Math

```
ascending_trendline := line through 2+ ascending swing lows
trendline_liquidity_below(t) := { price points along the line at time t }

descending_trendline := line through 2+ descending swing highs
trendline_liquidity_above(t) := { price points along the line at time t }
```

The stop level moves with time (slope), unlike horizontal SSL/BSL.

## Machine-Readable

```json
{
  "id": "trendline-liquidity",
  "category": "02-liquidity",
  "aliases": ["trendline-stops", "sloped-liquidity"],
  "criteria": [
    {"id": "c1", "expr": "line_connects_2plus_swings == true"},
    {"id": "c2", "expr": "line_is_obvious_to_retail == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["buy-side-liquidity","sell-side-liquidity","liquidity-sweep","equal-highs","equal-lows","stop-run-definition"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   descending trendline (BSL above)

        x  ← SH_1
         \
          \  x  ← SH_2
           \   \
            \   \  x  ← SH_3
             \   \  \
              \   \  \      buystops along the line
               ───────────  ← if price reaches it from below, it sweeps the stops
```

```
   ascending trendline (SSL below)

   x          ← SL_3
    \
     x        ← SL_2
      \
       x      ← SL_1
        \
         ─── sellstops along the line
```

## Timeframes

Most useful M15 → D. Lower TFs have noisy "trendlines" of little structural significance; HTF trendlines (D, W) reflect long-term retail chart patterns and concentrate larger stop pools.

## Examples

**Example 1 — H1 ascending trendline sweep:**
- H1 trends up; three ascending lows form a clean trendline.
- Price sells off, wicks below the trendline, and prints a bullish FVG.
- → trendline SSL was swept; the FVG is an entry zone for a long.

## Common Mistakes

- **Drawing trendlines retroactively.** A trendline only matters as liquidity if it was visible to retail at the time the stops were placed.
- **Using non-obvious anchor points.** A trendline through random pivots that no retail trader would draw isn't liquidity.
- **Treating sweep as automatic reversal.** Trendline sweep is a *pretext* for a reaction; whether the reaction is a full reversal depends on confluence.

## Related Concepts

- [buy-side-liquidity](buy-side-liquidity.md) — descending-trendline liquidity is BSL.
- [sell-side-liquidity](sell-side-liquidity.md) — ascending-trendline liquidity is SSL.
- [liquidity-sweep](liquidity-sweep.md) — what taking trendline stops looks like.
- [equal-highs](equal-highs.md) / [equal-lows](equal-lows.md) — horizontal analogue.
- [stop-run-definition](../29-stop-runs/stop-run-definition.md) — broader stop-hunt concept.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — trendline liquidity introduced.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use as sweep target.
