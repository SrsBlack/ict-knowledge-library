# London Session Avoidance

**Category:** 15-sessions
**Aliases:** when to avoid London, London stand-aside rules, London session filters, London slop
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-AVOID-LONDON
**Tags:** sessions, london, filters, stand-aside, risk, cbdr, asian-range

## Definition

London Session Avoidance is the **stand-aside rule set** of the April-2017 day-trading model:
a fixed list of conditions that disqualify the London session *before* any setup is looked
for. It is deliberately chart-free — "this lesson is going to be **completely void of any
charts, any kind of examples, any kind of distractions**" (00:23–00:37) — and ICT frames it as
the counterweight to the rest of the month: "the **best rules are the ones that help you stay
out of the marketplace**, because everybody can get in … very little is written about **how do
you know when to stay out**" (31:07–31:31).

The stated consequence of ignoring it is not merely lower expectancy but inverted expectancy:
"if the conditions we're showing you in lesson six are there, you have **a great deal of odds
in your favour of losing money**" (16:30).

## Formal Criteria

**A. Prior-day and calendar disqualifiers**

- **Large range day.** The previous trading day's range exceeded **2× its five-day average
  daily range** → stand aside the next day; "typically there'll be a consolidation, or it
  could go choppy" (01:16–02:01).
- **Three consecutive up closes** on the daily → **no London longs** on the fourth day
  (02:01–02:35).
- **Three consecutive down closes** on the daily → **no London shorts** on the fourth day
  (02:35–03:04). Both cases risk "a deep retracement, or it can go sideways", and both also
  make a big range day "**highly unlikely** to occur on the fourth trading day" (03:04–03:34).
- **FOMC whipsaw.** An FOMC event that produced extreme two-way price action — "generally FOMC
  comes out at **2 o'clock in the afternoon** New York time … that's going to **screw up the
  central bank dealers range** and possibly roll right on into the Asian session" (03:34–04:40).
- **Non-Farm Payroll day** — "typically the **first Friday** … we are **not trading London
  session at all** on that Friday" (04:40–05:02).
- **Day into a long weekend or holiday** — "usually it's a Friday, could be a Thursday …
  probably going to be a quiet session, **it's not worth taking on the risk**" (05:02–05:56).
- **Multiple high- or medium-impact drivers** for that pair in the London window. The ideal is
  **one** high-impact event, "and that way we know there's going to be **one stage of
  manipulation** for that particular day" (05:56–07:29).
- **Total absence of London news** is a **wild card**, not a green light — the source case is
  the UK snap-election announcement that moved cable **400 pips** with no scheduled London
  driver (07:29–08:28).

**B. Overnight-range disqualifiers (checked at midnight NY)**

- **CBDR greater than 50 pips** → "I'm already knowing firsthand I'm **possibly going to pass**
  on a London session" (08:28–08:52). ⚠ Note this is **50**, not the 40-pip qualification limit
  used for projections in [central-bank-dealers-range](central-bank-dealers-range.md) and
  [cbdr-projected-daily-range](cbdr-projected-daily-range.md) — see `## Common Mistakes`.
- **Asian range greater than 40 pips** → the standard profile is off; "I'm going to consider
  the **delayed protraction profile** … but it **has to meet every one of those criteria** …
  otherwise I'll move to the sidelines" (09:26–09:41).
- **A sustained rally or decline from 20:00 NY** → "it's usually a **poor indication** of a
  London session … the real event started at zero GMT and they're probably going to keep a
  sustained move going through" (09:41–10:04), with any retracement deferred to New York.
- **Either range failing to consolidate** — the master condition: "**central bank dealers range
  and/or Asian range must trade down into a small tight consolidation range**. If we don't see
  that — if it's trending in both or either — it makes the London session **highly suspect**"
  (10:04–11:39).

**C. The mechanism behind condition B**

The consolidation is not cosmetic; it is the observable trace of order build-up. "We're aiming
for days when the **banks will hold the market to build open float** … allowing orders to build
above and below the intraday high that's being formed between the Asian range open and the
Asian range close … we can **see it indicated in how they maintain a very narrow price range**"
(11:50–12:50). Without it, "you're not going to see a clear manipulation cycle or protractionary
state" (12:44).

**D. What an ideal London looks like (the positive form)**

- The **daily chart is visibly respecting PD arrays** — "obvious, clear, non-ambiguous"
  (20:18–21:02).
