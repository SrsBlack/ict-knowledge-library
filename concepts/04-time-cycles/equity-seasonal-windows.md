# Equity Seasonal Windows

**Category:** 04-time-cycles
**Aliases:** stock seasonals, equity seasonality, Dow monthly seasonals, buy and sell programs for stocks, low magnitude period
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STOCK-SEASONALS, ICT-2017-STOCK-OPTIONS
**Tags:** time-cycles, seasonality, equities, indices, dow, buy-program, sell-program

## Definition

Equity seasonal windows are ICT's **calendar map of the US stock market**: three divisions
of the year by magnitude and direction, refined into a **month-by-month tendency table** for
the Dow Jones Industrial Average. Its purpose is selecting *when* to be an active equity
trader, not what to buy — "there's times you want to be in stocks and times you want to be
out of stocks" (`ICT-2017-STOCK-SEASONALS`, 18:39).

It is the equity-specific instance of [seasonal-tendency](seasonal-tendency.md), which
covers the FX and commodity form. The underlying data is credited to **Steve Moore / Moore
Research** and read as 20-year, 15-year and 5-year averages (00:38, 06:21).

## Formal Criteria

**The three divisions of the year** (02:00–04:56)

| Division | Window | Character |
|---|---|---|
| 1 | **First half of the year** | **high magnitude** — volatile but directionally driven, generally bullish |
| 2 | **May → October** | **low magnitude** — range-bound, far less directionally driven |
| 3 | **Last quarter** | **bullish**, and the strongest in magnitude and velocity |

- The **low-magnitude period is the one ICT calls most critical to understand**. It does not
  forbid trading — short-term biases still occur — but the instruction is to **reduce
  leverage, reduce option activity and be less aggressive**, and to expect a **range-bound
  consolidation environment overall** (03:52–04:39).
- Cause given for the strong fourth quarter: the calendar is "laden with holidays and
  year-end spending has to come in" (03:03); the summer lull is attributed to seasonal
  spending shifting to vacations.
- **Focus windows for active trading: October → end of year, and February → May** (04:49).

**Buy and sell programs** (`ICT-2017-STOCK-OPTIONS`, 00:12–00:54)

- **February → May** — buy program.
- **May → second half of September** — sell program.
- **Late September / early October → end of year** — buy program.

**Month-by-month tendency, Dow Jones Industrial** (05:03–06:21)

| Month | Tendency |
|---|---|
| January | bearish |
| February | bullish |
| March | consolidation |
| April | bullish |
| May | bearish |
| June | consolidation, ending with a bearish tone |
| July | bullish into the mid-year high |
| August | consolidation |
| September | split — first half bullish, second half bearish |
| October | usually makes the final quarter's low (can occur in late September instead), then trades aggressively higher |
| November | bullish |
| December | bullish — "Santa Claus rally" |

- **Lowest-probability months: March, June, August** — "typically going to be not fruitful in
  terms of high probability conditions" (08:10–08:23).
- **Bearish months amplify in bear markets.** January, May and the second half of September
  are bearish even inside secular bull markets; when the broad tide is also down they "could
  spell aggressive selling… really supercharged short selling months" (09:44–10:05).

**Instrument choice**

- The **Dow Jones Industrial** (30 blue chips) is used for simplicity; ICT states the
  **S&P 500** is "a more accurate depiction of what the stock market is doing" and that the
  two seasonals mirror each other closely (00:57–01:42).

**Confirmation at the seasonal turn**

- Seasonal windows are confirmed with **index SMT divergence** across the NASDAQ, e-mini S&P
  and Dow — an average failing to make the matching low or high signals smart-money
  accumulation or distribution at the seasonal date (11:27–15:29).

**Standing caveat**

- "There's always going to be some aberration where it just simply doesn't fit the seasonal,
  and that's okay" (08:36–08:57). Aberrations are attributed to the prevailing market
  environment, not to a broken tendency. ICT applies this to his own recording year, calling
  2017 "an unorthodox stock market" making higher highs while leadership stopped confirming
  (15:43–16:18).

## Formula / Math

