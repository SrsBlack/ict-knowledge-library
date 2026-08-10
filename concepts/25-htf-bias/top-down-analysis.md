# Top-Down Analysis

**Category:** 25-htf-bias
**Aliases:** TDA, top-down, multi-TF analysis, HTF-to-LTF read, the four-tier protocol
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-LONGTERM-TOP-DOWN, ICT-2017-INTERMEDIATE-TOP-DOWN, ICT-2017-TOPDOWN-SHORT-TERM, ICT-2017-INTRADAY-TOP-DOWN, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** top-down, multi-tf, framework, capstone, protocol

## Definition

Top-down analysis is ICT's **prescribed analysis sequence**: start from the highest-relevant timeframe and descend, each tier's output constraining the next. The "down" direction is non-negotiable — "you have to work from the higher timeframe down" (`ICT-2017-TOPDOWN-SHORT-TERM`, 32:03–32:12).

The definitive treatment is the **four-lecture capstone that closes the August-2017 mentorship** — long-term (monthly→weekly), intermediate-term (weekly→daily), short-term (daily→H4) and intraday (H4→M5). It is deliberately a graded series, not four independent lessons: each tier ends by **transposing** its output onto the next chart down, and each tier adds a *different* set of non-price inputs on top of a shared technical spine. ICT frames the whole month as the assembly instruction for the preceding eleven: "you have all this information but you haven't had any idea what to do with it specifically **in an order**" (`ICT-2017-INTERMEDIATE-TOP-DOWN`, 00:28).

## Formal Criteria

**The shared spine — run at every tier, in this order**

1. **Market profile** — consolidating, trending, or retracing (see the decision tree below).
2. **Intermarket analysis** — confirm in positively correlated markets, oppose in negatively correlated ones.
3. **Market structure + SMT** — classify highs and lows as short/intermediate/long-term; compare against USDX or a correlated pair.
4. **PD array matrix** — split the chosen range into premium and discount arrays. "Not every price range will have every possible premium and or discount array — I just note the ones that are obvious" (`ICT-2017-LONGTERM-TOP-DOWN`, 32:42).
5. **Key price levels** — calibrate each array by rounding (see [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md)).
6. **Bias** → **transpose down one tier.**

**Tier 1 — monthly → weekly** (`ICT-2017-LONGTERM-TOP-DOWN`)

Run **once a month**, at the close of the month just ended: "I try to do this level of analysis once a month… you only have a candle forming once a month" (02:01, 12:04). Three inputs precede the spine, in order:

- **Seasonal tendency** for the month about to begin — "it all starts here" (03:16).
- **Quarterly shift** — the anticipated 3-to-4-month direction, read against the **9-to-18-month trend on the monthly chart**. "It has nothing to do with moving averages here. I'm just looking at the actual candles going back 18 candles" (19:16). Trade *with* that trend: "I'm trying to avoid picking the tops or the bottoms of the 9 to 18 month trend" (19:07).
  - **Default when unclear:** "if the 9 to 18 month trend is not clear or it's in consolidation… I will elect to anticipate the direction of the previous **three to four months** direction to **reverse**" (20:16).
- **Interest-rate differentials** — pair a high-rate currency against a low-rate one from the central-bank table.
- Horizon: "I'm trying to forecast the next **three months** movement" (14:47), and half a monthly candle is enough to be profitable (15:34).
- Ordering rationale: "my concepts are primarily **time and price, not price and time**. Time then price" (07:31) — which is why two time studies (seasonal, quarterly) precede any price work.

**Tier 2 — weekly → daily** (`ICT-2017-INTERMEDIATE-TOP-DOWN`)

Tier 1's three inputs are **replaced**, not repeated: "there's a couple things missing here that we saw in the monthly that is not in the weekly portion" (04:38). The weekly-tier inputs are:

- **Relative strength**, run first as the fallback when the monthly did not speak clearly (02:52). Markets "**lead in strength** by failing to make lower lows and **lead in weakness** by failing to make higher highs" (08:23) — both are leadership, long-side and short-side; *leaders vs laggards* is a separate strongest/weakest ranking (09:23). Equities screened via IBD's top 30 industry groups (08:50). See [relative-strength-analysis](../03-order-flow/relative-strength-analysis.md).
- **Commitment of traders** — commercials at a **12-month or 6-month extreme**, also sorted for **2-year and 4-year extremes** (10:28); the recentred zero line is the 12-month high/low split in half (19:05).
- **Market sentiment**, from three independent readings that must agree: faded newspaper headlines, retail forums, and a **Williams %R on the weekly at period 20, 14 or 10** — whichever best overlaps the chart's own past highs and lows. Long at the **80** reading, short at **20** (40:01); ICT settles on **14** as optimal (41:17).
- Then the spine, with institutional order flow folded into step 3: down-close candles support price in a bull, up-close candles break (06:39).

