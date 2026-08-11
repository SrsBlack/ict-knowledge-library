# CBDR Projected Daily Range

**Category:** 15-sessions
**Aliases:** projecting daily highs and lows, protraction multiplier, CBDR range projection, IPDA projected daily range
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-PROJECTING-HIGHS-LOWS
**Tags:** sessions, cbdr, standard-deviations, projections, daily-range, day-trading

## Definition

The CBDR Projected Daily Range is ICT's method for calling the **second** extreme of the day
once the **first** has formed. It is not a second use of the plain
[central-bank-dealers-range](central-bank-dealers-range.md) standard-deviation ladder. The
input is the **distance price actually travelled** away from the CBDR to make the first
extreme — the protraction, i.e. the [judas-swing](../13-judas-swing/judas-swing.md) — expressed
as a whole number of CBDR standard deviations. That measured block is then **replicated from
the opposite edge of the CBDR** to locate the opposing extreme.

"You have to look at the range that is created by the central bank dealer's range
protractionary state — in other words, **how much of a standard deviation did we see**, because
**that becomes the known range to work with, and it becomes our multiplier as well** … all the
standard deviations it uses to make the high or low of the day in London — **that becomes your
measurement**" (09:38–10:14).

ICT presents it as previously withheld material: "some of those things that I've kept for a
long, long time … it's not common knowledge, it's not out there anywhere else" (04:39–05:09).

## Formal Criteria

**Qualification (unchanged from the CBDR page, restated here as a gate)**

- CBDR window **14:00 → 20:00 New York**; the range must be **under 40 pips**, "preferably
  20 to 30" (03:02–03:16). Over 40, "we move to the sidelines" (03:16–03:24).
- Measured on **bodies first**: "I like to look at the bodies — highest high in the form of an
  open or close and the lowest low in the form of an open or close, **not the wicks** … but I
  also do it on the wicks as well" (03:47–04:15). Bodies are the primary; wicks are run as a
  second pass.
- A range disqualifies on **both** measurements or neither — the 58-pip example is skipped
  "regardless if we used wicks as the high and low, or if we used the bodies" (11:55–12:10).
- A **directional bias must already exist** from the daily PD array matrix (24:46–25:12).

**The projection**

1. Wait for the first extreme (usually London) to form at a CBDR standard deviation.
2. Count the standard deviations consumed, **counting the CBDR itself as one**: "we're taking
   the total range used of all the standard deviations — one, two, three — **counting central
   bank dealer's range always**" (15:50–16:00).
3. Take that whole block as a single measurement.
4. **Project it from the opposite edge of the CBDR**, stacking it: "then project it from the
   low on sell days — it's one, two, three — and it gives you the **IPDA projected daily range
   low**" (16:03–16:10).
5. The result is a **price/time overlap**, not a price alone: read it against the London-close
   window (10:00 → 12:00 NY) and the 14:00 cap.

**Bounds**

- "Ideal scenarios are going to be seen with **no more than two standard deviations** … many
  times just one … but two is generally the rule of thumb", and "they generally don't like to
  go **beyond three**" (02:17–02:36).
- Typical London protraction is "an average about **33 pips** … it can be just six pips … but
  generally we allow up to 33", against an average daily range "about **100 pips**, not
  always" (29:18–29:31).
- **Time cap:** "**2 o'clock usually caps the high or low of the day**. If we go past noon New
  York time, we look for it to go to 2 o'clock and dribble down or run up until that specific
  time of the day" (11:26–11:52).

**Accuracy ICT claims for it**

- Hits quoted in the lesson: right to the pip; "we called 124.41 … it was **off by one pip**"
  (15:09–15:17); one standard deviation that "**misses it by two pips**" (16:46). He also
  concedes "sometimes it'll be just maybe five or six pips above" (24:16).
- **The arrays override the arithmetic.** "It's the **PD arrays that call the shot** — it's not
  the magic of these projections. These projections will lead you to an **overlap of time and
  price**" (22:08–22:18).
- The precision is one-sided: "the precision really is on the **entry side** — of the low on the
  buy days and the high on the sell days" (24:35–24:45).

## Formula / Math

```
# 1. qualify (bodies primary, wicks as a second pass)
CBDR_high := max(close, open) over 14:00-20:00 New York     # bodies
CBDR_low  := min(close, open) over 14:00-20:00 New York
R         := CBDR_high - CBDR_low
require R < 40 pips                                          # ideal 20..30

# 2. observe the protraction that made the FIRST extreme (usually London)
n := number of CBDR standard deviations consumed, CBDR itself counted as one
     # n in {1,2,3}; 2 is the working default, >3 is out of profile

# 3. the measured block
B := n * R

# 4. project from the OPPOSITE edge
sell_day:  projected_daily_low  := CBDR_low  - B     # high made above, low projected below
buy_day:   projected_daily_high := CBDR_high + B     # low made below, high projected above

# 5. read as a time/price overlap, not a price
expect fulfilment in [10:00, 12:00] New York; if unfulfilled by 12:00, cap at 14:00
```

## Machine-Readable

