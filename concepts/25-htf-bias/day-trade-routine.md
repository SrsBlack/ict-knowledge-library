# ICT Day Trade Routine

**Category:** 25-htf-bias
**Aliases:** daily day trade routine, ICT daily routine, day-trade preparation sequence, scalping routine
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-DAYTRADE-ROUTINE
**Tags:** htf-bias, routine, day-trading, scalping, top-down, ipda-data-ranges, workflow

## Definition

The ICT Day Trade Routine is the **ordered preparation sequence ICT states he runs before every
trading day** — the May-2017 mentorship answer to "what do you actually do each morning". It is
a *workflow*, not a setup: no entry rule appears anywhere in it. Its output is a set of framed
scenarios and levels, from which a separate pattern supplies the trade.

"I'm using what I just showed you here **in this order, in this manner, this routine**. I do
that very thing **every single trading day**" (49:32–49:41). And on the claimed precision: "when
I'm picking daily highs and lows and I'm getting really close to it, sometimes right to the pip
… **this is the procedure I'm using. There's nothing else that I'm doing that's secret**"
(41:14–41:30).

It is distinct from [top-down-analysis](top-down-analysis.md), the four-tier August-2017
protocol. Top-down analysis is a *staged bias derivation* run at four different cadences
(monthly, weekly, daily, intraday); this is a *single daily pass* that starts from the calendar
rather than from the monthly chart, and ends in scenario branches rather than in a bias. They
overlap at the daily and H4 tiers and disagree nowhere.

## Formal Criteria

**Step 1 — economic calendar first, not the chart**

- Read the calendar for **the next trading day**, at the end of the current session (00:23–00:46).
- Filter to **high- and medium-impact** events, then filter again by **time of day**: only
  events landing inside the London-open or New-York-open killzones matter, "because those are
  two dominant high-volume times of the day" (01:03–01:25).
- The event is treated as the **manipulation trigger**: "during London we're looking for the
  high or low of the day to form — it's usually under the guise of manipulation, so with that
  manipulation we know that generally it's going to be seen with an economic news release or
  some kind of **volatility injection**" (01:25–01:42).
- Output: **one pair and one time**. The worked example fixes EURUSD at **03:00 NY Tuesday**
  (Spanish flash CPI) — "the heart of the London open killzone" (01:48–02:23).

**Step 2 — the dollar index, before the pair**

- Daily chart. Establish the **IPDA data ranges** (below), mark every PD array, classify
  premium/discount, then read institutional order flow (02:44–17:44).
- Order flow is read off candle behaviour, not indicators: up candles that price moves away
  from are bearish order blocks and are being respected → "institutional order flow for the
  dollar index is what? **Bearish**" (16:16–16:46).

**Step 3 — IPDA data ranges: 60 / 40 / 20 trading days**

- Count **backwards from yesterday as day one**, "skipping Sundays, to get 60 days, then 40
  days and then 20 days — and there's your true IPDA data ranges" (06:02–06:11).
- **Sunday candles are excluded** as unreliable data; on a platform that prints them they must
  be counted out by hand (03:52–05:03).
- The ranges **roll**: "every new day, IPDA data ranges add one more day … and we cut off one
  day looking back, so it's always shifting dynamically forward" (06:19–06:32). ICT draws three
  boxes and slides them one day at a time.
- **Day trading works inside the 20-day range.** Fall back to the 40-day only if every array
  inside the 20 has already been consumed — "highly unlikely, but it can happen" (08:46–09:19).
- A **quarterly shift** is anticipated every three months as a possible structure change, "but
  we don't always expect it … it's not a panacea" (07:44–08:07).

**Step 4 — the pair, same treatment, then descend**

