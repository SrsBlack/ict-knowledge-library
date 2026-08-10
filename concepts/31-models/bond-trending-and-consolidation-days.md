# Bond Trending & Consolidation Days

**Category:** 31-models
**Aliases:** bond day types, trending days, consolidation days, range expansion day, volatility squeeze, bond auction day
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-BOND-TRENDING-DAYS, ICT-2017-BOND-CONSOLIDATION-DAYS
**Tags:** models, bonds, futures, day-classification, volatility, news, economic-calendar, intermarket

## Definition

This is ICT's **advance classification of the 30-year Treasury bond's trading day** into a
**trending / large-range-expansion day** or a **consolidation / small-range day**, decided the
night before from four inputs: the daily range history, the economic calendar, where price sits
in the higher-timeframe PD array matrix, and the yield-curve divergence at the open.

Its stated purpose is not to trade bonds. ICT frames it as the permission slip for every other
asset class: "**you can't get explosive price action without the participation in the interest
rate**… if you follow the bond market, **it unlocks everything — it's like tumblers in a lock**"
(`ICT-2017-BOND-TRENDING-DAYS`, 12:25–12:41). The consolidation lecture states the same in
reverse: "**while the bond market is held in a narrow range, this will create a stranglehold on
volatility for the other asset classes** on average"
(`ICT-2017-BOND-CONSOLIDATION-DAYS`, 18:09).

It is explicitly **not a setup**: "let me preface it by saying **I'm not teaching specific
setups. I'm teaching thought process**" (`ICT-2017-BOND-CONSOLIDATION-DAYS`, 00:23).

## Formal Criteria

**Trending / large-range-expansion day — all four conditions**
(`ICT-2017-BOND-TRENDING-DAYS`, 01:03–02:52)

1. **Volatility filter.** The daily chart shows a **small range day, or a series of contracting
   small ranges** — "trending days or large range expansion days are seen typically **after small
   range days or a series of small range days**" (01:17).
2. **Position in the matrix.** Those small ranges have **recently traded into a discount array**
   (for an up-day) or a **premium array** (for a down-day). "We have the stage set for an
   **expansion from discount to premium**" (02:21).
3. **Volatility injection.** The economic calendar shows **high-to-medium-impact US reports due
   at 08:30 NY** (01:03).
4. **Yield-curve trigger at the open.** Compare the **5-year, 10-year and 30-year** at the lows
   (or highs) forming in the **08:00 → 08:30 NY** window; one refuses to confirm. "Notice that it
   did **not go lower. That's our trigger.** That's where we see the **professional
   accumulation**" (06:01–06:05). See [interest-rate-triad](../03-order-flow/interest-rate-triad.md).

- Overnight price action is **not** an input: "obviously overnight price action… can be trending
  or range bound. **It's never a precursor**" (00:55).
- Analysis timeframes for the curve comparison: "doing your analysis on the higher timeframe
  charts, but **focusing primarily on the daily, the four hour and two hour**" (07:52).
- Output: "we will know **beforehand** that price will be allowed to **expand dynamically across
  other asset classes**" (08:31).

**FOMC handling** (03:47–04:37)

- **Trade the morning session, never the afternoon.** "FOMC is always typically a **2 o'clock PM**
  New York time. So **we can trade the morning session, but we cannot be in the afternoon
  trading**."
- The morning is tradeable only if the volatility-squeeze conditions above are present.

**Consolidation / small-range day — the causes**
(`ICT-2017-BOND-CONSOLIDATION-DAYS`, 01:51–08:00)

| Cause | Detail |
|---|---|
| **News vacuum** | "when there's a **lack of noteworthy reports** due, the New York session vacuum… will create a **dead space** in the bond market" |
| **News scheduled later in the week** | high/medium-impact US reports due on **another trading date later in the week** promote consolidation now |
| **A higher-timeframe premium or discount array has been met** | price pauses, retraces or reverses at the array; profit-taking stalls the advance |
| **A higher-timeframe equilibrium / midpoint has been reached** | price can work the level **more than once**; do not expect an immediate response |
| **US bank holiday** | the day(s) before a holiday go quiet, and "that consolidation is going to **reverberate throughout the marketplace**" |
| **Bond auction day** | the **day before** an auction can consolidate, and the **AM session of the auction day itself** generally consolidates |

- Framing: "the markets move from **consolidation to expansion to consolidation to expansion**"
  (05:23), and "**consolidations, by far and large, will be the most dominant consideration** when
  we look at price action" (05:33).

