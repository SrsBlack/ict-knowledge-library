# Ideal Swing Conditions

**Category:** 31-models
**Aliases:** ideal swing trading conditions for any market, swing market profile filter, swing-tradeable market test
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-SWING-IDEAL-CONDITIONS
**Tags:** models, swing-trading, market-profile, market-selection, watchlist, htf-bias

## Definition

Ideal swing conditions is the **market-profile precondition** for swing trading — the test applied
*before* any setup is looked for, asking whether a market is swing-tradeable at all. Delivered as
lesson 1 of the February-2017 swing-trading month: "this is **February 2017, lesson one, swing
trading**… this teaching is going to be specifically dealing with the **ideal swing trading conditions
for any market**" (`ICT-2017-SWING-IDEAL-CONDITIONS`, [00:00–00:27]).

ICT's definition of the discipline is given in the same lecture: "the discipline of trading
**predictable price movements** in the market with a high degree of consistency" [00:32–00:40], with
"trade durations of **two weeks or longer**" [00:51–01:00], capitalising "on the effects of **larger
entities** moving into a market and causing a **significant displacement in price**" [01:05–01:21].

The filter itself is a single question — is the monthly/weekly profile **trending**, or has it
**already left a consolidation**? — and the answer decides whether the market enters the watchlist:
"building your watch list of markets that are trending… on the monthly and/or weekly puts **high
probability behind your setups**" [03:29–03:42].

⚠ **It is a precondition, not a setup.** ICT closes the filter explicitly: "just simply because the
market's most likely to move higher or lower in the chart **doesn't indicate that there's a setup** —
there's other things you have to look for" [10:27–10:33]. Those other things are lessons 2 through 8;
see [swing-trading-hallmarks](swing-trading-hallmarks.md) and [million-dollar-swing-setup](million-dollar-swing-setup.md).

## Formal Criteria

**The three market profiles** [02:43–03:01]

- **Consolidation** — range-bound.
- **Trending** — "inside of the middle one here, trending, this is going to be seen as **expansion and
  retracement**."
- **Reversal.**

⚠ **The reversal profile is named and never developed** in this lecture. Do not quote criteria for it
from this page.

**The filter** [02:21–04:07]

- Read the **current** profile on the **monthly and weekly** charts. "Markets move from one profile to
  the next **in all time frames**."
- **Reject** lackluster markets — "avoid lackluster or lethargic markets that have **little to no
  movement over the last three months**."
- **Accept** either of two states: (a) currently trending, or (b) **already out of consolidation** —
  "once it's left the consolidation area, chances are we're going to be in a trending environment, and
  it will most likely move to a **larger level or PD array** on the higher timeframe monthly and/or
  weekly" [03:53–04:07].
- **Rationale — consolidation is an absence of sponsorship:** "if the market is confined to a small
  consolidation or range-bound environment, it's showing an indication of a **lack of institutional
  interest**. So if the market can't move out of that consolidation higher, then there's evidence of
  what? A **lack of buying**. If it can't break out of that consolidation to the lower end, it's a
  **lack of selling**" [05:34–05:58].
- **Trending is the positive signal:** "trending markets on higher timeframe charts are indicative of
  **major players buying or selling** that particular asset" [04:19–04:31]; a market that has left
  consolidation shows "**big players having muscled the marketplace** out of that holding pattern"
  [06:05–06:21].

**No favourite markets** [01:34–02:11]

- "You want to be **avoiding favorite markets** in general for swing trading purposes. Larger moves
  every year **rotate in and out** of different marketplaces. There is **no standard swing trading
  market or pair**."
- "**Every three months**, there is a new opportunity formed for swing trading. What once was a big
  mover will **not always** be the next big mover this time."

**Directional discipline** [06:41–07:34]

- "**Avoid the temptation to pick market tops and bottoms.** It's far more likely to see the existing
  long-term trending market profile to influence price action **over a long-term reversal**."
- Justification for the two-week hold: "if they're seeing it clearly on a **monthly** chart, then it's
  probably going to move **another month at least**" [07:28–07:34].
