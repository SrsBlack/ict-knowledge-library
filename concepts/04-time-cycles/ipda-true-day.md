# IPDA True Day

**Category:** 04-time-cycles
**Aliases:** interbank trading day, IPDA trading day, true day, midnight-to-3pm day, ICT daily range frame
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-DEFINING-DAILY-RANGE
**Tags:** time, true-day, ipda, killzones, daily-range, session-times

⚠ **Transcription artifact.** The whisper transcript of this packet renders **IPDA** as
"IPTA" (and sometimes as "if the") throughout. Quotes below normalise it to IPDA; every
other word is verbatim.

## Definition

The IPDA True Day is ICT's **replacement for the retail 24-hour trading day**: the interval
from **00:00 to 15:00 New York time**, inside which the daily open, high, low and close are
framed. Its stated justification is reference-frame alignment — "if it's going to be a high
probability trade scenario … it stands to reason we have to start with the **same reference
point that IPDA itself, the interbank price delivery algorithm, uses in referencing time**"
(01:11–01:28).

The same lesson fixes every other time anchor in the April-2017 day-trading model, and ICT
labels it the settled version: "this is the **definitive teaching** … this is the only one
you'll ever need to refer to, so **if you've seen anything different in the past, this is the
real one**" (02:13–02:27).

⚠ **The killzone times here differ from the 2016/2022 set carried on
[killzone-times-table](../10-killzones/killzone-times-table.md).** London opens at **01:00**,
not 02:00, and New York runs **07:00–10:00**, not 08:00–11:00. ICT rejects the later reading
by name in this lesson — see `## Common Mistakes`.

## Formal Criteria

**The interval**

- **IPDA true day = 00:00 → 15:00 New York.** "Every day at 12 a.m. midnight New York time
  begins the IPDA true day … every day at **3 p.m.** New York time ends the IPDA true day"
  (05:07–05:38).
- ICT calls 15:00 the **"New York close"**: "when I say New York close, I'm referring to the
  IPDA true day close" (09:13).
- **Rationale for 15:00** — "because **bonds close**, and the influence that interest rates
  have on the currency markets will have ended by then" (09:48). The final hour also absorbs
  the news: "the last hour, **2 o'clock to 3 p.m.** New York time, will always encapsulate any
  movement that's related to FOMC … generally the move is ended, or the bulk of the move is
  ended, by 3 p.m." (09:53–10:13).

**The anchors inside it (all New York time, DST-adjusted)**

| Window | Time | ICT's wording |
|---|---|---|
| Asian range | **20:00 → 00:00** | "every day at 8 p.m. … begins the Asian range; every day at midnight … ends the Asian range" (02:27–02:41) |
| ICT London killzone | **01:00 → 05:00** | "every day at 1 a.m. … begins the London killzone; every day at 5 a.m. … ends the London killzone" (03:06–03:24) |
| London lunch | **05:00 → 07:00** | "this area here between the London and New York killzones — this is London lunch" (07:47) |
| ICT New York killzone | **07:00 → 10:00** | "every day at 7 a.m. … begins the New York killzone; every day at 10 a.m. … ends the New York killzone" (03:57–04:17) |
| CME open | **08:20** | "I want to add the 8:20 a.m. New York time — this is the CME open" (07:17) |
| ICT London close killzone | **10:00 → 12:00** | "every day at 10 a.m. … begins the London close killzone; every day at 12 p.m. noon New York time ends the London close killzone" (04:31–04:39) |
| IPDA true day close | **15:00** | (05:29–05:38) |

**Operating rules**

- **Clock, not broker.** "You have to have a **New York time clock** — either on your
  smartphone they give you an opportunity to do world clocks. Whatever the time is in New
  York, use the times I'm giving you" (03:35–03:50).
- **DST is absorbed, not adjusted for.** "Always in whatever New York time is — whether it's
  daylight savings time or regular time — this is the times I'm using" (04:55). See
  [dst-handling](dst-handling.md).
- **London lunch is a stand-down window.** "Generally when we're **not looking for any major
  significant price moves** — usually the market goes quiet, or continues in the path that is
  set for London open" (07:47).
- **The frame is read with [power-of-three](../12-power-of-three/power-of-three.md).**
  "Framing the day like this you can clearly see, using **power 3**, the open at midnight"
  (08:04). The output is "how you frame the entire daily range — **open, high, low and
  close**" (10:21).

## Formula / Math

```
# all times America/New_York, DST included (no manual offset)
ipda_true_day   := [00:00, 15:00]

asian_range     := [20:00, 24:00]        # previous calendar evening
london_kz       := [01:00, 05:00]
london_lunch    := [05:00, 07:00]
ny_kz           := [07:00, 10:00]
cme_open        := 08:20                 # point in time, not a window
london_close_kz := [10:00, 12:00]

day_open  := open (00:00)
day_close := close(15:00)                # "New York close" == IPDA true day close
day_high  := max(high) over ipda_true_day
day_low   := min(low)  over ipda_true_day
```

