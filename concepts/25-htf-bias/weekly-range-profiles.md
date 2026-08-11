# Weekly Range Profiles

**Category:** 25-htf-bias
**Aliases:** weekly profiles, weekly market profiles, weekly range templates, the twelve weekly profiles
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STT-WEEKLY-PROFILES, ICT-2017-STT-MM-TEMPLATES, ICT-2017-STT-BLENDING-IPDA-PD, ICT-2017-STT-INTRAWEEK-REVERSALS, ICT-2017-TOPDOWN-SHORT-TERM, ICT-2017-DAYTRADE-ROUTINE
**Tags:** weekly, profile, day-of-week, short-term-trading, taxonomy

## Definition

Weekly range profiles are ICT's **catalogue of the shapes a trading week takes** — six bidirectional families, twelve variants in all, each defined by *which day makes the weekly high or low* and *what manipulation precedes it*. Delivered as lesson 2 of the March-2017 short-term-trading month, it is the catalogue that the August-2017 top-down lecture defers to (`ICT-2017-TOPDOWN-SHORT-TERM`, 16:16).

⚠ **It is a closed set of *named profiles*, not a closed enumeration of which day can make the weekly extreme.** No variant here is anchored on **Monday**, yet ICT treats a Monday weekly extreme as routine in three other 2017 lessons — including one in **this same March module**. The May-2017 routine lecture starts the search there: "we obviously **start from the Monday low of the week**, and if Monday doesn't give us enough evidence, we look for **Tuesday low of the week** to form" (`ICT-2017-DAYTRADE-ROUTINE`, 41:52–41:54). See `## Common Mistakes` for the full reconciliation; the twelve profiles remain the taught catalogue.

Each profile is stated as a triple: an underlying directional bias you already hold, a **manipulation** signature, and an **anticipation** rule that fires *before* the profile completes. The anticipation rule is the same shape in every bullish profile — the market **fails to reach a higher-timeframe discount array** on the earlier days, so the drive into it is deferred to the named day — and mirrored in every bearish one.

ICT prefaces the lesson by warning that it reads thin on paper: "this is one of the lessons that if you just look through it quickly and not paying much attention to it it's going to look rather ambiguous it's going to seem unfruitful but its impact is shown and solidified really by you going through price data and seeing these profiles unfold" (`ICT-2017-STT-WEEKLY-PROFILES`, 00:19). All diagrams are drawn on a **60-minute chart** (`ICT-2017-STT-MM-TEMPLATES`, 01:22).

## Formal Criteria

**1. Classic Tuesday low / high of the week** — the base case.
- *Bullish:* "price hovering above a higher timeframe discount array on Monday then drops into a higher timeframe discount array on Tuesday to form the low of the week" (01:08). Anticipate it when "the market fails to drop into that array odds are Tuesday will likely see the drive lower Tuesday London open and or New York session" (01:22).
- *Bearish:* mirror — hovering *below* a HTF premium array Monday, rising into it Tuesday to form the high (01:50, 02:03).
- **Shared caveat (ICT flags it explicitly as one caveat covering both):** the Tuesday London extreme can be exceeded later the same week — "it can come back and run the London high out and still form this for the classic Tuesday low of the week it can come back and make a lower low in the New York sessions. There's one caveat that has to be applied to both of them" (02:31–02:41).

**2. Wednesday low / high of the week** — the Tuesday case slipped one day.
- *Bullish:* hovering above a HTF discount array **Monday and Tuesday**, dropping into it Wednesday (02:57). "Monday and Tuesday can also be down days as well to form this profile" (03:26).
- Wednesday's London low can be run out in Wednesday's New York session and still make the weekly low (03:26–03:39); mirrored bearish (04:24).

**3. Consolidation Thursday reversal** — the news-driven case.
- Consolidation **Monday through Wednesday**, then "price runs the intrad week low and rejects it forming a market reversal" (04:53). "The key is it's consolidating. It's not really going higher or lower Monday through Wednesday" (05:00).
- Timing is explicit: "Thursday on a market driver news and or rate release late news and late New York session… typically around the 2 o'clock Eastern Standard Time or 2 p.m. New York time" (05:05–05:28).
- Driver: "This is generally on rate announcements FOMC or interest rate adjustments" (06:12). Mirrored bearish (05:29–06:05).

