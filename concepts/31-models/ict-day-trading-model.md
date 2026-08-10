# ICT Day Trading Model

**Category:** 31-models
**Aliases:** ICT day trading, daytrading model, 2017 day trade model, daily range model
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-DAYTRADE-ESSENTIALS, ICT-2017-DAYTRADE-HTF
**Tags:** models, day-trading, daily-range, adr, sunday-open, weekly-bias, killzones

## Definition

The ICT day trading model is the **April-2017 mentorship framework for capturing a
single day's range**. Its stated aim is to "capitalize on at least **65 to 70 percent
of the daily range**" (`ICT-2017-DAYTRADE-ESSENTIALS`, 01:52), with an expected range
drawn from the **last five days' average daily range** and direction supplied by a
higher-timeframe read rather than by the intraday chart.

The model is deliberately low-frequency: "generally there are **two setups per trading
day on average**" (01:24), and "just because the name… is day trading it does not mean
or equate to **every day** trading" (01:18). A companion lesson closes the month by
showing that the same entry mechanics can position **higher-timeframe** trades without
ever watching the London session (`ICT-2017-DAYTRADE-HTF`).

## Formal Criteria

**Range expectation**

- Target **65–70 %** of the day's range; the rest is conceded near the high and low.
- Expected daily range ≈ **average of the last five days' ranges** (01:36–02:30). ICT
  allows a 5-period ATR on the daily as a substitute for his own ADR indicator
  (`ICT-2017-DAYTRADE-HTF`, 22:06–22:26).

**Directional frame (set before the week, not during the day)**

- Bias comes from monthly / weekly / daily **PD arrays** read over the **last 20, 40 and
  60 trading days** (07:37–07:50); for day trades "we're going to focus primarily on the
  daily" (08:05).
- Forecast the **current weekly candle's direction**, then take day trades only in that
  direction (08:35–09:26).

**Sunday-opening-price filter**

- Record the **Sunday opening price** (or Monday's open if the broker publishes no Sunday
  candle) and project it across the hourly chart **through Thursday** (23:09–24:06).
- Bearish weekly bias + price **below** the Sunday open → sell in London, continuation in
  New York, **every day** (26:45–27:40).
- Bullish weekly bias + price **above** the Sunday open → buy in London, continuation in
  New York, every day (28:04–29:07).
- **The filter is subordinate to the PD array matrix.** It holds "only until we trade to
  a higher time frame … PD array that's contrary to how our trade is unfolding"
  (27:00). Trading the filter alone is named as the error (45:22–45:47).
- Price crossing back through the Sunday open **on Thursday** registers an **intra-week
  reversal** and re-frames the following week (24:06–25:35).

**Time windows (New York time)**

| Window | Time | Use |
|---|---|---|
| London open killzone | 01:00–05:00 (hotspot 02:00–04:00) | primary day-trade window; the 4-hour envelope absorbs DST drift (11:59–12:38) |
| London lunch | 05:00–07:00 | retracement / consolidation; bank part of the London trade at or before 05:00 (17:20–18:58) |
| New York open | around the 08:20 CME open | "the easiest one to work with" (13:03) |
| London close | — | position exit, or entry for longer-term trades (14:35–15:28) |
| New York close | 14:00, bond close 15:00 | range is finished; "generally by noon you're done" (15:36–16:24) |
| Asia open | 20:00 | small setups; yen/AUD/NZD can form the daily extreme here (16:31–17:17) |

- "You have to be **flexible with time and demand specifics in price**" (10:39).

**Day-of-week profile**

- **Sunday** — opt out; range too small (18:47).
- **Monday** — typically small-range. Exception: a large range straight out of the gate
  into a daily premium/discount array often marks the **week's high or low** (19:44–20:47).
- **Tuesday** — in bullish weeks, **~70 % likelihood the week's low forms in London**;
  reversed in bearish weeks (21:00–21:19).
- **Wednesday** — ideal; two or three days of data are already behind you (21:26–21:53).
- **Thursday** — ideal but reversal-prone; the weekly range is often **capped by
  Thursday's New York session** (21:59–22:14).
