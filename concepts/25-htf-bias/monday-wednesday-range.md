# Monday–Wednesday Range

**Category:** 25-htf-bias
**Aliases:** Mon-Wed range, day-of-week gate, intraweek range break, Monday through Wednesday phenomenon
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STT-MONTHLY-WEEKLY-RANGES, ICT-2017-STT-LRLR-TRENDING, ICT-2017-STT-ONE-SHOT-ONE-KILL
**Tags:** day-of-week, weekly-range, confirmation, statistics, short-term-trading

## Definition

The Monday–Wednesday range is the high-to-low band built by the week's **first three sessions**, used two ways in ICT's short-term trading model: as the **window in which the weekly extreme is expected to form**, and as a **confirmation trigger** when the opposite side of that band is broken later in the week.

Three numbers are attached to it, all from the March-2017 module:
- the weekly high or low forms Monday–Wednesday with **~70 % odds** (`ICT-2017-STT-ONE-SHOT-ONE-KILL`, 01:30–01:41);
- **30–50 %** of the whole weekly range is complete by **Wednesday's London close** (`ICT-2017-STT-LRLR-TRENDING`, 23:37–23:48);
- breaking the Mon–Wed band on the bias side later in the week is "an aggressive confirmation" of the higher-timeframe target (`ICT-2017-STT-MONTHLY-WEEKLY-RANGES`, 43:25).

## Formal Criteria

**Where the extreme forms.**
- "Notice how the lows of the week are generally formed in Monday, Tuesday, and Wednesday in this context" (`…-MONTHLY-WEEKLY-RANGES`, 42:33).
- In a trending bullish market the search is narrowed to those three days: "we're looking essentially for is the low of the week to form between Monday, Tuesday and Wednesday. They are the highest probable trading days in this environment" (`…-LRLR-TRENDING`, 20:46–20:52).
- Stated as an odds figure in the lesson-8 prerequisite list: "**Day of week concept looking for the high or low to form on Monday through Wednesday with the 70% odds of it happening**" (`…-ONE-SHOT-ONE-KILL`, 01:30–01:41).

**The break as confirmation.**
- Bullish: "from a Monday's opening to Tuesday and Wednesday's range, whatever the highest high is when the markets are bullish, if that high is broken intra-week, say for instance on Thursday or Friday, generally that is indicative of an aggressive confirmation that we're going to be moving to our premium array that we were looking for or identified ahead of time" (43:25).
- Restated: "When that high is taken out intra-week, this is significant because price will tend to expand aggressively towards the monthly and or weekly premium array" (42:52).
- Bearish mirror: "the low that's formed between Monday through Wednesday, if that is broken on an intra-week basis, that is confirmation that you are an aggressive sell-off or sell program and your long-term higher timeframe discount array that you're aiming for is a high probability condition" (44:14).
- The confirmation is **not** a same-week guarantee: "May not happen that week, but you're going to keep looking for the next week to be bullish or bearish respectively based on that information" (44:34).
- Anchor: Monday's opening, with Sunday optional — "You can use Sunday for completeness sake" (43:25).

**How much range is left after Wednesday.**
- "typically the weekly ranges, they have a 30 to 50 percent of the weekly range completed between Monday to Wednesday. In other words, by London close on Wednesday, 30 to 50 percent generally the range is completed" (`…-LRLR-TRENDING`, 23:37–23:48).
- Consequence: "don't expect a massive move higher or lower in the last two days of the trading week" (25:02); and "Generally, if you get an explosive move, usually on Tuesday or Wednesday, Thursday may see a little bit of follow through, but then Friday has either retracement or… it's basically a neutral close" (25:18–25:30).
- Missing the window is not a reason to force size: "it's important not to get **pip drunk** trying to get a lion's portion of a move by Friday's close because the weekly range may end up being smaller or less volatile than you've anticipated" (24:43–24:59).

**Where the entry sits inside the window.** The bullish sequence is impulse → retracement → expansion, all three compressed into Monday–Wednesday: "we're looking for a market that rallies higher than retraces. And this is going to occur Monday through Wednesday" (`…-MONTHLY-WEEKLY-RANGES`, 27:48–27:54), with the retracement traded at a monthly/weekly/daily/H4 discount array inside a killzone (29:37–30:07).

## Formula / Math