## Machine-Readable

```json
{
  "id": "ipda-true-day",
  "category": "04-time-cycles",
  "aliases": ["interbank-trading-day", "ipda-trading-day", "true-day", "ict-daily-range-frame"],
  "criteria": [
    {"id": "c1", "expr": "ipda_true_day == [00:00, 15:00] America/New_York"},
    {"id": "c2", "expr": "asian_range == [20:00, 24:00]"},
    {"id": "c3", "expr": "london_killzone == [01:00, 05:00]"},
    {"id": "c4", "expr": "london_lunch == [05:00, 07:00]"},
    {"id": "c5", "expr": "ny_killzone == [07:00, 10:00]"},
    {"id": "c6", "expr": "cme_open == 08:20"},
    {"id": "c7", "expr": "london_close_killzone == [10:00, 12:00]"},
    {"id": "c8", "expr": "times are NY wall clock; DST absorbed, not offset"},
    {"id": "c9", "expr": "close_rationale == bond_close AND FOMC_absorbed_by_14:00-15:00"},
    {"id": "c10", "expr": "supersedes the 02:00 London / 08:00 New York killzone reading for the 2017 model"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["true-day-open", "killzone-times-table", "london-open-killzone", "ny-am-killzone", "london-close-killzone", "asia-killzone", "asian-range", "central-bank-dealers-range", "ny-lunch", "dst-handling", "power-of-three", "ict-day-trading-model", "filling-the-numbers", "ny-judas-swing"],
  "sources": ["ICT-2017-DEFINING-DAILY-RANGE"]
}
```

## Visual Pattern

```
  THE IPDA TRUE DAY — 00:00 to 15:00 New York
  (the retail 00:00-24:00 day is discarded)

  20:00 ──── 00:00 ── 01:00 ──── 05:00 ── 07:00 ─ 08:20 ─ 10:00 ── 12:00 ──── 15:00
   │  Asian   │        │  London  │ London │  New York KZ  │ London  │        │
   │  range   │        │   KZ     │ lunch  │               │ close   │        │
   └──────────┤        └──────────┘        └──── ▲ ────────┴─ KZ ────┘        │
              │                                CME                            │
              │                                open                           │
              ├────────────── IPDA TRUE DAY ─────────────────────────────────►┤
            OPEN                                                            CLOSE
                                                              (bonds close; FOMC
                                                               absorbed 14:00-15:00)
```

## Timeframes

Marked on **M15/H1** for the windows themselves; the resulting open/high/low/close frame is
read on the **daily**. Not applicable above the daily.

## Examples

**Example 1 — GBPUSD, Monday 3 April 2017, ICT's own walkthrough (05:48–09:13):**
- Setup: a true day framed from the 00:00 open to the 15:00 close.
- Sequence: open at midnight → small decline inside the Asian range (the PO3 open) → rally
  through Asian-range resistance → **high of the day at 01:00, the start of the London
  killzone**, with a second high "at 5 a.m., at the very end of London killzone, exactly
  right there" (08:16–08:44).
- New York: a short-term high forms inside the NY killzone, and **the low of that killzone
  forms at 08:20, the CME open** — "draw straight up with your imagination and it goes right
  to that little short-term low, and price rallies away from that. **That is not randomness**"
  (07:17, 08:44).
- Outcome: London close makes the low of the day; price consolidates and closes off the low
  at 15:00 (09:13).

## Common Mistakes

- **Using the retail 24-hour day.** The MT4 `Ctrl+Y` period separators frame a different day:
  "the retail version of the 24-hour trading day is **not what we focus on**" (00:50), and
  charts carrying those separators are "pretty much a classic **telltale sign** they have no
  idea what they're doing" (01:36–01:49).
- **Starting London at 02:00, 03:00 or 04:00.** ICT names this error directly in this lesson:
  "folks that are using my **free tutorials**, they're waiting for 2 o'clock, 3 o'clock or 4
  o'clock — **this is the actual killzone I use**, so the time window begins at **1 a.m.**, it
  ends at 5 a.m." (08:16). The 02:00–05:00 window on
  [london-open-killzone](../10-killzones/london-open-killzone.md) is the 2016/2022 public
  formulation, not the 2017 mentorship one.
- **Running the New York killzone to 11:00.** In this lesson it is **07:00–10:00**. The
  08:00–11:00 window is again the later public set.
- **Treating 15:00 as arbitrary.** It is the bond close, chosen so the interest-rate influence
  and any 14:00 FOMC reaction are inside the day rather than after it.
- **Manually offsetting for DST.** The times are New York wall clock; if the clock says 1 a.m.
  in New York, it is the London killzone open, summer or winter.