**Consolidation-day trading rules** (08:56–17:21)

- **Scalp 5–10 ticks** in the AM session (1 tick = $31.25).
- **Opening range ≤ 12 ticks** is the squeeze condition that still produces an expansion move —
  often just a run of the previous overnight high or low.
- **PM session gate:** "you **only want to trade the PM session if the AM session has not yet ran
  a stop run**." Once the untapped liquidity pool is taken, take profit and stand down.
- **Avoid the AM session on bond auction days** — "the market usually is on hold waiting for the
  auction."
- **Avoid the PM session when interest-rate drivers are due** (typically 14:00 NY) — "regardless
  of how good the volatility looks, **trust me, just avoid it**."
- **Targets:** overnight and short-term highs and lows, as **low-resistance liquidity runs**.
- **Be done before noon, preferably before 11:00 NY.**
- **Set the limit exit beyond the objective.** Working an 8-tick idea, place a **16-tick** limit:
  "it can **pay you for being wrong** a bonus."

**The forward-looking consequence** (12:50, 17:39–17:55)

- "Recall **small ranges precede large ranges** on daily."
- "When we identify the market is likely to trade in small range or consolidation day, we should
  **immediately note the next trading day, or the day not long after it, will produce a large
  range day or trending day. How do we know this? The economic calendar.**"

## Formula / Math

```
# --- trending / expansion day (bonds) ---
volatility_filter := daily_range(t-1) is small
                     OR daily ranges contracting over a series of days
matrix_ok         := price recently traded into a discount array   # for an up-day
                     (premium array for a down-day)
news_ok           := economic_calendar has high/medium impact US report at 08:30 NY
trigger           := failure swing among {ZF_5y, ZN_10y, ZB_30y}
                     observed at the extreme forming in [08:00, 08:30] NY

trending_day := volatility_filter AND matrix_ok AND news_ok AND trigger
# overnight session is NOT an input

# --- FOMC ---
if FOMC (typically 14:00 NY):  trade AM only, never PM

# --- consolidation day ---
consolidation_day := no_noteworthy_reports_today
                     OR high/medium impact report scheduled LATER in the week
                     OR HTF premium/discount array just met
                     OR HTF equilibrium/midpoint just reached
                     OR US bank holiday adjacent
                     OR bond auction today (AM) or tomorrow

# --- consolidation-day execution ---
target        := 5..10 ticks                     # 1 tick = $31.25
squeeze       := opening_range <= 12 ticks       # expect an expansion anyway
draw          := overnight / short-term highs and lows (low-resistance liquidity runs)
trade_PM only if AM has NOT already run a stop
skip AM if bond auction today
skip PM if interest-rate driver due (~14:00 NY)
be flat by noon, preferably 11:00 NY
limit_exit    := 2 x objective                   # 16-tick limit on an 8-tick idea

# --- the cycle ---
consolidation -> expansion -> consolidation -> expansion
small_ranges precede large_ranges (daily)
```

## Machine-Readable

```json
{
  "id": "bond-trending-and-consolidation-days",
  "category": "31-models",
  "aliases": ["bond-day-types", "trending-days", "consolidation-days", "volatility-squeeze", "bond-auction-day"],
  "criteria": [
    {"id": "c1", "expr": "trending_day requires small prior daily range(s) AND recent HTF discount/premium array AND 08:30 NY high/medium impact US news AND a 5y/10y/30y failure swing in [08:00,08:30] NY"},
    {"id": "c2", "expr": "overnight session is not a precursor and is not an input"},
    {"id": "c3", "expr": "curve comparison read on daily, H4 and H2"},
    {"id": "c4", "expr": "FOMC (~14:00 NY) => AM session tradeable, PM session forbidden"},
    {"id": "c5", "expr": "consolidation causes := news vacuum, news later in week, HTF array met, HTF equilibrium met, US bank holiday, bond auction (day before or auction-day AM)"},
    {"id": "c6", "expr": "consolidation-day objective == 5..10 ticks; 1 tick == $31.25"},
    {"id": "c7", "expr": "opening_range <= 12 ticks => expansion move expected regardless"},
    {"id": "c8", "expr": "trade PM only if AM has not already run a stop"},
    {"id": "c9", "expr": "skip AM on auction days; skip PM when a ~14:00 rate driver is due; be flat by noon, ideally 11:00"},
    {"id": "c10", "expr": "limit exit set beyond the objective (16 ticks on an 8-tick idea)"},
    {"id": "c11", "expr": "small daily ranges precede large daily ranges; the calendar dates the expansion"},
    {"id": "c12", "expr": "supplies_setup == false; it classifies the day"}
  ],
  "timeframes": ["M15","H1","H2","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["multi-asset-analysis", "bond-split-session-rules", "futures-opening-range", "interest-rate-triad", "range-contraction", "range-expansion", "news-blackout-rules", "explosive-market-selection", "premium-array", "discount-array", "equilibrium-definition"],
  "sources": ["ICT-2017-BOND-TRENDING-DAYS", "ICT-2017-BOND-CONSOLIDATION-DAYS"]
}
```

