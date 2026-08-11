# True Week Open (TWO)

**Category:** 22-quarterly-theory
**Aliases:** TWO, weekly true open, weekly opening price, Monday midnight open
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-TOPDOWN-SHORT-TERM, ICT-2017-CHARTER-OVERVIEW, ICT-2023-QUARTERLY-THEORY
**Tags:** quarterly-theory, true-week-open, weekly-opening-price, monday-midnight

⚠ **Body corrected 2026-08-11 — the page contradicted its own source.** It previously
offered **Sunday 18:00 NY** as the primary reading, with Monday 00:00 NY as a broker
variant. The primary source says the opposite: ICT carries the **Monday midnight New York**
open across the whole week and explicitly sets the Sunday portion aside for that purpose.
Sunday's open is retained — he watches *two* prices — but it is the secondary reference,
and **"18:00" appears nowhere in the corpus**; ICT only ever says "Sunday's opening price".

⚠ **The term "true week open" is not ICT's.** A corpus-wide search of all 153 mentorship
packets returns **0 hits** for `true week` and **0 hits** for `true weekly`. The *level* is
taught in detail; the *label* is community vocabulary back-formed from
[true-day-open](true-day-open.md), which ICT does name. See `## ICT vs Community`.

## Definition

The True Week Open is the **opening price of the week carried horizontally across every day
of that week** as a premium/discount reference, the way the [true-day-open](true-day-open.md)
is carried across a single day. ICT tracks **two** such prices and says so explicitly: "I have
**two opening prices** that I'm looking at for the weekly profile and weekly range — the
standard natural Sunday's opening price, and then I have midnight opening on Monday"
(`ICT-2017-TOPDOWN-SHORT-TERM`, 20:09–20:20).

Of the two, the one he defines operationally and projects forward is **Monday 00:00 New
York**: "I take that **Monday midnight open** … and I take it across the entire weekly, every
day, all throughout the entire week … So I'm **disregarding the entire first portion of the
trading that starts on Sunday**" (19:14–19:44). And, unambiguously: "whatever the opening
price is on the hourly at **midnight Monday** for whatever pair or market you're looking at,
**that's the opening price I use for the weekly**" (21:17–21:27).

It is a tier-3 input in the [top-down-analysis](../25-htf-bias/top-down-analysis.md)
protocol, and ICT states he uses the same price for
[power-of-three](../12-power-of-three/power-of-three.md) (19:45).

## Formal Criteria

- **Primary reference: the open at 00:00 New York on Monday.** Read it off the **hourly
  chart** — "easiest way to do it is get an hourly chart open" (21:17).
- **Secondary reference: Sunday's open**, "our natural opening to FX" (19:47–19:52). Retained
  as a second line, not as the projected one.
- **Projection: horizontal, across the entire week**, every day, not just Monday.
- **Directional use, gated on higher-timeframe bias:**
  - Bullish (monthly/weekly) → want price **below** those prices, "and seek some kind of a
    discount array" (20:41–20:51).
  - Bearish → want price **above** "both of those prices, or at least one of them that makes
    sense in terms of discount to premium" (20:55–21:05).
- The level is a **reference, not a trigger**. It sits between the weekly-profile forecast and
  the SMT-divergence check in the tier-3 sequence.

## Formula / Math

```
# primary — the one ICT projects across the week
two := open(H1 candle at 00:00 America/New_York, Monday)

# secondary — retained, not projected
sunday_open := open(first tick of the FX week, Sunday)

weekly_premium_vs_TWO  := price > two
weekly_discount_vs_TWO := price < two

# gated read (bias supplied by the monthly/weekly tiers, not by TWO)
bullish_target_zone := (price < two) AND at_discount_PD_array
bearish_target_zone := (price > two OR price > sunday_open) AND at_premium_PD_array
```

## Machine-Readable

```json
{
  "id": "true-week-open",
  "category": "22-quarterly-theory",
  "aliases": ["TWO", "weekly-true-open", "weekly-opening-price", "monday-midnight-open"],
  "criteria": [
    {"id": "c1", "expr": "two == open at 00:00 America/New_York on Monday, read on H1"},
    {"id": "c2", "expr": "projected horizontally across every day of the week"},
    {"id": "c3", "expr": "sunday_open tracked as a SECOND reference, not the projected one"},
    {"id": "c4", "expr": "bullish => want price < two at a discount array; bearish => price > two at a premium array"},
    {"id": "c5", "expr": "reference_only == true (not an entry trigger)"},
    {"id": "c6", "expr": "label 'true week open' absent from corpus; level taught, term not"}
  ],
  "timeframes": ["H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["quarterly-theory-overview","weekly-quarters","true-day-open","time-of-day-pivots","sunday-open-gap","nwog","htf-bias-framework","top-down-analysis","weekly-bias","power-of-three"],
  "sources": ["ICT-2017-TOPDOWN-SHORT-TERM","ICT-2017-CHARTER-OVERVIEW","ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   Two opening prices, one of them projected:

   Sun 18:00?  ← NOT in the corpus. ICT says "Sunday's opening price", no clock time.
        │
        ▼
   ░░░░░░░░░░  Sunday trading — "disregarding the entire first portion"
   ┌── Mon 00:00 NY ───────────────────────────────────────────────┐
   │                                                               │
   ═══════════════ TWO, carried across the whole week ═════════════  ← the projected line
   │   Mon      Tue      Wed      Thu      Fri                     │
   └───────────────────────────────────────────────────────────────┘

   bullish bias → want price BELOW the line, into a discount array
   bearish bias → want price ABOVE the line, into a premium array
```

