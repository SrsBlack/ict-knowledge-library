# NDOG (New Day Opening Gap)

**Category:** 31-models
**Aliases:** NDOG, daily session-reopen gap (term unverified)
**ICT Confidence:** medium
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-NDOG-NWOG, ICT-2022-MENTORSHIP-EP11, ICT-2022-MENTORSHIP-EP34, ICT-2022-MENTORSHIP-EP19, ICT-2016-VACUUM-BLOCK
**Tags:** model, opening-gap, unverified-term

⚠ **WRONG time anchor — corrected 2026-10-08 per audit.** This page previously anchored the daily
gap at 17:00 NY close → 00:00 NY midnight (the True Day Open). Every daily-opening-gap passage
located in the corpus instead places the gap at the **~18:00 NY futures session reopen**, not
midnight — midnight appears only ever as an **opening price** in the corpus, never as a gap
boundary. `ndog|new day opening gap|midnight gap|daily open gap` has 0 hits in either corpus; the
term and its 2023 date remain unverified. "~70% fill same day" had no corpus support and is
removed.

## Definition

No source in this library names or dates "NDOG," and **neither corpus instance located here is
an ordinary Monday–Thursday daily reopen gap** — both are special sessions. The clearest is a
Monday bank-holiday abbreviated session: "now on monday it was a bank holiday and trading stops
at one o'clock in the afternoon on holidays generally and resumes around six o'clock in the
afternoon[,] new york time" (`ICT-2022-MENTORSHIP-EP11` [04:01]); "monday again was a holiday so i
knew i had abbreviated session hours so it's going to close at one o'clock" (`ICT-2022-MENTORSHIP-EP11`
[19:04]). That session's reopen gap: "it opened up six o'clock in [N]ew [Y]ork time[,] opened up
and slammed down accelerating lower... you have a big gap here[;] it's likely to come back and
rebalance that and fill it in[,] and it does" (`ICT-2022-MENTORSHIP-EP11` [19:59]). The second
instance is the **Sunday weekly reopen**, not a daily one: "a gap when the session started again
last night[,] my local time[,] about six o'clock" (`ICT-2022-MENTORSHIP-EP34` [00:06]) — the same
gap ICT elsewhere calls "the opening gap on sunday" (`ICT-2022-MENTORSHIP-EP34` [09:31]; see
[nwog](nwog.md)). **No ordinary daily reopen gap is described in either corpus; the "six o'clock"
NY clock is the stated reopen time for both of these special sessions only, not for an everyday
Tuesday–Thursday reopen.** Separately, **midnight NY is never described as a gap boundary in the
corpus — only as an opening price**: "new york midnight candle opening price[,] opportunity
again... it trades up into the new york midnight opening candle[,] trades back into another gap"
(`ICT-2022-MENTORSHIP-EP19` [103:45]) — the gap in that sentence is a separate FVG the price later
reaches, not a midnight gap itself. On FX, where price trades continuously through 00:00 NY in
ICT's framing, a "17:00 close vs. 00:00 open" span is seven hours of ordinary traded range, not a
gap.

## Formal Criteria

- **Neither corpus-located gap is an ordinary daily reopen.** One is a Monday bank-holiday
  abbreviated-session reopen (`ICT-2022-MENTORSHIP-EP11`); the other is the Sunday weekly reopen
  (`ICT-2022-MENTORSHIP-EP34`, shared territory with [nwog](nwog.md)). Both happen to reopen
  "around six o'clock in the afternoon[,] new york time" (`ICT-2022-MENTORSHIP-EP11` [04:01]), but
  no statement generalizes this to every weekday.
- Boundary convention by analogy with the general breakaway-gap framing (not NDOG-specific): "the
  opening of the gapped up candle and the close of the up candle right before the gap forms"
  (`ICT-2016-VACUUM-BLOCK` [10:15]).
- No stated fill-rate or fill-window statistic exists for this pattern in either corpus.
- Functions as the daily analogue of the vacuum block / opening-gap reference: "a vacuum block is
  nothing more than a breakaway gap" (`ICT-2016-VACUUM-BLOCK` [12:48]); "not all gaps fill
  completely" (`ICT-2016-VACUUM-BLOCK` [12:58]).

## Formula / Math

```
# ICT gives no "17:00 close -> 00:00 open" gap rule, and no rule for an ORDINARY daily reopen.
# The two corpus-confirmed instances are both special sessions (a Monday bank-holiday abbreviated
# session, and the Sunday weekly reopen shared with nwog.md):

session_close  = last trade before the special-session halt   # ~13:00 NY on the bank-holiday case
session_reopen = first trade after the halt                    # ~18:00 NY, stated "six o'clock"

gap_size = abs(session_reopen - session_close)
gap_dir  = "bullish" if session_reopen > session_close else "bearish"

# Midnight NY (00:00) is an opening price in the corpus, never a gap boundary — do not model a
# midnight-anchored gap on this source set, especially not on FX. ICT gives no fill-rate number.
```

