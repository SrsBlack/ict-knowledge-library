# Intraweek Market Reversal

**Category:** 31-models
**Aliases:** intra-week reversal, market reversal profile, overlapping models reversal, midweek reversal
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STT-INTRAWEEK-REVERSALS, ICT-2017-STT-LRLR-CONSOLIDATION
**Tags:** reversal, weekly, timeframe-conflict, displacement, short-term-trading

## Definition

An intraweek market reversal is a week that **starts in one direction, covers an abnormal distance in one or two days, reaches a higher-timeframe PD array, and turns**. ICT teaches it as the failure mode of the [weekly range profile](../25-htf-bias/weekly-range-profiles.md) you committed to on Monday, and gives it a single diagnostic: **the speed and magnitude of the Monday/Tuesday move**.

Its cause is stated structurally, not psychologically: every intraweek reversal is **two trading disciplines disagreeing** on the same chart, and the higher-timeframe one wins. "Here's the secret. They occur in overlapping models. Every market reversal that happens intraweek will be a overlapping of two types of trading disciplines. They'll be at odds with one another. Here's the rub. The higher time frame discipline will always win" (`ICT-2017-STT-INTRAWEEK-REVERSALS`, 26:03–26:24).

## Formal Criteria

**The trigger — abnormal distance, early in the week.**
- "The classic telltale signs are the magnitude at which the price moves on Monday and Tuesday. Okay, so it's only two days you have to focus on" (23:23–23:31).
- Quantified against the recent daily range: "If we see sudden quick movement in price and magnitude, here's the key word here. It's got to cover a lot of distance. What's average distance of the last few days? If it exceeds it a lot, whatever the **average daily range is for the last five days**, if it gets well above it, chances are you're probably going to see a market reversal profile" (20:41–21:04).
- Extreme case — the whole week in a day: "we were probably going to see the weekly range form in one day. And we did… The whole range for cable was really formed on Tuesday" (21:11–21:27).

**The interpretation — speed means valuation, not momentum.**
- "When we see a fast market, we have to immediately assume that they're reaching for a level institutional order flow that is highly critical for efficiency on the interbank level" (05:29).
- "**Speed in price is indicative of them getting to a valuation point**" (14:31).
- ICT separates the two causes: a central-bank repricing "is not attributed to buying and selling… that's a repricing based at the central bank level" (14:56–15:02), whereas "when there is no central bank involvement and price is just aggressively and speedily moving… that's based on evaluation through speculation" (15:25–15:33).
- The wrong inference is named explicitly: "it's moving quickly, it's moving fast. Therefore, I'm going to make a lot more money in double time. And it's probably going to have an equal leg lower later in the week… No, don't think like that" (14:10–14:29).

**The confirmation — refusal to leave the higher-timeframe range.**
- "First thing you want to notice is that price is unwilling to leave the premium" (08:47). The fast leg travels from a premium sub-array to a discount sub-array *while remaining inside the larger premium range* (15:33–15:54).
- "why didn't this continuously go lower Wednesday and the Thursday going into the discount market? Because it needs to go higher. It wants to go higher. So if it's not going to go lower and it wants to go higher, where do we focus? We focus on premium PD arrays" (17:02–17:19).
- After the turn, sponsorship is visible on every subsequent order block: "Every order block that forms with a down candle or a series of down candles, we extend that out of the time and you can see them capitalizing each one of them with new long positions" (17:36–17:46).

**The shape — a market-maker profile in miniature.** ICT walks it as: price balanced range (consolidation) → aggressive departure Tuesday → **smart money reversal in the Tuesday/Wednesday overlap** → low-risk entry Thursday → reaccumulation Friday back into the price balanced range, which price "may exceed… and go past it, which is what the market maker buy profile really aims to do" (18:21–19:26).

**Frequency.** "Wednesday or Thursday reversals generally form every month. So no matter what pair you're looking at, there's generally some kind of reversal of sorts that can form" (22:51–23:03).

## Formula / Math

