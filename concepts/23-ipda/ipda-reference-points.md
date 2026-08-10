# IPDA Reference Points

**Category:** 23-ipda
**Aliases:** IPDA references, IPDA anchors, algorithmic reference levels
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-IPDA-DATA-RANGES, ICT-2017-QUARTERLY-SHIFTS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ipda, references, anchors

## Definition

IPDA Reference Points are the **complete set of price levels the IPDA tracks for delivery decisions** — synthesizing the 20/40/60-day lookback extremes with structural pivots, session extremes, and PD arrays into a unified reference grid. ICT teaches IPDA reference tracking as a **multi-tier discipline**: at any moment, the algorithm has a hierarchy of reference points it can deliver toward, and the analyst's job is to identify which is the next target.

## Formal Criteria

The full IPDA reference set:

| Tier | Reference type | Examples |
|---|---|---|
| 1 | 20/40/60-day lookback extremes | ipda_20_high, ipda_40_low, etc. |
| 2 | Time-of-day pivots | TDO, TWO, PWH/PWL, PMH/PML |
| 3 | Structural pivots | unswept LTH/LTL on D/W/MN |
| 4 | PD arrays | unmitigated FVGs, OBs, breakers on HTF |
| 5 | Session extremes | Asia high/low, lunch high/low |

The "next algorithmic DOL" is selected from this set based on: HTF bias, current price position, recent setups.

## Formula / Math

```
ipda_reference_set(t) = union(
    ipda_lookback_extremes(t),
    time_of_day_pivots(t),
    htf_structural_pivots(t),
    htf_pd_arrays(t),
    session_extremes(t),
)

next_DOL := select(reference_set, criteria=[
    aligns_with_HTF_bias,
    not_yet_swept,
    closest_in_bias_direction
])
```

## Machine-Readable

```json
{
  "id": "ipda-reference-points",
  "category": "23-ipda",
  "aliases": ["IPDA-references", "IPDA-anchors", "algorithmic-reference-levels"],
  "criteria": [
    {"id": "c1", "expr": "5-tier reference set: lookback + TOD + structural + PD-array + session"},
    {"id": "c2", "expr": "next DOL selected from the set"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ipda-definition","ipda-data-ranges","ipda-20-day-lookback","ipda-40-day-lookback","ipda-60-day-lookback","time-of-day-pivots","draw-on-liquidity","htf-pd-array-hierarchy","liquidity-matrix"],
  "sources": ["ICT-2017-IPDA-DATA-RANGES","ICT-2017-QUARTERLY-SHIFTS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   IPDA reference grid (snapshot example):
   
   1.1180 ─── 60-day high (tier 1, untaken)
   1.1050 ─── 40-day high (tier 1, untaken)
   1.1000 ─── PWH (tier 2, untaken)
   1.0985 ─── 20-day high (tier 1, untaken)
   1.0950 ─── PDH (tier 2, untaken)
   1.0935 ─── H4 bearish FVG (tier 4, fresh)
   ─── current price 1.0855 ───
   1.0830 ─── H1 bullish OB (tier 4, fresh)
   1.0820 ─── PDL (tier 2, swept earlier)
   1.0790 ─── 20-day low (tier 1, untaken)
   1.0750 ─── 40-day low (tier 1)
   1.0700 ─── 60-day low (tier 1)
```

## Timeframes

All TFs.

## Examples

**Example 1 — selecting next DOL from reference grid:**
- HTF bias bullish.
- Reference grid as above; current price 1.0855.
- Closest unswept upside reference: PDH 1.0950 (tier 2).
- Next: 20-day high 1.0985 (tier 1).
- Then: PWH 1.1000 (tier 2), 40-day 1.1050, 60-day 1.1180.
- → DOL ladder: 1.0950 → 1.0985 → 1.1000 → 1.1050 → 1.1180.

## Common Mistakes

- **Tracking only one reference type.** Lookback extremes alone miss session-extreme and PD-array references; combine all 5 tiers.
- **Forgetting to update.** Once a reference is swept, it leaves the active set; the next-most-recent untaken reference takes over.
- **Treating all references equally.** Tier weights matter: 60-day extremes are stronger than session extremes.

## Related Concepts

- [ipda-definition](ipda-definition.md), [ipda-data-ranges](ipda-data-ranges.md), [ipda-20-day-lookback](ipda-20-day-lookback.md), [ipda-40-day-lookback](ipda-40-day-lookback.md), [ipda-60-day-lookback](ipda-60-day-lookback.md).
- [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md), [htf-pd-array-hierarchy](../05-pd-arrays/htf-pd-array-hierarchy.md), [liquidity-matrix](../02-liquidity/liquidity-matrix.md).

## Citations

- `ICT-2017-IPDA-DATA-RANGES` (81:03) — "It's January 12, 2017"; (27:52–28:27) "if you look back 60 days in the past, what was the highest high in the last 60 days? There's going to be buy stops above that high… Inside of the range of 20 days, 40 days, and 60 days."
- `ICT-2017-QUARTERLY-SHIFTS` (00:21) — "the January 2017 ICT Mentorship Long Term Analysis Lesson 1.1"; (22:22–23:41) "60 trading days, 40 trading days, and 20 trading days… and they're all trading days, not calendar days."
- `ICT-2022-MENTORSHIP-OVERVIEW` — the windows re-taught in the 2022 season.