**4. Consolidation midweek rally / decline** — the continuation case.
- Consolidation Monday–Wednesday, then "runs the intrad week high and then expands higher into Friday" (06:29).
- Anticipated by *unfinished business*: "when the market is bullish and has yet to run to the premium array on the higher timeframes. It has recently rallied from a discount array and simply paused without any bearish reversal price action" (06:37–06:43). Mirrored bearish (07:02–07:23).

**5. Seek and destroy Friday, bullish / bearish** — the stand-aside case.
- "This is a neutral or low probability market profile" (07:46). Manipulation is two-sided: "prices consolidating Monday through Thursday running shallow stops under and above the intra week highs and lows" (07:51), then a Friday expansion.
- Conditions: "when the market is awaiting interest rate announcements and or nonfarm payroll can create this profile in the summer months of **July and August**" (08:10).
- Verdict: "It's better to avoid trading these conditions altogether" (08:19).

**6. Wednesday weekly reversal, bullish / bearish** — the HTF-turn case.
- "prices consolidating Monday through Tuesday and drives lower into a higher timeframe discount array to induce sell stops then strongly reverses" (09:05).
- Anticipated by *location*, not by news: "when the market is trading at a long term or intermediate term low price will pair institutional buying with pending sell side liquidity or traditionally known as a sell stop rate" (09:18). Mirrored bearish at a long/intermediate-term high (09:39–09:52).

## Formula / Math

```
# A profile is a triple (bias, manipulation, anticipation).
# Anticipation is the same predicate in all six bullish variants:

anticipate(profile) := HTF_discount_array_exists            # bullish
                       AND NOT reached(HTF_discount_array, days_before(D))
                       -> drive_lower expected on day D, London open and/or NY session

D  = Tue  for classic-tuesday-low
     Wed  for wednesday-low-of-week          (hover spans Mon AND Tue)
     Thu  for consolidation-thursday-reversal (14:00 NY, FOMC/rate release)
     Wed  for wednesday-weekly-reversal       (consolidate Mon-Tue, sweep, reverse)

# Bearish variants: swap discount<->premium, lower<->higher, sell-stops<->buy-stops.

# Two families are not anticipated by an unreached array:
consolidation_midweek_* := consolidate(Mon..Wed) AND HTF_opposing_array_unrun
                           AND no_reversal_price_action -> expand into Friday
seek_and_destroy_*      := consolidate(Mon..Thu) AND shallow_stops_both_sides
                           AND (rate_announcement OR NFP) AND month in {Jul, Aug}
                           -> DO NOT TRADE
```

## Machine-Readable

```json
{
  "id": "weekly-range-profiles",
  "category": "25-htf-bias",
  "aliases": ["weekly-profiles", "weekly-market-profiles", "weekly-range-templates"],
  "criteria": [
    {"id": "c1", "expr": "six bidirectional families == [classic_tuesday, wednesday_of_week, consolidation_thursday_reversal, consolidation_midweek, seek_and_destroy_friday, wednesday_weekly_reversal]"},
    {"id": "c2", "expr": "each profile == (pre-existing bias, manipulation signature, anticipation rule)"},
    {"id": "c3", "expr": "bullish anticipation := HTF discount array NOT reached on earlier days => drive lower on day D"},
    {"id": "c4", "expr": "day D extreme may be exceeded later the same week without invalidating the profile"},
    {"id": "c5", "expr": "consolidation_thursday_reversal fires ~14:00 America/New_York on FOMC or rate release"},
    {"id": "c6", "expr": "seek_and_destroy is neutral/low-probability; ICT says avoid trading it"},
    {"id": "c7", "expr": "wednesday_weekly_reversal is located at a long- or intermediate-term extreme, not at news"},
    {"id": "c8", "expr": "all profile diagrams drawn on H1"},
    {"id": "c9", "expr": "closed set of NAMED profiles; NOT a closed enumeration of extreme-forming days"},
    {"id": "c10", "expr": "no Monday-anchored variant exists, but a Monday weekly extreme is taught elsewhere in 2017"},
    {"id": "c11", "expr": "day-of-week search order (day-trade routine) == Monday -> Tuesday -> Wednesday, weekly high capped ~Thursday NY open"},
    {"id": "c12", "expr": "a US holiday shifts the whole day-of-week frame forward one session"}
  ],
  "timeframes": ["H1", "H4", "D", "W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["daily-bias", "weekly-bias", "top-down-analysis", "monday-wednesday-range", "market-maker-manipulation-template", "intraweek-market-reversal", "one-shot-one-kill", "turtle-soup", "premium-array", "discount-array", "liquidity-pool", "day-trade-routine"],
  "sources": ["ICT-2017-STT-WEEKLY-PROFILES", "ICT-2017-STT-MM-TEMPLATES", "ICT-2017-STT-BLENDING-IPDA-PD", "ICT-2017-STT-INTRAWEEK-REVERSALS", "ICT-2017-TOPDOWN-SHORT-TERM", "ICT-2017-DAYTRADE-ROUTINE"]
}
```