- Daily poised toward a **premium** array → **London longs**; poised toward a **discount** array
  → **London shorts** (21:26–23:04). Either is cancelled by any condition in A or B
  (23:04–23:22).
- **The five-day ADR has not been met on the previous day** → an expansion day is due
  (23:30–24:55). "The five-day average daily range has **not been traded to or exceeded** in
  the previous day, so we have a condition of volatility — it's low — and the average daily
  range many times will be either **one and a half or maybe even two times** the five-day
  average" (24:55–25:25).

## Formula / Math

```
# A — calendar and prior-day gates (any true => stand aside)
ADR5           := mean(range(D-1 .. D-5))
large_range_day:= range(D-1) > 2 * ADR5
three_up       := all(close(D-i) > close(D-i-1) for i in 1..3)   # blocks LONGS only
three_down     := all(close(D-i) < close(D-i-1) for i in 1..3)   # blocks SHORTS only
news_gate      := is_NFP_friday OR fomc_whipsaw(D-1) OR pre_holiday
                  OR count(high_or_medium_impact events in London window) > 1

# B — overnight gates (evaluated ~00:00 NY)
cbdr_pips      := CBDR_high - CBDR_low
asia_pips      := asian_high - asian_low
gate_B := cbdr_pips > 50
       OR asia_pips > 40                       # delayed-protraction profile only, if it qualifies
       OR trending_since(20:00 NY)
       OR NOT consolidating(CBDR) OR NOT consolidating(asian_range)

trade_london := NOT gate_B
                AND NOT large_range_day
                AND NOT news_gate
                AND daily_respecting_PD_arrays
                AND (direction == long  ? NOT three_up : NOT three_down)

# D — the expansion-day bonus condition
expansion_due := range(D-1) < ADR5
# then expect range(D) ~ 1.5 * ADR5 .. 2.0 * ADR5
```

## Machine-Readable

```json
{
  "id": "london-session-avoidance",
  "category": "15-sessions",
  "aliases": ["when-to-avoid-london", "london-stand-aside-rules", "london-slop"],
  "criteria": [
    {"id": "c1", "expr": "stand_aside if range(D-1) > 2 * ADR5"},
    {"id": "c2", "expr": "no_london_longs if 3 consecutive daily up closes"},
    {"id": "c3", "expr": "no_london_shorts if 3 consecutive daily down closes"},
    {"id": "c4", "expr": "stand_aside if FOMC whipsaw on the prior 14:00 release"},
    {"id": "c5", "expr": "stand_aside on NFP Friday (first Friday of the month)"},
    {"id": "c6", "expr": "stand_aside on the day into a holiday or long weekend"},
    {"id": "c7", "expr": "stand_aside if count(high_or_medium_impact London events) > 1; ideal == 1"},
    {"id": "c8", "expr": "cbdr_range > 50 pips => likely stand aside"},
    {"id": "c9", "expr": "asian_range > 40 pips => delayed-protraction profile only, all criteria required"},
    {"id": "c10", "expr": "sustained trend from 20:00 NY => stand aside"},
    {"id": "c11", "expr": "CBDR AND asian_range must both be visibly consolidating"},
    {"id": "c12", "expr": "ideal_london requires daily visibly respecting PD arrays"},
    {"id": "c13", "expr": "expansion_day_due if range(D-1) < ADR5; expect 1.5x-2.0x ADR5"},
    {"id": "c14", "expr": "absence_of_news == wildcard, not permission"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["central-bank-dealers-range", "cbdr-projected-daily-range", "asian-range", "london-session", "london-open-killzone", "ict-day-trading-model", "nfp-protocol", "news-blackout-rules", "amd-cycle-overview", "day-trade-routine", "daily-bias"],
  "sources": ["ICT-2017-AVOID-LONDON"]
}
```

## Visual Pattern

```
  THE OVERNIGHT SHAPE THAT QUALIFIES (condition B)

   2pm ───────────── 8pm ───────────── midnight NY
   │     CBDR         │   Asian range   │
   │  ▄▄▀▀▄▄▀▄▄▀▀▄▄   │  ▄▀▄▄▀▀▄▄▀▄▄▀   │   narrow, overlapping, obvious
   └──────────────────┴─────────────────┘   -> orders stack above and below
        "small tight consolidation"          -> London protraction has something to run

  THE SHAPE THAT DISQUALIFIES

   2pm ───────────── 8pm ───────────── midnight NY
   │            ▄▄▀▀                    │
   │      ▄▄▀▀▀▀                        │   trending / wide / erratic
   │▄▄▀▀▀▀                              │   -> "the real event started at zero GMT"
   └────────────────────────────────────┘   -> sleep in, trade New York
```

