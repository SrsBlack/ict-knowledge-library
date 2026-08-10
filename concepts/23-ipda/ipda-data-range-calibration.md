# IPDA Data Range Calibration

**Category:** 23-ipda
**Aliases:** look back and cast forward, anchoring the data ranges, calibrating market structure, 20/40/60 projection
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-QUARTERLY-SHIFTS, ICT-2017-IPDA-DATA-RANGES
**Tags:** ipda, calibration, lookback, cast-forward, daily, quarterly, anchor

## Definition

Data range calibration is the **procedure** for placing the IPDA 20/40/60-day windows on a
chart. The windows are not measured from today: they are measured from an **anchored vertical
line**, and they run in **both directions** from it. "You're looking back left 60 trading days
at the maximum" (`ICT-2017-QUARTERLY-SHIFTS`, 22:22) and "the cast forward is when you look
ahead with the same parameters we use when we look back" (34:52).

The anchor is a **calendar-month first trading day**, then re-anchored onto the most recent
[quarterly market structure shift](../01-market-structure/quarterly-market-structure-shift.md).
The **look back** finds the liquidity; the **cast forward** dates the next setup. "You're
looking back to find what the liquidity is, and you're looking forward or to the right of it
to get the very next setup in terms of the data range" (52:38).

⚠ This is the missing half of [ipda-data-ranges](ipda-data-ranges.md), which describes only the
trailing measurement.

## Formal Criteria

**Step 1 — provisional anchor.** Put a vertical line on the **first trading day of the most
recent *closed* calendar month**. ICT tests this explicitly: "say it was November 14th, 2016 —
what month would you calibrate your vertical line to, to start? If you said October 1st, 2016,
you're accurate. You want to go back to the previous closed month" (`ICT-2017-QUARTERLY-SHIFTS`,
53:28–53:44).

**Step 2 — re-anchor to structure.** Look back over the last 60 trading days for the most
obvious intermediate-term high or low. "Whichever is true and whichever is obvious to you, then
you put your vertical line on that high or that low. So now you're calibrating it to the market
structure that's in place right now… you're anchoring your vertical line to a previous market
structure shift" (27:00–27:23). In `ICT-2017-IPDA-DATA-RANGES` the same step is stated as rolling
back to the **month start** of the shift: "you have to roll back to the beginning of that month"
(39:06).

**Step 3 — look back.** From the anchor, measure **60, 40 and 20 trading days to the left** —
"and they're all trading days, not calendar days" (23:41). In each window record:

| What to find | Why |
|---|---|
| Highest high | buy stops rest above it |
| Lowest low | sell stops rest below it |
| Fair value gaps / price gaps | "where price has not been efficiently delivered" |
| Liquidity voids | one-sided delivery that must be rebalanced |
| Consolidations | their midpoints are the equilibrium price points |
| Order blocks, rejection blocks | institutional reference points |

"Last 60 days, where's the high and the low? Last 40 days… Last 20 days… That's where your
liquidity pools are. Okay, last 20 days, where is the gaps?… That's where all your fair value
levels are… Where's the consolidations…? That's where your equilibrium price points are going to
be" (`ICT-2017-IPDA-DATA-RANGES`, 77:54–78:26).

**Step 4 — cast forward.** Draw vertical lines **20, 40 and 60 trading days to the right** of the
anchor. That range dates the next shift: "the algorithm is going to anticipate doing a shift in
the marketplace in that range between 60 and 20 days" (`ICT-2017-QUARTERLY-SHIFTS`, 34:29). The
denominator never changes — "we cast forward 20 days to the right of our vertical line when the
last shift was 40 days ago… we cast forward 40 days when the last shift was 20 days ago. Again,
the common denominator is it's 60 days of range that we're always using" (35:26–36:09).

