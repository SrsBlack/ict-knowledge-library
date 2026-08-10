# Projected Range & Objectives

**Category:** 31-models
**Aliases:** projected range, daily profiles, index day profiles, session projection, range projection
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-INDEX-PROJECTED-RANGE
**Tags:** models, index-futures, daily-profile, am-session, pm-session, ny-lunch, taxonomy

## Definition

Projected range is ICT's **taxonomy of how an index-futures day fulfils its range**, split
by AM session, lunch hour and PM session. Before the day starts, the trader selects the
profile the day is most likely to follow from higher-timeframe context, and that profile
supplies the **objectives** — which stop pool or PD array each session is reaching for.

It is a **classification, not a setup**: "these are my general classifications, or how I
interpret how the daily range should fulfil for … indices"
(`ICT-2017-INDEX-PROJECTED-RANGE`, 01:07). The selector across every profile is the same
one question: **has price already traded into the opposing four-hour-or-higher PD array?**

⚠ **Count discrepancy.** ICT states the number twice — "these **eight** ways of projecting
the range" (03:05) and "there's only **eight** projected ranges that I use for the S&P"
(16:38) — but this lesson enumerates and diagrams **six**. The six below are what is
actually taught here; the remaining two are not identified in this source.

## Formal Criteria

**The six profiles taught**

| # | Profile | HTF order flow | AM | Lunch | PM |
|---|---|---|---|---|---|
| 1 | **Two-session up close** | bullish on D and H4 | returns to a discount array, then rallies | consolidates, shallow retracements | runs lunch lows for sell stops **or** drops into a discount FVG, then rallies into the close |
| 2 | **Two-session down close** | bearish on D and H4 | returns to a premium array, then declines | consolidates, shallow retracements | runs lunch highs for buy stops **or** rises into a premium FVG, then declines into the close |
| 3 | **AM rally, PM reversal** | bullish, but **beneath** an H4/D premium array | returns to a discount array, then rallies **until it hits the HTF premium array** | consolidates, shallow retracements | runs lunch highs or the intraday high, then reverses into the close |
| 4 | **AM decline, PM reversal** | bearish, but **above** an H4/D discount array | returns to a premium array, then declines | consolidates, shallow retracements | runs lunch lows or the intraday low, then reverses into the close |
| 5 | **Consolidation, AM rally, PM decline** | **neutral / unclear** | returns to a discount array then rallies, or expands up from equilibrium after the opening range to run London buy stops | consolidates, shallow retracements | runs lunch highs then reaches for intraday sell stops, **or** runs the intraday high then reaches for intraday/London sell stops |
| 6 | **Consolidation, AM decline, PM rally** | **neutral / unclear** | returns to a premium array then declines, or expands down from equilibrium to run London sell stops | consolidates, shallow retracements | runs lunch lows then reaches for the day's buy stops, **or** runs the intraday low then reaches for intraday/London buy stops |

**Selection rules**

- **Trending profiles (1, 2) require unfinished business:** they hold "as long as the four-hour
  and/or daily discount arrays have not been traded to" (05:37). Once price reaches the
  opposing H4/D/W array, stop expecting the trending profile.
- **Reversal profiles (3, 4) require the opposing HTF array to be near.** The reversal is
  *caused* by price reaching an H4-or-higher premium (profile 3) or discount (profile 4).
- **Consolidation profiles (5, 6) require an absent driver:** neutral or unreadable order
  flow **and** no medium- or high-impact news expected in the 10:00 hour or the afternoon
  (11:11–11:46). Explicitly **not** to be expected when directional bias is strong (16:14).
- **The PM continuation filter (the load-bearing rule).** After an AM reversal, whether the
  PM resumes the AM direction depends on the *rank* of the array the AM turned at:
  - AM turned at an **H4, daily, weekly or monthly** array → price can return to that array
    in the PM, **recapitalise** it and resume (07:44–08:04, 10:12–10:41).
  - AM turned at only a **60-minute or 15-minute** array → "expect it to trade through it and
    go lower" (08:50). The lower-timeframe array will not hold a second time.
- **Which high or low the PM runs** is decided the same way: if the AM already hit an HTF
  premium array, that level has been defended and the PM will likely only take the **lunch**
  extreme; if it did not, the PM can run the **intraday** extreme (13:19–13:54).

**Invariants**

- **The lunch hour is the same across all six** — consolidation with shallow retracements.
  The only exception is the trending profiles (1, 2), where a strong catalyst can carry
  price straight through lunch with little or no consolidation (02:02–02:50, 16:54–17:16).
- A PM session may simply **consolidate into the close** instead of completing its leg
  (14:01, 15:39).
