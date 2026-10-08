# Judas Swing

**Category:** 13-judas-swing
**Aliases:** Judas, opening Judas, false-direction open, betrayal swing
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PROTRACTION, ICT-2017-MARKET-REVERSALS, ICT-2017-BREAD-BUTTER-BUY, ICT-2017-INTRADAY-PROFILES, ICT-2022-MENTORSHIP-EP21, ICT-2022-MENTORSHIP-EP24, ICT-2022-MENTORSHIP-EP25
**Tags:** judas, manipulation, sweep, foundational

## Definition

A Judas swing is the **deceptive opening move at the start of a session** that goes in the opposite direction of the session's true intended delivery. ⚠ **The "New Testament betrayal" naming is a library gloss, not in corpus** — searched `betray|testament|bible` over both corpora: zero hits. The Judas swing is ICT's name for the manipulation phase ([manipulation-phase](../12-power-of-three/manipulation-phase.md)) at the session-open scale. It is most commonly observed at the London open ([london-judas-swing](london-judas-swing.md)) but also appears at the NY AM open ([ny-judas-swing](ny-judas-swing.md)).

**There are four session Judas swings, not two.** `ICT-2017-MARKET-REVERSALS` enumerates them in one sentence: "we can reduce it to the London open for Judas, the CME open for the New York Judas, and Asia it has its Judas at eight o'clock and then New York time or … zero GMT, and then you have it also in London close on days that create London close reversals" [28:07]. The generalisation is stated outright in the companion lecture — "that's the Judas swing for the New York session, so that **every session has a protractionary market stage**" (`ICT-2017-BREAD-BUTTER-BUY` [20:29], cited on [ny-judas-swing](ny-judas-swing.md)). See [asia-judas-swing](asia-judas-swing.md) and [london-close-judas-swing](london-close-judas-swing.md); the London-close instance is the one that does **not** fit the definition above, because it extends the day's direction rather than opposing it.

⚠ **Dating corrected 2026-08-09.** This page previously carried `Year Introduced: 2018`. The
**September-2016** mentorship lecture on market protraction uses the term directly — "we see
that as market protraction **or a Judas swing**; it's a false rally to sell into"
(`ICT-2016-PROTRACTION`, 06:40) and again at 09:50 — and describes the London instance in full.
The term is therefore in use in 2016, and the year has been corrected. See
[market-protraction](market-protraction.md) for the parent concept.

## Formal Criteria

A canonical Judas swing requires:

- ⚠ **Not measured from "the first 15–60 minutes of the killzone."** Not in either
  corpus — searched `15 minutes|first hour|first 30|thirty minutes|60 minutes` within
  120 characters of `judas|protraction`: zero hits. ICT measures the Judas from a
  **session opening price**, and the anchor differs by session: London — the
  **midnight NY open** (normal profile: "we're looking at 12 a.m. for a classic London
  protraction or Judas swing," `ICT-2017-INTRADAY-PROFILES` 18:42; "if you're bullish in
  London you're looking for New York midnight candle and price trading lower after,"
  `ICT-2017-BREAD-BUTTER-BUY` 20:42), with the delayed case occurring "between 2 o'clock
  and 3 a.m." (`ICT-2017-INTRADAY-PROFILES`, 21:25) rather than anchored to a second
  opening price; New York — the **08:20 CME open** ("using the 820 a.m. New York time
  for CME," `ICT-2017-BREAD-BUTTER-BUY` 19:04; "if you're bullish in New York you're
  looking for 820 and the Judas swing dropping down after 820," 20:35) or, in the 2022
  indices teaching, the **08:30 opening price** (ep21 [15:58]), with a separate episode
  describing the Judas as occurring **at the 09:30 equities open** rather than naming
  09:30 itself an opening-price anchor ("i'm waiting for that judas swing to happen
  where it drops down at 9 30," ep24 [05:59]); Asia — "that is the Judas swing at zero
  GMT or Asia's open" (`ICT-2017-BREAD-BUTTER-BUY`, 21:11). A directional move away from
  that opening price is the Judas, not a fixed clock window after the killzone starts.
- That directional move sweeps a known liquidity pool (typically the prior session's range bound — Asian range high/low for London Judas; lunch range or NY AM range for NY-PM Judas).
- A **reversal** within the same killzone in the opposite direction.
- The reversal usually displaces and leaves a fair value gap that becomes the entry zone.
  ⚠ **ERA-SPLIT on the entry mechanic.** The 2022 teaching ties the reversal directly
  to an FVG-plus-market-structure-shift sequence: "judas swing that fake rally up …
  then it creates the pattern that's in the mentorship fair value gap market structure
  shift then starts to show displacement" (ep25 [32:46–33:13]). The 2017 teaching
  instead enters on a PD-array retracement measured in CBDR deviations: "You're going
  to be looking for an intraday premium PDRA to short on inside that retracement"
  (`ICT-2017-INTRADAY-PROFILES`, 09:29); "reach down one to two standard deviations in
  the central bank dealer's range. And that will be your projected low" (13:37). Both
  are recorded; the FVG-market-structure-shift version is 2022-specific, not a
  restatement of the 2017 mechanic.
- The reversal direction aligns with HTF bias (the actual draw on liquidity).

## Formula / Math

```
judas_swing(session) :=
  session_open_price     = midnight NY (London normal)   # delayed case occurs 02:00-03:00 NY,
                                                            # a WINDOW, not a second opening price
                            | 08:20 CME (NY, 2017) | 08:30 (NY indices, 2022; occurs at 09:30 per ep24)
                            | 00:00 GMT (Asia)
  initial_move_direction = direction(session_open_price -> first swing)
  swept_liquidity        = pool taken during initial_move
  reversal_direction     = opposite of initial_move_direction
  reversal_aligns_with_HTF_bias == true
  displacement_after_reversal == true
  fvg_in_reversal == true   # 2022 teaching ties this to an MSS; 2017 enters on a CBDR-deviation PD array instead
```

## Machine-Readable

```json
{
  "id": "judas-swing",
  "category": "13-judas-swing",
  "aliases": ["judas", "opening-judas", "false-direction-open", "betrayal-swing"],
  "criteria": [
    {"id": "c1", "expr": "initial_move_measured_from_session_opening_price, NOT a fixed 15-60min killzone window"},
    {"id": "c2", "expr": "initial_move_sweeps_known_pool == true"},
    {"id": "c3", "expr": "reversal_within_same_killzone == true"},
    {"id": "c4", "expr": "reversal_aligns_with_HTF_bias == true"},
    {"id": "c5", "expr": "displacement_with_fvg_after_reversal == true (2022: FVG+MSS sequence; 2017: CBDR-deviation PD array retracement)"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["london-judas-swing","ny-judas-swing","asia-judas-swing","london-close-judas-swing","judas-swing-failure","manipulation-phase","liquidity-sweep","asian-range-sweep","power-of-three"],
  "sources": ["ICT-2016-PROTRACTION","ICT-2017-MARKET-REVERSALS","ICT-2017-BREAD-BUTTER-BUY","ICT-2017-INTRADAY-PROFILES","ICT-2022-MENTORSHIP-EP21","ICT-2022-MENTORSHIP-EP24","ICT-2022-MENTORSHIP-EP25"]
}
```

## Visual Pattern

```
   session_open
       │
       ↓
       █  Judas swing (initial fakeout direction)
       █
       █  ← sweeps prior pool
   ────█──── (e.g. asian_low)
                          ↑
                          █  reversal back through range
                          █  (true direction = HTF bias)
                          █  + FVG inside
                          █
                          → continues to HTF DOL
```

## Timeframes

M1 / M5 / M15 — the Judas itself plays out as a move away from the session's opening price (not a fixed clock window; see Formal Criteria).

## Examples

**Example 1 — bullish-bias London Judas:**
- HTF bias bullish; Asian range 1.0848–1.0876.
- 02:30 NY (LO-KZ): M5 wicks 1.0846 (Asian SSL swept), closes 1.0853.
- 02:55–03:10: M5 displaces 18 pips up, FVG at 1.0858–1.0862.
- 03:20: returns to FVG; long entry triggered.
- 04:30: takes 1.0900 PDH BSL.
- → textbook Judas: down-then-up matching HTF bullish bias.

## Common Mistakes

- **Trading the Judas direction itself.** The Judas IS the trap; you're meant to enter on the *reversal*, not the initial fakeout.
- **No bias filter.** A Judas swing without HTF bias confirmation is just chop. The reversal direction MUST agree with HTF.
- **Wrong session.** Judas usually means "London open Judas." NY AM has a smaller-scale Judas; PM session sometimes has a lunch-Judas. Specify which.
- **Applying the "opposes delivery" rule to London close.** Three of the four session Judas swings fake against the coming move. The London-close one is described as "the opposite" — a post-10:00 extension that prints the day's extreme and is then faded (`ICT-2017-BREAD-BUTTER-BUY` [21:19–21:43]). See [london-close-judas-swing](london-close-judas-swing.md).
- **Late identification.** By the time the Judas + reversal + FVG are all visible, the high-conviction entry window may have closed; entries on FVG retest are the standard play.
- **Anchoring the Judas to a fixed "15–60 minute" window after the killzone opens.** Not in corpus. ICT anchors it to the session's **opening price** — midnight NY for London, 08:20 CME (2017) or 08:30/09:30 (2022 indices) for New York, 00:00 GMT for Asia — and measures the move from there, however long it takes.
- **Treating the 2022 FVG-plus-MSS entry as a restatement of the 2017 mechanic.** The 2017 teaching enters on a PD-array retracement measured in CBDR standard deviations; the 2022 teaching enters on a fair-value-gap-after-market-structure-shift sequence. Both are ICT's words, in different eras — don't present one as "the" entry trigger.

## Related Concepts

- [london-judas-swing](london-judas-swing.md), [ny-judas-swing](ny-judas-swing.md), [asia-judas-swing](asia-judas-swing.md), [london-close-judas-swing](london-close-judas-swing.md), [judas-swing-failure](judas-swing-failure.md) — variant deep dives, one per session.
- [manipulation-phase](../12-power-of-three/manipulation-phase.md), [power-of-three](../12-power-of-three/power-of-three.md) — broader AMD framing.
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [asian-range-sweep](../14-asian-range/asian-range-sweep.md) — sweep mechanics.
- [london-open-killzone](../10-killzones/london-open-killzone.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md) — typical killzones.

## Citations

- `ICT-2017-MARKET-REVERSALS` (28:07) — the four-session enumeration: "the London open for Judas, the CME open for the New York Judas, and Asia it has its Judas at eight o'clock and then New York time or … zero GMT, and then you have it also in London close on days that create London close reversals."
- `ICT-2016-PROTRACTION` (06:32–06:49) "if we see a movement higher and we're bearish, we see that as market protraction or a Judas swing; it's a false rally to sell into"; (09:50) "in the next London session, it's in Judas swing lower or market protractionary phase" — the earliest use of the term located in the corpus, which is why this page is dated 2016 rather than 2018.
- `ICT-2017-BREAD-BUTTER-BUY` (19:04) "using the 820 a.m. New York time for CME"; (20:29) "that's the Judas swing for the New York session, so every session has a protractionary market stage"; (20:35) "if you're bullish in New York you're looking for 820 and the Judas swing dropping down after 820"; (20:42) "if you're bullish in London you're looking for New York midnight candle and price trading lower after"; (21:11) "that is the Judas swing at zero GMT or Asia's open"; (21:19–21:43) London-close Judas described as "the opposite," extending rather than opposing the day's direction.
- `ICT-2017-INTRADAY-PROFILES` (09:29) "You're going to be looking for an intraday premium PDRA to short on inside that retracement"; (12:04) "if we do not see an immediate decline from 12 a.m. New York down into 2 a.m. New York, this is not going to be a London normal protraction buy day"; (13:37) "reach down one to two standard deviations in the central bank dealer's range. And that will be your projected low"; (18:42) "So we're looking at 12 a.m. for a classic London protraction or Judas swing"; (21:25) "So between 2 o'clock and 3 a.m., that Judas swing should occur."
- `ICT-2022-MENTORSHIP-EP21` (15:58) "the opening price at 8 30 i use that for again power 3 for the new york session … i want to see a move above that's what i dub a judas swing."
- `ICT-2022-MENTORSHIP-EP24` (05:59) "i'm waiting for that judas swing to happen where it drops down at 9 30."
- `ICT-2022-MENTORSHIP-EP25` (32:46–33:13) "judas swing that fake rally up … then it creates the pattern that's in the mentorship fair value gap market structure shift then starts to show displacement."
