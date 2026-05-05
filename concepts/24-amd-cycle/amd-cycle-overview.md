# AMD Cycle — Overview

**Category:** 24-amd-cycle
**Aliases:** AMD cycle, accumulation-manipulation-distribution cycle
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2023
**Source IDs:** ICT-2016-PO3, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** amd, cycle, time-construct

## Definition

The **AMD cycle** is the time-construct version of the AMD doctrine: it emphasizes the cycle as a **repeatable temporal pattern** that re-runs at every TF. Where [power-of-three](../12-power-of-three/power-of-three.md) emphasizes the model as a market-maker framework, AMD-cycle emphasizes the **rhythm of the cycle** — that delivery happens in waves of accumulation→manipulation→distribution, and each completed cycle starts a new one. The two perspectives describe the same phenomenon; this file focuses on the **temporal cycle** lens.

## Formal Criteria

The cycle structure:

- **Phase 1 (A):** accumulation/build (low volatility).
- **Phase 2 (M):** manipulation (engineered fake-out).
- **Phase 3 (D):** distribution (true delivery).
- (Optional Phase 4 X): continuation/reversal.
- After cycle completes: a new accumulation begins on the same TF.

Cycle scales:

- 90-min cycle (smallest tradeable).
- 6-hour session quarter.
- Daily.
- Weekly.
- Monthly.
- Yearly.

## Formula / Math

```
amd_cycle = (A_phase, M_phase, D_phase, X_phase?)

cycle_completes_when:
  D_phase ends (or X_phase ends)
  AND new accumulation forms

cycle_period_by_tf = {
  90min, 6h, day, week, month, year
}
```

## Machine-Readable

```json
{
  "id": "amd-cycle-overview",
  "category": "24-amd-cycle",
  "aliases": ["AMD-cycle", "accumulation-manipulation-distribution-cycle"],
  "criteria": [
    {"id": "c1", "expr": "phases = [A, M, D] (and optional X)"},
    {"id": "c2", "expr": "cycle repeats at every TF"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2023",
  "related": ["power-of-three","amd-on-htf","amd-on-intraday","amd-vs-po3","accumulation-phase","manipulation-phase","distribution-phase","quarterly-shift-theory","90-minute-cycle"],
  "sources": ["ICT-2016-PO3","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   AMD cycle as repeating waves:

   A ── M ── D ── (X) ── A' ── M' ── D' ── (X') ── A'' ── ...
   |         ↑                   ↑                    ↑
   start of  start of new        start of             cycle
   cycle 1   cycle 2             cycle 3              continues
```

## Timeframes

All TFs.

## Examples

**Example 1 — 90-min AMD cycle:**
- 03:00 NY: London open. Asia-range setup.
- 03:00–03:22 (A): tight range building.
- 03:22–03:45 (M): wick below Asia low (manipulation).
- 03:45–04:07 (D): 18-pip displacement up (distribution).
- 04:07–04:30 (X): pullback consolidation.
- 04:30: new 90-min cycle begins.

**Example 2 — daily AMD cycle = standard intraday AMD** (Asia-London-NYAM-NYPM).

## Common Mistakes

- **Treating cycles as deterministic.** AMD is a typical-pattern, not a guarantee. Counter-examples are common.
- **Confusing scales.** A 90-min cycle inside a daily cycle is normal — both are valid concurrently.

## Related Concepts

- [power-of-three](../12-power-of-three/power-of-three.md), [amd-on-htf](amd-on-htf.md), [amd-on-intraday](amd-on-intraday.md), [amd-vs-po3](amd-vs-po3.md).
- [accumulation-phase](../12-power-of-three/accumulation-phase.md), [manipulation-phase](../12-power-of-three/manipulation-phase.md), [distribution-phase](../12-power-of-three/distribution-phase.md).
- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [90-minute-cycle](../04-time-cycles/90-minute-cycle.md).

## Citations

- `ICT-2016-PO3`, `ICT-2022-MENTORSHIP-OVERVIEW`.
