# Quarterly Market Structure Shift

**Category:** 01-market-structure
**Aliases:** quarterly shift, quarterly market shift, 3-to-4-month shift, quarterly effect
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-QUARTERLY-SHIFTS, ICT-2017-IPDA-DATA-RANGES, ICT-2017-OPEN-FLOAT-L12
**Tags:** structure, quarterly, htf, daily, mss, position-trading

## Definition

The quarterly market structure shift is ICT's claim that **every three to four months, on every
asset class, the daily chart changes direction**. "I teach that there is a market structure shift
that takes place every three to four months. And for the most part, that's universal. It doesn't
apply just to the foreign exchange market, but it does apply to all asset classes"
(`ICT-2017-QUARTERLY-SHIFTS`, 05:00–05:13).

The stated cause is engineered interest, not a calendar: "this effect takes place because the
market has to generate new interest. It has to have a new sense of urgency" (05:13). It is the
event that **anchors** the IPDA data ranges — see
[ipda-data-range-calibration](../23-ipda/ipda-data-range-calibration.md).

⚠ **Not the same concept as [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md).**
That page describes the 2023+ fractal Q1–Q4 AMD decomposition and a 2024–25 ERL↔IRL rotation.
This is the 2017 teaching: a directional structure break on the daily chart, once a quarter.
Same words, different mechanism, six years apart.

## Formal Criteria

- **Cadence:** every 3–4 months. "Every three months, there's going to be something like this
  occurring" (`ICT-2017-IPDA-DATA-RANGES`, 12:27).
- **Timeframe:** identified on the **daily** chart, with monthly and weekly for context.
- **Obviousness is the test.** "If I was to ask everyone… raise your hand if you can clearly see
  that that is the most obvious market shift in the last three to six months. Everybody invariably
  would raise their hand" (12:11–12:22). If it is not obvious, it is not the one.
- **Search window:** the most recent 3 months, extendable to 6. "It may require you going back
  three months. But find the most recent one where the market structure has shifted and there was
  a move that took place that was obvious" (16:18–16:31).
- **Form:** either direction. "It could be a sell-off creating a high, or it could be a low where
  it starts to rally" (12:31).
- **The counter-move need not be a retracement.** "It doesn't need to be a counter trend move…
  It can be a consolidation" (`ICT-2017-IPDA-DATA-RANGES`, 14:27–14:35). In a strong trend ICT
  expects a range instead: "many times you won't see much of a retracement, but you will see
  consolidation or trading range form" (`ICT-2017-QUARTERLY-SHIFTS`, 07:31).
- **Maturity tell:** roughly six months of one-way movement precedes the shakeup. "It's been
  essentially six months of down movement on the dollar. That's about when you're going to see
  the shakeup that takes place" (48:36–48:45).
- **A quick way to find them:** "divide your daily chart into quarters, like put a line on March,
  put a line on June and September, December… Your eye will go right to where these quarterly
  shifts are happening. They're not going to always occur on those months"
  (`ICT-2017-IPDA-DATA-RANGES`, 16:36–16:50).

**Confirmation via open interest** (futures only, `ICT-2017-IPDA-DATA-RANGES`, 58:23–59:26):
a drop in open interest of **15% or more** at a major support level, while price is sideways, is
read as the liquidity provider closing out its short book — bullish. "If open interest has a 15%
or more drop or change lower like it does here, this is a very significant drop. While price is
sideways, this is bullish."

**How much of it is tradeable:** despite four quarters a year, ICT expects only two — occasionally
three — executable position setups annually (see
[capital-allocation-30-percent](../32-risk-management/capital-allocation-30-percent.md)).

## Formula / Math

```
# on the DAILY chart
candidate_shift := the single most obvious break of structure
                   within the last 60-120 trading days

cadence          ≈ every 3 to 4 months
one_way_run_before_shift ≈ 6 months
anchor           := first trading day of month(candidate_shift)

post_shift_expectation := retracement OR consolidation   # not necessarily counter-trend

# futures confirmation
open_interest_drop >= 15%  AND price sideways AND at major support  ->  bullish
```

## Machine-Readable

```json
{
  "id": "quarterly-market-structure-shift",
  "category": "01-market-structure",
  "aliases": ["quarterly-shift", "quarterly-market-shift", "3-to-4-month-shift"],
  "criteria": [
    {"id": "c1", "expr": "cadence_months in [3, 4]"},
    {"id": "c2", "expr": "identified_on == daily_chart"},
    {"id": "c3", "expr": "is_the_single_most_obvious_MSS in last 3-6 months"},
    {"id": "c4", "expr": "post_shift_move in {retracement, consolidation}"},
    {"id": "c5", "expr": "applies_to_all_asset_classes == true"},
    {"id": "c6", "expr": "futures_confirmation := open_interest_drop_pct >= 15 at support"}
  ],
  "timeframes": ["D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["mss","bos-bullish","bos-bearish","ipda-data-range-calibration","ipda-data-ranges","open-float-liquidity-pool","open-interest","quarterly-shift-theory","seasonal-tendency","capital-allocation-30-percent"],
  "sources": ["ICT-2017-QUARTERLY-SHIFTS","ICT-2017-IPDA-DATA-RANGES","ICT-2017-OPEN-FLOAT-L12"]
}
```

