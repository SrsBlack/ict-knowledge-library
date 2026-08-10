# Daily Bias

**Category:** 25-htf-bias
**Aliases:** D bias, daily direction, daily setup bias
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-TOPDOWN-SHORT-TERM, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** htf-bias, daily, foundational

## Definition

Daily bias is the directional read from the **daily chart** — the primary bias-setting TF for ICT day-traders. While weekly and monthly provide context, daily bias is what most intraday setups align against. It changes faster than weekly but slower than H4, and a fresh daily CHoCH/MSS frequently signals the start of a new multi-day swing.

## Formal Criteria

Daily bias is bullish when:

- Most recent daily external BOS was up OR a daily CHoCH-up has just printed.
- Current price below daily EQ (in daily discount).
- Daily DOL is upside (PDH/PWH ahead).

Bearish when symmetric. Neutral when conflicting.

Common signals:

- True Day Open (00:00 NY) above prior day's range = mild bullish lean.
- Daily candle closed strongly directional yesterday = momentum continuation expected today.
- Daily wicked one bound = sweep + reversal possible.

**ICT's own daily routine** (`ICT-2017-TOPDOWN-SHORT-TERM`) — tier 3 of [top-down-analysis](top-down-analysis.md). Nothing new is added beyond the two higher tiers: "I've used everything I've done in the monthly and weekly presentation… that is all the work I do, I don't do anything additional to that" (01:07). The daily's job is to **confirm** — "all monthly and weekly analysis is carried over into the daily timeframe… preferably the daily should confirm it" (05:08).

1. **Commercial hedging (COT)** — the 12-month high/low of commercial net holdings, split in half to make a private zero line; **fall back to 6 months** "if that range is very narrow or can't discern from looking at 12 months" (09:39). Below the midpoint → hunt discount arrays and expect upside expansion (10:22).
2. **Open interest, gated on where price is.** A **decline of ~15 % or more while price trades at a higher-timeframe *discount* array is "extremely bullish"**; an **increase of ~15 % or more at a higher-timeframe *premium* array is "extremely bearish"** (11:03–11:22). Outside those two cases it is discarded outright: "in between either of the above conditions, for my personal style of trading, open interest is **not considered** in my analysis… it either has to meet one of these two criterias, or I'm not going to refer to it at all" (11:26–11:38).
3. **Institutional order flow on the daily** — in a bullish higher timeframe, the daily should find **support at down-close daily candles** and **break through up-close daily candles**; mirrored when bearish. This is the tier's load-bearing read: "the daily order flow is the **most important one to know**" (12:15), and skipping it means "you're playing with Russian roulette" (12:49).
4. **Weekly profile** — see below.
5. **SMT divergence** — "I'm looking for SMT divergence at this point from daily going into the four hour, because I think that's where the **heart of its effectiveness** exists" (22:04–22:08).
6. **Market structure with breakers and mitigation blocks.** Breakers are sought on the daily above any other timeframe, because they "alert you to where the next intermediate-term price swing is going to form"; trade **between** the daily bullish and bearish breaker — "there's a lot of movement generally between those two reference points, **it's the meat in the middle**" (22:19–22:47).
7. Shared spine → daily bias → **transpose onto the H4 chart** (09:16).

**Weekly profile and the two opening prices**

- **"The weekly range typically forms between Tuesday and Thursday. That's the bulk of the weekly range"** (13:58).
  - *Bullish week:* a low can form Monday, Tuesday dilly-dallies, then price takes off through the second half of Tuesday, all of Wednesday and the first half of Thursday to make the high of the week; Friday retraces (14:04–14:15).
  - *Bearish week:* **Tuesday makes the high of the week**, **Thursday's New York open makes the low**, and Friday and Monday are consolidation (14:19–14:38).