## Visual Pattern

```
   TRENDING DAY — THE FOUR-CONDITION STACK

   daily    ████ ▒▒ ▒ ▒     small ranges contracting
                      ▲
                      └─ and price sat in a DISCOUNT array

   calendar 08:30 NY  ⚡ high/medium impact US report

   curve    5y  ╲__╱   higher low   ✓
   08:00-   10y ╲__╱   higher low   ✓
   08:30    30y ╲___   LOWER low    ✗  <- the trigger:
                                        "it did not go lower" = accumulation

   ────►  expansion from discount to premium, and the same
          volatility is released across FX, indices, commodities

   ═══════════════════════════════════════════════════════════
   CONSOLIDATION DAY — THE CAUSE LIST

     ▪ no noteworthy reports today          ▪ US bank holiday adjacent
     ▪ big report later in the week         ▪ bond auction (today AM / tomorrow)
     ▪ HTF premium or discount array met    ▪ HTF equilibrium reached

     execution:  AM only · 5-10 ticks · flat by 11:00
                 PM only if the AM did NOT run a stop
                 limit exit at 2x the objective

   ═══════════════════════════════════════════════════════════
   THE CYCLE      consolidation → expansion → consolidation → expansion
                  small ranges PRECEDE large ranges (daily)
```

## Timeframes

The classification is a **daily** decision, executed on **15-minute** charts. The PD-array and
curve context is read on the **daily, four-hour and two-hour**.

## Examples

**Example 1 — 14 June 2017, FOMC day (`ICT-2017-BOND-TRENDING-DAYS`, 02:52–07:07):**
- Setup: ZB at a discount on the two-hour chart; small daily ranges; a loaded 08:30 calendar plus
  FOMC at 14:00.
- Trigger: into the **08:00–08:30** window ZB made a **lower low** while the **10-year note did
  not** — the curve divergence. (Charts shown in Central time, one hour behind.)
- Called in advance: "I outlined it **before the fact** in the live session on the 14th that we're
  expecting a buy stop run or expansion on the upside."
- Outcome: ZB expanded higher; **EURUSD vaulted higher in the same New York session** — "the
  precursor and the release of that energy was **directly related to the treasury bond market**."
- Rule applied: morning session only, no FOMC-afternoon trading.

**Example 2 — 2 June 2017, one bond day, three FX moves (07:05–12:24):**
- Same conditions: heavy dollar-based news, ZB permitted to trend higher off a small-range
  consolidation.
- Outcome: an explosive up-day in **EURUSD**, an explosive up-day in **AUDUSD**, and a dynamic
  **decline in USDJPY** (dollar index bearish) — all on the same bond precursor.

**Example 3 — 18 April 2017 and 15 March 2017 (13:07–17:45):**
- 18 April: high-impact building permits at 08:30, ZB at a discount array on the daily, small
  daily ranges → large ZB up-day → "an amazing day in the **British pound**", and EURUSD rallied
  at the New York open.
- 15 March: another FOMC day; ZB rallied from the 08:30 window in a discount array with bullish
  daily institutional order flow; cable rallied through the session, with the large move arriving
  around 14:00 on the FOMC release.

**Example 4 — a consolidation day forecast a week ahead
(`ICT-2017-BOND-CONSOLIDATION-DAYS`, 02:21–03:21, 17:39–18:09):**
- The Wednesday of the recording had **both** a heavy 08:30 calendar **and** a 14:00 FOMC → a
  high-volatility day, "**which we anticipated before the trading week began**."
- The counterfactual is stated as the rule: had FOMC been the *only* high-impact event, the days
  leading in and the morning session itself would have consolidated, with volatility arriving only
  in the PM.

## Common Mistakes

- **Using the overnight session as a tell.** ICT states flatly that it is "**never a precursor**".
- **Taking the volatility squeeze as a direction signal.** Small ranges say a large range is due;
  **direction** comes from the PD array matrix and institutional order flow.