## Visual Pattern

```
  All twelve drawn on a 60-minute chart, Sunday open -> Friday close.

  CLASSIC TUESDAY LOW          WEDNESDAY LOW OF WEEK       CONSOLIDATION THU REVERSAL
  M  T  W  T  F                M  T  W  T  F               M  T  W  T  F
  ‾‾\        __/‾              ‾‾‾‾‾\     __/‾             ────────\   __/‾
     \____/‾                         \__/‾                          \_/     <- 14:00 NY
     ^ HTF discount array             ^ HTF discount array           ^ intraweek low swept

  CONSOLIDATION MIDWEEK RALLY  SEEK & DESTROY BULL FRI      WEDNESDAY WEEKLY REVERSAL
  M  T  W  T  F                M  T  W  T  F                M  T  W  T  F
  ─────/‾‾‾‾‾/‾                ‾\_/‾\_/‾\_/‾‾‾/‾            ────\      __/‾‾
       ^ runs intraweek high        ^ shallow stops both        \____/
         then expands to Fri          sides, then Friday run    ^ HTF discount array,
                                      DO NOT TRADE                sell stops induced

  Bearish variants are these six inverted.
```

## Timeframes

Profiles are read on **H1** (the teaching chart) and framed by **monthly / weekly / daily** premium and discount arrays. The profile classifies a *week*, so it is only meaningful once the weekly bias exists — see [weekly-bias](weekly-bias.md).

## Examples

**Example 1 — AUDUSD, week of the March-2017 recording, classic Tuesday high (`ICT-2017-STT-BLENDING-IPDA-PD`, 13:44–14:41):**
- Setup: bullish expectation going in; ICT was "originally long or bullish on the Australian dollar with the expectation of a larger price move" (10:50).
- Trigger: "forming the high of the week on Tuesday, trading at an old monthly, weekly and or daily high liquidity pool… It traded slightly above Monday's high. Rejected it" (13:44–14:04).
- Outcome: shorts framed at 76.80, downside objective 76.05, reached via a liquidity void that "came down and closed in the liquidity void right to the PIP" (13:28).

**Example 2 — GBPUSD, March 2017, Wednesday weekly reversal (`ICT-2017-STT-INTRAWEEK-REVERSALS`, 04:56–12:19):**
- Setup: price in the premium range of the 60-day consolidation; a weekly rejection block / daily bearish order block above.
- Trigger: "trades over 200 points in a period of 24 hours" into a **daily bullish order block mean threshold**, Wednesday's low.
- Outcome: reversal, then "IPTA draws price up into a four hour bearish order block premium PD array" (11:43).

## Common Mistakes