Daily → H4 → H1, each time: IPDA ranges → PD arrays → premium/discount → order flow. The
descent is explicitly *argumentative*, not confirmatory: "if I know the institutional order flow
on the daily chart is bullish, I want to **first make a case and argue that there's reasons for
them to want to take it down** to take out sell stops to accumulate new long positions"
(23:36–23:58). Where no such case can be built, the read flips: "if you **can't make a sound
argument** for entries based on that, then you have to start electing to say — okay, we are in a
premium market, maybe the market needs to go down into a discount" (28:38–28:50).

**Step 5 — M15 execution layer**

Only once a level is reached does the intraday layer go on (32:54–33:23, 40:38–41:07):

- **Standard deviations** of the [central-bank-dealers-range](../15-sessions/central-bank-dealers-range.md),
  the [asian-range](../14-asian-range/asian-range.md) and the [flout](../15-sessions/flout.md),
  projected above and below.
- **Average daily range**, layered on top.
- **The opening prices** — 0 GMT and **midnight New York**. ICT states a preference: "primarily
  that's what I like to do — use that **opening at midnight New York**" (46:05–46:20), because
  trading both invites overtrading (45:46–46:05).
- **The trigger condition is a confluence, not any single line:** "if there's a **confluence of
  those standard deviations, ADR and a PD array** on a 15-minute basis, or the 60-minute or
  4-hour PD arrays, then you know there's a high probability for price to want to expand"
  (40:48–41:14).
- Expected protraction size: "using the **33-pip** standard deviation that we expect from the
  opening price on a classic **100-pip day**" (46:52–47:02).

**Step 6 — weekly template, then daily template**

- Pick the weekly profile the week is fitting, then the day-of-week within it. Buy days run
  **Monday–Wednesday** when the daily order flow is bullish, and mirror for shorts (55:24–55:34).
- **The weekly template is not forecastable in advance:** "you're **never going to know** what
  weekly template it's going to unfold before Sunday's open" (44:19–44:28). It is a frame, not
  a prediction.
- ADR is the day's throttle: if ADR5 is under **60 pips** a large-range day is likely due
  (47:30–47:47); if ADR5 is **met before or at the New York open**, "we probably caught a tiger
  by the tail and we need to leave something on for that large range day to complete itself" —
  possibly running past London close to 13:00 or 14:00 (47:47–48:04).

## Formula / Math

```
# Step 1
events := calendar(D+1) filtered to {high, medium} impact
        filtered to time in london_open_KZ or new_york_open_KZ
target_pair, target_time := argmax(events)              # one pair, one time

# Step 3 — IPDA data ranges (day D-1 is day one; Sundays excluded)
days   := [d for d in trading_days descending from D-1 if weekday(d) != Sunday]
IPDA60 := days[0:60];  IPDA40 := days[0:40];  IPDA20 := days[0:20]
working_range := IPDA20                                  # IPDA40 only if IPDA20 exhausted
# rolls forward one day per day; the window length never changes

# Steps 2 and 4 — repeated per chart, DXY then pair, D -> H4 -> H1
for tf in [D, H4, H1]:
    mark_pd_arrays(tf); classify premium/discount; read institutional_order_flow(tf)

# Step 5 — M15 confluence gate
levels := SD(CBDR) + SD(asian_range) + SD(flout) + ADR5_bounds
trigger_zone := levels INTERSECT pd_array(M15 | H1 | H4)   # confluence required
reference    := open(00:00 NY)                             # preferred over 0 GMT
protraction  := ~33 pips on a ~100-pip ADR day

# Step 6
if ADR5 < 60 pips:            expect a large-range day is due
if ADR5 met by NY open:       hold a runner, extend beyond London close
```

## Machine-Readable