- **Forecast confidence is stated numerically:** with Monday behind you, "about a **60 %** likelihood that I'll be able to determine… what the weekly profile is going to be"; it "goes into a **70 %** likelihood" once Tuesday is resolved (18:25–18:47). ICT concedes he has "never been able to create a systematic approach for forecasting weekly profiles" (18:19).
- **Two opening prices are projected across the entire week on the hourly:** Sunday's natural forex open, and **midnight New York on Monday** — "whatever the opening price is on the hourly at midnight Monday… that's the opening price I use for the weekly" (19:05–21:27). Bullish → want price *below* those into a discount array; bearish → *above* them into a premium array (20:41–21:04).
- ICT defers the full profile catalogue to the **March-2017** content (16:16). That catalogue is now distilled at [weekly-range-profiles](weekly-range-profiles.md) — twelve variants across six bidirectional families.
- ⚠ **The two lectures disagree about the window.** This lecture says the weekly range forms **Tuesday to Thursday**; the March-2017 module says the weekly high or low forms **Monday through Wednesday**, "with the 70% odds of it happening". The 70 % figures are also different quantities — here it is the confidence with which the *profile* can be named once Tuesday resolves, there it is the frequency with which the *extreme* falls in the window. Both are recorded; see [monday-wednesday-range](monday-wednesday-range.md).

## Formula / Math

```
daily_dealing_range = [LTL_d, LTH_d]
d_eq = (LTL_d + LTH_d) / 2

daily_bias :=
  "bullish" if last_daily_external == bullish AND price < d_eq AND upside_DOL
  "bearish" if last_daily_external == bearish AND price > d_eq AND downside_DOL
  "neutral" otherwise
```

## Machine-Readable

```json
{
  "id": "daily-bias",
  "category": "25-htf-bias",
  "aliases": ["D-bias", "daily-direction"],
  "criteria": [
    {"id": "c1", "expr": "uses_daily_external_structure"},
    {"id": "c2", "expr": "considers_price_vs_daily_eq"},
    {"id": "c3", "expr": "considers_PDH_PDL_DOL"},
    {"id": "c4", "expr": "tier-3 inputs == [COT, open_interest, daily_IOF, weekly_profile, SMT, breakers] then shared spine"},
    {"id": "c5", "expr": "COT lookback 12m, fallback 6m when the 12m range is too narrow"},
    {"id": "c6", "expr": "open_interest actionable ONLY at a HTF array: dOI<=-15% at discount => bullish; dOI>=+15% at premium => bearish; otherwise ignored"},
    {"id": "c7", "expr": "bullish daily IOF := support at down-close daily candles AND breaks through up-close daily candles"},
    {"id": "c8", "expr": "weekly_range bulk forms Tuesday..Thursday"},
    {"id": "c9", "expr": "bearish week: Tuesday high-of-week, Thursday NY open low-of-week"},
    {"id": "c10", "expr": "weekly_profile confidence == 0.60 after Monday, 0.70 after Tuesday"},
    {"id": "c11", "expr": "two weekly opens projected on H1: Sunday open AND Monday 00:00 America/New_York"},
    {"id": "c12", "expr": "SMT most effective from D into H4"},
    {"id": "c13", "expr": "breakers read on D above all other TFs; trade between bullish and bearish daily breaker"}
  ],
  "timeframes": ["D","H4","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","monthly-bias","weekly-bias","bias-confluence","top-down-analysis","true-day-open","time-of-day-pivots","commitment-of-traders","open-interest","breaker-block","mitigation-block","smt-divergence","weekly-range-profiles","monday-wednesday-range"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2017-TOPDOWN-SHORT-TERM","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Daily chart bullish bias:

   PDH ───────────  (yesterday's high — potential BSL target today)
       /\
      /  \   today's price near discount of D range
   ──────── D_EQ
            \
   PDL ────── (yesterday's low — already swept = manipulation)
```

## Timeframes

D / H4 / H1.

## Examples