```
ADR5 = mean(daily_range(d)) for the last 5 completed sessions

reversal_watch := day in {Mon, Tue}
                  AND move_distance(day) >> ADR5          # "well above it"
                  AND HTF_PD_array reached (D / W / MN, or H4 at minimum)
                  AND price has NOT left the larger premium/discount range

# The overlap rule that decides the outcome
if model_A(tf_A) says BUY and model_B(tf_B) says SELL:
    winner := model with max(tf)          # "the higher time frame discipline will always win"

# Sequence
price_balanced_range -> aggressive_departure(Tue)
                     -> smart_money_reversal(Tue/Wed overlap)
                     -> low_risk_entry(Thu)
                     -> reaccumulation(Fri) -> return to (or exceed) price_balanced_range

# Management corollary
if trade_open and thesis_not_confirming:
    exit even while profitable and re-enter on a strong entry point
```

## Machine-Readable

```json
{
  "id": "intraweek-market-reversal",
  "category": "31-models",
  "aliases": ["intra-week-reversal", "market-reversal-profile", "overlapping-models-reversal"],
  "criteria": [
    {"id": "c1", "expr": "trigger := Monday or Tuesday range >> 5-day ADR"},
    {"id": "c2", "expr": "speed interpreted as reaching a valuation point, never as momentum"},
    {"id": "c3", "expr": "destination := HTF PD array on D/W/MN (H4 is the floor)"},
    {"id": "c4", "expr": "price refuses to exit the larger premium (or discount) range"},
    {"id": "c5", "expr": "cause := two trading disciplines in conflict; the higher timeframe wins"},
    {"id": "c6", "expr": "sequence == [price_balanced_range, departure, Tue/Wed reversal, Thu low-risk entry, Fri reaccumulation]"},
    {"id": "c7", "expr": "return to the price balanced range may be exceeded (market maker buy/sell profile)"},
    {"id": "c8", "expr": "expected frequency == roughly one Wednesday-or-Thursday reversal per month per pair"}
  ],
  "timeframes": ["H1", "H4", "D", "W", "MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["weekly-range-profiles", "one-shot-one-kill", "monday-wednesday-range", "market-maker-manipulation-template", "low-resistance-liquidity-run", "balanced-price-range", "mean-threshold", "timeframe-selection", "bias-invalidation", "swing-trading-hallmarks"],
  "sources": ["ICT-2017-STT-INTRAWEEK-REVERSALS", "ICT-2017-STT-LRLR-CONSOLIDATION"]
}
```

## Visual Pattern

```
  GBPUSD, March 2017 — H1, one week

   Mon        Tue              Wed        Thu        Fri
   ╱▔╲___                                        ____/▔  <- back into the
  ╱      ╲                                  ___╱          price balanced range
            ╲                          ___╱               (may exceed it)
              ╲                    __╱
                ╲              __╱
                  ╲________╱
                  ^ >200 points in 24 hours, one dominating candle
                  ^ terminates at the DAILY bullish order block MEAN THRESHOLD
                    then IPDA draws price to the H4 bearish order block

  THE OVERLAP THAT CAUSES IT
     one-shot-one-kill model (weekly)  says: SELL, continue lower
     swing-trading model     (daily)   says: BUY, this is the entry
     ------------------------------------------------------------
     higher timeframe wins  ->  reversal
```

## Timeframes

Diagnosed on **daily and H4**, executed on **H1**. The array that stops the move must be daily, weekly or monthly — "That's why we have to focus on monthly, weekly, and daily PD arrays… Anything less than that four hour that's about as low as you want to go" (26:29–26:36).

## Examples

**Example 1 — GBPUSD, week of the March-2017 recording (`ICT-2017-STT-INTRAWEEK-REVERSALS`, 04:01–19:26):**
- Setup: price in the premium range of the 60-day consolidation graded in lesson 5, having traded into a weekly rejection block / daily bearish order block. A Monday-high-of-week profile was the reasonable read.
- Trigger: "the cable, British pound USD, trades over 200 points in a period of 24 hours" from Tuesday into Wednesday, terminating at a **daily bullish order block mean threshold** — "there's very little movement below the level that's identified as the daily bullish order block mean threshold" (12:07).
- Outcome: "After the bounce at the daily bullish order block mean threshold, IPTA draws price up into a four hour bearish order block premium PD array" (11:43). ICT had flagged "a potential area of bounce likely in this pair" in that week's chart index (06:49).
- Overlap: the same low is a textbook **swing-trade** entry — "This is a swing trade entry. This is exactly what you look for for a swing trade" (25:04) — while the short-term model was short.