```json
{
  "id": "day-trade-routine",
  "category": "25-htf-bias",
  "aliases": ["ict-daily-routine", "day-trade-preparation-sequence", "scalping-routine"],
  "criteria": [
    {"id": "c1", "expr": "step1 == economic calendar for D+1, high/medium impact, filtered to London/NY killzone times"},
    {"id": "c2", "expr": "step1 output == exactly one pair and one time"},
    {"id": "c3", "expr": "step2 == dollar index daily analysed before the pair"},
    {"id": "c4", "expr": "ipda_data_ranges == last 60, 40, 20 trading days counting D-1 as day one, Sundays excluded"},
    {"id": "c5", "expr": "day_trading works inside IPDA20; IPDA40 only if IPDA20 arrays exhausted"},
    {"id": "c6", "expr": "ranges roll forward one day per day, fixed length"},
    {"id": "c7", "expr": "descent order == D -> H4 -> H1 -> M15, each with arrays + premium/discount + order flow"},
    {"id": "c8", "expr": "HTF order flow must be argued AGAINST before it is accepted"},
    {"id": "c9", "expr": "M15 trigger requires confluence of SD(CBDR|asian|flout) AND ADR AND a PD array"},
    {"id": "c10", "expr": "reference open == 00:00 America/New_York, preferred over 0 GMT"},
    {"id": "c11", "expr": "expected protraction ~33 pips on a ~100-pip ADR day"},
    {"id": "c12", "expr": "ADR5 < 60 pips => large-range day due; ADR5 met by NY open => hold a runner"},
    {"id": "c13", "expr": "weekly template is not forecastable before Sunday open"},
    {"id": "c14", "expr": "no entry rule is part of this routine"}
  ],
  "timeframes": ["M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["top-down-analysis", "daily-bias", "weekly-bias", "weekly-range-profiles", "ipda-data-range-calibration", "central-bank-dealers-range", "asian-range", "flout", "ict-day-trading-model", "london-session-avoidance", "pd-array-matrix", "true-day-open", "quarterly-shift-theory"],
  "sources": ["ICT-2017-DAYTRADE-ROUTINE"]
}
```

## Visual Pattern

```
  THE SEQUENCE — calendar first, chart last

  1  ECONOMIC CALENDAR (D+1)   high/medium impact, London KZ or NY KZ only
        └─► one pair, one time            e.g. EURUSD, 03:00 NY Tuesday
  2  DOLLAR INDEX, daily        IPDA 60/40/20 -> arrays -> premium/discount -> order flow
  3  THE PAIR, daily            same treatment
  4  H4                         argue the case AGAINST the daily order flow first
  5  H1                         locate the confluence level
  6  M15                        SD(CBDR) + SD(Asian) + SD(flout) + ADR + PD array
                                measured from the 00:00 NY open
  7  WEEKLY TEMPLATE            which profile is the week fitting?
  8  DAY-OF-WEEK TEMPLATE       Mon/Tue/Wed with the flow; scenario branches

  IPDA DATA RANGES — count back from YESTERDAY, skip Sundays, roll daily

     |<------------------------ 60 ------------------------>|
                     |<-------- 40 -------->|
                              |<--- 20 --->| <- day trading lives here
     ...  Sun  x  x  x  Sun  x  x  x  x  Sun  x  x  x  [D-1] [today]
          ^skip              ^skip           ^skip
```

## Timeframes

D and H4 for framing, H1 to locate, **M15** for the confluence layer. Weekly only as the
template check. ICT notes the pass takes a beginner "30, 40 minutes … every single day"
(52:14–52:19).

## Examples

**Example 1 — EURUSD into Tuesday 30 May 2017, the routine walked end to end (00:23–39:00):**
- *Calendar:* Spanish flash CPI, medium impact, **03:00 NY Tuesday** → EURUSD, inside the London
  open killzone.
- *DXY daily:* IPDA 60/40/20 marked; price in the **discount** of all three ranges; order flow
  **bearish**; premium arrays listed above (breaker low 98.53, fair value gap from 98.14).
- *EURUSD daily:* at a **premium** of the 20-day range, above an old high; discount arrays below
  (bullish order block, fair value gap, an old high at 110.15).
- *H4:* daily order flow bullish, so the case *for a decline* is built — equal lows below to
  sweep, then a bullish order block at 109.90.
