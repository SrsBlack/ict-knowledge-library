# AMD on Intraday

**Category:** 24-amd-cycle
**Aliases:** intraday AMD cycle, daily AMD cycle
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PO3, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** amd, intraday, foundational

## Definition

AMD on intraday — the cycle applied at the daily-and-below scale: daily session structure (Asia-London-NY), 6-hour Quarterly Theory blocks, 90-minute cycles. Cycle-side companion to [intraday-amd](../12-power-of-three/intraday-amd.md), which covers the same content from the PO3 / market-maker angle.

## Formal Criteria

Cycle scales (intraday only):

- **Daily** — Asia (A), London open KZ (M), NY AM (D), NY PM (X).
- **6-hour** — within a session-quarter, 4 sub-90-minute mini-cycles.
- **90-minute** — within a 90-min window, 4 mini-quarters of ~22.5 min each (A/M/D/X).

Multiple scales run concurrently — a 90-min cycle inside a 6-hour cycle inside a daily cycle.

## Formula / Math

```
intraday_amd_scales = {
  daily:        ~24 hours,
  6_hour:       ~6 hours (yearly Q1/Q2/Q3/Q4 of the day's clock),
  90_min:       ~90 minutes,
  22_5_min:     ~22.5 minutes (mini-quarters within 90 min)
}
```

## Machine-Readable

```json
{
  "id": "amd-on-intraday",
  "category": "24-amd-cycle",
  "aliases": ["intraday-AMD-cycle", "daily-AMD-cycle"],
  "criteria": [
    {"id": "c1", "expr": "AMD at daily, 6-hour, 90-min, 22.5-min scales"},
    {"id": "c2", "expr": "scales run concurrently"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["amd-cycle-overview","amd-on-htf","amd-vs-po3","intraday-amd","power-of-three","90-minute-cycle","quarterly-shift-theory"],
  "sources": ["ICT-2016-PO3","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   intraday AMD scales (concurrent):

   Daily:         A───────M───D───X───
   6-hour:        |─Q1─Q2─Q3─Q4─|─Q1─Q2─Q3─Q4─|
   90-minute:     |a-m-d-x|a-m-d-x|...
   
   Multiple cycles fire at the same time at different fractal levels.
```

## Timeframes

M5–H4.

## Examples

**Example 1 — concurrent cycles:**
- Daily: in distribution phase (NY AM, 09:30 NY).
- 6-hour Q3 (06:00–12:00 NY): mid-distribution.
- 90-min cycle (09:00–10:30): in M phase (manipulation, sweep just occurred).
- 22.5-min mini-Q within that 90-min: in D mini-phase.
- → multi-scale alignment for high-conviction long.

## Common Mistakes

- **Reading only one scale.** Single-scale AMD reads miss the bigger picture; multi-scale alignment is what produces high-conviction setups.
- **Demanding all scales perfectly aligned.** Often only 2–3 scales align at any moment; that's still actionable.

## Related Concepts

- [amd-cycle-overview](amd-cycle-overview.md), [amd-on-htf](amd-on-htf.md), [amd-vs-po3](amd-vs-po3.md), [intraday-amd](../12-power-of-three/intraday-amd.md), [power-of-three](../12-power-of-three/power-of-three.md), [90-minute-cycle](../04-time-cycles/90-minute-cycle.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md).

## Citations

- `ICT-2016-PO3`, `ICT-2022-MENTORSHIP-OVERVIEW`.
