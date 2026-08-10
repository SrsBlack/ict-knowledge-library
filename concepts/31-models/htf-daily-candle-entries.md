# HTF Daily-Candle Entries

**Category:** 31-models
**Aliases:** stop entry technique, limit entry technique, buy the down candle's open, buy the down candle's close, long-term entry techniques
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STOP-ENTRY-LT, ICT-2017-LIMIT-ENTRY-LT
**Tags:** entry, daily, position-trading, order-block, stop-order, limit-order

## Definition

Two mechanical entry triggers for long-term trades executed on the **daily** chart, sharing one
prerequisite and differing only in which price of the counter-trend candle is used:

| Technique | Order | Price used | What it buys |
|---|---|---|---|
| **Stop entry** | buy stop / sell stop | the counter candle's **open** | strength — "using strength to get you long" (`ICT-2017-STOP-ENTRY-LT`, 01:18) |
| **Limit entry** | buy limit / sell limit | the counter candle's **close** | discount — "buying at a deeply undervalued price" (`ICT-2017-LIMIT-ENTRY-LT`, 02:24) |

ICT treats the choice as a preference on the same setup: "you're going to have to determine
whether you're going to be a buyer on a stop or a buyer on a limit. It doesn't matter which one
you'll elect to go with" — with the caveat that limits miss fills and stops widen the gap to the
stop-loss.

## Formal Criteria

**Shared prerequisites (identical in both lessons):**

1. The **monthly and/or weekly** chart must show institutional order flow seeking a PD array
   *above* daily market price (for longs) or *below* it (for shorts).
2. The **daily** candle must be counter-directional: a **down close** for a long, an **up close**
   for a short.
3. **The candle must be closed.** "It is not valid while the daily chart candle is trading and or
   forming" — stated verbatim in both lessons.
4. The daily candle must sit at a **daily PD array** — not any candle. "We're not just
   indiscriminately going out and finding up candles and down candles… you have to blend the PD
   arrays on the daily chart as well" (`ICT-2017-LIMIT-ENTRY-LT`, 04:50–05:09).
5. Prefer entries **at or below equilibrium** of the monthly/weekly range: "you will be buying
   preferably at equilibrium or less than the range that you would identify on the monthly and
   weekly charts" (`ICT-2017-STOP-ENTRY-LT`, 05:45).

**Stop entry — long:** place a buy stop at the **open** of the closed down candle. Filled when
price trades back up through it. If unfilled, roll the order to each successive new down candle:
"you keep moving forward every time you get a new successive down candle. You keep adding that new
entry at the opening price" (03:12–03:21). Short is the mirror on an up candle's open.

**Limit entry — long:** place a buy limit at the **close** of the closed down candle. Filled when
the next session trades below it. Short is the mirror on an up candle's close.

**Why the open, not an arbitrary level.** The trigger is order-block theory restated: "order block
theory, this would be a bullish order block. A down candle is a bullish order block. If price
trades away from a down candle and we trade back down into that opening of the down candle, that's
also what? A future entry long position" (`ICT-2017-STOP-ENTRY-LT`, 02:31–02:48).

**Re-entry / scaling.** Both lessons attach the same management: after several hundred pips, take
partial profit; if price returns to the same open, re-establish the same portion at the same
average price (`ICT-2017-STOP-ENTRY-LT`, 04:32–05:03).

**Where it stops working.** "The higher we get on the monthly and weekly range and get closer to
those premium ranges, the less likely these candles are going to promote strong buying" (05:32).

## Formula / Math

```
# prerequisite
HTF_draw := monthly and/or weekly PD array above (long) / below (short) daily price
C        := last CLOSED daily candle
valid    := (long  and close(C) < open(C) and C sits at a daily discount PD array)
         or (short and close(C) > open(C) and C sits at a daily premium  PD array)

# triggers
stop_entry_long   : BUY STOP  @ open(C)      # fills on strength through the open
limit_entry_long  : BUY LIMIT @ close(C)     # fills on the next session trading lower
stop_entry_short  : SELL STOP @ open(C)
limit_entry_short : SELL LIMIT@ close(C)

# unfilled -> roll to the next counter-directional closed daily candle
```

## Machine-Readable

```json
{
  "id": "htf-daily-candle-entries",
  "category": "31-models",
  "aliases": ["stop-entry-technique", "limit-entry-technique", "daily-candle-open-entry"],
  "criteria": [
    {"id": "c1", "expr": "monthly_or_weekly_PD_array is the draw in the trade direction"},
    {"id": "c2", "expr": "daily candle closed counter-directional (down close for long)"},
    {"id": "c3", "expr": "candle must be CLOSED; forming candle is invalid"},
    {"id": "c4", "expr": "candle must coincide with a daily PD array"},
    {"id": "c5", "expr": "stop_entry_price == open(candle)"},
    {"id": "c6", "expr": "limit_entry_price == close(candle)"},
    {"id": "c7", "expr": "entry_zone preferably at or below equilibrium of the HTF range"},
    {"id": "c8", "expr": "unfilled orders roll to the next counter-directional daily candle"}
  ],
  "timeframes": ["D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["bullish-order-block","bearish-order-block","htf-pd-array-hierarchy","pd-array-hierarchy","ipda-trailing-stop","capital-allocation-30-percent","equilibrium-definition","judas-swing"],
  "sources": ["ICT-2017-STOP-ENTRY-LT","ICT-2017-LIMIT-ENTRY-LT"]
}
```