- **Trading London lunch.** 05:00–07:00 is explicitly a quiet or continuation window.

## Related Concepts

- [true-day-open](../22-quarterly-theory/true-day-open.md) — the 00:00 anchor this interval opens on.
- [killzone-times-table](../10-killzones/killzone-times-table.md) — the reference card, which carries the later 2016/2022 windows; this page is the 2017 divergence.
- [london-open-killzone](../10-killzones/london-open-killzone.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [london-close-killzone](../10-killzones/london-close-killzone.md), [asia-killzone](../10-killzones/asia-killzone.md) — the four windows, per-page.
- [asian-range](../14-asian-range/asian-range.md) — the 20:00–00:00 leg.
- [central-bank-dealers-range](../15-sessions/central-bank-dealers-range.md) — the 14:00–20:00 window immediately preceding it.
- [ny-lunch](../15-sessions/ny-lunch.md) — the *New York* lunch, distinct from the London lunch named here.
- [dst-handling](dst-handling.md) — why no manual offset is applied.
- [power-of-three](../12-power-of-three/power-of-three.md) — the shape read across the interval.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — the April-2017 model this lesson supplies the clock for.
- [filling-the-numbers](filling-the-numbers.md), [ny-judas-swing](../13-judas-swing/ny-judas-swing.md) — where inside the frame the levels and the 08:20 protraction sit.

## Citations

- `ICT-2017-DEFINING-DAILY-RANGE` (00:14) "okay welcome back folks, this is **lesson two of the April 2017 ICT mentorship** content dealing with ICT day trading model — this lesson is **defining the daily range**"; (00:50–01:11) "the **retail version of the 24-hour trading day is not what we focus on** … the interbank 24-hour IPDA trading day is very different"; (01:11–01:28) "if it's going to be a high probability trade scenario that we're going to be looking for, it stands to reason we have to start with the **same reference point that IPDA itself, the interbank price delivery algorithm, uses in referencing time**"; (01:36–01:49) "when we see these retail delineations … that's pretty much a **classic telltale sign** they have no idea what they're doing"; (02:13–02:27) "**this is the definitive teaching** … this is the only one you'll ever need to refer to, so if you've seen anything different in the past, **this is the real one**"; (02:27–02:41) "every day at **8 p.m.** Eastern Standard Time in New York time, this begins the Asian range; every day at **midnight** … ends the Asian range"; (03:06–03:24) "the ICT London killzone — every day at **1 a.m.** … begins the London killzone; every day at **5 a.m.** … ends the London killzone"; (03:35–03:50) "you have to have a **New York time clock**"; (03:57–04:17) "the ICT New York killzone — every day at **7 a.m.** … begins the New York killzone; every day at **10 a.m.** … ends the New York killzone"; (04:31–04:39) "the ICT London killzone for **London close** — every day at **10 a.m.** … begins the London close killzone; every day at **12 p.m. noon** New York time ends the London close killzone"; (04:55) "always in whatever New York time is, whether it's **daylight savings time or regular time**, this is the times I'm using"; (05:07–05:29) "the IPDA true day definition — **every day at 12 a.m. midnight New York time begins the IPDA true day**. This is the beginning of the 24-hour interbank trading day"; (05:29–05:38) "**every day at 3 p.m. New York time ends the IPDA true day**"; (05:48–06:11) "a true day for a **Monday, April 3rd 2017** … the true day open at midnight and Monday true day close at 3 p.m. New York time"; (07:17–07:37) "I want to add the **8:20 a.m.** New York time — **this is the CME open** … draw straight up with your imagination and it goes right to that little short-term low, and price rallies away from that. **That is not randomness**"; (07:47) "this area here between the London and New York killzones — **this is London lunch** — this is generally when we're **not looking for any major significant price moves**"; (08:04) "framing the day like this you can clearly see, using **power 3**, the open at midnight"; (08:16) "folks that are using my **free tutorials**, they're waiting for 2 o'clock, 3 o'clock or 4 o'clock — **this is the actual killzone I use**, so the time window begins at **1 a.m.**, it ends at 5 a.m."; (08:44) "look at the low that forms in the actual New York killzone — **it forms at 8:20, CME open**"; (09:13) "**when I say New York close, I'm referring to the IPDA true day close**"; (09:48) "**because bonds close**, and the influence that interest rates have on the currency markets will have ended by then"; (09:53–10:13) "the last hour, **2 o'clock to 3 p.m.** New York time, will always **encapsulate any movement that's related to FOMC** … no matter what happens in FOMC, generally the move is ended, or the bulk of the move is ended, **by 3 p.m.**"; (10:21) "that's how you frame the **entire daily range — open, high, low and close**". ⚠ Whisper renders IPDA as "IPTA"/"if the" throughout; normalised in the quotes above.