- *H1:* the actual level — a fair value gap (111.30–111.36) overlapping a bullish order block,
  sitting **below the equal lows** at 111.62. "A convergence of two discount arrays right here,
  and it's below the equal lows" (32:09–32:19).
- *Branches, both written before the fact:* (a) price reaches 111.30–111.35 and holds → buy for
  a London day trade, continuation in New York, possible NY reversal at overhead resistance;
  (b) it fails → "you'll get immediate feedback by being stopped out", and the objective becomes
  110.20/110.00 — "over a hundred pips … **more range to work with, let's call it that, not
  profit**" (36:59–37:24, 54:16–54:25).
- *Calendar overlay:* Monday is a US bank holiday, so "**Tuesday becomes what would normally be
  a Monday**", pushing a possible reversal to **Wednesday** (57:16–57:34).

## Common Mistakes

- **Starting with the chart.** The calendar comes first and it selects the pair and the hour.
- **Skipping the dollar index.** It is analysed *before* the pair, not as a confirmation
  afterwards.
- **Counting Sundays into the IPDA ranges.** They are excluded; on platforms that print a Sunday
  candle they must be deducted by hand (03:52–05:03).
- **Counting today as day one.** "You **always count yesterday's day as one** and go backwards"
  (06:02).
- **Working in the 40- or 60-day range for day trades.** The 20-day is the day-trading range
  unless it is genuinely exhausted.
- **Treating HTF order flow as permission.** The routine requires arguing the *contrary* case
  first; where that case cannot be made, the bias itself is re-examined.
- **Acting on one standard-deviation line.** The gate is a **confluence** of deviations, ADR and
  a PD array — no single element is a signal.
- **Forecasting the weekly template.** Not possible before Sunday's open; the templates supply
  a frame to recognise, not a prediction to trade.
- **Expecting a mechanical output.** "If you're still looking for the **unicorn** … that's the
  type of trade you're looking for, and **they do not exist**" (48:38–48:55).
- **Reading a loss as failure of the routine.** "Smart money investors do not view a loss as a
  defeat — it's a **premium paid for greater insight**" (50:17–50:26).

## Related Concepts

- [top-down-analysis](top-down-analysis.md) — the August-2017 four-tier protocol; a staged bias derivation, where this is a single daily pass.
- [ipda-data-range-calibration](../23-ipda/ipda-data-range-calibration.md) — the 60/40/20 lookback in its own right.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — the April-2017 model this routine operationalises.
- [london-session-avoidance](../15-sessions/london-session-avoidance.md) — the stand-aside gates applied before step 5.
- [central-bank-dealers-range](../15-sessions/central-bank-dealers-range.md), [asian-range](../14-asian-range/asian-range.md), [flout](../15-sessions/flout.md) — the three overnight deviation inputs.
- [true-day-open](../22-quarterly-theory/true-day-open.md) — the 00:00 NY reference ICT prefers over 0 GMT.
- [weekly-range-profiles](weekly-range-profiles.md) — the templates step 6 selects from.
- [daily-bias](daily-bias.md), [weekly-bias](weekly-bias.md) — the outputs carried into the routine.
- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md) — the three-month structure change anticipated in step 3.
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md) — the array set marked at every tier.

## Citations