```
# --- divisions ---
division(month) :=
    Jan..Apr           -> HIGH_MAGNITUDE, generally bullish
    May..Oct           -> LOW_MAGNITUDE, range-bound      # reduce leverage/activity
    Oct..Dec           -> BULLISH, highest magnitude and velocity

active_window := month in (Feb..May) or (Oct..Dec)

# --- programs ---
program(month) :=
    Feb..May                  -> BUY
    May..mid_Sep              -> SELL
    late_Sep/Oct..Dec         -> BUY

# --- month table (Dow Jones Industrial) ---
tendency := { Jan: bearish, Feb: bullish, Mar: consolidation, Apr: bullish,
              May: bearish, Jun: consolidation_then_bearish, Jul: bullish_into_midyear_high,
              Aug: consolidation, Sep: bullish_H1 / bearish_H2,
              Oct: quarter_low_then_higher, Nov: bullish, Dec: bullish_santa_rally }

low_probability_months := {Mar, Jun, Aug}
amplified_short_months := {Jan, May, Sep_H2}   # when the broad market is also bearish

# --- confirmation at a seasonal date ---
turn_confirmed := index_SMT_divergence(NASDAQ, ES, YM) at the seasonal window
```

## Machine-Readable

```json
{
  "id": "equity-seasonal-windows",
  "category": "04-time-cycles",
  "aliases": ["stock-seasonals", "equity-seasonality", "low-magnitude-period"],
  "criteria": [
    {"id": "c1", "expr": "year splits into 3 divisions: H1 high-magnitude bullish, May..Oct low-magnitude range-bound, Q4 bullish highest-velocity"},
    {"id": "c2", "expr": "active_windows == {Feb..May, Oct..Dec}"},
    {"id": "c3", "expr": "low_magnitude_period => reduce leverage and activity, expect consolidation"},
    {"id": "c4", "expr": "buy_programs == {Feb..May, late_Sep/Oct..year_end}; sell_program == May..mid_Sep"},
    {"id": "c5", "expr": "low_probability_months == {March, June, August}"},
    {"id": "c6", "expr": "bearish months {Jan, May, Sep_H2} amplify in bear markets"},
    {"id": "c7", "expr": "instrument == DJIA for simplicity; SP500 stated as more accurate"},
    {"id": "c8", "expr": "seasonal turns confirmed by index_SMT across NASDAQ/ES/YM"},
    {"id": "c9", "expr": "aberrations expected; tendency is not a guarantee"},
    {"id": "c10", "expr": "supplies_entry == false"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["seasonal-tendency", "index-smt", "smt-divergence", "mega-trade", "explosive-market-selection", "quarterly-shift-theory"],
  "sources": ["ICT-2017-STOCK-SEASONALS", "ICT-2017-STOCK-OPTIONS"]
}
```

## Visual Pattern

```
   THE THREE DIVISIONS

   Jan   Feb   Mar   Apr   May   Jun   Jul   Aug   Sep   Oct   Nov   Dec
   ──────────────────────────────────────────────────────────────────────
   ▼     ▲     ═     ▲     ▼     ═▼    ▲     ═     ▲|▼   ▼▲    ▲     ▲
   │           │           │                       │     │           │
   └─ HIGH MAGNITUDE ──────┤                       │     └─ Q4 BULLISH ┘
      directional, bullish │                       │        strongest velocity
                           └── LOW MAGNITUDE ──────┘
                               May → October
                               range-bound; cut leverage

   ACTIVE WINDOWS:   ████ Feb–May ████            ████ Oct–year end ████

   ▲ bullish   ▼ bearish   ═ consolidation   ▲|▼ split month (Sep)

   LOW-PROBABILITY MONTHS: March · June · August
   October usually prints the final quarter's LOW, then runs.
```

## Timeframes

Daily, weekly and monthly. A calendar bias filter — it carries no entry, stop or target.

## Examples

All from `ICT-2017-STOCK-SEASONALS`, each pairing a month's tendency with index SMT
confirmation across the NASDAQ, e-mini S&P and Dow futures.

**Example 1 — February, a bullish month (11:00–12:22):**
- 2nd–3rd February: the **NASDAQ made an equal low while the S&P and Dow made higher lows** —
  an unwillingness to go lower.
- Read: index SMT showing smart-money accumulation at the start of a seasonally bullish month.
- Repeat on the 6th–8th trading day, followed by another move higher across the averages.