```
MWH = max(high(Mon), high(Tue), high(Wed))     # anchored at Monday's open
MWL = min(low(Mon),  low(Tue),  low(Wed))      # Sunday optional
MW_range = MWH - MWL

P(weekly extreme forms in Mon..Wed)  ~= 0.70
MW_range / weekly_range              in [0.30, 0.50]   # measured at Wed London close

confirmation_bullish := breakout_above(MWH) on Thu or Fri
                        -> aggressive expansion toward the MN/W premium array
confirmation_bearish := breakdown_below(MWL) on Thu or Fri
                        -> aggressive expansion toward the MN/W discount array

# The confirmation may resolve in a LATER week; it is not invalidated by Friday's close.

# Expectation for the back half of the week
expected_remaining_range = weekly_range - MW_range   # i.e. 50-70% nominal,
                           but Friday typically retraces or closes neutral
```

## Machine-Readable

```json
{
  "id": "monday-wednesday-range",
  "category": "25-htf-bias",
  "aliases": ["mon-wed-range", "day-of-week-gate", "intraweek-range-break"],
  "criteria": [
    {"id": "c1", "expr": "weekly high or low forms Monday..Wednesday with ~0.70 probability"},
    {"id": "c2", "expr": "MWH/MWL anchored at Monday's open; Sunday optional"},
    {"id": "c3", "expr": "break of MWH (bullish) or MWL (bearish) on Thu/Fri == aggressive confirmation of the HTF array target"},
    {"id": "c4", "expr": "confirmation may resolve in a later week; not invalidated at Friday's close"},
    {"id": "c5", "expr": "30-50% of the weekly range is complete by Wednesday's London close"},
    {"id": "c6", "expr": "Friday typically retraces or closes neutral after a Tue/Wed expansion"},
    {"id": "c7", "expr": "entry sequence inside the window == impulse -> retracement -> expansion, retracement taken at a discount/premium array in a killzone"}
  ],
  "timeframes": ["H1", "H4", "D", "W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["weekly-range-profiles", "weekly-bias", "daily-bias", "top-down-analysis", "one-shot-one-kill", "market-maker-manipulation-template", "intraweek-market-reversal", "low-resistance-liquidity-run", "power-of-three", "killzone-overview"],
  "sources": ["ICT-2017-STT-MONTHLY-WEEKLY-RANGES", "ICT-2017-STT-LRLR-TRENDING", "ICT-2017-STT-ONE-SHOT-ONE-KILL"]
}
```

## Visual Pattern

```
  BULLISH WEEK — the band and its break

   S │  M     T     W  │  T     F
     │                 │
     │        ╱▔╲   ╱▔ │▔▔╲    ╱▔▔▔▔  <- expansion to the W/MN premium array
  MWH├───────────────── ─ ─ ─ ─┼─ ─ ─   break of MWH on Thu = CONFIRMATION
     │   ╱╲  ╱   ╲ ╱   │
     │  ╱  ╲╱         │
  MWL├──╲__╱───────────┼──────────────  low of week (~70% forms in this window)
     │                 │
     └── 30-50% of the weekly range done by Wednesday's London close ──┘

  BEARISH WEEK is this inverted: MWL broken on Thu/Fri confirms the sell program.
```

## Timeframes

Measured on **D** (three daily candles) or **H1/H4** with weekly dividers; the break is watched on **H1**. All times New York.

## Examples

**Example 1 — USDJPY, 2016 monthly-range worked example (`ICT-2017-STT-MONTHLY-WEEKLY-RANGES`, 40:55–43:11):**
- Setup: monthly discount array at ~104.35 framed against a weekly premium array at ~118.70; six consecutive weeks of buying opportunities, "one each week".
- Trigger: with Monday–Wednesday shaded on the H4, "the lows of the week are generally formed in Monday, Tuesday, and Wednesday in this context"; the Mon–Wed highs are then taken out intraweek.
- Outcome: "price will tend to expand aggressively towards the monthly and or weekly premium array."

**Example 2 — GBPUSD, two consecutive March-2017 weeks (`ICT-2017-STT-LRLR-TRENDING`, 20:46–23:48):**
- Week 1: low forms **Tuesday** at a daily fair value gap; Wednesday breaks Monday's high and makes the intraweek high; Thursday retraces into a fair value gap plus mitigation block and expands again; Friday prints "a small little Judas swing, trades down into equilibrium and then expands on the upside going into the close."
- Week 2: low forms **Monday** at the macro-range equilibrium; Tuesday retests it; Wednesday buys a bullish breaker formed on Monday's high; Thursday slightly bullish and "a relatively flat close on that week's Friday" — the stated Friday behaviour.

