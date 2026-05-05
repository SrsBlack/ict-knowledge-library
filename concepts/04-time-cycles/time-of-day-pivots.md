# Time-of-Day Pivots

**Category:** 04-time-cycles
**Aliases:** TOD pivots, time anchors, opening references
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** time, pivots, opens, references

## Definition

Time-of-day pivots are specific NY-clock prices that the algorithm references repeatedly across the trading day: midnight open (true day open), 08:30 NY open, 09:30 NY equities open, 17:00 NY (forex daily close), session highs/lows, prior day high/low (PDH/PDL). These are NOT structural pivots like swing highs — they are **time-anchored** price levels. ICT teaches them as a parallel reference layer to the structural and PD-array layers.

## Formal Criteria

Common time-of-day pivots used in ICT analysis:

| Pivot | NY Time | Use |
|---|---|---|
| True Day Open (TDO) | 00:00 | daily reference for premium/discount intraday |
| 08:30 NY open | 08:30 | reference for NY AM, often pre-news |
| 09:30 NY equities | 09:30 | indices session open |
| Prior Day High (PDH) | — | BSL pool from yesterday |
| Prior Day Low (PDL) | — | SSL pool from yesterday |
| Asian session high | 03:00 | Asian range BSL pool |
| Asian session low | 03:00 | Asian range SSL pool |
| Lunch high | 13:30 | dead-session liquidity |
| Lunch low | 13:30 | dead-session liquidity |
| 17:00 NY (forex close) | 17:00 | end of forex day, brief liquidity gap |

## Formula / Math

```
TDO         = open_price(00:00 NY)
0830_open   = open_price(08:30 NY)
0930_open   = open_price(09:30 NY)   # indices
PDH         = max(high) over prior_day NY 00:00–24:00
PDL         = min(low)  over prior_day NY 00:00–24:00
asia_high   = max(high) over [18:00 prev, 03:00 NY]
asia_low    = min(low)  over [18:00 prev, 03:00 NY]
```

## Machine-Readable

```json
{
  "id": "time-of-day-pivots",
  "category": "04-time-cycles",
  "aliases": ["TOD-pivots", "time-anchors"],
  "criteria": [
    {"id": "c1", "expr": "level_anchored_to_specific_NY_clock_time == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["true-day-open","true-week-open","liquidity-pool","draw-on-liquidity","htf-bias-framework","asian-range"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
24-hour day with key time pivots (NY):

00:00 ────────── 03:00 ── 08:30 ── 09:30 ── 12:00 ── 13:30 ── 17:00 ── 24:00
   |               |        |        |        |        |        |
   TDO          Asia      NY-AM    Indices   Lunch     Lunch    Forex
                close     open     open      start     end      close
                ↓         ↓         ↓                            ↓
                Asia       08:30    09:30                        17:00
                H/L         open     open                         close
```

## Timeframes

H1 / D for HTF reference; M5 / M15 for intra-session pivot use.

## Examples

**Example 1 — TDO + PDH stack:**
- TDO at 1.0900 (midnight open).
- PDH BSL at 1.0925 (yesterday's high).
- HTF bullish bias → both are upside reference levels: price above TDO is intraday premium relative to TDO; above PDH = daily ERL takeout.

## Common Mistakes

- **Mixing TF anchors with structural pivots.** TDO and swing-high are different things; both can coincide but their meaning is distinct.
- **Wrong timezone.** All TOD pivots are NY-time. Server-time charts must be converted.
- **Treating 17:00 close as a hard pivot.** Most brokers continue trading through 17:00 NY with brief illiquidity; ICT references it as the structural daily-close moment but it's not a hard halt.

## Related Concepts

- [true-day-open](../22-quarterly-theory/true-day-open.md) — TDO deep dive.
- [true-week-open](../22-quarterly-theory/true-week-open.md) — weekly equivalent.
- [liquidity-pool](../02-liquidity/liquidity-pool.md) — TOD pivots act as pool anchors.
- [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md) — TOD pivots are common DOL choices.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md) — bias relative to TDO/PDH/PDL is a routine bias signal.
- [asian-range](../14-asian-range/asian-range.md) — Asian session pivots.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — TDO and TOD pivot terminology refined.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use as bias and DOL anchors.