- Take the signal even when it argues with you: if monthly/weekly say higher and a daily or H4 buy
  signal appears, "**you want to take that signal**" [08:23–08:36].

**The two-consecutive-losses diagnostic** [08:52–09:21]

- One failed buy in an established bullish HTF profile is normal cost. **Two in a row is information**:
  "then you take the next signal and it's a buying opportunity and it fails — what it's telling you is
  it's probably near a **longer-term or intermediate-term shift** in the marketplace, and that present
  bullishness may be **waning**, or that trend may be **tired**."

**Execution tier** [04:49–05:01]

- "We're going to look for the setups on **monthly and weekly and daily**, but we'll **execute on
  four-hour** charts."

**What swing trading is not** [19:07–19:28]

- "We're **not** looking for range-bound trading. We're **not** looking for turtle swoops to stay inside
  of a consolidation. We're looking for **strong directional plays**." The model "is highly linked to
  a **directional mindset**."

## Formula / Math

```
# --- the profile filter, run on M and W ---
profile(tf) ∈ { CONSOLIDATION, TRENDING, REVERSAL }        # reversal undefined in this lecture
trending(tf) := successive higher_highs AND higher_lows     # or the bearish mirror
left_consolidation(tf) := price now outside a prior range it was confined to

swing_tradeable := trending(M) OR trending(W)
                   OR left_consolidation(M) OR left_consolidation(W)

# --- the rejection test ---
lethargic := movement over the last 3 months ~ 0
reject    := lethargic OR (confined to an obvious range on M and W)

# --- rotation ---
opportunity_period ~= 3 months     # "every three months there is a new opportunity formed"
# no market is permanently on the watchlist

# --- direction and entry side ---
bias  := direction of the M/W trending profile
side  := DISCOUNT array if bias bullish, PREMIUM array if bias bearish
setup_tf   := {M, W, D}
execute_tf := H4

# --- the trend-tired diagnostic ---
if signal_in_HTF_direction fails twice consecutively:
    infer possible intermediate-term shift; the trend may be tired
```

## Machine-Readable

```json
{
  "id": "ideal-swing-conditions",
  "category": "31-models",
  "aliases": ["ideal-swing-trading-conditions", "swing-market-profile-filter", "swing-tradeable-market-test"],
  "criteria": [
    {"id": "c1", "expr": "market_profiles := {consolidation, trending, reversal}; trending == expansion_and_retracement"},
    {"id": "c2", "expr": "profile read on monthly AND weekly charts"},
    {"id": "c3", "expr": "accept if trending(M|W) OR already_left_consolidation(M|W)"},
    {"id": "c4", "expr": "reject if lethargic over last 3 months OR confined to an obvious range"},
    {"id": "c5", "expr": "consolidation interpreted as lack of institutional interest (no buying / no selling)"},
    {"id": "c6", "expr": "no favourite markets; big movers rotate, new opportunity roughly every 3 months"},
    {"id": "c7", "expr": "do not pick tops or bottoms; existing HTF trend outweighs a long-term reversal"},
    {"id": "c8", "expr": "two consecutive failed signals in the HTF direction => trend may be tired"},
    {"id": "c9", "expr": "setups framed on M/W/D, executed on H4"},
    {"id": "c10", "expr": "swing duration >= 2 weeks"},
    {"id": "c11", "expr": "supplies_entry == false; this is a precondition, not a setup"}
  ],
  "timeframes": ["H4","D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["swing-trading-hallmarks","explosive-market-selection","million-dollar-swing-setup","stock-watchlist-construction","monthly-bias","weekly-bias","top-down-analysis","range-contraction","liquidity-void"],
  "sources": ["ICT-2017-SWING-IDEAL-CONDITIONS"]
}
```

## Visual Pattern

