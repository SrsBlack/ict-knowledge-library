# Distribution Phase

**Category:** 12-power-of-three
**Aliases:** D-phase, distribution, true delivery, expansion phase
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PO3, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** po3, amd, distribution

## Definition

The **distribution phase** is the third phase of the PO3 / AMD cycle: the **true intended directional delivery** toward HTF DOL. Following the manipulation reversal, distribution is the phase where institutions deliver the move they accumulated for — typically the largest, fastest, displacement-rich part of the cycle. Daily-scale distribution = NY AM session.

## Formal Criteria

- Occurs after manipulation reversal.
- Direction: aligned with HTF bias.
- Wide bodies, displacement candles, FVGs, structure breaks (BOS in trend direction).
- Often produces the daily HOD (MMBM) or LOD (MMSM).
- Time-of-day correspondence: NY AM (intraday), session Q3 (90-min), week's Q3 = Wednesday.

## Formula / Math

```
distribution_phase := after_manipulation_reversal
                      AND directional_alignment_with_HTF_bias
                      AND wide_body_displacement_candles
                      AND FVGs_and_BOS_present
                      AND moves_toward_DOL
```

Equivalent to [range-expansion](../01-market-structure/range-expansion.md) at the price-action level.

## Machine-Readable

```json
{
  "id": "distribution-phase",
  "category": "12-power-of-three",
  "aliases": ["D-phase", "distribution", "true-delivery", "expansion-phase"],
  "criteria": [
    {"id": "c1", "expr": "after_manipulation == true"},
    {"id": "c2", "expr": "directional_with_HTF_bias == true"},
    {"id": "c3", "expr": "displacement_candles_with_FVG == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["power-of-three","accumulation-phase","manipulation-phase","intraday-amd","htf-amd","range-expansion","ny-am-session","ny-am-killzone","draw-on-liquidity"],
  "sources": ["ICT-2016-PO3","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   distribution in MMBM (bullish daily):

   accumulation → manipulation reversal → DISTRIBUTION
                                                ▲
                                               ▲▲
                                              ▲▲▲   ← wide bodies
                                             ▲▲▲▲   ← displacement
                                            ▲▲▲▲▲   ← FVGs forming
                                           ▲▲▲▲▲▲   ← BOS through HTF DOL
```

## Timeframes

M5–D.

## Examples

**Example 1 — daily distribution (MMBM):**
- After Asian-low Judas swept, M5 displaces up 18 pips at 03:05 NY (post-manipulation).
- 04:00–11:00 NY: H1 prints 60-pip green candle, breaks PDH BSL by 09:30.
- 10:00–11:00: NY AM SB extends to PWH at 1.0975 (HOD).
- → distribution complete; daily candle prints clean bullish body.

## Common Mistakes

- **Late entries during distribution.** By the time displacement is visible, the optimal entry (post-manipulation FVG) may already be filled. Late chasing in distribution gets stopped on retracements.
- **Confusing exhaustion with distribution.** A move that's been distributing for 4–6 hours often exhausts; the last-leg displacement may fail and reverse.

## Related Concepts

- [power-of-three](power-of-three.md), [accumulation-phase](accumulation-phase.md), [manipulation-phase](manipulation-phase.md), [intraday-amd](intraday-amd.md), [htf-amd](htf-amd.md), [range-expansion](../01-market-structure/range-expansion.md), [ny-am-session](../15-sessions/ny-am-session.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md).

## Citations

- `ICT-2016-PO3`, `ICT-2022-MENTORSHIP-OVERVIEW`.
