# Daily Quarters

**Category:** 22-quarterly-theory
**Aliases:** day-quarters, 6h-blocks, intraday QT
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-QUARTERLY-THEORY
**Tags:** quarterly-theory, daily, intraday

## Definition

Daily Quarters split each 24-hour trading day into **four 6-hour blocks** anchored to NY clock at 18:00 (the forex daily candle open), each carrying an AMD-X phase: Q1 (18:00-00:00 NY, A), Q2 (00:00-06:00 NY, M), Q3 (06:00-12:00 NY, D), Q4 (12:00-18:00 NY, X). The 6-hour blocks **do not coincide perfectly with named ICT sessions** (Asia 18-03, London 02-11, etc.) — they are a separate fractal lens. See `quarterly-shift-theory.md` for the disambiguation note.

## Formal Criteria

The daily map (6-hour NY-clock blocks):

| Quarter | Window (NY) | Phase | Approx session |
|---|---|---|---|
| Q1 | 18:00–00:00 | Accumulation | Asia (most of) |
| Q2 | 00:00–06:00 | Manipulation | end of Asia + London open KZ |
| Q3 | 06:00–12:00 | Distribution | London tail + NY AM |
| Q4 | 12:00–18:00 | X | NY lunch + NY PM |

Within each 6-hour block, **four 90-minute sub-quarters** further refine the AMD-X cycle (see [90-minute-quarters](90-minute-quarters.md)).

## Formula / Math

```
daily_quarters_NY = {
    Q1: [18:00 prev, 00:00],
    Q2: [00:00, 06:00],
    Q3: [06:00, 12:00],
    Q4: [12:00, 18:00],
}
```

## Machine-Readable

```json
{
  "id": "daily-quarters",
  "category": "22-quarterly-theory",
  "aliases": ["day-quarters", "6h-blocks", "intraday-QT"],
  "criteria": [
    {"id": "c1", "expr": "Q1=18-00, Q2=00-06, Q3=06-12, Q4=12-18 NY"},
    {"id": "c2", "expr": "6-hour blocks anchored to forex daily candle open"}
  ],
  "timeframes": ["M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["quarterly-theory-overview","weekly-quarters","90-minute-quarters","true-day-open","intraday-amd","quarterly-shift-theory"],
  "sources": ["ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   daily AMD-X (6-hour NY-clock blocks):

   18:00 ─── 00:00 ─── 06:00 ─── 12:00 ─── 18:00 NY
        Q1         Q2          Q3          Q4
       (A)        (M)         (D)         (X)
   Asia    | LDN open  | LDN tail+ | NY lunch+
            (early)     | NY AM     | NY PM
```

## Timeframes

M15 / H1 / H4.

## Examples

**Example 1 — clean daily MMBM:**
- Q1 (18:00-00:00 NY): tight Asian range (accumulation).
- Q2 (00:00-06:00 NY): London open Judas wicks below Asia low (manipulation).
- Q3 (06:00-12:00 NY): NY AM 80-pip rally to PDH (distribution).
- Q4 (12:00-18:00 NY): pulls back into NY AM range, consolidates (X).

## Common Mistakes

- **Equating daily-Q with named sessions.** Asia session = 18-03 (9 hours), Q1 = 18-00 (6 hours). Different windows.
- **Single-Q analysis.** QT is multi-scale; daily-Q is one of multiple concurrent fractals.

## Related Concepts

- [quarterly-theory-overview](quarterly-theory-overview.md), [weekly-quarters](weekly-quarters.md), [90-minute-quarters](90-minute-quarters.md), [true-day-open](true-day-open.md), [intraday-amd](../12-power-of-three/intraday-amd.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md).

## Citations

- `ICT-2023-QUARTERLY-THEORY`.
