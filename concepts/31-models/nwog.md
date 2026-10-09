# NWOG (New Week Opening Gap)

**Category:** 31-models
**Aliases:** NWOG, weekly gap, weekend gap, Sunday session gap
**ICT Confidence:** medium
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-NDOG-NWOG, ICT-2022-MENTORSHIP-EP11, ICT-2022-MENTORSHIP-EP34, ICT-2022-MENTORSHIP-EP14, ICT-2017-DAYTRADE-ROUTINE
**Tags:** model, weekend-gap, unverified-term

⚠ **UNVERIFIABLE (term) per 2026-10-08 audit.** `nwog|new week opening gap|weekend gap` has
**zero hits** in either corpus (153 2016-17/2020-21 packets, 40 captioned 2022 Mentorship episodes); the
term and its 2023 date are consistent with, but not confirmed by, this library's material. The
2022 precursor located is on **index futures**, not FX, and anchors to the **session reopen
(~18:00 NY, "six o'clock")**, not to a stated 17:00 NY Friday close — the page's prior FX-first
framing and specific clock times have been corrected below. "Fills within 1–2 trading days" /
"~75%" had no corpus support and are removed.

## Definition

No source in this library names or dates "NWOG." The nearest 2022 precursor is the gap on CME
index futures between Friday's last trade and the Sunday-evening session reopen, treated as a
level for the coming week: "we had a gap when the session started again last night[,] my local
time[,] about six o'clock" (`ICT-2022-MENTORSHIP-EP34` [00:06], ES); "i'm looking for a gap fill
from friday's close[,] so i'm going to go long here[,] 12 micros of the... micro [N]asdaq futures
contract" (`ICT-2022-MENTORSHIP-EP14` [00:01]). ICT treats it as a level, not just a historical
mark: "the opening gap on sunday[,] if you put it in your charts and just plot it across the
entire week[,] you'll see that many times there's a lot of valuation around that gap[,] so it'll
be treated as a dynamic price level[;] if it's above it[,] look for it to act as support"
(`ICT-2022-MENTORSHIP-EP34` [09:31]); "if it's below it[,] look for it to act as resistance"
(`ICT-2022-MENTORSHIP-EP34` [10:00]). The "six o'clock" reopen is confirmed in NY time elsewhere
in the same 2022 corpus: "resumes around six o'clock in the afternoon[,] new york time"
(`ICT-2022-MENTORSHIP-EP11` [04:01]). **ERA-SPLIT:** in May-2017 ICT instead downplayed Sunday
gaps for FX day trading: "But in here we have a Sunday gap. Okay, so it's going to be less likely
to be that much in terms of an influence.... Now for those without Sunday candles, you wouldn't
have this on your chart at all." (`ICT-2017-DAYTRADE-ROUTINE` [11:31]–[12:01]).

## Formal Criteria

- Reference boundary 1: last traded price before the weekend close.
- Reference boundary 2: first traded price at the next session's reopen.
- **2022 corpus example is futures, anchored at the session reopen "six o'clock" (~18:00 NY)**,
  not a stated 17:00 NY Friday close — see Common Mistakes.
- Zone boundary convention (close-to-open on the gap-forming candle) follows the general
  breakaway-gap framing: "[t]he opening of the gapped up candle and the close of the up candle
  right before the gap forms" (`ICT-2016-VACUUM-BLOCK` [10:15]) — not a NWOG-specific statement,
  offered here only by analogy since no NWOG-specific boundary rule exists.
- No stated fill-rate, fill-window, or reliability statistic exists in either corpus.

## Formula / Math

```
# ICT gives no exact clock boundary for "NWOG" by this name. The nearest corpus anchors are:
session_close  = last trade before the weekend break      # Friday, time not stated for FX
session_reopen = first trade of the new week               # "six o'clock" NY on index futures, 2022

gap_size = abs(session_reopen - session_close)
gap_dir  = "bullish" if session_reopen > session_close else "bearish"

# ICT gives no number for fill-rate or fill-window — see Common Mistakes.
```