```json
{
  "id": "cbdr-projected-daily-range",
  "category": "15-sessions",
  "aliases": ["projecting-daily-highs-and-lows", "protraction-multiplier", "ipda-projected-daily-range"],
  "criteria": [
    {"id": "c1", "expr": "CBDR window == 14:00-20:00 America/New_York AND range < 40 pips"},
    {"id": "c2", "expr": "range measured on candle BODIES first, wicks as a second pass"},
    {"id": "c3", "expr": "n := standard deviations consumed making the first extreme, CBDR counted as one"},
    {"id": "c4", "expr": "B := n * CBDR_range"},
    {"id": "c5", "expr": "projected_opposite_extreme := opposite CBDR edge -/+ B"},
    {"id": "c6", "expr": "n in [1,3]; n == 2 typical; n > 3 out of profile"},
    {"id": "c7", "expr": "directional bias must pre-exist from the daily PD array matrix"},
    {"id": "c8", "expr": "PD array overrides the projection where they disagree"},
    {"id": "c9", "expr": "expected fulfilment window 10:00-12:00 NY, capped 14:00 NY"},
    {"id": "c10", "expr": "precision claimed on the entry side only (buy-day low / sell-day high)"}
  ],
  "timeframes": ["M15","M30","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["central-bank-dealers-range", "asian-range", "flout", "london-close", "judas-swing", "ict-day-trading-model", "pd-array-matrix", "filling-the-numbers", "ipda-true-day", "london-session-avoidance"],
  "sources": ["ICT-2017-PROJECTING-HIGHS-LOWS"]
}
```

## Visual Pattern

```
  SELL DAY — the high is made first, the low is projected

                            ── SD_up(2)  ◄── first extreme prints here, in London
                            │
                            │   n = 2 SDs consumed (CBDR counted as one)
   2pm ┌────────────┐ 8pm   │   B = 2 x R
       │    CBDR    │  R    │
       └────────────┘ ──────┘
            │
            │  replicate B downward from the CBDR LOW
            ▼
       ─ ─ ─ ─ ─ ─ ─   block 1
       ─ ─ ─ ─ ─ ─ ─   block 2
       ═══════════════ PROJECTED DAILY LOW
                       expected 10:00-12:00 NY, capped 14:00

  Buy day is the exact mirror: low first, high projected upward from the CBDR high.
```

## Timeframes

Marked on **M15–H1**. ICT does the measuring by hand — "yes, I do all this by hand"
(12:47) — by copying the range object and dragging duplicates with `Ctrl` held (12:56–13:11).

## Examples

**Example 1 — GBPJPY sell day, 2 SD (JKzEhfwV1dY, 08:23–15:17):**
- Setup: daily premium; price trades up into the **body of a daily bearish order block**
  (12593–12597) in London and turns.
- Count: the protraction into that high consumed **two** CBDR standard deviations.
- Projection: that two-SD block replicated below the CBDR low.
- Outcome: the London-close candle closes "right at two standard deviations … **boom, hits
  it**" (14:41–14:51); the day's low printed **124.40** against a called **124.41** — "off by
  one pip" (15:09–15:17).

**Example 2 — the skipped day (11:55–12:14):**
- Setup: CBDR measured **58 pips**.
- Trigger: none. "It doesn't make a difference … it's still **too much** of a central bank
  dealers range to use for our projections, so we have to **skip on this day**."
- Outcome: the day was traded off the daily bullish order block instead — the arrays still
  worked, the projection simply was not available.

**Example 3 — buy day capped by a fair value gap, not by the ladder (16:22–20:02):**
- Setup: price into a daily **bullish order block** stack; London swept one standard deviation
  down, "misses it by two pips".
- Projection: two SDs up gives the projected high.
- Trigger: a **23-pip fair value gap** (125.03 → 125.26) sat at that level.
- Outcome: price closed the gap "a pip or two above it" and stalled. Three SDs would have
  reached a bearish order block, "but we were getting close to the time window, so **two is
  about right**" — the array and the clock, not the ladder, set the stop point.

## Common Mistakes

- **Running it every day.** Named as the failure mode: "where this will get you in trouble is
  you're going to try to apply the standard deviations … **every single day**, and you're going
  to forget about the importance of having a range between 20 and 30 pips" (24:46–25:03).
- **Skipping the bias step.** "You have to have a **directional bias**" from the daily PD array
  matrix before the projection means anything (25:03–25:12).
- **Counting the standard deviations without counting the CBDR.** The CBDR block is always one
  of the *n* — "counting central bank dealer's range always" (15:57).
- **Treating the projection as a target in its own right.** It locates an overlap; the PD array
  decides. Where they disagree the array wins (22:08–22:18).
- **Expecting symmetry of precision.** The pip-accurate side is the *entry* side — the low on
  buy days, the high on sell days. The projected side is looser by design (24:35–24:45).
- **Using a >40-pip CBDR anyway.** Beyond 40 pips it "usually messes up the synchronisation for
  the London open killzone" (29:33–29:40); the whole method is off for that day.
