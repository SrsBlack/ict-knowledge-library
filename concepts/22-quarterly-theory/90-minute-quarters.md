# 90-Minute Quarters

**Category:** 22-quarterly-theory
**Aliases:** 90-min mini-Q, 22.5-min sub-quarters, micro-quarters
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2024
**Source IDs:** ICT-2023-QUARTERLY-THEORY
**Tags:** quarterly-theory, 90-min, micro-quarters

## Definition

90-Minute Quarters are the **smallest fractal level in QT**: each 90-minute cycle subdivides into **four 22.5-minute mini-quarters** carrying AMD-X phases. This is the operational scale ICT day-traders use for execution — within a single 90-min window, the A/M/D/X mini-quarters predict the micro-pattern of price delivery. The 90-min cycle itself is documented in [90-minute-cycle](../04-time-cycles/90-minute-cycle.md); this file focuses on the 22.5-min sub-quarter mapping inside it.

## Formal Criteria

Within any 90-minute window:

| Mini-Q | Sub-window | Phase | Character |
|---|---|---|---|
| Q1 | 0–22.5 min | A | range building |
| Q2 | 22.5–45 min | M | manipulation / sweep |
| Q3 | 45–67.5 min | D | true directional move |
| Q4 | 67.5–90 min | X | continuation / reversal / consolidation |

The 22.5-minute boundaries are **approximate** — phases blur, and the exact transitions are visible in retrospect more than in real time.

## Formula / Math

```
within_90min_window:
    miniQ1 = [0, 22.5] min   (A)
    miniQ2 = [22.5, 45] min  (M)
    miniQ3 = [45, 67.5] min  (D)
    miniQ4 = [67.5, 90] min  (X)
```

## Machine-Readable

```json
{
  "id": "90-minute-quarters",
  "category": "22-quarterly-theory",
  "aliases": ["90-min-mini-Q", "22.5-min-sub-quarters", "micro-quarters"],
  "criteria": [
    {"id": "c1", "expr": "90-min window splits into 4 x 22.5-min mini-quarters"},
    {"id": "c2", "expr": "mini-quarters carry AMD-X phases"}
  ],
  "timeframes": ["M5","M15"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2024",
  "related": ["quarterly-theory-overview","daily-quarters","90-minute-cycle","quarterly-shift-theory","power-of-three"],
  "sources": ["ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   90-minute window with 22.5-min mini-quarters:

   0 ──── 22.5 ──── 45 ──── 67.5 ──── 90 (minutes)
       Q1        Q2         Q3         Q4
      (A)       (M)        (D)        (X)
   range    sweep       true       continue
   build    Judas       move       / reverse
```

## Timeframes

M5 / M15. Within a 90-min window, ~18 M5 candles or ~6 M15 candles cover the full cycle.

## Examples

**Example 1 — 90-min cycle 03:00-04:30 NY (London open):**
- 03:00–03:22.5: range tight around 1.0855 (Q1, A).
- 03:22.5–03:45: M5 wicks 1.0846 (Asian SSL swept) (Q2, M).
- 03:45–04:07.5: M5 displaces +18 pips, FVG up (Q3, D).
- 04:07.5–04:30: pulls back to FVG, consolidates (Q4, X).

## Common Mistakes

- **Pixel-precision boundaries.** 22.5-min boundaries are approximate; treat as zones, not exact times.
- **Forcing 4 phases on every 90-min window.** Some 90-min windows skip a phase or have an outsized one.

## Related Concepts

- [quarterly-theory-overview](quarterly-theory-overview.md), [daily-quarters](daily-quarters.md), [90-minute-cycle](../04-time-cycles/90-minute-cycle.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [power-of-three](../12-power-of-three/power-of-three.md).

## Citations

- `ICT-2023-QUARTERLY-THEORY`.