- **Treating the named day's extreme as untouchable.** ICT states the opposite: the Tuesday-London extreme can be run out later in the week and the profile still stands (02:31–02:41).
- **Trading seek and destroy.** It is catalogued so it can be *recognised and avoided*, not traded — see also [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md), where ICT says of it "we're not looking to trade this. We're looking for it to unfold."
- **Confusing "Wednesday low of week" with "Wednesday weekly reversal".** ICT separates them explicitly: "this is not the same as the Wednesday low of the week templates" (`ICT-2017-STT-MM-TEMPLATES`, 35:58). The first is a routine pullback into a discount array; the second is a HTF turn at a long- or intermediate-term extreme.
- **Waiting for the profile to complete before acting.** Each profile carries its own *forward-looking* anticipation rule, keyed on an array the market has so far failed to reach.
- **Reading the profile without a prior bias.** Every non-neutral profile opens "this is a market profile that is generally bullish so you're already looking for bullish prices anyway" (01:02). The profile refines an existing bias; it does not create one.
- **Expecting a systematic classifier.** ICT concedes elsewhere that he "never been able to create a systematic approach for forecasting weekly profiles" (`ICT-2017-TOPDOWN-SHORT-TERM`, 18:19), and that no template can be chosen in advance: "you're **never going to know** what weekly template it's going to unfold **before Sunday's open**" (`ICT-2017-DAYTRADE-ROUTINE`, 44:19).
- **Reading the twelve as the complete list of days a weekly extreme can form on.** They are not, and the gap is Monday. Reconciliation, in ICT's own sources:
  - **Same module, lesson-level:** "notice how the **lows of the week are generally formed in Monday**, Tuesday, and Wednesday in this context" (`ICT-2017-STT-MONTHLY-WEEKLY-RANGES`, 42:33), and "the high or low to form on **Monday through Wednesday** with the **70 %** odds" (`ICT-2017-STT-ONE-SHOT-ONE-KILL`, 01:30). Both are cited on [monday-wednesday-range](monday-wednesday-range.md).
  - **April 2017:** Monday is normally small-range, *except* when a large range out of the gate into a daily array "often marks the week's high or low" (`ICT-2017-DAYTRADE-ESSENTIALS`, 19:44–20:47, via [ict-day-trading-model](../31-models/ict-day-trading-model.md)).
  - **May 2017:** the routine's search **starts** at Monday (41:52).
  The consistent reading is that the twelve name the *recurring, anticipable* shapes — each carrying a manipulation signature and an anticipation rule — while a Monday extreme is treated as a **day-of-week statistic without a named profile**. It has no manipulation signature to anticipate, which is plausibly why it was never given one.
- **Applying the day names through a holiday week.** The frame shifts with the sessions, not the calendar: "**Monday is a U.S. holiday** … then **Tuesday becomes what would normally be a Monday**", pushing an expected reversal to Wednesday (`ICT-2017-DAYTRADE-ROUTINE`, 57:16–57:34). The March catalogue carries no such rule.

## Related Concepts

- [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md) — the entry/exit template layered onto each profile, lesson 3 of the same month.
- [monday-wednesday-range](monday-wednesday-range.md) — the day-of-week statistics the profiles rest on.
- [intraweek-market-reversal](../31-models/intraweek-market-reversal.md) — what happens when the profile you chose is the wrong one.
- [one-shot-one-kill](../31-models/one-shot-one-kill.md) — the model that consumes these profiles.
- [daily-bias](daily-bias.md), [weekly-bias](weekly-bias.md), [top-down-analysis](top-down-analysis.md).
- [day-trade-routine](day-trade-routine.md) — the May-2017 pass that selects a profile in step 6, and the source of the Monday-first search order and the holiday-shift rule.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — the consolidation-Thursday-reversal entry is a turtle soup.
- [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md), [liquidity-pool](../02-liquidity/liquidity-pool.md).

## Citations