**Step 5 — the exhaustion rule.** If every high and low inside the 60-day look back has already
been traded through, the next move must reach **outside** the window: "if everything's been
cleaned out above and below the highs and lows, there's no more buy stops… it has to create a
new expansion. So you have to identify what the next high and low outside that range of 60 days
looking back where that is" (`ICT-2017-IPDA-DATA-RANGES`, 32:40–33:04). That condition is the
tell for an outsized move.

**Step 6 — recurse.** Each cast-forward line becomes a future anchor with its own 20/40/60
look back. "By having these things on your chart, you'll be able to look backwards and forwards…
and if you get an overlap, that's when the magic happens" (121:56–122:05).

## Formula / Math

```
anchor A := first trading day of the most recent closed calendar month,
            re-anchored to the month start of the most obvious
            quarterly market structure shift in the last 60 trading days

# all counts are TRADING days
lookback_high(n)  := max(high) over [A-n, A]      n in {20, 40, 60}
lookback_low(n)   := min(low)  over [A-n, A]
equilibrium(n)    := (lookback_high(n) + lookback_low(n)) / 2

cast_forward(n)   := A + n trading days           n in {20, 40, 60}

next_shift_window := [A+20, A+60]
total_span        := 120 trading days             # 60 back + 60 forward

expansion_required := all(lookback extremes swept)   # -> target outside [A-60, A]
```

## Machine-Readable

```json
{
  "id": "ipda-data-range-calibration",
  "category": "23-ipda",
  "aliases": ["look-back-and-cast-forward", "data-range-anchoring"],
  "criteria": [
    {"id": "c1", "expr": "anchor == first_trading_day(previous_closed_calendar_month)"},
    {"id": "c2", "expr": "anchor re-set to month_start(most_obvious_quarterly_MSS in last 60 trading days)"},
    {"id": "c3", "expr": "windows == [20, 40, 60] TRADING days, measured left AND right of anchor"},
    {"id": "c4", "expr": "next_shift_expected in [anchor+20, anchor+60]"},
    {"id": "c5", "expr": "all_lookback_extremes_swept -> target lies outside [anchor-60, anchor]"},
    {"id": "c6", "expr": "each cast_forward line becomes a future anchor"}
  ],
  "timeframes": ["D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["ipda-definition","ipda-data-ranges","ipda-20-day-lookback","ipda-40-day-lookback","ipda-60-day-lookback","ipda-reference-points","quarterly-market-structure-shift","open-float-liquidity-pool","dealing-range"],
  "sources": ["ICT-2017-QUARTERLY-SHIFTS","ICT-2017-IPDA-DATA-RANGES"]
}
```

## Visual Pattern

```
        LOOK BACK                A                 CAST FORWARD
   <-- 60 --><-- 40 --><-20->    |    <-20-><-- 40 --><-- 60 -->
   |         |         |         |         |         |        |
   |         |         |    anchored on    |         |        |
   |         |         |    the month of   |         |        |
   |         |         |    the quarterly  |         |        |
   |         |         |    shift          |         |        |
   ─────────────────────────────────────────────────────────────
   find:  highest high / lowest low       expect: the next
          FVGs, liquidity voids                   quarterly shift
          consolidation midpoints                 somewhere in
          order & rejection blocks                [A+20, A+60]

   A daily-chart procedure. 60 back + 60 forward = 120 trading days.
```

## Timeframes

Daily chart only for the measurement — "this is all relative to the daily timeframe only,
nothing less than a daily chart" (`ICT-2017-QUARTERLY-SHIFTS`, 13:41). ICT states the read is
"more confirmed when you start applying it to the weekly chart and the monthly chart"
(`ICT-2017-IPDA-DATA-RANGES`, 33:08).

## Examples

**Example 1 — dollar index, anchor 1 Dec 2015 (`ICT-2017-QUARTERLY-SHIFTS`, 28:31–41:01):**
- Anchor: first trading day of December 2015.
- Look back 60: market rallied from an October 2015 intermediate-term low → institutional order
  flow bullish → "where is the liquidity at? It's going to be… below the marketplace" (30:05).