- **Friday** — quiet if the weekly PD-array objective was met by Thursday; capable of a
  surprise expansion if it was not (22:21–22:52).

**No-trade conditions**

- **FOMC and Non-Farm Payroll days are no-setup days** (06:47–07:26).
- Skip New York entirely if **London already delivered ~80 % or more of the five-day
  ADR** (13:55–14:31).

**Integrating day-trade entries with HTF setups** (`ICT-2017-DAYTRADE-HTF`)

- **Precondition:** the *previous* trading day must already have **respected a daily
  discount array** (for longs) or a **daily premium array** (for shorts) — "it has to
  have happened the day before the trade day" (15:21).
- Reference price is the **0 GMT open** — the true-day reset (05:47–06:04).
- **Entry:** at the 0 GMT open, or a limit **10–20 pips** beyond it in the protraction
  direction (below for buys, above for sells) to catch the Judas swing (16:01, 19:10–20:11).
- **Stop:** the **five-day ADR**, subtracted from (longs) or added to (shorts) the entry
  (14:00–14:09).
- **Splitting:** half the intended size at market at 0 GMT, half on the 10–20-pip limit,
  so a runaway open still fills something (18:03–18:51).
- **Target:** the opposing higher-timeframe PD array, held past the day. A 90–100-pip
  stop "is relatively insignificant because you're looking for moves that are going to be
  paying several hundred pips" (13:37–13:51).

## Formula / Math

```
ADR5      := mean(range(D-1 .. D-5))            # 5-day average daily range
target    := 0.65 * ADR5 .. 0.70 * ADR5         # intended capture

# --- day-trade direction filter ---
sunday_open := open(first candle of the trading week)   # Monday open if no Sunday candle

bearish_day_trades := weekly_bias == bearish
                      AND price < sunday_open
                      AND NOT reached(contrary_HTF_discount_PD_array)

bullish_day_trades := weekly_bias == bullish
                      AND price > sunday_open
                      AND NOT reached(contrary_HTF_premium_PD_array)

intraweek_reversal := (day == Thursday) AND price crosses sunday_open against weekly_bias

# --- stand-aside gates ---
no_trade := day in {FOMC, NFP, Sunday}
skip_NY  := london_range >= 0.80 * ADR5

# --- HTF integration (0 GMT entries) ---
precondition_long  := previous_day respected daily_discount_PD_array
entry_long         := open_0GMT   OR  limit(open_0GMT - 10..20 pips)
stop_long          := entry_long - ADR5
target_long        := opposing HTF premium PD array          # held beyond the day
# shorts mirror exactly
```

## Machine-Readable

```json
{
  "id": "ict-day-trading-model",
  "category": "31-models",
  "aliases": ["ict-day-trading", "daytrading-model", "daily-range-model"],
  "criteria": [
    {"id": "c1", "expr": "target_capture in [0.65, 0.70] * daily_range"},
    {"id": "c2", "expr": "expected_range == mean(range(last_5_days))"},
    {"id": "c3", "expr": "setups_per_day <= 2 (average)"},
    {"id": "c4", "expr": "direction from daily_PD_arrays over lookback in {20,40,60} days + weekly candle forecast"},
    {"id": "c5", "expr": "sunday_open projected on H1 through Thursday acts as the daily side filter"},
    {"id": "c6", "expr": "filter_overridden_when contrary_HTF_PD_array is reached"},
    {"id": "c7", "expr": "no_trade if day in {FOMC, NFP, Sunday}"},
    {"id": "c8", "expr": "skip_NY if london_range >= 0.80 * ADR5"},
    {"id": "c9", "expr": "tuesday_london makes week_low ~0.70 probability in bullish weeks (mirrored in bearish)"},
    {"id": "c10", "expr": "HTF_integration: prev_day respected daily discount/premium array => entry at open_0GMT (or +/- 10-20 pips), stop = ADR5"}
  ],
  "timeframes": ["M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["bread-and-butter-setup", "power-of-three", "true-day-open", "central-bank-dealers-range", "filling-the-numbers", "london-open-killzone", "daily-bias", "judas-swing", "nfp-protocol"],
  "sources": ["ICT-2017-DAYTRADE-ESSENTIALS", "ICT-2017-DAYTRADE-HTF"]
}
```

