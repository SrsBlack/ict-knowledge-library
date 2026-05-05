# 90-Minute Cycle

**Category:** 04-time-cycles
**Aliases:** 90-min cycle, ICT 90-minute fractal, quarter-of-quarter cycle
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2024
**Source IDs:** ICT-2023-QUARTERLY-THEORY
**Tags:** time, cycle, fractal, quarterly-theory

## Definition

The 90-minute cycle is the smallest time-fractal in ICT's [quarterly-shift-theory](quarterly-shift-theory.md): each 6-hour session quarter is divided into four 90-minute quarters, and each 90-minute quarter is itself an AMD (accumulation-manipulation-distribution) micro-cycle. ICT teaches that price delivery follows the same A-M-D-X pattern at every fractal level — yearly, monthly, weekly, daily, session-quarter, and 90-minute. The 90-minute cycle is the operational unit for intra-session trading.

## Formal Criteria

- Each 90-minute window is divided into four ~22.5-minute mini-quarters: Q1 (accumulation), Q2 (manipulation / Judas swing), Q3 (distribution / true move), Q4 (continuation or reversal / X).
- The four 90-minute cycles inside a 6-hour session quarter map to: Asia (00:00–06:00 NY rolling), London (06:00–12:00 NY), NY AM/PM (12:00–18:00 NY), late NY/Asia (18:00–00:00 NY).
- Cycle boundaries are NY-time-anchored at :30 and :00 of each clock hour as the 90-minute periods rotate.

## Formula / Math

```
quarter_cycle_starts (NY time, rotating quarterly):
  Q1: 00:00, 06:00, 12:00, 18:00     # 6-hour session quarters

within each Q (6 hours), four 90-min cycles:
  90m_1: 0:00 – 1:30 from Q-start
  90m_2: 1:30 – 3:00
  90m_3: 3:00 – 4:30
  90m_4: 4:30 – 6:00

within each 90-min, four 22.5-min mini-quarters (A/M/D/X)
```

## Machine-Readable

```json
{
  "id": "90-minute-cycle",
  "category": "04-time-cycles",
  "aliases": ["90-min-cycle", "quarter-of-quarter-cycle"],
  "criteria": [
    {"id": "c1", "expr": "duration == 90_minutes"},
    {"id": "c2", "expr": "subdivides_into_4_AMD_X_phases == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2024",
  "related": ["quarterly-shift-theory","macro-times-overview","power-of-three","accumulation-phase","manipulation-phase","distribution-phase"],
  "sources": ["ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
6-hour session quarter (e.g. 06:00–12:00 NY = London / start NY):

|── 90m ──|── 90m ──|── 90m ──|── 90m ──|
06:00    07:30    09:00    10:30    12:00

Each 90-min subdivides:

|── A ──|── M ──|── D ──|── X ──|
0:00    22.5   45     67.5    90
        Judas   true   continuation
        swing   move   or reversal
```

## Timeframes

M1 / M5 / M15. The 90-minute cycle is too large to see on M1 alone (90 bars) and too small to see on H4. M5 is the natural reading TF.

## Examples

**Example 1 — London 90-min cycle (06:00–07:30 NY):**
- 06:00–06:22: range-building, accumulation (no decisive direction).
- 06:22–06:45: M5 sweeps Asian SSL, fakeout down (manipulation / Judas).
- 06:45–07:07: displacement up, FVG, primary move (distribution).
- 07:07–07:30: extension or pullback (X).
- → all four AMD mini-quarters visible inside the single 90-minute window.

## Common Mistakes

- **Forcing the 22.5-minute boundaries.** AMD phases inside a 90-min cycle rarely hit exactly 22.5 minutes — treat the boundaries as approximate. The pattern is the sequence (A → M → D → X), not the precise timestamps.
- **Confusing with macro times.** Macros are 20-minute precision windows centered on hour boundaries; 90-min cycles are 90-minute fractal windows. Different concepts; sometimes overlap.
- **Skipping the bias filter.** AMD pattern is direction-agnostic; without HTF bias you cannot tell whether the manipulation is to the upside or downside.

## Related Concepts

- [quarterly-shift-theory](quarterly-shift-theory.md) — the larger fractal in which 90-min sits.
- [macro-times-overview](macro-times-overview.md) — narrower precision windows.
- [power-of-three](../12-power-of-three/power-of-three.md) — A-M-D phases.
- [accumulation-phase](../12-power-of-three/accumulation-phase.md), [manipulation-phase](../12-power-of-three/manipulation-phase.md), [distribution-phase](../12-power-of-three/distribution-phase.md) — phase deep-dives.

## Citations

- `ICT-2023-QUARTERLY-THEORY` — 90-minute fractal taught publicly within Quarterly Theory.