```
  THE THREE PROFILES, READ ON MONTHLY AND WEEKLY

   CONSOLIDATION            TRENDING                   REVERSAL
   ─────────────            (expansion + retracement)  (named, not
   ┌───────────┐                        ╱‾╲   ╱‾‾      developed in
   │ ∿∿∿∿∿∿∿∿∿ │              ╱‾╲   ╱‾‾╱   ╲_╱         this lecture)
   └───────────┘          ╱‾‾╱   ╲_╱
    no higher high,        higher highs AND higher lows
    no lower low
        ✗ REJECT                ✓ ACCEPT

   ALSO ACCEPT — the break-out state:

        ┌────────┐
        │ ∿∿∿∿∿∿ │──────►  ▲▲▲   "already left the consolidation area"
        └────────┘         ▲▲▲   -> expect a reach for a larger M/W PD array

  THE PIPELINE

    M / W profile ──trending?──► watchlist ──► M/W/D setup ──► H4 execution
          │ no                                                   │
          ▼                                                      ▼
      lack of institutional interest                      hold >= 2 weeks
      -> drop the market entirely
```

## Timeframes

**Monthly and weekly** for the profile read, **daily** joins them for setup framing, **four-hour** for
execution. The profile concept itself is timeframe-agnostic — "markets move from one profile to the
next **in all time frames**" [02:25] — but the filter is specified on the monthly and weekly only.

## Examples

**Example 1 — EURUSD monthly, rejected (10:38–12:23):**
- Window: from around end of February 2015 ("we'll just use the **March 1st, 2015**") to the time of
  the lecture.
- Read: "this would clearly be a **consolidation market profile** — the market's showing an
  unwillingness to go higher and an unwillingness to go lower. It's stuck in a range."
- The weekly is checked and shows the same range. ICT pre-empts the objection: "one would quickly be
  saying, oh well, I can see there's **several hundred pips** of still probable market direction in
  here — and that would be true. The problem is it's **not having a great ease of moving outside of
  that range**."
- Verdict: tradeable back and forth inside the range, but **not** a swing-trading market.

**Example 2 — NZDUSD, accepted (12:23–13:35):**
- Read: "we have a market that's trying to go higher. It has **higher lows**. It has **higher highs**.
  It's **closed in a liquidity void** up to the **7490** level."
- Weekly confirms: "successive higher high and higher low."
- Verdict: "it's a **trending environment** for the monthly chart" — buyers are willing to buy this pair.

**Example 3 — USDJPY, accepted on the break-out state (13:35–14:06):**
- Read: "price was staying inside of a consolidation and then it **left the consolidation abruptly**…
  it moves several hundred pips higher."
- Verdict: "that is very strong for looking for swing trades — in this case you'd be looking for swing
  trades on the **long side**."

**Example 4 — the three-month rhythm on NZDUSD (14:50–15:49):**
- Method: vertical lines segment the weekly chart by month; alternating white and orange squares on
  the axis mark successive months in three-month groups.
- Observation: "price offered that just about **every three to four months** — so every orange area we
  saw some measure of retracement, and then there was a buying opportunity the very next month or
  inside of the next month."
- The entry side is named: "you're looking for a buying opportunity — the price has to come back to a
  level of what? **Discount**" [17:35–17:48]; "and there's **PD arrays** at each one of these reference
  points" [18:01–18:05].

## Common Mistakes

- **Trading a favourite pair.** Named directly as the error this lesson exists to prevent: big moves
  rotate, and there is no standard swing-trading market.
- **Reading "several hundred pips of range" as opportunity.** ICT raises and dismisses exactly this
  objection on the EURUSD chart. Range size is not the test; **ease of leaving the range** is.
- **Confusing this with market selection for magnitude.** [explosive-market-selection](explosive-market-selection.md)
  (lesson 7) picks which trending market will move *explosively*, using COT, open interest, volatility
  contraction and sentiment. This page only asks *trending or not*.
- **Quoting reversal-profile criteria.** The third profile is named once and never defined here.
- **Picking tops and bottoms inside a trending profile.** Ruled out explicitly.
- **Treating a single stop-out as a trend failure.** One loss in the HTF direction is expected; the
  diagnostic requires **two consecutive** failures.