**Tier 3 — daily → H4** (`ICT-2017-TOPDOWN-SHORT-TERM`)

- **Commercial hedging**, 12-month range, falling back to 6 months "if that range is very narrow" (09:39).
- **Open interest**, gated on array location — a **15 %-or-more decline at a HTF discount array is extremely bullish**, a **15 %-or-more increase at a HTF premium array is extremely bearish**, and "in between either of the above conditions… open interest is **not considered** in my analysis" (11:03–11:31).
- **Institutional order flow on the daily** — "the daily order flow is the **most important one to know**" (12:15); without it "you're playing with Russian roulette" (12:49).
- **Weekly profile** — forecast the week's shape from the economic calendar. "The weekly range typically forms **between Tuesday and Thursday**" (13:58). Confidence is stated: **~60 %** once Monday is behind you, **~70 %** once Tuesday is (18:25).
- **Two weekly opening prices** carried across the whole week on the hourly: **Sunday's open** and **Monday 00:00 New York** (19:05–21:27). Bullish → want price below them into a discount array; bearish → above them into a premium array.
- **SMT divergence** — "from daily going into the four hour, because I think that's where the **heart of its effectiveness** exists" (22:04–22:08).
- **Breakers and mitigation blocks**, sought on the daily above every other timeframe; trade between the daily bullish and bearish breaker — "it's the meat in the middle" (22:43).

**Tier 4 — H4 → M5** (`ICT-2017-INTRADAY-TOP-DOWN`)

- **Day of week** — take the HTF direction on **Monday, Tuesday and Wednesday**; if it does not materialise, fall back to Thursday/Friday templates (06:25–06:50).
- **True day** — "the bulk of the daily volume will be between **3 a.m. and 10 a.m. New York time**"; position ahead of that window or in its first half, and after the New York open "lower my expectations and be content with smaller objectives" (07:25–07:44).
- **Killzones** — London open, New York open, London close, Asia. London is where the day's low (bullish) or high (bearish) is sought; a failure there is re-attempted at the New York open. Positions are collapsed in the **10:00–11:00 NY** window (07:47–08:34).
- **Overnight range deviations** — [central-bank-dealers-range](../15-sessions/central-bank-dealers-range.md), [asian-range](../14-asian-range/asian-range.md) and [flout](../15-sessions/flout.md), each projected in standard deviations and each actionable only where it **overlaps a 15-to-60-minute array** on the correct side (08:41–09:53).
- **Intraday profile** — bullish seeks the low of day in London; if H4 has *not* yet reached its opposing array, New York continues; if it *has*, a New York reversal is likely (15:44–16:42).
- **Average daily range** — five-day ADR; if broken, fib the ADR high-to-low for **127 % and 162 % extensions**, which "by themselves they're nothing" and must overlap a 60- or 15-minute array (17:29–18:15).
- **Entry timeframe is the trader's choice**, subject to one test: pick the timeframe **that produces fair value gaps** (05:41). ICT's own preference is H4 → M30/M15, refined to M5 where possible.

**Market profile decision tree** (asked at tiers 1 and 2, verbatim in both)

- *Are we consolidating?* — asked **first**, deliberately: "I don't ask if it's trending first… consolidation is the beginning of the next move" (29:23–29:36). If yes → look for evidence of which side breaks. If no → the trend may be reaching an extreme.
- *Is the market trending?* — if yes, continuation trades only, to avoid top- and bottom-picking: "trend is your friend but not in the end" (30:43).
- *Is the market retracing?* — if yes, use the PD array matrix to find how deep, then take the continuation from there.

## Formula / Math