## Machine-Readable

```json
{
  "id": "nwog",
  "category": "31-models",
  "aliases": ["NWOG", "weekend-gap", "Sunday-session-gap"],
  "criteria": [
    {"id": "c1", "expr": "UNVERIFIED term; 2022 precursor = gap between weekend close and next-session reopen"},
    {"id": "c2", "expr": "corpus example is index futures at ~18:00 NY reopen, not a stated FX 17:00 close"},
    {"id": "c3", "expr": "no corpus fill-rate or fill-window statistic"}
  ],
  "timeframes": ["H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["ndog","sunday-open-gap","true-week-open","vacuum-block","time-of-day-pivots"],
  "sources": ["ICT-2023-NDOG-NWOG","ICT-2022-MENTORSHIP-EP11","ICT-2022-MENTORSHIP-EP34","ICT-2022-MENTORSHIP-EP14","ICT-2017-DAYTRADE-ROUTINE"]
}
```

## Visual Pattern

```
   2022 index-futures precursor (illustrative, not a "NWOG"-named example):

   Friday last trade ──── level A
                                    ▲
                                    █
                                    █  ← gap zone
                                    █
   Sunday ~18:00 NY reopen ──── level B
                                    ↓
                                    treated as support/resistance for the coming week
                                    (`ICT-2022-MENTORSHIP-EP34` [09:31]-[10:00])
```

## Timeframes

H1 / H4 / D, by analogy with the 2022 precursor's use as a weekly level. Not stated by name.

## Examples

**Example 1 — 2022 index-futures precursor (not a corpus-named "NWOG"):**
- ES gaps at the Sunday ~18:00 NY session reopen.
- ICT treats the gap as a level for the week, support if price sits above it, resistance if below
  (`ICT-2022-MENTORSHIP-EP34` [09:31]–[10:00]).
- Some weeks the gap is not revisited: "sometimes the week will just run away from it and won't
  really come back to it[,] but in weeks where there's consolidation[,] like [F]OMC[,] we have
  that... to deal with" (`ICT-2022-MENTORSHIP-EP34` [10:25]).

## Common Mistakes

- **Citing "NWOG" as confirmed 2022/2023 ICT vocabulary.** 0 hits in either corpus; treat the term
  and its date as unverified.
- **Using a stated fill statistic ("1–2 days," "~75%").** No such number exists in the corpus; the
  only stated tendency is that some weeks never revisit the gap (`ICT-2022-MENTORSHIP-EP34` [10:25]).
- **Anchoring the futures close at "16:00 NY."** ICT's own 2022 examples give the reopen as "six
  o'clock," i.e. the session restarting after the weekend (Sunday) halt — or, in ep11, a holiday halt — not a 16:00 close boundary.
- **Treating Sunday gaps as uniformly important.** ICT's May-2017 statement downplays them for FX
  day trading, in contrast with the 2022 index-futures weekly-level usage — state both eras, do
  not collapse them (see Definition).

## Related Concepts

- [ndog](ndog.md), [sunday-open-gap](sunday-open-gap.md), [true-week-open](../22-quarterly-theory/true-week-open.md), [vacuum-block](../07-order-blocks/vacuum-block.md), [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md).

## Citations

- `ICT-2023-NDOG-NWOG` — registry stub, no video, no quotation behind it. Retained only as the
  claimed-origin pointer for the term; not corpus-evidenced.
- `ICT-2022-MENTORSHIP-EP11` — States the Sunday/holiday reopen clock explicitly in NY time
  [04:01].
- `ICT-2022-MENTORSHIP-EP34` — Session-reopen gap as a weekly dynamic level [00:06], [09:31],
  [10:00], [10:25].
- `ICT-2022-MENTORSHIP-EP14` — Gap-fill-from-Friday's-close trade example on index futures [00:01].
- `ICT-2017-DAYTRADE-ROUTINE` — "Month 09 — ICT Day Trade Routine" (May 2017). Era-split: Sunday
  gaps downplayed for FX day trading [11:31]–[12:01].