- **Trading the FOMC afternoon.** The morning is permitted under the squeeze conditions; the
  afternoon is not, on either day type.
- **Trading the bond AM session on an auction day.** The market is on hold for the auction.
- **Pressing the PM on a consolidation day after the AM already ran stops.** The single untapped
  liquidity pool is the whole PM opportunity; once taken, the day is over.
- **Expecting an immediate reaction at a higher-timeframe equilibrium.** Large traders work that
  level, sometimes more than once — a pause is the expectation, not a bounce.
- **Reading consolidation as a loss of opportunity.** ICT's framing is the opposite: "consolidation
  days are like **big banner signs** — hello, there's a big opportunity coming."
- **Treating this as a bond setup.** It classifies the day. The setups still come from the ordinary
  toolkit inside [bond-split-session-rules](../15-sessions/bond-split-session-rules.md).

## Related Concepts

- [multi-asset-analysis](../03-order-flow/multi-asset-analysis.md) — why a currency trader classifies the bond day at all.
- [bond-split-session-rules](../15-sessions/bond-split-session-rules.md) — the AM/PM structure the rules above are executed inside.
- [futures-opening-range](../15-sessions/futures-opening-range.md) — the 12-tick opening-range squeeze condition.
- [interest-rate-triad](../03-order-flow/interest-rate-triad.md) — the 5y/10y/30y failure swing used as the trigger; this page fixes it to the 08:00–08:30 window on a news day.
- [range-contraction](../01-market-structure/range-contraction.md), [range-expansion](../01-market-structure/range-expansion.md) — the structural cycle underneath.
- [news-blackout-rules](../30-news-driven/news-blackout-rules.md) — the stand-aside discipline around FOMC and NFP.
- [explosive-market-selection](explosive-market-selection.md) — hallmark 6 is the same volatility-contraction filter, stated for swing trades.
- [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md), [equilibrium-definition](../27-equilibrium/equilibrium-definition.md) — the locations that cause a pause.

## Citations