```
# Four tiers, each: [tier-specific inputs] -> [shared spine] -> bias -> transpose down
TIERS = [ (MN, W,  cadence="monthly", inputs=[seasonal, quarterly_shift, rate_differentials]),
          (W,  D,  cadence="weekly",  inputs=[relative_strength, COT, sentiment]),
          (D,  H4, cadence="daily",   inputs=[COT, open_interest, daily_IOF,
                                              weekly_profile, opening_prices, SMT, breakers]),
          (H4, M5, cadence="daily",   inputs=[day_of_week, true_day, killzones,
                                              CBDR_sd, asian_sd, flout_sd,
                                              intraday_profile, ADR5]) ]

spine(tf, carried):
    profile   := consolidating? -> trending? -> retracing?      # in that order
    confirm   := intermarket(correlated_markets)
    structure := classify_highs_lows(tf) + SMT(USDX or correlated pair)
    matrix    := premium_arrays(tf) + discount_arrays(tf)       # only those present
    levels    := calibrate(matrix)                              # see pd-array-matrix
    return bias(tf)

carried = {}
for (tf, next_tf, cadence, inputs) in TIERS:
    carried = spine(tf, carried) with inputs        # never discarded downward
assert entry_tf == argmin_tf(produces_fair_value_gaps)

# Tier-1 quarterly-shift default
if trend_9_to_18_months is unclear or consolidating:
    expect reversal_of(direction of last 3..4 months)

# Tier-3 open-interest gate
oi_signal := BULLISH if dOI <= -0.15 and price at HTF_discount_array
             BEARISH if dOI >= +0.15 and price at HTF_premium_array
             IGNORED otherwise
```

## Machine-Readable

```json
{
  "id": "top-down-analysis",
  "category": "25-htf-bias",
  "aliases": ["TDA", "top-down", "multi-tf-analysis", "four-tier-protocol"],
  "criteria": [
    {"id": "c1", "expr": "analysis_sequence_starts_at_highest_TF"},
    {"id": "c2", "expr": "each_TF_inherits_higher_TF_constraints"},
    {"id": "c3", "expr": "entry_TF_is_last_step"},
    {"id": "c4", "expr": "four tiers: MN->W (monthly cadence), W->D, D->H4, H4->M5"},
    {"id": "c5", "expr": "tier inputs differ; tier-1 seasonal/quarterly/rates are NOT repeated at tier 2"},
    {"id": "c6", "expr": "shared spine order == [market_profile, intermarket, structure+SMT, pd_array_matrix, key_levels, bias]"},
    {"id": "c7", "expr": "market_profile question order == [consolidating?, trending?, retracing?]"},
    {"id": "c8", "expr": "quarterly_shift read over 9-18 monthly candles; if unclear expect reversal of last 3-4 months"},
    {"id": "c9", "expr": "time_studies precede price_studies ('time then price')"},
    {"id": "c10", "expr": "entry_tf := lowest tf that produces fair value gaps"},
    {"id": "c11", "expr": "weekly_range forms Tuesday..Thursday; profile confidence 0.60 after Mon, 0.70 after Tue"},
    {"id": "c12", "expr": "true_day volume window == 03:00-10:00 America/New_York"}
  ],
  "timeframes": ["M5","M15","M30","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","monthly-bias","weekly-bias","daily-bias","bias-confluence","bias-invalidation","htf-pd-array-hierarchy","pd-array-matrix","flout","ict-core-patterns","timeframe-selection","seasonal-tendency","quarterly-shift-theory","commitment-of-traders","open-interest"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2017-LONGTERM-TOP-DOWN","ICT-2017-INTERMEDIATE-TOP-DOWN","ICT-2017-TOPDOWN-SHORT-TERM","ICT-2017-INTRADAY-TOP-DOWN","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
  THE FOUR-TIER PROTOCOL — each tier's own inputs, then the shared spine, then transpose

  TIER 1  MN -> W    seasonal  |  quarterly shift (9-18 candles)  |  rate differentials
          run once a month, at the close of the month just ended
                  │  ── monthly bias ──────────────────────────────┐
                  ▼                                                │ transposed
  TIER 2  W  -> D    relative strength  |  COT 12/6-mo  |  sentiment (%R 20/14/10)
                  │  ── weekly bias ───────────────────────────────┤
                  ▼                                                │
  TIER 3  D  -> H4   COT  |  open interest (±15% gate)  |  daily IOF
                     weekly profile (Tue-Thu)  |  Sun + Mon-00:00 opens  |  breakers
                  │  ── daily bias ────────────────────────────────┤
                  ▼                                                │
  TIER 4  H4 -> M5   day of week  |  true day 03:00-10:00  |  killzones
                     CBDR / Asian / flout deviations  |  intraday profile  |  ADR5
                  │  ── execution ─────────────────────────────────┘
                  ▼
             the two patterns (see ict-core-patterns)

  THE SPINE, identical at every tier:
     consolidating? ─► trending? ─► retracing?     (profile, in this order)
        └─► intermarket ─► structure + SMT ─► PD array matrix ─► key levels ─► bias
```

## Timeframes