## Machine-Readable

```json
{
  "id": "ndog",
  "category": "31-models",
  "aliases": ["NDOG", "session-reopen-gap (term unverified)"],
  "criteria": [
    {"id": "c1", "expr": "UNVERIFIED term; corpus has only 2 special-session reopens (bank-holiday Monday, Sunday weekly), not an ordinary daily reopen, and neither is 17:00-close-to-midnight"},
    {"id": "c2", "expr": "midnight NY = opening price in corpus, never a gap boundary"},
    {"id": "c3", "expr": "no corpus fill-rate statistic"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["nwog","sunday-open-gap","true-day-open","vacuum-block","time-of-day-pivots"],
  "sources": ["ICT-2023-NDOG-NWOG","ICT-2022-MENTORSHIP-EP11","ICT-2022-MENTORSHIP-EP34","ICT-2022-MENTORSHIP-EP19","ICT-2016-VACUUM-BLOCK"]
}
```

## Visual Pattern

```
   2022 Monday bank-holiday abbreviated-session precursor (not a corpus-named "NDOG", and NOT an
   ordinary daily reopen — see Definition):

   last trade before the holiday-session halt (~13:00 NY) ──── level A
                                    ▲
                                    █  ← gap at the session reopen
                                    █     (NOT at midnight NY)
   ~18:00 NY session reopen  ──── level B
                                    ↓
                                    "likely to come back and rebalance that and fill it in"
                                    (`ICT-2022-MENTORSHIP-EP11` [19:59])
```

## Timeframes

M15 / H1 / H4 / D, by analogy with the two special-session reopen examples. Not stated by name,
and not stated for an ordinary daily reopen.

## Examples

**Example 1 — 2022 Monday bank-holiday abbreviated-session reopen gap (not a corpus-named "NDOG",
not an ordinary daily reopen):**
- Monday is a bank holiday; the session closes early at 13:00 NY and reopens at 18:00 NY: "now on
  monday it was a bank holiday and trading stops at one o'clock in the afternoon on holidays
  generally and resumes around six o'clock in the afternoon[,] new york time"
  (`ICT-2022-MENTORSHIP-EP11` [04:01]).
- Price opens with a gap and continues lower: "it opened up six o'clock in [N]ew [Y]ork time[,]
  opened up and slammed down accelerating lower" (`ICT-2022-MENTORSHIP-EP11` [19:59]).
- ICT states the gap is "likely to come back and rebalance that and fill it in[,] and it does"
  (`ICT-2022-MENTORSHIP-EP11` [19:59]) — same session, not stated as a probability.

## Common Mistakes

- **Presenting either corpus instance as an ordinary daily reopen gap.** One is a Monday
  bank-holiday abbreviated session (`ICT-2022-MENTORSHIP-EP11` [04:01], [19:04]); the other is the
  Sunday weekly reopen (`ICT-2022-MENTORSHIP-EP34` [00:06], shared territory with [nwog](nwog.md)).
  No ordinary Tuesday–Thursday daily reopen gap is described in either corpus.
- **Anchoring this gap at 17:00 NY close → 00:00 NY midnight.** Not in the corpus.
- **Treating midnight NY as a gap boundary, especially on FX.** The corpus never describes a
  midnight gap; midnight is only ever an opening price (`ICT-2022-MENTORSHIP-EP19` [103:45]), and
  FX trades continuously through it in ICT's framing — a 17:00→00:00 span there is ordinary
  traded range, not a gap.
- **Using a stated fill statistic ("~70% same day").** No such number exists in the corpus.
- **Citing "NDOG" as confirmed 2022/2023 ICT vocabulary.** 0 hits in either corpus.

## Related Concepts

- [nwog](nwog.md), [sunday-open-gap](sunday-open-gap.md), [true-day-open](../22-quarterly-theory/true-day-open.md), [vacuum-block](../07-order-blocks/vacuum-block.md), [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md).

## Citations

- `ICT-2023-NDOG-NWOG` — registry stub, no video, no quotation behind it. Retained only as the
  claimed-origin pointer for the term; not corpus-evidenced.
- `ICT-2022-MENTORSHIP-EP11` — Monday bank-holiday abbreviated session stated explicitly [04:01];
  same-session reopen gap and rebalance [19:30]–[19:59].
- `ICT-2022-MENTORSHIP-EP34` — The Sunday weekly reopen gap, not a daily one [00:06].
- `ICT-2022-MENTORSHIP-EP19` — Midnight NY as an opening price, not a gap boundary [103:45].
- `ICT-2016-VACUUM-BLOCK` — "Month 04 — ICT Vacuum Block" (Dec 2016). General breakaway-gap
  boundary convention by analogy [10:15]; vacuum-block/breakaway-gap link [12:48]; no guaranteed
  full fill [12:58].