## Visual Pattern

```
   One closed DOWN daily candle, two ways in:

              │  high
              │
        ┌─────┴─────┐  <── OPEN     ...... BUY STOP here (stop entry)
        │███████████│                      fills on the move back up
        │███████████│
        └─────┬─────┘  <── CLOSE    ...... BUY LIMIT here (limit entry)
              │                            fills on the next day's dip
              │  low

   Prerequisite in both cases:
     monthly/weekly PD array sits ABOVE  ────────►  the draw
     the down candle sits at a daily discount PD array

   Mirror everything for shorts on an UP candle.
```

## Timeframes

Daily execution only, framed by monthly and weekly. ICT notes the intraday analogue of the limit
entry: "many times when we look at day trades… which you'll see as the Judas swing, it'll open,
make the high in London and then sell off" (`ICT-2017-LIMIT-ENTRY-LT`, 06:05).

## Examples

**Example 1 — USDJPY limit entries, Sep 2016 → Jan 2017 (`ICT-2017-LIMIT-ENTRY-LT`, 07:57–09:24):**
Weekly bullish order block near 100, weekly bearish order block near 118–119 as the draw. Six
successive down-candle-close limit fills, measured to the weekly bearish order block:

| Fill | Move to the weekly PD array |
|---|---|
| September 2016 low | **1,800 pips** |
| ~17 November 2016 | **980 pips** |
| next down close | **785 pips** |
| next | **600 pips** |
| next | **500 pips** |
| last before target | **360 pips** |

**Example 2 — USDJPY stop entries off the 2007 high (`ICT-2017-STOP-ENTRY-LT`, 11:14–12:57):**
Price pierces 123.50, rejects, breaks structure bearishly. Five up candles inside the premium of
the daily range each trip a sell stop at their open; "several hundred pips again, and this last
one here, over a thousand pips available in terms of downside potential."

## Common Mistakes

- **Entering on a live candle.** Both lessons state the invalidation explicitly; a candle that is
  still forming has no settled open-to-close relationship to trade.
- **Taking any counter candle.** Without a daily PD array under it and an HTF draw above it, the
  candle is not a signal — "it's not a be all end all and, you know, a system in and of itself"
  (`ICT-2017-LIMIT-ENTRY-LT`, 05:00).
- **Confusing the two prices.** Open = stop entry (buy strength). Close = limit entry (buy
  discount). Swapping them inverts the fill logic.
- **Expecting the limit to fill.** "If you are going to be trading with limit orders there's a
  probability of you missing moves or missing your fills because you're demanding a specific price
  level."
- **Ignoring the stop-distance cost of the stop entry.** "When you go on a buy stop generally
  you're going to end up getting filled more times using that order, but unfortunately that creates
  a little bit more gap in between where you're entering and where your stop loss is going to be."
- **Running it into premium.** Near the top of the monthly/weekly range the down candles stop
  producing buying; the technique is a discount-side tool.

## Related Concepts

- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md) — the theory the trigger price is derived from.
- [htf-pd-array-hierarchy](../05-pd-arrays/htf-pd-array-hierarchy.md), [pd-array-hierarchy](../05-pd-arrays/pd-array-hierarchy.md) — how the HTF draw is selected.
- [ipda-trailing-stop](../32-risk-management/ipda-trailing-stop.md) — the stop rule applied after either fill.
- [capital-allocation-30-percent](../32-risk-management/capital-allocation-30-percent.md) — the sizing regime.
- [judas-swing](../13-judas-swing/judas-swing.md) — the intraday analogue ICT names for the limit fill.

## Citations

- `ICT-2017-STOP-ENTRY-LT` (00:00) — "Welcome back folks this is lesson 7.1 stop entry techniques for long term traders"; (00:22–00:52) the four prerequisites and the buy stop at the bearish candle's opening; (01:18) "you're going to be using strength to get you long"; (02:31–02:48) the order-block derivation; (03:12–03:21) rolling the order to each new down candle; (04:32–05:03) partial-profit re-entry at the same open; (05:32–05:45) diminishing effect approaching premium; (11:14–12:57) the USDJPY 2007-high sell-stop sequence.
- `ICT-2017-LIMIT-ENTRY-LT` (00:11) — "This is lesson 7.2 of the January 2017 content, using limit entry techniques for long-term traders"; (00:24–00:53) the same prerequisites with the buy limit at the bearish candle's close; (02:24–02:37) "we're buying at a deeply undervalued price… a deep, deep discount"; (04:50–05:09) the candle alone is not a system, blend the daily PD arrays; (06:05) the Judas-swing analogue; (07:57–09:24) the six USDJPY limit fills and their pip measures.