## Common Mistakes

- **Reading speed as follow-through.** The single most costly inference in the lesson; ICT names and rejects it at 14:10.
- **Holding a profitable trade through a failing thesis.** "when you have a trade that doesn't seem like it's working out for you, even though you're profitable, chances are it's probably better for you to get out of it and look for another entry point" (22:32–22:41).
- **Specialising in one discipline.** "If you're only focusing on I'm going to be a short term trader or I'm going to only be a day trader or I'm only being a scalper. These types of setups will evade you" (25:25–25:33). The reversal is invisible unless you can also read the opposing model.
- **Anchoring the diagnosis below H4.** A reversal caused by an H1 array is not this pattern.
- **Assuming the reversal must return exactly to the price balanced range.** It may stop there or run past it; the market-maker profile aims to "take out the liquidity above an old high" (19:26).
- **Abandoning the week's plan at the first adverse move.** ICT's stance is the opposite until the array evidence arrives: "you're going to anticipate at the beginning of the week a certain outcome. And it's prudent that you stick to that" (06:14).

## Related Concepts

- [weekly-range-profiles](../25-htf-bias/weekly-range-profiles.md) — the profile that this pattern invalidates mid-week.
- [monday-wednesday-range](../25-htf-bias/monday-wednesday-range.md) — the Monday/Tuesday window the diagnosis lives in.
- [one-shot-one-kill](one-shot-one-kill.md), [market-maker-manipulation-template](market-maker-manipulation-template.md), [low-resistance-liquidity-run](../02-liquidity/low-resistance-liquidity-run.md).
- [balanced-price-range](../06-fair-value-gaps/balanced-price-range.md) — ICT's "price balanced range" in the sequence above.
- [mean-threshold](../27-equilibrium/mean-threshold.md) — the daily order block mean threshold that stops the move in the worked example.
- [timeframe-selection](../25-htf-bias/timeframe-selection.md), [bias-invalidation](../25-htf-bias/bias-invalidation.md), [swing-trading-hallmarks](swing-trading-hallmarks.md).

## Citations

- `ICT-2017-STT-INTRAWEEK-REVERSALS` (00:00) "Welcome to **lesson 7** folks of the short term trading module for ICT mentorship… intra-week reversals and overlapping models"; (04:01–05:08) the cable low, "over 200 points in a period of 24 hours"; (05:29–05:44) a fast market means a critical institutional reference point is being reached; (06:14–06:21) stick to the week's anticipated outcome; (08:47–08:58) "price is unwilling to leave the premium"; (10:03–10:24) the dominating Tuesday candle; (11:29–12:19) the daily bullish order block mean threshold and the H4 bearish order block draw; (12:39–13:10) speed on Monday or Tuesday as the classic telltale sign; (14:10–14:31) the wrong inference, and "Speed in price is indicative of them getting to a valuation point"; (14:44–15:33) central-bank repricing versus speculative valuation; (15:33–17:19) travelling premium→discount *within* the larger premium range, and why the focus flips back to premium arrays; (17:24–18:06) institutional sponsorship visible on each subsequent order block; (18:11–19:26) the price-balanced-range sequence and the market-maker buy profile; (20:41–21:27) the 5-day ADR test and "the weekly range form in one day"; (22:32–22:45) exiting a profitable trade whose thesis has failed; (22:51–23:03) Wednesday/Thursday reversals form roughly every month; (23:23–23:31) magnitude on Monday and Tuesday as the number-one sign; (25:04–25:33) the same low as a swing-trade entry, and the cost of single-discipline specialisation; (26:03–26:36) the overlapping-models secret and "the higher time frame discipline will always win", with monthly/weekly/daily arrays as the reason; (28:17) "The arm wrestling match is always going to be won by the higher time frame".
- `ICT-2017-STT-LRLR-CONSOLIDATION` (08:26–19:12) the 60-day cable consolidation and its quadrant grading, referred back to throughout lesson 7 as "the large trading range that we talked about and outlined in lesson five".