## Timeframes

Prior-day and consecutive-close conditions are read on the **daily**. The consolidation check
is made on the **M15** — "you'll see it clearly by going through your charts and going back
over a **15-minute** time frame" (11:12–11:32).

## Examples

**Example 1 — the black-swan wildcard (07:29–08:28):**
- Setup: **no** scheduled London-time news event for GBPUSD — by condition A7 this looks clean.
- Trigger: the UK Prime Minister announced a snap election "right on the heels of the holiday
  break, and it took the cable by storm".
- Outcome: "a **400-pip move in one trading day** … there was an absence completely of any
  London time-based news events". ICT files this under *wild card*, not under *ideal* —
  absence of drivers is a source of unquantifiable risk, not of clarity.

**Example 2 — the personal-schedule gate (08:28–09:11):**
- Setup: CBDR measured above 50 pips.
- Trigger: "if I have plans with my family and I want to be rested, I'll just pass on a London
  session, and **even if it moves well I won't even get up at night to see how it sets up**."
- Outcome: stand aside. ICT records the decision as taken *before* the session, not revised
  during it — the rule and the schedule are settled at the same time.

## Common Mistakes

- **Reading "50 pips" as the CBDR limit.** Two different numbers do two different jobs. The
  **40-pip** ceiling in `ICT-2017-CBDR` and `ICT-2017-PROJECTING-HIGHS-LOWS` qualifies the range
  for **standard-deviation projection**; the **50-pip** line here is a softer *session*
  avoidance trigger ("possibly going to pass"). A 45-pip CBDR is unusable for projections but
  not automatically a no-trade day.
- **Treating the list as advisory.** "You have to accept it, you got to **submit** to it … if
  you don't have them, you're going to over-trade" (19:43).
- **Trading it anyway and citing the winner.** Pre-empted verbatim: "you'll be able to show me
  an email — 'I made 120 pips here, Michael, look at this' — and I'm going to say **you didn't
  follow the rules** … if you make money I don't want to know about it" (19:50–20:18).
- **Assuming a valid daily bias overrides the filters.** It does not: "regardless of what we
  have as a daily bias … **all those things fall second to this criteria**, because we're
  specifically dealing with intraday action" (19:13–19:30).
- **Reading a quiet calendar as a clean session.** See Example 1.
- **Expecting the filters to be sufficient.** They remove drawdown-prone days; they do not
  produce winners. "This helps you avoid the ugly periods, but you're still going to get these
  once-in-a-while moves where it would have been better had you taken a trade" (17:00–17:30).
- **Substituting a checklist ICT wrote.** He declines on purpose: "I'm **not** going to give you
  a checklist … I want you to write it in your **own handwriting**" (33:13–33:32).

## Related Concepts

- [central-bank-dealers-range](central-bank-dealers-range.md) — the 40-pip projection ceiling this page's 50-pip line must not be confused with.
- [cbdr-projected-daily-range](cbdr-projected-daily-range.md) — lesson 4; what a qualifying day is used *for*.
- [asian-range](../14-asian-range/asian-range.md) — the second overnight range checked.
- [london-session](london-session.md), [london-open-killzone](../10-killzones/london-open-killzone.md) — the session being filtered.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — the April-2017 model; this is its lesson 6.
- [day-trade-routine](../25-htf-bias/day-trade-routine.md) — the May-2017 procedure these filters sit inside.
- [nfp-protocol](../30-news-driven/nfp-protocol.md), [news-blackout-rules](../30-news-driven/news-blackout-rules.md) — the calendar gates in detail.
- [amd-cycle-overview](../24-amd-cycle/amd-cycle-overview.md) — the accumulation the consolidation requirement is looking for.
- [daily-bias](../25-htf-bias/daily-bias.md) — the input these filters explicitly outrank intraday.

## Citations