## Timeframes

Read on **H1** (ICT's stated method), applied against H1/H4/D price action for the week.

## Examples

**Example 1 — ICT's stated procedure (`ICT-2017-TOPDOWN-SHORT-TERM`, 19:05–21:27):**
- Setup: monthly and weekly tiers have produced a **bearish** bias.
- Marking: on the hourly, take the open of the 00:00 NY Monday candle; also note Sunday's open.
- Trigger: "I want to see price trade up above both of those prices, or at least one of them
  that makes sense in terms of discount to premium" (20:55–21:05).
- Outcome: the rally above the line into a **premium PD array** is the short location; the
  opening price itself is never the entry.

## Common Mistakes

- **Using Sunday 18:00 as the level.** It is not in the corpus. If a broker's week opens
  Sunday evening, that price is ICT's *secondary* reference and it has no stated clock time.
- **Projecting Sunday's open instead of Monday's.** ICT projects the Monday midnight open
  across the week and sets the Sunday session aside when he does so.
- **Marking it only on Monday.** The whole point is that it is carried "every day, all
  throughout the entire week".
- **Trading the cross on its own.** Bias comes from the monthly and weekly tiers; the open is
  a location filter that must land on a PD array on the correct side.
- **Treating TWO as the weekly equilibrium.** It is the open, not the midpoint of the range.

## ICT vs Community

**The level is ICT's; the name is not.** Searching all 153 mentorship packets in `raw/` for
`true week` and `true weekly` returns **zero hits**. ICT's own vocabulary for this level is
"the weekly opening price", "Sunday's opening price" and "midnight opening on Monday".

"True Week Open" / "TWO" is community terminology, formed by analogy with ICT's own
[true-day-open](true-day-open.md) — a term he *does* use verbatim ("the IPDA true day",
`ICT-2017-DEFINING-DAILY-RANGE` 05:07). This library keeps the community label as the page
title because it is how readers will search for it, and records the divergence here rather
than implying ICT coined it. The same treatment is used on
[judas-swing-failure](../13-judas-swing/judas-swing-failure.md).

The **Sunday 18:00** clock time is a third-party addition — a platform convention from FX
brokers whose week opens at 17:00/18:00 NY. No ICT source in this corpus states it.

## Related Concepts

- [true-day-open](true-day-open.md) — the daily analogue, and the term this label was formed from.
- [top-down-analysis](../25-htf-bias/top-down-analysis.md) — the tier-3 step this level belongs to.
- [weekly-bias](../25-htf-bias/weekly-bias.md) — supplies the direction the level is read against.
- [power-of-three](../12-power-of-three/power-of-three.md) — ICT states he uses the same Monday open for PO3.
- [quarterly-theory-overview](quarterly-theory-overview.md), [weekly-quarters](weekly-quarters.md), [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md), [sunday-open-gap](../31-models/sunday-open-gap.md), [nwog](../31-models/nwog.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-TOPDOWN-SHORT-TERM` (00:00) "welcome back to **lesson three** for the **August 2017** ICT mentorship content" — dates the source; (19:05–19:12) "the main thing I'd like to focus in on is that weekly opening. The weekly opening price on Sunday, I start there, but I also look at **the midnight opening price on Monday**"; (19:14–19:44) "I take that **Monday midnight open** and I take that opening price and **I take it across the entire weekly, every day, all throughout the entire week** … **So I'm disregarding the entire first portion of the trading that starts on Sunday**, and I'm looking at exactly when Monday begins in the States, the US, at midnight, that opening price"; (19:45) "I use that also for **Power 3** as well"; (19:47–19:56) "I use Sunday's opening price — that's our **natural opening to FX** — and/or I use the Monday opening price at midnight"; (20:09–20:20) "so I have **two opening prices** that I'm looking at for the weekly profile and weekly range: the standard natural Sunday's opening price, and then I have midnight opening on Monday"; (20:41–20:51) "if I'm bullish, preferably I want to see price go down below those prices and **seek some kind of a discount array**"; (20:55–21:05) "if I'm bearish … I want to see price trade up **above both of those prices, or at least one of them** that makes sense in terms of discount to premium"; (21:17–21:27) "easiest way to do it is get an **hourly chart** open, and whatever the opening price is on the hourly at **midnight Monday** for whatever pair or market you're looking at, **that's the opening price I use for the weekly**".
- `ICT-2017-CHARTER-OVERVIEW` — general weekly-opening reference; carries no clock time for the Sunday open.
- `ICT-2023-QUARTERLY-THEORY` — 2023 restatement in the quarterly-theory framing.