## Common Mistakes

- **Confusing this with the August-2017 Tuesday-to-Thursday statement.** They are different claims about different quantities — see the flag under [daily-bias](daily-bias.md) and the note below.
- **Treating the break as a same-week promise.** ICT explicitly allows the expansion to land in the following week.
- **Anchoring the band on Sunday's open by default.** Monday's open is the stated anchor; Sunday is "for completeness sake".
- **Expecting the back half of the week to deliver the bulk of the move.** The 30–50 %-by-Wednesday figure implies the opposite: Thursday follows through, Friday retraces or goes flat.
- **Sizing up after missing the window.** The "pip drunk" warning is attached specifically to chasing a Friday close.
- **Using the 70 % figure as a systematic edge.** It is stated once, in a prerequisite list, with no derivation.

> ⚠ **Cross-source tension, unresolved.** This page's Mon–Wed window comes from the **March-2017** short-term module. Five months later, `ICT-2017-TOPDOWN-SHORT-TERM` states "**the weekly range typically forms between Tuesday and Thursday**" (13:58) and attaches a *different* 70 % — the confidence with which ICT can identify the weekly profile once Tuesday has resolved (18:25). The two statements are about different objects (where the extreme prints vs. how confidently the profile can be named) and disagree on the window's edges (Monday vs. Thursday). Both are recorded; neither is treated here as superseding the other. See [daily-bias](daily-bias.md) c8/c10.

## Related Concepts

- [weekly-range-profiles](weekly-range-profiles.md) — which day inside the window makes the extreme, by profile.
- [one-shot-one-kill](../31-models/one-shot-one-kill.md) — the model that uses this as its day-of-week gate.
- [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md) — what is traded at the extreme once it forms.
- [intraweek-market-reversal](../31-models/intraweek-market-reversal.md) — the case where the Mon/Tue move is *too* large and the window's extreme reverses instead of confirming.
- [low-resistance-liquidity-run](../02-liquidity/low-resistance-liquidity-run.md), [weekly-bias](weekly-bias.md), [daily-bias](daily-bias.md), [top-down-analysis](top-down-analysis.md).
- [power-of-three](../12-power-of-three/power-of-three.md) — the open-near-low / close-near-high shape the window produces on a weekly candle.
- [killzone-overview](../10-killzones/killzone-overview.md) — where inside the window the retracement is taken.

## Citations

- `ICT-2017-STT-MONTHLY-WEEKLY-RANGES` (27:48–27:54) "we're looking for a market that rallies higher than retraces. And this is going to occur Monday through Wednesday"; (28:21–28:45) the impulse/retracement placement across those three days; (29:37–30:07) the retracement traded at a monthly/weekly/daily/H4 discount array, "and it has to drop down into a kill zone"; (40:55–41:53) the USDJPY monthly→weekly framing and the six weekly buying opportunities; (42:07–42:33) the day dividers and "Notice how the lows of the week are generally formed in Monday, Tuesday, and Wednesday in this context"; (42:41–43:04) the Mon–Wed high taken out intraweek as the trigger for aggressive expansion to the monthly/weekly premium array; (43:11–43:52) the anchor at Monday's open with Sunday optional, and the full confirmation statement; (43:58–44:34) the bearish mirror and "May not happen that week, but you're going to keep looking for the next week".
- `ICT-2017-STT-LRLR-TRENDING` (20:40–20:55) "the low of the week to form between Monday, Tuesday and Wednesday. They are the highest probable trading days in this environment"; (21:27–23:00) the two worked weeks including the Friday Judas swing into equilibrium; (23:37–23:48) "**30 to 50 percent of the weekly range completed between Monday to Wednesday… by London close on Wednesday**"; (24:43–24:59) "don't get pip drunk"; (25:02–25:35) no massive move expected in the last two days; explosive move Tuesday or Wednesday, Thursday follow-through, Friday retracement or neutral close.
- `ICT-2017-STT-ONE-SHOT-ONE-KILL` (01:30–01:41) "Day of week concept looking for the high or low to form on Monday through Wednesday with the 70% odds of it happening"; (29:04–29:12) applied — "we're going to be expecting either monday, tuesday or wednesday to be the high of the week".