## Visual Pattern

```
  WEEK FRAME — Sunday open projected on the H1 chart through Thursday
  (bearish weekly bias example)

   price
     │   ····························································  <- Sunday open
     │  ╱╲    (Judas above the open early in the week)
     │ ╱  ╲___
     │        ╲__      sell London ──► continue NY, every day
     │           ╲__        while price stays BELOW the line
     │              ╲__
     │                 ╲__●  <- contrary daily DISCOUNT array reached:
     │                        filter is now void, expect intra-week reversal
     └──────────────────────────────────────────────────────────────► Mon..Fri

  DAY FRAME — the two windows that matter
     01:00 ─────── 05:00      05:00 ── 07:00      08:20 ──── 12:00     15:00
     │ London killzone │      │ London lunch │    │  New York AM │      │ bond
     │ (hotspot 02-04) │      │ retrace/cons │    │              │      │ close
     └── setup 1 ──────┘      └─────────────┘     └── setup 2 ───┘
```

## Timeframes

Analysis on **daily and weekly** (PD arrays, ADR, weekly candle forecast); the Sunday-open
filter is drawn on the **hourly**; execution on H1 and below. The HTF-integration variant
uses the same daily inputs but holds the position past the session.

## Examples

All three are GBPUSD daily-chart case studies from `ICT-2017-DAYTRADE-ESSENTIALS`.

**Example 1 — filter and matrix agree (35:01–37:45):**
- Setup: price traded into a **daily rejection block** (premium array) and above the
  Sunday open; an old low sat below as the discount array.
- Trigger: price turned down through the Sunday open on Monday — sells every day.
- Outcome: downside objectives given as 1.2420 / 1.2375 / 1.2310; the week's low printed
  **1.2365**, ten pips below the old-low discount array. 1.2310 was never reached.

**Example 2 — the filter alone would have been wrong (37:48–41:31):**
- Setup: price below the Sunday open, so the mechanical read said "sell".
- Trigger: price had traded down into a **daily discount bullish order block inside a
  fair value gap** — a contrary HTF array. "We **cannot be a seller** in this particular
  setup" (39:11).
- Outcome: Wednesday formed the low of the week; the filter was discarded and the weekly
  profile re-framed around a Wednesday low.

**Example 3 — bullish mirror, Friday capped (41:31–44:24):**
- Setup: Monday traded down into a **bullish order block** discount array; Tuesday closed
  back **above** the Sunday open.
- Trigger: from Tuesday on, buy the London decline, continue in New York around the
  08:20 CME open.
- Outcome: the weekly range was **capped by Thursday's New York session** and Friday was
  quiet — the stated Friday profile.

## Common Mistakes

- **Trading the Sunday-open filter mechanically.** ICT names this directly: "it's simply
  … you don't look at the opening price on Sunday and therefore it's above or below so
  I'm going to just do that — no, you have to incorporate the PD arrays" (45:22).
  Example 2 exists to break exactly this habit.
- **Taking many trades because it is "day trading".** Two setups a day on average; more
  trades is not more edge (05:17–06:39).
- **Trading every day.** FOMC and NFP are stand-aside days, and not all days offer a setup.
- **Trading New York after London already ran.** If London printed ~80 % of the five-day
  ADR, New York is chop or a reversal (14:03).
- **Confusing this with scalping.** ICT separates the two explicitly — scalping is the
  following month's content (01:33, 05:34).
- **Applying the 0 GMT entry without the prior-day precondition.** The HTF-integration
  entry is only valid after the previous day *respected* the relevant daily array; without
  it the ADR-wide stop is unprotected (`ICT-2017-DAYTRADE-HTF`, 15:21).