**Example 1 — bullish daily bias:**
- D LTH 1.0950 (yesterday); D LTL 1.0820 (3 days ago).
- D_EQ = 1.0885.
- Today's price 1.0855 = discount.
- Today's TDO 1.0860 above PDH 1.0860? → mild bullish lean.
- DOL: PDH BSL above 1.0950 (today's target).
- → bullish daily bias; intraday setups long-aligned.

## Common Mistakes

- **Stale daily bias.** Once today's session confirms a structural shift on D, refresh the bias.
- **Single-candle daily reads.** A daily CHoCH on a thin-volume day may not stick — wait for confirmation in the next 1-2 sessions.
- **Conflict ignorance.** When weekly and daily disagree, the conflict itself is the signal — reduce conviction or wait.
- **Reading open interest outside a PD array.** The ±15 % gate is conditional on price sitting at a higher-timeframe discount or premium array. Between those cases ICT discards the input entirely rather than weighting it lightly.
- **Treating a bullish bias as a daily buy licence.** "Just because we're bullish doesn't mean we buy every day and just because we're bearish we don't sell every day. We are still waiting for conditions to meet that expectation" (26:02–26:12) — a discount array *at a specific time of day*.
- **Forcing a weekly profile.** ICT states plainly that he has no systematic method for calling them, and puts the post-Monday accuracy at 60 %.
- **Skipping the daily to trade H1 and below.** Named as the highest-cost shortcut at this tier: "what may look like bullishness on a four-hour, one-hour or less may actually just be a setup that gets you short from a daily perspective" (12:58).

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [monthly-bias](monthly-bias.md), [weekly-bias](weekly-bias.md), [bias-confluence](bias-confluence.md), [top-down-analysis](top-down-analysis.md).
- [weekly-range-profiles](weekly-range-profiles.md) — the twelve-variant catalogue this lecture defers to.
- [monday-wednesday-range](monday-wednesday-range.md) — the March-2017 day-of-week window and the tension with the Tuesday-to-Thursday statement above.
- [true-day-open](../22-quarterly-theory/true-day-open.md), [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md).
- [commitment-of-traders](../03-order-flow/commitment-of-traders.md), [open-interest](../03-order-flow/open-interest.md) — tier-3 inputs 1 and 2.
- [breaker-block](../08-breaker-blocks/breaker-block.md), [mitigation-block](../08-breaker-blocks/mitigation-block.md) — read on the daily above every other timeframe.
- [smt-divergence](../16-smt-divergence/smt-divergence.md) — most effective from daily into H4.

## Citations

- `ICT-2017-TOPDOWN-SHORT-TERM` (00:00–00:33) "lesson three for the August 2017 ICT mentorship content, this is short term top-down analysis and it's daily to the four hour"; (01:07–01:20) "that is all the work I do, I don't do anything additional to that"; (04:48–05:20) the self-built zero line, and "all monthly and weekly analysis is carried over into the daily timeframe… preferably the daily should confirm it"; (09:39–09:52) the six-month COT fallback; (10:22–10:30) below the midpoint → focus on discount arrays; (11:03–11:38) the ±15 % open-interest gate at a higher-timeframe discount or premium array, and "it either has to meet one of these two criterias, or I'm not going to refer to it at all"; (11:43–12:15) daily institutional order flow — support at down-close candles when bullish, resistance at up-close candles when bearish — "the daily order flow is the most important one to know"; (12:49–13:06) "you're playing with Russian roulette… what may look like bullishness on a four-hour, one-hour or less may actually just be a setup that gets you short"; (13:58–14:38) the Tuesday-to-Thursday weekly range and the bullish and bearish week shapes; (16:16) weekly profiles deferred to March's content; (18:19–18:47) "I've never been able to create a systematic approach for forecasting weekly profiles", 60 % after Monday and 70 % after Tuesday; (19:05–21:27) Sunday's open and Monday midnight New York carried across the week on the hourly; (22:04–22:11) SMT's effectiveness peaks daily-into-H4; (22:19–22:47) daily breakers and "the meat in the middle"; (26:02–26:24) a bias is not a licence to trade every day; (09:16) the daily read transposed onto the four-hour chart.
- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW` — the general daily-bias restatement in later years.