## Visual Pattern

```
   daily chart, ~12 months

        Q1 shift          Q2 shift            Q3 shift
           |                 |                    |
      /\   |                 |        /\          |
     /  \  |    \           /|       /  \        /|
    /    \ |     \         / |      /    \      / |
   /      \|      \_/\_/\_/  |     /      \    /  |
           |                 |    /        \__/   |
           v                 v                    v
      break lower       break higher         break lower

   Each shift = the single most obvious BOS in its 3-month block.
   Between shifts: either a retracement OR a consolidation.
```

## Timeframes

Daily is the identification chart; monthly and weekly supply the PD-array context that says which
way the next shift should run. Intraday charts do not show it.

## Examples

**Example 1 — AUD futures, November 2016 (`ICT-2017-IPDA-DATA-RANGES`, 09:52–15:15):**
- Consolidation between roughly 77.50 and 74.50 through August–October 2016.
- November: false breakout above 77.50, rejection, then equal highs pierced and a low broken —
  "we have a shift in market structure and it breaks lower" (14:55).
- "That's a quarterly market shift. Over the last three to six months, that's the most obvious
  one" (12:03–12:10).
- Post-shift sell profile ran into 71.50; open interest collapsed there; the market turned bullish
  into January 2017.

**Example 2 — EURUSD, December 2015 → March 2016 (`ICT-2017-QUARTERLY-SHIFTS`, 40:51–45:45):**
- Dollar index breaks structure bearishly after 1 December 2015; EURUSD breaks bullishly.
- Between the December and March vertical lines, EURUSD posts higher lows while DXY posts higher
  highs — "this was under what? Accumulation" (44:30).
- The move completes at the 60-day cast-forward line.

## Common Mistakes

- **Marking more than one shift per quarter.** Only the single most obvious break qualifies;
  "if you do that, you're really doing too much anticipation" (`ICT-2017-IPDA-DATA-RANGES`, 16:13).
- **Assuming the shift lands on a calendar-quarter boundary.** It does not — "they're not going
  to always occur on those months. There's a little bit of gray area, which is the reason why we
  have a look back and a cast forward" (16:48–16:54).
- **Confusing it with Quarterly Theory's fractal AMD.** See the warning in the Definition.
- **Expecting the long-term trend to reverse.** "While that may not undo the long-term bullish or
  bearish moves, they are executable" (71:19–71:28). Long-term macro fundamentals "are not
  impacted by three-month cycles" (41:54).
- **Trading all four a year.** ICT expects two, occasionally three, executable position setups.

## Related Concepts

- [mss](mss.md), [bos-bullish](bos-bullish.md), [bos-bearish](bos-bearish.md) — the break itself.
- [ipda-data-range-calibration](../23-ipda/ipda-data-range-calibration.md) — the shift's month start is the anchor.
- [open-float-liquidity-pool](../02-liquidity/open-float-liquidity-pool.md) — what gets targeted across the quarter.
- [open-interest](../03-order-flow/open-interest.md) — the 15%-drop confirmation.
- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md) — the later, different concept sharing the name.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — the calendar filter ICT pairs with the shift.

## Citations

- `ICT-2017-QUARTERLY-SHIFTS` (00:21) — "Welcome to the January 2017 ICT Mentorship Long Term Analysis Lesson 1.1"; (00:29) "this teaching is Quarterly Shifts and IPTA Data Ranges"; (05:00–05:13) every three to four months, universal across asset classes; (05:13) "the market has to generate new interest"; (07:31) consolidation in place of retracement; (48:36–48:45) six months of one-way movement before the shakeup.
- `ICT-2017-IPDA-DATA-RANGES` (12:03–12:31) the November 2016 quarterly shift and the obviousness test; (14:27–14:35) "it can be a consolidation"; (16:13–16:54) one per quarter, gray area around month boundaries; (41:54) long-term macro is not impacted by three-month cycles; (58:23–59:26) the 15% open-interest drop; (71:19–71:28) the shift does not undo the long-term trend.
- `ICT-2017-OPEN-FLOAT-L12` (03:48–04:23) — "because we're looking at the quarterly shift, that's going to be a very significant price level where buy stops will be resting… every three months, you want to be noting where that high is"; (09:27) "pay attention to the quarterly shift markers that we have here. Every three months, there is a significant run on liquidity."