- After the anchor, a key low breaks → bearish expectation for the next quarter.
- Cast forward: the EURUSD high "falls directly right at the 60-day IPDA data range. Nails it on
  the very high" (39:39–39:50).

**Example 2 — AUD futures, anchor 1 Nov 2016 (`ICT-2017-IPDA-DATA-RANGES`, 34:10–40:04):**
- Anchor: 1 November 2016, the month of the quarterly shift.
- Cast forward 20 days → consolidation into an October low, no shift.
- Cast forward 40 days → 71.50 reached; "very significant price move occurred from that price,
  71.50" (40:20). The exact low printed two days earlier — inside, not on, the 40-day line.
- Look back 20 trading days from the 40-day line → mid-December equal highs → "what's resting
  above that? Buy stops. So what is the IPTA algorithm going to do? It's going to seek that
  liquidity" (43:35–43:51).

## Common Mistakes

- **Anchoring on today.** The windows hang off a *month-start* vertical line, not the right edge
  of the chart. Measuring from today gives different levels.
- **Expecting a turn exactly on day 20/40/60.** "I'm not telling you that the market turns every
  20 days, every 40 days, and every 60 days. But it can and will sometimes do that"
  (`ICT-2017-IPDA-DATA-RANGES`, 38:45–38:58). The line dates a *window*, not a bar. ICT notes the
  turn may land on day 19 or day 21 (38:19–38:30).
- **Treating the ranges as a high/low forecast.** "Some of you are thinking that it's going to
  call the high and low 20 days, 40 days, and 60 days away. That's not what happens… that's not
  what its job is" (10:18–10:31).
- **Calendar days instead of trading days.** Explicitly stated at 23:41.
- **Skipping the exhaustion check.** If both sides of the 60-day range are already cleared, the
  in-window levels are spent and the draw is outside the window.
- **Reading direction off the ranges.** "Now, it's not giving you directional bias yet"
  (30:34) — the ranges locate liquidity; bias comes from structure and the HTF charts.

## Related Concepts

- [ipda-data-ranges](ipda-data-ranges.md) — the 20/40/60 windows themselves; this page is the placement procedure.
- [quarterly-market-structure-shift](../01-market-structure/quarterly-market-structure-shift.md) — the event the anchor is re-set onto.
- [open-float-liquidity-pool](../02-liquidity/open-float-liquidity-pool.md) — the same 120-day span read as a fund-level pool.
- [ipda-reference-points](ipda-reference-points.md) — what the look back is cataloguing.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the range whose midpoint gives the equilibrium price points.

## Citations

- `ICT-2017-QUARTERLY-SHIFTS` (00:21) — "Welcome to the January 2017 ICT Mentorship Long Term Analysis Lesson 1.1… Quarterly Shifts and IPTA Data Ranges"; (22:22) "you're looking back left 60 trading days at the maximum"; (23:41) "they're all trading days, not calendar days"; (27:00–27:23) re-anchoring onto the obvious high or low; (34:52) "the cast forward is when you look ahead with the same parameters we use when we look back"; (35:26–36:09) the 60-day common denominator; (39:39–39:50) the 60-day line marking the EURUSD high; (52:38) look back for liquidity, look forward for the setup; (53:28–53:44) the October-1st calibration test.
- `ICT-2017-IPDA-DATA-RANGES` (10:18–10:31) the ranges do not forecast the extremes; (15:52–16:07) "cast out 20 days… from the beginning of the month that that market structure shift or quarterly shift takes place"; (31:41) "you have 120 days of range from the past and going forward"; (32:40–33:04) the exhaustion rule; (38:19–38:58) day-19/day-21 tolerance; (39:06) "you have to roll back to the beginning of that month"; (43:35–43:51) recursive look back from a cast-forward line; (77:54–78:26) the full catalogue of what each window yields; (121:56–122:05) "if you get an overlap, that's when the magic happens."