- `ICT-2017-BOND-TRENDING-DAYS` (00:20–00:28) "**June 2017 content, ICT Mentorship. ICT Bond Trading Lesson 4, Trending Days**" — self-dates the lecture; (00:55–01:03) "obviously overnight price action… can be trending or range bound. **It's never a precursor**"; (01:03–01:17) "New York session news — we're expecting a **volatility injection**. The economic calendar will show **high to medium impact US reports due to release at 8:30 a.m.** New York time"; (01:17–01:38) "**trending days or large range expansion days are seen typically after small range days or a series of small range days**. They're **directionally driven by the daily PD array matrix**. And they are **liquidity seeking movement, PD array and order flow based**"; (01:38–02:26) the volatility filter on the daily chart, "we're **due for a range expansion**… if the small ranges have just recently traded down into a **discount array**, and the economic calendar is calling for high to medium impact news reports at 8:30 a.m.… we have the **stage set for an expansion from discount to premium**"; (02:26–02:52) the bearish mirror from a premium array; (03:36–04:37) FOMC handling — "**we don't want to trade the FOMC afternoon session, but we can trade the morning session** if we have a volatility squeeze, small ranges… **FOMC is always typically a 2 o'clock PM** New York time"; (04:54–05:23) "the lower low going into the opening — or in this case, it's the **8 to 8:30 a.m.**… the chart that's shown here is in **central time**, so it's going to be an hour earlier"; (05:30–06:08) "when we see that lower low in the bond market, the stage is set… but look at the lows in the treasury bond here in relationship to the **10-year note. Notice that it did not go lower. That's our trigger. That's where we see the professional accumulation**"; (06:08–06:32) "**they don't cause small little moves when they step in — it's noticeable**… you see the divergence between the 10-year and the 30-year"; (07:44–08:12) "when you're looking for trades, you have to have the **sponsorship** behind it by way of the interest rate markets… looking at the **five year, the 10 year and the 30 year** and comparing them… **focusing primarily on the daily, the four hour and two hour**"; (08:16–08:37) "when you're bullish at the lows going into that time window of **eight o'clock to eight thirty** in the morning New York time… we will know **beforehand** that price will be allowed to **expand dynamically across other asset classes**"; (11:04–11:17) "**keep your opportunities few and far between in highly selected cherry-picking situations** where the perfect criteria is there before you take the trade"; (11:24–11:46) the recipe restated — "big impactful news in New York, the bond market has the condition where it's small ranges, we're expecting expansion, it's trading at a discount… therefore the **currencies are going to chase yield**"; (12:25–12:49) "**you can't get explosive price action without the participation in the interest rate**… **it's like tumblers in a lock**"; (02:52–07:07) the 14 June 2017 FOMC example with the EURUSD response; (07:05–12:24) the 2 June 2017 example across EURUSD, AUDUSD and USDJPY; (13:07–15:04) the 18 April 2017 example with the British pound; (15:54–17:45) the 15 March 2017 FOMC example; (19:23–19:49) the contrast homework — a declining bond market from a premium array means "**interest rates are increasing, which is going to cause the dollar to rally, and foreign currencies decline**".
- `ICT-2017-BOND-CONSOLIDATION-DAYS` (00:17–00:29) "**June 2017, ICT Mentorship, ICT Bond Trading, Lesson 3, Consolidation Days**" — self-dates the lecture; (00:23–00:40) "let me preface it by saying **I'm not teaching specific setups. I'm teaching thought process**"; (01:15–01:32) overnight price action again dismissed as a precursor — "whatever takes place in London doesn't always translate to future prognostication for the New York trading hours"; (01:51–02:05) "when there's a **lack of noteworthy reports** due, the New York session vacuum… will create a **dead space** in the bond market"; (02:05–02:21) "if we see high to medium impact U.S. reports due to release on **another trading date later in the week**, this is going to promote the idea of a consolidation day"; (02:21–03:21) the recording-week example — a heavy 08:30 calendar plus a 14:00 FOMC gave a high-volatility day "**which we anticipated before the trading week began**", against the counterfactual where FOMC alone would have produced consolidation into the PM; (03:21–04:43) "**after a higher time frame premium or discount array is met**… generally what will happen is **profit taking** will come in and there will be a **pause** in the advancement"; (05:00–05:23) "when price hits an **equilibrium of a higher time frame price swing or midpoint**, we can anticipate a **pause**"; (05:23–05:41) "the markets move from **consolidation to expansion to consolidation to expansion**… **consolidations, by far and large, will be the most dominant consideration**"; (06:06–06:28) "don't always anticipate or expect an immediate response in price because it can stay around equilibrium… **they're going to work that level sometimes more than one time**"; (06:51–07:29) "when there's a **bank holiday** in the United States… it's going to cause consolidation days… that consolidation is going to **reverberate throughout the marketplace**"; (07:29–07:47) "**bond auction days**… the day before the bond auction could be a consolidation day, and the day of that bond auction day, the **AM session** of that particular day, generally is a consolidation"; (08:56–09:22) "when we have consolidation days… we can **scalp for 5 to 10 ticks**… one tick is **$31.25**"; (09:22–10:13) "if the **opening range is 12 ticks or less**, generally you'll have an **expansion move** of some kind… that **volatility squeeze**"; (10:05–10:59) "you **only want to trade the PM session if the AM session has not yet ran a stop run**… once it takes those stops, don't be greedy"; (10:59–11:12) "when we're consolidating or we're anticipating small ranges, **do your trading in the AM session before noon**"; (11:04–11:18) "**avoid trading the AM session on bond auction days** — the market usually is on hold waiting for the auction"; (11:15–11:31) "**avoid trading the PM session when there's interest rate drivers due**. Usually it's 2 o'clock in the afternoon New York time… **regardless of how good the volatility looks, trust me, just avoid it**"; (12:46–12:50) "**recall small ranges precede large ranges on daily**"; (13:59–14:10) "**consolidation days are like big banner signs — hello, there's a big opportunity coming**"; (14:20–15:37) "**always allow your limit exits to exceed your targets**… if we put a **16 tick target** on the bond market, we could originally be only looking for **8**… **it can pay you for being wrong** a bonus"; (15:57–16:31) "**keep overnight short-term highs and lows in mind for low resistance liquidity runs**… that's where the market is going to reach for during consolidation days"; (16:31–17:21) "unless PM session news drivers are due out, consolidation days typically offer setups in the **AM session** most of the time… all of your trading has to be done, **preferably before 11 o'clock a.m. New York time**"; (17:39–17:55) "when we identify the market is likely to trade in small range or consolidation day, we should immediately note the **next trading day, or the day not long after it, will produce a large range day or trending day. How do we know this? The economic calendar**"; (18:09–18:32) the volatility stranglehold across asset classes; (24:55–25:36) the 2017 range-bound bond market and the trending "protractionary state" expected on the exit.