MN → M5, in four hops. Time-of-day analysis is **excluded above the daily** by design: "notice we didn't do a whole lot of detail with analysis with time-of-day type things — it's not required on these timeframes, monthly and weekly" (`ICT-2017-INTERMEDIATE-TOP-DOWN`, 46:44).

## Examples

**Example 1 — AUDUSD, June 2017, tiers 1 and 2 walked end to end (`ICT-2017-LONGTERM-TOP-DOWN` 37:26–52:52, `ICT-2017-INTERMEDIATE-TOP-DOWN` 20:40–45:31):**
- *Seasonal:* the Aussie tends to form a June/July low and rally into August.
- *Quarterly shift:* the prior three months had declined; 18 monthly candles back showed a consolidation, so a reversal was anticipated.
- *Rates:* RBA **1.5 %** against a Fed **1.0 %** pre-14-June — "the yield attraction is better in Australian than it is of the dollar" (42:44).
- *Profile:* consolidation, so the break side had to be inferred from intermarket work.
- *Intermarket / SMT:* DXY made a **higher high** off the December highs while AUDUSD refused a lower low off the December lows — SMT divergence, plus a failed DXY breakout that returned through the range midpoint.
- *Matrix:* only **three** discount arrays existed below — a bullish order block, a rejection block at 72.16, and the old low. No liquidity void, no vacuum gap, no breaker: "you're only left with three choices" (49:22).
- *Key level:* the order block's open at **7380** — already on a zero level, so no rounding needed (50:26).
- *Tier 2:* relative strength showed no crack in correlation; COT commercials bought at the low on the recentred 12-month line; Bloomberg ran "The Australian dollar's outlook darkens" on 15 May and DailyFX called it "directionless" on 30 May while the weekly %R sat at an oversold extreme — sentiment maximally opposed.
- *Outcome:* June and July "deliver very handsome rewards for being a long trader on Aussie dollar" (52:44); the weekly chart refined the monthly order block to a **73.29–73.57** rebalance.

**Example 2 — gold, tier 4 execution, 2017-08-23 (`ICT-2017-INTRADAY-TOP-DOWN`, 51:51–60:00):**
- H4 condition bullish → wait for a discount. Drop to H1, find the buy-side-only gap at **1280–1278**.
- Next discount array below is a swing high at 1275, so the stop goes to **1274**.
- Long **1278**, stop never hit, **1290** reached. See [ict-core-patterns](../31-models/ict-core-patterns.md).

## Common Mistakes

- **Bottom-up analysis.** Reading M5 first and projecting up produces a confirmation-biased read.
- **Repeating tier-1 inputs at tier 2.** Seasonals, quarterly shifts and rate differentials belong to the monthly tier only; the weekly tier substitutes relative strength, COT and sentiment. ICT flags the substitution explicitly (`ICT-2017-INTERMEDIATE-TOP-DOWN`, 04:55).
- **Asking "is it trending?" first.** The profile tree opens with consolidation on purpose.
- **Expecting every PD array to be present.** Most ranges hold only two or three. "People make this a lot harder than it has to be" (`ICT-2017-LONGTERM-TOP-DOWN`, 49:22).
- **Running the monthly tier more often than monthly.** One candle a month; one analysis a month.
- **Treating a bias as a licence to trade daily.** "Just because we're bullish doesn't mean we're buying every day" (`ICT-2017-TOPDOWN-SHORT-TERM`, 26:02) — the array and the time of day still have to arrive.
- **Forcing a single entry timeframe.** The correct one is whichever shows fair value gaps for that instrument; H1 can be muddy where M15 is clean.
- **Expecting the protocol to be mechanical.** "There's too many variables. You have to think" (`ICT-2017-INTRADAY-TOP-DOWN`, 38:45).

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [monthly-bias](monthly-bias.md), [weekly-bias](weekly-bias.md), [daily-bias](daily-bias.md) — the four tier outputs.
- [bias-confluence](bias-confluence.md), [bias-invalidation](bias-invalidation.md).
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md) — the spine's step 4 and the calibration rule.
- [htf-pd-array-hierarchy](../05-pd-arrays/htf-pd-array-hierarchy.md).
- [ict-core-patterns](../31-models/ict-core-patterns.md) — what the protocol hands over to at execution.
- [flout](../15-sessions/flout.md) — a tier-4 projection input.
- [timeframe-selection](timeframe-selection.md) — which tier a given trader *operates* on, a separate question.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [commitment-of-traders](../03-order-flow/commitment-of-traders.md), [open-interest](../03-order-flow/open-interest.md) — the non-price tier inputs.

## Citations