- **Reading "65–70 %" as a requirement.** Capturing 30–40 pips of a 100-pip day is
  explicitly called successful, not a miss (05:55–06:29).

## Related Concepts

- [bread-and-butter-setup](bread-and-butter-setup.md) — the later, session-sequence phrasing of the same daily rhythm.
- [power-of-three](../12-power-of-three/power-of-three.md) — the open-rally/decline-close shape the 0 GMT entry exploits.
- [true-day-open](../22-quarterly-theory/true-day-open.md) — the daily reset the HTF-integration entry is priced from.
- [filling-the-numbers](../04-time-cycles/filling-the-numbers.md) — where inside the day's range the levels sit.
- [central-bank-dealers-range](../15-sessions/central-bank-dealers-range.md) — ICT's stated way to gauge how far the protraction runs.
- [london-open-killzone](../10-killzones/london-open-killzone.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md) — the two execution windows.
- [judas-swing](../13-judas-swing/judas-swing.md) — the protraction the 10–20-pip limit is placed to catch.
- [daily-bias](../25-htf-bias/daily-bias.md), [weekly-bias](../25-htf-bias/weekly-bias.md) — the directional inputs.
- [nfp-protocol](../30-news-driven/nfp-protocol.md), [news-blackout-rules](../30-news-driven/news-blackout-rules.md) — the stand-aside days.
- [timeframe-selection](../25-htf-bias/timeframe-selection.md) — where day trading sits among the trading styles.

## Citations

- `ICT-2017-DAYTRADE-ESSENTIALS` (00:00–00:22) "this is April 2017 content for the ICT mentorship… we'll be teaching my day trading model, this is lesson one"; (01:18–01:33) "just because the name… is day trading it does not mean or equate to every day trading… generally there are two setups per trading day on average"; (01:52–02:02) "our expectation is to capitalize on at least 65 to 70 percent of the daily range"; (02:14–02:30) five-day average daily range; (06:47–06:56) "FOMC days and non-farm payroll days keep us on the sidelines and they are basically a no setup day"; (07:37–08:16) monthly/weekly/daily PD arrays over the last 20, 40 and 60 trading days, daily primary for day trades; (10:39–10:46) "you have to be flexible with time and demand specifics in price"; (11:44–12:38) London killzone 01:00–05:00 NY, hotspot 02:00–04:00, four-hour envelope to absorb DST; (13:55–14:31) skip New York if London puts in 80 % of the average daily range; (15:36–16:24) 14:00 hour and the 15:00 bond close; (16:31–17:17) Asia open 20:00; (17:20–18:58) London lunch 05:00–07:00; (18:47–22:52) day-of-week profiles including "Tuesday has a 70 [%] likelihood of creating the low of the week in London"; (23:09–24:06) Sunday opening price drawn on the hourly through Thursday; (24:06–25:35) Thursday cross-back = intra-week reversal; (26:45–27:40) sell every day below the Sunday open until a contrary HTF PD array; (28:04–29:07) bullish mirror; (35:01–44:24) the three GBPUSD case studies; (45:22–45:47) "you don't look at the opening price on Sunday and therefore it's above or below so I'm going to just do that — no, you have to incorporate the PD arrays".
- `ICT-2017-DAYTRADE-HTF` (00:00–00:19) "lesson 8, the final of April 2017 content… integrating day trades with higher time frame trade entries"; (00:49–01:07) the London killzone is not required; (05:47–06:04) 0 GMT as the daily reset / true day open; (08:54–09:38) the previous day must have respected a daily discount or premium array; (13:12–13:51) a 90–100-pip stop is insignificant against several-hundred-pip HTF targets; (14:00–14:09) stop = five-day ADR from the 0 GMT open; (16:01–16:40) sell at 0 GMT or 0 GMT +20 pips; (18:03–18:51) split the position half at market, half on the limit; (19:10–20:39) 10–20-pip limits either side and why the ADR stop is rarely reached; (22:06–22:26) 5-period ATR on the daily as a substitute for the ICT ADR indicator.