- Profile 3's PM high need not exceed the AM high — a run above only the lunch high produces
  a **failure swing** against the AM high (07:23–07:44).
- **Intraday indices hunt liquidity.** "On an intraday basis you have to understand it's all
  about liquidity and where the stops are — it's a trader's market" (17:31).
- Consolidation days are **not** seek-and-destroy; ICT reserves that label for NFP in the
  S&P (16:20–16:36).

## Formula / Math

```
# --- profile selection ---
opposing_array_reached := price has traded into the opposing PD array on H4 or higher

profile :=
  if   order_flow(D, H4) is bullish  and not opposing_array_reached  -> TWO_SESSION_UP
  elif order_flow(D, H4) is bearish  and not opposing_array_reached  -> TWO_SESSION_DOWN
  elif order_flow is bullish and HTF_premium_array is near           -> AM_RALLY_PM_REVERSAL
  elif order_flow is bearish and HTF_discount_array is near          -> AM_DECLINE_PM_REVERSAL
  elif order_flow is neutral and no_medium_or_high_impact_news       -> CONSOLIDATION_*
                                                                       # direction from the AM leg

# --- PM continuation filter (applies to profiles 3 and 4) ---
am_turn_tf := timeframe of the PD array the AM session reversed at

pm_resumes_am_direction := am_turn_tf in {H4, D, W, M}     # array can be recapitalised
pm_trades_through       := am_turn_tf in {M15, H1}         # LTF array will not hold twice

# --- which extreme the PM runs ---
pm_target := am_session_hit_HTF_array ? lunch_extreme : intraday_extreme

# --- invariant ---
lunch := consolidation with shallow retracements
         EXCEPT profile in {TWO_SESSION_UP, TWO_SESSION_DOWN} with a strong catalyst
```

## Machine-Readable

```json
{
  "id": "projected-range-objectives",
  "category": "31-models",
  "aliases": ["projected-range", "daily-profiles", "index-day-profiles"],
  "criteria": [
    {"id": "c1", "expr": "profiles_taught_in_source == 6 (ICT states 8; two are not enumerated here)"},
    {"id": "c2", "expr": "trending_profile valid only while opposing H4_or_higher array not yet traded to"},
    {"id": "c3", "expr": "reversal_profile requires near HTF premium (bullish) or discount (bearish) array"},
    {"id": "c4", "expr": "consolidation_profile requires neutral order_flow AND no medium/high impact news"},
    {"id": "c5", "expr": "pm_resumes_am_direction iff am_reversal_array_tf >= H4"},
    {"id": "c6", "expr": "am_reversal_array_tf in {M15,H1} => pm trades through it"},
    {"id": "c7", "expr": "pm_target := am_hit_HTF_array ? lunch_extreme : intraday_extreme"},
    {"id": "c8", "expr": "lunch == shallow_consolidation for all profiles except trending days with a strong catalyst"},
    {"id": "c9", "expr": "consolidation_day != seek_and_destroy (reserved for NFP in S&P)"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["ny-am-session", "ny-lunch", "ny-pm-session", "ny-pm-reversal", "ny-am-open-range-model", "pd-array-hierarchy", "institutional-order-flow", "bread-and-butter-setup", "ict-day-trading-model"],
  "sources": ["ICT-2017-INDEX-PROJECTED-RANGE"]
}
```

## Visual Pattern

```
   AM          LUNCH        PM
  ─────────────────────────────────────────────────────────────────
1 TWO-SESSION UP CLOSE        ╱‾            bullish D + H4,
     ╲__╱‾‾‾    ▪▪▪▪       ╱‾               opposing array NOT yet hit
   (discount)  (shallow)  (runs lunch lows -> rallies into close)

2 TWO-SESSION DOWN CLOSE   — mirror of 1

3 AM RALLY, PM REVERSAL       ●  <- HTF PREMIUM array hit here
     ╲__╱‾‾‾‾‾╲  ▪▪▪▪    ╱‾╲__
   (discount)  (shallow)  (runs lunch/intraday high, reverses)

4 AM DECLINE, PM REVERSAL  — mirror of 3

5 CONSOLIDATION, AM RALLY, PM DECLINE     order flow NEUTRAL,
     ╱‾‾‾╲     ▪▪▪▪      ╱╲___             no news driver
   (runs London buy stops) (runs lunch high -> reaches for sell stops)

6 CONSOLIDATION, AM DECLINE, PM RALLY  — mirror of 5

  ─────────────────────────────────────────────────────────────────
  THE FILTER THAT DECIDES PROFILE 3/4's PM LEG:

     AM turned at an H4/D/W/M array   ->  PM can return, recapitalise, RESUME
     AM turned at an M15/H1 array     ->  PM trades THROUGH it
```

## Timeframes