- `ICT-2017-AVOID-LONDON` (00:12–00:23) "welcome back to **lesson six of the April 2017 ICT mentorship** — this month is ICT day trading model, this lesson is **when to avoid the London session**" — dates the source; (00:23–00:50) "**completely void of any charts** … I want you to think about the things I'm outlining in this lesson from a **conceptual or characteristic viewpoint**"; (01:16–02:01) "after a **large range day**, which is **greater than two times the average five-day range** … that is a day that you **do not want to trade immediately the day after**"; (02:01–02:35) "after a series of **three consecutive up closes** on a daily chart you want to **avoid trading longs**, at least in the London session"; (02:35–03:04) the mirrored three-down-closes rule; (03:04–03:34) "generally you won't see a big range day … it's **highly unlikely** to occur on the fourth trading day"; (03:34–04:40) "**after a FOMC event that produces extreme whipsaw** … generally FOMC comes out at **2 o'clock in the afternoon** New York time … it's going to **screw up the central bank dealers range** and possibly roll right on into the Asian session"; (04:40–05:02) "ahead of **non-farm payroll** numbers, typically the **first Friday** … we are **not trading London session at all** on that Friday"; (05:02–05:56) "the same trading day that's heading into a **long weekend or a holiday** … **it's not worth taking on the risk**"; (05:56–07:29) "**multiple high- to medium-impact news drivers** … if we see multiple events due out on the economic calendar for a particular pair it could be problematic … what we ideally look for is **one high-impact news event**, and that way we know there's going to be **one stage of manipulation**"; (07:29–08:28) "in **absence of any news** during London can be a **wild card** day … the UK Prime Minister came out with a **snap election** decision right on the heels of the holiday break … a **400-pip move in one trading day** for the British pound"; (08:28–09:11) "the **central bank dealers range — if it's greater than 50 pips** — I'm already knowing firsthand I'm **possibly going to pass** on a London session … even if it moves well I won't even get up at night"; (09:11–09:26) "I will still wake up around midnight time to see what the Asian range did"; (09:26–09:41) "**if the Asian range is greater than 40 pips** I'm going to consider the **delayed protraction profile**, but it **has to meet every one of those criteria** … otherwise I'll move to the sidelines"; (09:41–10:04) "if the market starts a **sustained rally or decline from 8 p.m. New York** it's usually a **poor indication** of a London session"; (10:04–11:39) "**central bank dealers range and/or Asian range must trade down into a small tight consolidation range** — if we don't see that, if it's trending in both or either or, it makes the London session **highly suspect**"; (11:12–11:32) "going back over a **15-minute** time frame, you'll see it clearly when it creates a consolidation"; (11:50–12:50) "we're going to be aiming for days when the **banks will hold the market to build open float** … allowing orders to build above and below the intraday high that's being formed between the Asian range open and the Asian range close … we can **see it indicated in how they maintain a very narrow price range**"; (13:17–13:47) "when the market is conditioned for **London slop** … **sleep in, trade New York**"; (16:30) "if the conditions we're showing you here in lesson six are there, you have **a great deal of odds in your favour of losing money**"; (17:00–17:30) "this helps you avoid the ugly periods, but you're still going to get these once-in-a-while moves where it would have been better had you taken a trade"; (19:13–19:30) "regardless of what we have as a daily bias … **all those things fall second to this criteria**"; (19:43–20:18) "you have to **submit** to it … you'll be able to show me an email — 'I made 120 pips here, Michael' — and I'm going to say **you didn't follow the rules** … if you make money **I don't want to know about it**"; (20:18–21:02) "the daily chart is going to be clearly respecting PD arrays … **obvious, clear, non-ambiguous**"; (21:26–22:32) "when the market is poised to trade higher on the daily to a premium array we're going to be looking for **London longs**"; (22:32–23:22) the mirrored discount/shorts case and "either one of these conditions can be **cancelled out** if we've seen the conditions in the previous two slides"; (23:30–25:25) "when the daily range has **not recently exceeded its five-day average daily range**, an **expansion day is due to form** … the average daily range many times will be either **one and a half or maybe even two times** the five-day average"; (26:48–27:07) "if you take out your largest profitable day you probably **aren't making money** — you don't want conditions like that in your equity growth"; (31:07–31:31) "the **best rules are the ones that help you stay out of the marketplace** … very little is written about **how do you know when to stay out**"; (33:13–33:32) "I'm **not** going to give you a checklist … I want you to write it in your **own handwriting**"; (34:18–34:28) "then what everybody else does — **gamble** — and gamblers sometimes make money, but gamblers rarely make a living".