- `ICT-2017-STT-WEEKLY-PROFILES` (00:00) "Welcome back to lesson two of short-term trading **March 2017** ICT mentorship content"; (00:16) "This lesson is defining the weekly range profiles"; (00:19–00:49) the "looks rather ambiguous" preface and the price-data homework; (01:02–01:37) classic Tuesday low, its manipulation and anticipation; (01:44–02:16) classic Tuesday high; (02:16–02:41) the shared caveat that the Tuesday London extreme can be exceeded later in the week; (02:48–03:39) Wednesday low of week; (03:46–04:33) Wednesday high of week; (04:34–06:18) consolidation Thursday reversal, bullish and bearish, "around the 2 o'clock Eastern Standard Time or 2 p.m. New York time" and "generally on rate announcements FOMC or interest rate adjustments"; (06:18–07:33) consolidation midweek rally and decline; (07:34–08:58) seek and destroy bullish and bearish Friday — "neutral or low probability", July and August, "better to avoid trading these conditions altogether"; (08:59–10:03) Wednesday weekly reversal, bullish and bearish, paired with pending sell-side / buy-side liquidity at a long- or intermediate-term extreme; (10:04–10:44) the one-hour-chart study assignment; (10:47) "We will be giving you more insights about this when we start looking at the market maker templates."
- `ICT-2017-STT-MM-TEMPLATES` (00:22–01:04) the templates blend onto the lesson-2 profiles; (01:22–01:38) "all of the charts or diagrams are represented in and depicted as a 60 minute chart"; (35:58) "this is not the same as the Wednesday low of the week templates".
- `ICT-2017-STT-BLENDING-IPDA-PD` — lesson 4 of the same March-2017 module; supplies **Example 1**, the AUDUSD classic-Tuesday-high week. (10:50) "originally long or bullish on the Australian dollar with the expectation of a larger price move" — the pre-existing bias every profile requires; (13:44–14:04) "forming the **high of the week on Tuesday**, trading at an old monthly, weekly and or daily high liquidity pool… it traded slightly above Monday's high, rejected it" — the classic-Tuesday manipulation signature in live data, including the Monday-high sweep the shared caveat describes; (13:28) the 76.80 → 76.05 objective closing an H4 liquidity void "right to the PIP". Also supplies the PD-array search order the anticipation rules run against (01:39–02:44) and the exhausted-array exclusion (04:31), both used when testing whether the HTF array has in fact gone unreached.
- `ICT-2017-STT-INTRAWEEK-REVERSALS` — lesson 7 of the same module; supplies **Example 2**, the GBPUSD Wednesday weekly reversal. (04:56–12:19) "over 200 points in a period of 24 hours" into a **daily bullish order block mean threshold** forming Wednesday's low, then "IPDA draws price up into a four hour bearish order block premium PD array" (11:43). Supplies the profile's **diagnostic**: "whatever the **average daily range is for the last five days**, if it gets well above it, chances are you're probably going to see a **market reversal profile**" (20:48–21:04), read on **Monday and Tuesday only**, with the worked week's whole range "really formed on Tuesday" (21:23); confirmation is that price is "**unwilling to leave the premium**" (08:47). Frequency: "Wednesday or Thursday reversals generally form **every month**" (22:51). Stated cause: "they occur in **overlapping models** … **the higher time frame discipline will always win**" (26:03–26:24). ⚠ Distinct from `ICT-2017-MARKET-REVERSALS`, which is the May-2017 day-trading lecture.
- `ICT-2017-TOPDOWN-SHORT-TERM` (16:16) the August-2017 deferral of the full profile catalogue to March's content; (18:19) "I've never been able to create a systematic approach for forecasting weekly profiles".
- `ICT-2017-DAYTRADE-ROUTINE` — May-2017 lesson 8; the profile-selection step in practice. (41:37–41:49) "if we're bullish, there's only **so many weekly templates** to outline the range for the weekly range to be bullish — so we look for **evidence to support those**"; (41:52–41:58) "we obviously **start from the Monday low of the week**, and if Monday doesn't give us enough evidence, we look for **Tuesday low of the week** to form. If Tuesday starts to trade up, then we know that **Wednesday** is probably going to be a good buying day"; (42:03–42:13) "all the way up into **Thursday's New York open**, where we can basically expect the **weekly high** to start to form — it doesn't have to, but that's the conditions we anticipate"; (42:17–42:23) "if Thursday continues higher, then there's probably going to be some **profit taking on Friday** — so **try not to buy on Friday**"; (44:19–44:28) "you're **never going to know** what weekly template it's going to unfold **before Sunday's open**"; (57:16–57:34) "**Monday is a U.S. holiday** … then **Tuesday becomes what would normally be a Monday**".