- **Executing on the monthly or weekly.** Those tiers frame; the H4 executes.

## Related Concepts

- [swing-trading-hallmarks](swing-trading-hallmarks.md) — lesson 2; what makes a *trade* valid once the market has passed this filter.
- [explosive-market-selection](explosive-market-selection.md) — lesson 7; the magnitude-oriented market-selection stack.
- [million-dollar-swing-setup](million-dollar-swing-setup.md) — lesson 8; the assembled model this precondition feeds.
- [stock-watchlist-construction](stock-watchlist-construction.md) — the equities analogue of building the watchlist.
- [monthly-bias](../25-htf-bias/monthly-bias.md), [weekly-bias](../25-htf-bias/weekly-bias.md) — the two charts the profile is read on.
- [top-down-analysis](../25-htf-bias/top-down-analysis.md) — the M→W→D→H4 descent this lecture specifies.
- [range-contraction](../01-market-structure/range-contraction.md) — the consolidation profile that disqualifies a market here.
- [liquidity-void](../02-liquidity/liquidity-void.md) — the NZDUSD read uses a closed void as trending evidence.

## Citations

- `ICT-2017-SWING-IDEAL-CONDITIONS` (00:00–00:27) "this is **February 2017, lesson one, swing trading**… the ideal swing trading conditions for any market" — the dating and lesson number are stated in the opening line; (00:32–00:40) swing trading as "the discipline of trading predictable price movements in the market with a high degree of consistency"; (00:51–01:00) "trade durations of **two weeks or longer** in time"; (01:05–01:21) capitalising on larger entities causing significant displacement, "potential rewards are considerable"; (01:34–02:11) no favourite markets, larger moves rotate annually, "**every three months** there is a new opportunity formed for swing trading"; (02:21–02:43) profiles matter, read on monthly and weekly, "avoid lackluster or lethargic markets that have little to no movement over the last three months"; (02:43–03:01) the three profiles, trending defined as "**expansion and retracement**"; (03:10–03:42) "trending markets equal large flows"; "if a market is confined to an obvious trading range, this does not indicate it has high odds for a directional setup"; the watchlist rule; (03:53–04:07) the already-left-consolidation state and the reach for a larger M/W PD array; (04:19–04:31) "trending markets on higher time frame charts are indicative of major players buying or selling"; (04:49–05:01) setups on M/W/D, execution on H4; (05:34–05:58) consolidation as lack of institutional interest — "a lack of buying… a lack of selling"; (06:05–06:21) "big players having muscled the marketplace out of that holding pattern"; (06:41–07:16) "avoid the temptation to pick market tops and bottoms… focus on the long-term trend"; (07:28–07:34) "if they're seeing it clearly on a monthly chart, then it's probably going to move another month at least"; (08:23–08:36) take the HTF-aligned signal even when you want to resist it; (08:52–09:21) the two-consecutive-losses diagnostic — "that present bullishness may be waning, or that trend may be tired"; (10:27–10:33) "just simply because the market's most likely to move higher or lower doesn't indicate that there's a setup"; (10:38–12:23) the EURUSD consolidation rejection from March 2015, including the several-hundred-pips objection and its dismissal; (12:23–13:35) the NZDUSD trending acceptance, higher highs and higher lows, "closed in a liquidity void up to the 7490 level"; (13:35–14:06) the USDJPY break-out acceptance; (14:50–15:49) the three-month segmentation and the recurring buying opportunity "every three to four months"; (17:13–17:25) "these are swing trades — the duration you're holding is for about two weeks or longer"; (17:35–18:05) the entry side is **discount**, and "there's PD arrays at each one of these reference points"; (18:50–18:54) "we just closed **January's content for long-term position trading**" — independent confirmation that Month 05 is Jan 2017 and this is the month after; (19:07–19:28) "we're not looking for range-bound trading… we're looking for strong directional plays"; the model "is highly linked to directional mindset".