- **Chasing the last pips.** "There's nothing wrong with leaving a little bit of that on the
  table, and if you're looking for that always, I'm not going to be able to help you with that
  measure of precision" (24:18–24:26).

## Related Concepts

- [central-bank-dealers-range](central-bank-dealers-range.md) — the range and the plain SD ladder this method consumes.
- [judas-swing](../13-judas-swing/judas-swing.md) — the protraction whose size is the multiplier.
- [asian-range](../14-asian-range/asian-range.md), [flout](flout.md) — the sibling overnight ranges run through the same deviation treatment.
- [london-close](london-close.md) — the 10:00–12:00 window the projection is expected to fill in.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — the April-2017 model this is lesson 4 of.
- [london-session-avoidance](london-session-avoidance.md) — lesson 6, the filters that decide whether the day qualifies at all.
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md) — the override.
- [filling-the-numbers](../04-time-cycles/filling-the-numbers.md), [ipda-true-day](../04-time-cycles/ipda-true-day.md) — the rest of the time-and-price frame.

## Citations

- `ICT-2017-PROJECTING-HIGHS-LOWS` (00:00–00:24) "welcome back folks to the **April 2017** ICT mentorship content — we're teaching ICT day trading model, this is **lesson [four]**, specifically teaching **projecting daily highs and lows**" — dates the source. ⚠ **Ordinal is ASR-ambiguous**: whisper renders the word as "lesson **for**". The number is fixed independently at (00:24), where ICT names the *preceding* lesson: "as we just mentioned in the **previous teaching, lesson number three**, central bank dealers range" — so this is lesson **four** by adjacency, not by a clean quote. The **year** is quoted verbatim and is not in doubt; (00:24–00:53) recap of lesson three, sell days up to three standard deviations, buy days down to three; (01:20–01:36) "we're looking specifically at the range that IPDA will go into protractionary state … in other words, **it's the Judas swing**"; (02:17–02:36) "ideal scenarios are going to be seen with **no more than two standard deviations** … two is generally the general rule of thumb … they generally don't like to go **beyond three**"; (03:02–03:24) CBDR 2 p.m.–8 p.m., "**less than 40 pips**, and again preferably **20 to 30** … we move to the sidelines … when the range is **greater than 40 pips**"; (03:47–04:15) "I like to look at the **bodies** — highest high in the form of an open or close and the lowest low in the form of an open or close, **not the wicks** … but I also do it on the wicks as well … I'm teaching it through the use of the bodies because **that's predominantly what I do**"; (04:39–05:09) "some of those things that I've kept for a long, long time … **it's not common knowledge, it's not out there anywhere else**"; (09:38–10:14) "you have to look at the range that is created by the central bank dealer's range **protractionary state** … **how much of a standard deviation did we see, because that becomes the known range to work with, and it becomes our multiplier as well** … all the standard deviations it uses to make the high or low of the day in London — **that becomes your measurement**"; (11:26–11:52) "**2 o'clock usually caps the high or low of the day** … if we go past noon New York time, we look for it to go to 2 o'clock and dribble down or run up"; (11:55–12:14) the **58-pip** CBDR — "regardless if we used wicks as the high and low, or if we used the bodies high and low, it doesn't make a difference … it's still **too much** … so we have to **skip on this day**"; (12:47–13:11) "yes, **I do all this by hand**" and the Ctrl-drag duplication method; (14:02–14:11) the London close window "closes it at noon … and it starts as early as **10 o'clock** in New York time"; (14:41–14:51) "the close on that candle stops **right at two standard deviations** … **boom, hits it**"; (15:09–15:17) "there's our projected low right here, **124.40** — we called **124.41**, so it was **off by one pip**"; (15:50–16:10) "we're taking the total range used of all the standard deviations — one, two, three — **counting central bank dealer's range always** … then project it from the low on sell days — one, two, three — and it gives you the **IPDA projected daily range low**"; (16:44–16:48) one standard deviation that "**misses it by two pips**"; (18:36–19:10) the **125.26 → 125.03**, **23-pip** fair value gap that capped the buy-day projection; (19:36–20:02) three SDs would have reached the bearish order block, "but we were getting close to the time window, so **two is about right**"; (22:08–22:18) "it's the **PD arrays that call the shot** — it's not the magic of these projections; these projections will lead you to an **overlap of time and price**"; (24:14–24:26) "sometimes you'll be just short one or two pips, and other times it'll be just maybe five or six pips above … **there's nothing wrong with leaving a little bit of that on the table**"; (24:35–24:45) "the precision really is on the **entry side** — of the low on the buy days and the high on the sell days"; (24:46–25:12) "where this will get you in trouble is you're going to try to apply the standard deviations … **every single day**, and you're going to forget about the importance of having a range between **20 and 30 pips** … and you have to have a **directional bias**"; (29:18–29:40) "average daily range is about **100 pips**, not always but generally, and we look for an average about **33 pips** for a protractionary state in London … it can be just six pips … but if we have a central bank dealer's range that's **greater than 40 pips**, it usually **messes up the synchronisation for the London open killzone**".