Intraday execution (M15–H1) inside a **daily** profile; the selector arrays are read on
**H4 and higher**. Taught for **index futures** (S&P / e-mini) specifically.

## Examples

**Example 1 — a live consolidation day (`ICT-2017-INDEX-PROJECTED-RANGE`, 12:06–12:43):**
- Instrument / date: S&P ("Spooz"), **22 June 2017** — the day of the recording.
- Profile selected: **consolidation, AM rally, PM decline** (profile 5).
- Action: sold short at **2437**, looking for price to trade down into a discount array or
  reach sell stops below the market.
- Stated as "the actual projected range I used for a live trade example".

**Example 2 — profile-3 selection logic (05:51–08:04):**
- Setup: institutional order flow bullish on daily and H4, but an H4 premium array sits
  just above current price.
- Read: the AM rallies **into** that array and reverses there.
- Continuation test: because the AM's *launch* array was itself H4-or-higher, a PM return to
  it can recapitalise and resume higher; had the AM launched from a 15-minute or hourly
  array, price would be expected to trade straight through it.

## Common Mistakes

- **Expecting a consolidation profile on a trending day.** "When there's a strong directional
  bias… do not look for this particular scenario" (16:14).
- **Calling a consolidation day seek-and-destroy.** ICT separates the two; seek-and-destroy
  is reserved for NFP in the S&P.
- **Assuming lunch always consolidates.** On trending days with a strong catalyst price can
  run straight through it.
- **Requiring the PM to exceed the AM extreme.** Running only the lunch extreme is a valid
  completion and produces a failure swing.
- **Ignoring the timeframe rank of the AM's reversal array.** This is the rule that decides
  whether the PM resumes or reverses, and it is the one most easily skipped.
- **Treating the profile as an entry model.** It supplies the day's *objectives*; entries
  still come from the ordinary toolkit.
- **Applying it to FX unchanged.** It is taught for index futures, whose intraday character
  ICT describes as predominantly stop-hunting.

## Related Concepts

- [ny-am-session](../15-sessions/ny-am-session.md), [ny-lunch](../15-sessions/ny-lunch.md), [ny-pm-session](../15-sessions/ny-pm-session.md) — the three blocks every profile is built from.
- [ny-pm-reversal](ny-pm-reversal.md) — the 2022 named form of profiles 3 and 4; this page is the parent taxonomy those sit inside.
- [ny-am-open-range-model](ny-am-open-range-model.md) — the opening-range expansion referenced in profiles 5 and 6.
- [pd-array-hierarchy](../05-pd-arrays/pd-array-hierarchy.md) — supplies the timeframe rank the PM continuation filter depends on.
- [institutional-order-flow](../03-order-flow/institutional-order-flow.md) — the input that selects trending vs neutral.
- [ict-day-trading-model](ict-day-trading-model.md) — the FX-side equivalent of forecasting the day before it starts.
- [bread-and-butter-setup](bread-and-butter-setup.md) — the session-sequence framing of the same day.

## Citations

- `ICT-2017-INDEX-PROJECTED-RANGE` (00:14–00:30) "June 2017 ICT mentorship, index trading concepts, lesson [4], projected range and objectives"; (01:07–01:22) "these are my general classifications or how I interpret how the daily range should fulfil for … indices"; (01:23–02:00) two-session up close; (02:02–02:50) the lunch-hour exception on strong trending days; (03:05) "these eight ways of projecting the range"; (03:12–04:39) two-session down close; (04:39–05:44) trending profiles hold only until an opposing H4/daily/weekly array is traded to; (05:51–07:08) AM rally, PM reversal; (07:23–07:44) the PM high may be relative only to the lunch hour, creating a failure swing; (07:44–09:02) the PM continuation filter — H4/daily/weekly arrays can be recapitalised, "if it's not a four-hour or a daily or higher than that discount array, expect it to trade through it and go lower"; (09:04–11:08) AM decline, PM reversal and its mirror filter; (11:09–11:46) consolidation profiles require neutral order flow and "a vacuum of any real market drivers"; (12:06–12:43) the live 22 June 2017 S&P short at 2437; (13:14–13:54) which extreme the PM runs, decided by whether the AM hit an HTF premium array; (14:01, 15:39) the PM may simply consolidate into the close; (14:13–15:39) consolidation, AM decline, PM rally; (16:14–16:36) do not expect consolidation profiles when directional bias is strong; consolidation is not seek-and-destroy, which is reserved for NFP; (16:38) "there's only eight projected ranges that I use for the S&P"; (16:54–17:16) the lunch hour is identical across profiles except on trending days; (17:22–17:40) "on an intraday basis you have to understand it's all about liquidity and where the stops are — it's a trader's market".