- `ICT-2017-DAYTRADE-ROUTINE` (00:14–00:28) "welcome back to **lesson 8 of the May 2017 ICT mentorship**, ICT amplified day trading and scalping — this lesson is the **ICT daily day trade routine**" — dates the source; (00:23–00:46) "the first thing I'd like to do is consider this **economic calendar for the next trading day**"; (01:03–01:25) "I want to take a look at the **times of those releases respective to the killzones** of London open and New York open, because those are two dominant **high-volume** times of the day"; (01:25–01:42) "during London we're looking for the high or low of the day to form — it's usually under the guise of **manipulation** … generally it's going to be seen with an economic news release or some kind of **volatility injection**"; (01:48–02:23) the Spanish flash CPI at **3 a.m. Tuesday** for EURUSD, "the **heart of the London open killzone**"; (02:44–02:56) "we first start with the **dollar index**"; (03:52–05:03) the ten Sunday candles deducted by hand; (06:02–06:11) "you **always count yesterday's day as one** and go backwards, **skipping Sundays**, to get 60 days, then 40 days and then 20 days — and **there's your true IPDA data ranges**"; (06:19–06:44) "every new day, IPDA data ranges add one more day … we cut off one day looking back, so it's **always shifting dynamically forward** … you can create a box like this and just simply **move the box one day forward**"; (07:44–08:07) "when we get to a new quarter or every three months, we anticipate a **shift in market structure** … but again it's **not a panacea**"; (08:46–09:19) "for day trading you're going to operate in **those last 20 days** most of the time … if we have already exhausted everything inside of the last 20 days … you would go back and look into the **last 40** trading days"; (16:16–16:46) "so institutional order flow for the dollar index is what? **Bearish**"; (20:57–21:07) "now we simply go down into a **4-hour** and we do the same thing"; (23:36–23:58) "I want to **first make a case and argue that there's reasons for them to want to take it down** to take out sell stops to accumulate new long positions"; (28:38–28:50) "if you **can't make a sound argument** for entries based on that, then you have to start electing to say — okay, we are in a **premium** market"; (32:09–32:19) "we have a **convergence of two discount arrays** right here, and it's **below the equal lows**"; (32:54–33:23) "we want to be in a **15-minute** time frame and look for our standard deviations — the **central bank dealer's range**, the **flout**, and **Asian range** standard deviations, and project them above and below"; (33:23–33:33) "we want to be looking at the opening price at **zero GMT** and the opening price at **midnight in New York**"; (36:59–37:24) "you'll get **immediate feedback by being stopped out** … then we'll anticipate price running below these lows, **not for a buying opportunity, but for targeting purposes**"; (40:38–41:14) "if there's a **confluence of those standard deviations, ADR and a PD array** on a 15-minute basis, or the 60-minute or 4-hour PD arrays, then you know there's a **high probability** for price to want to expand"; (41:14–41:30) "when I'm picking daily highs and lows and I'm getting really close to it, sometimes right to the pip … **this is the procedure I'm using. There's nothing else that I'm doing that's secret**"; (44:19–44:28) "you're **never going to know** what weekly template it's going to unfold **before Sunday's open**"; (45:46–46:20) "if you're going to trade at zero GMT every day … that creates and promotes **over-trading** … **primarily that's what I like to do — use that opening at midnight New York**"; (46:52–47:02) "using the **33-pip** standard deviation that we expect from the opening price on a classic **100-pip day**"; (47:30–48:04) "if the average daily range is smaller than **60 pips**, we know that there's going to be a likelihood of a **large range day** … if the average daily range is **met before New York or at New York's open**, we know that we probably **caught a tiger by the tail**"; (48:38–48:55) "if you're still looking for the **unicorn** … **they do not exist**"; (49:32–49:41) "I'm using what I just showed you here **in this order, in this manner, this routine** — I do that very thing **every single trading day**"; (50:17–50:26) "smart money investors do not view a loss as a defeat — **it's a premium paid for greater insight**"; (52:14–52:19) "for some of you it may take you **30, 40 minutes** to do this every single day"; (54:16–54:25) "over a hundred pips … **more range to work with, let's call it that, not profit**"; (55:24–55:34) "if institutional order flow is bullish we want to be looking to be a buyer **Monday, Tuesday, Wednesdays**"; (57:16–57:34) "**Monday is a U.S. holiday** … then **Tuesday becomes what would normally be a Monday** … so if we're going to see a reversal higher on euro after going down, it could happen on **Wednesday**".