- `ICT-2017-LONGTERM-TOP-DOWN` (00:00–00:21) "August 2017, we finally made it… it's the last month of the mentorship's teaching and this is going to be teaching the ICT long-term top-down analysis"; (02:01–02:10) once a month at the month's close; (03:16) "it all starts here — seasonal tendencies"; (05:44) quarterly shifts every three or four months; (06:40–07:12) interest-rate differentials third; (07:31–07:35) "time and price, not price and time"; (08:41–10:52) the spine — market profile, correlated markets, market structure and SMT, then the PD array matrix; (11:22–12:47) "by going through this entire process step by step in order in this way, I end up getting to a monthly bias… I transpose it to a weekly chart"; (14:47) forecasting three months; (18:37–19:21) the 9-to-18-month trend, "18 candles on the monthly chart", no moving averages; (20:16–20:27) the consolidation default — reverse the last three to four months; (29:23–31:36) the profile decision tree, consolidation asked first; (32:21–32:57) institutional focus points, only obvious arrays noted; (33:54–35:07) the rounding calibration; (37:26–52:52) the AUDUSD walkthrough including the 7380 order-block open and the three-array discount set.
- `ICT-2017-INTERMEDIATE-TOP-DOWN` (00:16–00:30) "second of four teachings in the final delivery month of our mentorship… ICT intermediate term top-down analysis, weekly to daily"; (00:28–01:32) eleven and a half months of parts, now placed "in an order"; (02:46–04:38) relative strength, COT, sentiment as the weekly-tier inputs; (04:38–05:13) the three monthly inputs explicitly absent from the weekly tier; (06:39–06:55) institutional order flow on down- and up-close candles; (08:02–08:20) weekly bias transposed to the daily; (08:23) markets "**lead in strength** by failing to make lower lows and **lead in weakness** by failing to make higher highs" — both leadership; (08:50) IBD top 30; (09:23) leadership and laggards as the separate strongest/weakest axis; (10:28–10:58) 12- and 6-month extremes, 2- and 4-year extremes; (12:02–14:24) sentiment from headlines, forums and Williams %R at 20/14/10; (19:05–19:42) the recentred 12-month COT line; (20:40–45:31) the AUDUSD weekly walkthrough, the 73.29/73.57 rebalance and the 15 May / 30 May headlines; (40:01–41:23) %R long at 80, short at 20, 14 optimal; (46:39–46:47) time-of-day analysis not required on monthly and weekly.
- `ICT-2017-TOPDOWN-SHORT-TERM` (00:00–00:33) "lesson three for the August 2017 ICT mentorship content, this is short term top-down analysis and it's daily to the four hour"; (01:07–01:20) nothing is added beyond the first two lessons; (04:48–05:08) the self-made zero line and the carry-over requirement; (09:39–09:52) the six-month fallback; (11:03–11:38) the open-interest gate and the explicit "not considered" band; (12:15–12:58) "the daily order flow is the most important one to know"; (13:58–14:38) the weekly range forms Tuesday to Thursday, and the bullish and bearish week shapes; (16:16) weekly profiles deferred to March's content; (18:25–18:47) the 60 % and 70 % confidence figures; (19:05–21:27) Sunday's open and Monday 00:00 New York carried across the week on the hourly; (22:04–22:11) SMT's effectiveness peaks daily-into-H4; (22:19–23:00) breakers sought on the daily, "the meat in the middle"; (26:02–26:24) a bias is not a daily buy licence.
- `ICT-2017-INTRADAY-TOP-DOWN` (00:11–00:26) "we are here, the last structured teaching of the ICT mentorship"; (01:37–01:41) monthly, weekly and daily analysis all carried into the H4 view; (01:41–04:04) the tier-4 input list — day of week, true day, killzones, CBDR, Asian range, flout, intraday profiles, PD arrays, ADR; (04:18–05:11) the entry-timeframe choice, M15 minimum and M5 preferred; (05:41–06:19) "we're looking for a timeframe that produces fair value gaps — that's the key"; (06:25–06:50) Monday/Tuesday/Wednesday first, Thursday/Friday as the fallback; (07:25–07:44) "the bulk of the daily volume will be between 3 a.m. and 10 a.m. New York time"; (07:47–08:34) the killzone sequence and the 10:00–11:00 profit-taking window; (15:44–16:42) the intraday profile and the New-York-reversal test; (17:29–18:15) the five-day ADR and the 127 %/162 % extensions; (38:45) "there's too many variables, you have to think"; (51:51–60:00) the gold case study.
- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW` — the general HTF-to-LTF descent as restated in later years.
