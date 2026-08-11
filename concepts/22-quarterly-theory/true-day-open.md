# True Day Open (TDO)

**Category:** 22-quarterly-theory
**Aliases:** TDO, midnight open, daily true open, IPDA true day open
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-DEFINING-DAILY-RANGE, ICT-2017-CHARTER-OVERVIEW, ICT-2023-QUARTERLY-THEORY
**Tags:** quarterly-theory, true-day-open, foundational, ipda

## Definition

The **True Day Open (TDO)** is the **00:00 NY-time price** — the official daily candle opening per ICT's framework. Distinct from "session open" or "broker open" times: TDO is anchored to NY midnight regardless of broker convention. ICT teaches TDO as the **primary intraday premium/discount reference**: price above TDO = intraday premium (favor shorts in bearish-bias contexts); price below TDO = intraday discount (favor longs in bullish-bias contexts). TDO is one of the most-cited time-of-day pivots in ICT analysis.

The term is ICT's own and it is defined verbatim in the April-2017 mentorship: "**every day at
12 a.m. midnight New York time begins the IPDA true day** — this is the beginning of the
24-hour interbank trading day" (`ICT-2017-DEFINING-DAILY-RANGE`, 05:07–05:29). The same lesson
supplies the *other* end of that interval, which TDO alone does not: the IPDA true day **ends
at 3 p.m. New York time** (05:29–05:38). See [ipda-true-day](../04-time-cycles/ipda-true-day.md)
for the full 00:00 → 15:00 frame and its rationale.

## Formal Criteria

- TDO = open price at exactly 00:00 NY (midnight, NY clock).
- Not the same as: 17:00 NY forex close, 18:00 NY Sunday open (NWOG), or broker server-time daily candle open.
- Acts as a horizontal price level on intraday charts; price relative to TDO drives intraday bias.
- Premium / discount classification on intraday is **TDO-anchored**, not necessarily the same as the daily-dealing-range premium/discount.
- **The open ICT names is the start of a bounded interval, not of a rolling 24 hours.** The
  IPDA true day runs **00:00 → 15:00 NY**; the daily open, high, low and close ICT frames are
  the extremes of that window (`ICT-2017-DEFINING-DAILY-RANGE`, 05:17–05:38, 10:21).

## Formula / Math

```
tdo = open_price_at(00:00 NY)

intraday_premium_vs_TDO := current_price > tdo
intraday_discount_vs_TDO := current_price < tdo

# Combined with HTF bias:
bullish_bias_setup_zone := price < tdo (intraday discount in bullish bias)
bearish_bias_setup_zone := price > tdo (intraday premium in bearish bias)
```

## Machine-Readable

```json
{
  "id": "true-day-open",
  "category": "22-quarterly-theory",
  "aliases": ["TDO", "midnight-open", "daily-true-open"],
  "criteria": [
    {"id": "c1", "expr": "tdo = open at 00:00 NY"},
    {"id": "c2", "expr": "horizontal intraday reference"},
    {"id": "c3", "expr": "drives intraday premium/discount classification"},
    {"id": "c4", "expr": "opens the IPDA true day interval 00:00 -> 15:00 America/New_York"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["quarterly-theory-overview","daily-quarters","time-of-day-pivots","ndog","true-week-open","htf-bias-framework","ipda-true-day"],
  "sources": ["ICT-2017-DEFINING-DAILY-RANGE","ICT-2017-CHARTER-OVERVIEW","ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   TDO as intraday pivot:

   intraday premium (above TDO)
   ───────── TDO (00:00 NY) ─────────
   intraday discount (below TDO)

   bullish bias + price below TDO = preferred long-zone
   bearish bias + price above TDO = preferred short-zone
```

## Timeframes

M5 / M15 / H1 / H4.

## Examples

**Example 1 — TDO + HTF bias confluence:**
- HTF bias bullish.
- TDO = 1.0860 (00:00 NY open).
- Current price 1.0840 → intraday discount vs TDO.
- → preferred long-zone; setups in this zone get TDO-confluence bonus.

## Common Mistakes

- **Using broker time as TDO.** If broker's daily candle opens at 17:00 NY (forex) or some other server-time, that is NOT the TDO; recompute the 00:00 NY open.
- **Confusing TDO with 17:00 NY close.** TDO is the open, not the close.
- **Ignoring TDO for intraday bias.** Many intraday traders skip TDO and use only daily range EQ; combining both is stronger.

## Related Concepts

- [ipda-true-day](../04-time-cycles/ipda-true-day.md) — the 00:00 → 15:00 interval this open begins, and the rest of the 2017 time frame.
- [quarterly-theory-overview](quarterly-theory-overview.md), [daily-quarters](daily-quarters.md), [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md), [ndog](../31-models/ndog.md), [true-week-open](true-week-open.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-DEFINING-DAILY-RANGE` (00:14) "this is **lesson two of the April 2017 ICT mentorship** content dealing with ICT day trading model — this lesson is defining the daily range" — dates the source; (05:07–05:29) "the IPDA true day definition — **every day at 12 a.m. midnight New York time begins the IPDA true day**. This is the beginning of the 24-hour interbank trading day"; (05:29–05:38) "**every day at 3 p.m. New York time ends the IPDA true day**"; (10:21) "that's how you frame the entire daily range — **open, high, low and close**".
- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2023-QUARTERLY-THEORY`.