**Example 2 — March, a consolidation month (12:28–13:44):**
- The month chopped, with a bearish lean from the second into the third week and a rally into
  the close.
- Divergence at the highs: NASDAQ higher highs against lower highs in the S&P and Dow →
  the sell-off followed.
- Point made: "while it's consolidation, it doesn't mean there isn't any opportunities."

**Example 3 — May, a bearish month (14:42–15:29):**
- The e-mini S&P made a **slightly higher high** and the NASDAQ made a higher high, while the
  **Dow failed** to — divergence.
- Sell-off into roughly the third week, then a small flurry higher into the close, matching
  the seasonal path's own intra-month low.

## Common Mistakes

- **Trading the low-magnitude period at full size.** May–October is the division ICT singles
  out as most important, and the instruction is to reduce leverage and activity — not to
  stop, but not to press.
- **Treating the month table as a forecast.** It is a tendency built from 20-, 15- and
  5-year averages; aberrations are expected and explicitly tolerated.
- **Confusing it with [seasonal-tendency](seasonal-tendency.md).** That page is the general
  concept, with the *ideal* form defined for FX as maximum opposition against the dollar
  index seasonal. This page is the equity calendar.
- **Taking the September tendency as one direction.** September is split — bullish first
  half, bearish second half — and its second half is one of the amplified short windows.
- **Assuming October is bullish throughout.** October typically prints the **low** of the
  final quarter first, sometimes as early as late September.
- **Using the Dow as the accurate instrument.** ICT uses it for simplicity and states the
  S&P 500 is the better depiction.

## Related Concepts

- [seasonal-tendency](seasonal-tendency.md) — the parent concept; FX and commodity form, including the *ideal* seasonal definition.
- [index-smt](../16-smt-divergence/index-smt.md), [smt-divergence](../16-smt-divergence/smt-divergence.md) — how a seasonal turn is confirmed.
- [quarterly-shift-theory](quarterly-shift-theory.md) — the three-to-four-month cadence underneath the divisions.
- [mega-trade](../31-models/mega-trade.md) — the six-to-nine-month equity move these windows bracket.
- [explosive-market-selection](../31-models/explosive-market-selection.md) — where seasonal alignment appears as hallmark 5.

## Citations

- `ICT-2017-STOCK-SEASONALS` (00:09–00:25) "we're in the final week of **June 2017** ICT mentorship content… ICT stock trading, lesson one, seasonals and monthly swings"; (00:38–00:43) the seasonal data credited to Steve Moore / Moore Research; (00:57–01:42) the Dow's 30 blue chips used for simplicity, with the S&P 500 stated as "a more accurate depiction of what the stock market is doing"; (02:00–03:26) the first-half high-magnitude division and the bullish final quarter "laden with holidays and year-end spending"; (03:27–04:39) "the last and most critical one you need to understand is this portion in the middle… **low magnitude period, and it begins in May and it ends in October**", with the instruction to use less leverage and less activity and to expect range-bound consolidation; (04:43–04:56) "you primarily want to focus on being a trader from October to the end of the year and from February to May"; (05:03–06:21) the month-by-month tendency table through the December "Santa Claus rally"; (06:21–07:21) the 20-, 15- and 5-year averages and what consistency does and does not mean; (08:10–08:23) March, June and August as the low-probability months; (08:28–08:57) "there's always going to be some aberration where it just simply doesn't fit the seasonal, and that's okay"; (09:24–10:05) bearish months as "supercharged short selling months" in bear markets; (11:00–15:29) the February, March, April and May case studies with index SMT across the NASDAQ, e-mini S&P and Dow; (15:43–16:18) 2017 called "an unorthodox stock market" making higher highs while leadership stopped confirming; (18:39) "there's times you want to be in stocks and times you want to be out of stocks".
- `ICT-2017-STOCK-OPTIONS` (00:00) "lesson 5 of the June 2017 ICT mentorship, using options and stocks"; (00:12–00:54) the three programs — "we look for **February to May** for our buy programs… from **May going into the second half of September** for our shorting of stocks… and then around the **last portion of September, beginning of October, till the end of the year** where we are bullish again". ⚠ The remainder of this lecture teaches long-call and long-put option mechanics (strike and expiration selection), which is outside this library's scope and is deliberately not documented here.
