# Judas Swing

**Category:** 13-judas-swing
**Aliases:** Judas, opening Judas, false-direction open, betrayal swing
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2016-PROTRACTION
**Tags:** judas, manipulation, sweep, foundational

## Definition

A Judas swing is the **deceptive opening move at the start of a session** that goes in the opposite direction of the session's true intended delivery. Named for the New Testament betrayal — the move "betrays" inattentive traders into committing to the wrong direction before the algorithm reverses and runs the actual delivery. The Judas swing is ICT's name for the manipulation phase ([manipulation-phase](../12-power-of-three/manipulation-phase.md)) at the session-open scale. It is most commonly observed at the London open ([london-judas-swing](london-judas-swing.md)) but also appears at the NY AM open ([ny-judas-swing](ny-judas-swing.md)).

⚠ **Dating corrected 2026-08-09.** This page previously carried `Year Introduced: 2018`. The
**September-2016** mentorship lecture on market protraction uses the term directly — "we see
that as market protraction **or a Judas swing**; it's a false rally to sell into"
(`ICT-2016-PROTRACTION`, 06:40) and again at 09:50 — and describes the London instance in full.
The term is therefore in use in 2016, and the year has been corrected. See
[market-protraction](market-protraction.md) for the parent concept.

## Formal Criteria

A canonical Judas swing requires:

- A session open with a clear directional move in the **first 15–60 minutes** of the killzone.
- That directional move sweeps a known liquidity pool (typically the prior session's range bound — Asian range high/low for London Judas; lunch range or NY AM range for NY-PM Judas).
- A **reversal** within the same killzone in the opposite direction.
- The reversal usually displaces and leaves a fair value gap that becomes the entry zone.
- The reversal direction aligns with HTF bias (the actual draw on liquidity).

## Formula / Math

```
judas_swing(session) :=
  initial_move_direction = direction(open of KZ -> first 15-60 min)
  swept_liquidity        = pool taken during initial_move
  reversal_direction     = opposite of initial_move_direction
  reversal_aligns_with_HTF_bias == true
  displacement_after_reversal == true
  fvg_in_reversal == true
```

## Machine-Readable

```json
{
  "id": "judas-swing",
  "category": "13-judas-swing",
  "aliases": ["judas", "opening-judas", "false-direction-open", "betrayal-swing"],
  "criteria": [
    {"id": "c1", "expr": "session_opens_with_initial_move == true"},
    {"id": "c2", "expr": "initial_move_sweeps_known_pool == true"},
    {"id": "c3", "expr": "reversal_within_same_killzone == true"},
    {"id": "c4", "expr": "reversal_aligns_with_HTF_bias == true"},
    {"id": "c5", "expr": "displacement_with_fvg_after_reversal == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["london-judas-swing","ny-judas-swing","judas-swing-failure","manipulation-phase","liquidity-sweep","asian-range-sweep","power-of-three"],
  "sources": ["ICT-2016-PROTRACTION", "ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
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

M1 / M5 / M15 — the Judas itself usually plays out in the first 15–60 minutes of the killzone.

## Examples

**Example 1 — bullish-bias London Judas:**
- HTF bias bullish; Asian range 1.0848–1.0876.
- 02:30 NY (LO-KZ): M5 wicks 1.0846 (Asian SSL swept), closes 1.0853.
- 02:55–03:10 (macro): M5 displaces 18 pips up, FVG at 1.0858–1.0862.
- 03:20: returns to FVG; long entry triggered.
- 04:30: takes 1.0900 PDH BSL.
- → textbook Judas: down-then-up matching HTF bullish bias.

## Common Mistakes

- **Trading the Judas direction itself.** The Judas IS the trap; you're meant to enter on the *reversal*, not the initial fakeout.
- **No bias filter.** A Judas swing without HTF bias confirmation is just chop. The reversal direction MUST agree with HTF.
- **Wrong session.** Judas usually means "London open Judas." NY AM has a smaller-scale Judas; PM session sometimes has a lunch-Judas. Specify which.
- **Late identification.** By the time the Judas + reversal + FVG are all visible, the high-conviction entry window may have closed; entries on FVG retest are the standard play.

## Related Concepts

- [london-judas-swing](london-judas-swing.md), [ny-judas-swing](ny-judas-swing.md), [judas-swing-failure](judas-swing-failure.md) — variant deep dives.
- [manipulation-phase](../12-power-of-three/manipulation-phase.md), [power-of-three](../12-power-of-three/power-of-three.md) — broader AMD framing.
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [asian-range-sweep](../14-asian-range/asian-range-sweep.md) — sweep mechanics.
- [london-open-killzone](../10-killzones/london-open-killzone.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md) — typical killzones.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — Judas swing terminology refined.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational framework for Judas + reversal entry.
- `ICT-2016-PROTRACTION` (06:32–06:49) "if we see a movement higher and we're bearish, we see that as market protraction or a Judas swing; it's a false rally to sell into"; (09:50) "in the next London session, it's in Judas swing lower or market protractionary phase" — the earliest use of the term located in the corpus, which is why this page is dated 2016 rather than 2018.
