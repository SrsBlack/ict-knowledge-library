# Monthly Bias

**Category:** 25-htf-bias
**Aliases:** MN bias, monthly direction
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-LONGTERM-TOP-DOWN, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** htf-bias, monthly

## Definition

Monthly bias is the directional read derived from the **monthly chart** — the broadest tradeable HTF in standard ICT analysis. Monthly bias sets the structural backdrop for every lower-TF bias read; it changes slowly and rarely, but when it flips, all lower-TF biases should be re-evaluated. Most day-traders defer to weekly / daily bias for execution but reference monthly for context.

## Formal Criteria

Monthly bias is bullish when:

- Most recent monthly external BOS was up.
- Current price below monthly EQ (in monthly discount).
- Monthly draw on liquidity is upside (BSL ahead).

Monthly bias is bearish when symmetric down-side conditions hold.

Monthly is **neutral** when at EQ ± buffer, or external structure in transition.

**ICT's own monthly routine** (`ICT-2017-LONGTERM-TOP-DOWN`) — tier 1 of [top-down-analysis](top-down-analysis.md), run **once a month at the close of the month just ended** ("you only have a candle forming once a month on a monthly timeframe", 12:04):

1. **Seasonal tendency** for the month about to begin. "It all starts here" (03:16).
2. **Quarterly shift** — the anticipated 3-to-4-month direction, judged against the **9-to-18-month trend read off the raw monthly candles**: "it has nothing to do with moving averages here, I'm just looking at the actual candles going back 18 candles on the monthly chart" (19:16). Trade with it — "I'm trying to avoid picking the tops or the bottoms of the 9 to 18 month trend" (19:07).
   - **Unclear-trend default:** "if the 9 to 18 month trend is not clear or it's in consolidation… I will elect to anticipate the direction of the previous **three to four months** direction to **reverse**" (20:16).
3. **Interest-rate differentials** — pair a high-rate against a low-rate currency from the central-bank policy table.
4. **Market profile** → **intermarket analysis** → **market structure + SMT** → **PD array matrix** → **key price levels** (the shared spine).
5. Output the bias, then **transpose it onto the weekly chart** (12:47).

**Horizon:** "I'm trying to forecast the next **three months** movement from a long-term perspective" (14:47) — and capturing half of the coming monthly candle is treated as sufficient: "if I can get that right, that's many times enough for me to be profitable for the month" (15:34).

## Formula / Math

```
mn_dealing_range = [LTL_mn, LTH_mn]
mn_eq = (LTL_mn + LTH_mn) / 2

mn_bias :=
  "bullish" if last_external_break == bullish AND price < mn_eq AND DOL_upside_present
  "bearish" if last_external_break == bearish AND price > mn_eq AND DOL_downside_present
  "neutral" otherwise
```

## Machine-Readable

```json
{
  "id": "monthly-bias",
  "category": "25-htf-bias",
  "aliases": ["MN-bias", "monthly-direction"],
  "criteria": [
    {"id": "c1", "expr": "uses_monthly_external_structure"},
    {"id": "c2", "expr": "considers_current_price_vs_monthly_eq"},
    {"id": "c3", "expr": "considers_monthly_DOL"},
    {"id": "c4", "expr": "cadence == once per month, at close of month just ended"},
    {"id": "c5", "expr": "input order == [seasonal, quarterly_shift, rate_differentials] then shared spine"},
    {"id": "c6", "expr": "trend lookback == 9..18 raw monthly candles, no moving averages"},
    {"id": "c7", "expr": "if trend unclear or consolidating => expect reversal of last 3..4 months"},
    {"id": "c8", "expr": "forecast_horizon_months == 3"}
  ],
  "timeframes": ["MN","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","weekly-bias","daily-bias","bias-confluence","top-down-analysis","dealing-range","seasonal-tendency","quarterly-shift-theory","interest-rate-differentials","pd-array-matrix"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2017-LONGTERM-TOP-DOWN","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Monthly chart:

   LTH_mn ─────────  monthly LTH (recently broken UP for bullish bias)
                /\
               /  \
   ──────────── MN_EQ
              ↓
              price (below EQ → discount)
   LTL_mn ─────────  prior monthly LTL
```

## Timeframes

MN — analyze on monthly candles.

## Examples

**Example 1 — bullish monthly bias:**
- Monthly LTH 1.1200 (broken up 3 months ago).
- Monthly LTL 1.0500 (4 months ago).
- MN_EQ = 1.0850; current price 1.0820 = discount.
- Upside DOL: monthly BSL above 1.1200 (already taken; new ATH BSL ahead).
- → bullish monthly bias.

## Common Mistakes

- **Reacting to single monthly candle.** Monthly bias changes slowly; one mixed monthly candle isn't a flip.
- **Ignoring monthly when day-trading.** Monthly bias provides backdrop conviction; setups against monthly are lower-probability even when daily aligns.
- **Re-running the routine mid-month.** One candle a month, one analysis a month. ICT answers the objection directly — "is this guy really want me to do this every single time I take a trade? **No, just once a month**" (`ICT-2017-LONGTERM-TOP-DOWN`, 11:47).
- **Reaching for a moving average to define the 9-to-18-month trend.** ICT rules it out by name; the read is off raw candles.
- **Treating a consolidating monthly as "no bias".** The taught default is a *reversal* of the last three-to-four months' direction, not a stand-aside.
- **Skipping time-of-day work here.** Correct, but for a reason: it is deliberately excluded above the daily, not forgotten (`ICT-2017-INTERMEDIATE-TOP-DOWN`, 46:44 — cited on [top-down-analysis](top-down-analysis.md)).

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [weekly-bias](weekly-bias.md), [daily-bias](daily-bias.md), [bias-confluence](bias-confluence.md), [top-down-analysis](top-down-analysis.md), [dealing-range](../05-pd-arrays/dealing-range.md).
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [interest-rate-differentials](../03-order-flow/interest-rate-differentials.md) — the three tier-1 inputs, in ICT's order.
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md) — where the monthly key levels are calibrated.

## Citations

- `ICT-2017-LONGTERM-TOP-DOWN` (00:13) "this is going to be teaching the ICT long-term top-down analysis… how I personally go through the monthly chart to arrive at levels that would be transposed… to the weekly chart"; (02:01–02:10) "I try to do this level of analysis once a month, and it's usually the close of the month that just ends"; (03:16) "it all starts here, seasonal tendencies"; (05:44–06:25) the quarterly shift as a three-to-four-month expectation; (06:40) interest-rate differentials third; (11:22–11:47) "by going through this entire process step by step in order in this way, I end up getting to a monthly bias… no, just once a month"; (12:47) transposed to the weekly; (14:47–15:44) forecasting three months, half a candle being enough; (18:37–19:21) the 9-to-18-month trend read off 18 raw monthly candles, "it has nothing to do with moving averages here"; (20:16–20:27) the consolidation default.
- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW` — the general monthly-context restatement in later years.
