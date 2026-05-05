# Quarterly Theory — Overview

**Category:** 22-quarterly-theory
**Aliases:** QT overview, Quarterly Theory primary
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2025
**Source IDs:** ICT-2023-QUARTERLY-THEORY, ICT-2025-ADV-LIQUIDITY
**Tags:** quarterly-theory, fractal, time

## Definition

Quarterly Theory (QT) is ICT's **fractal time framework** taught publicly in 2023: every higher-order time period decomposes into **four quarters** that map to the AMD-X cycle (Accumulation → Manipulation → Distribution → continuation/reversal). The fractal repeats at every scale: yearly → monthly → weekly → daily → 6-hour session → 90-minute → 22.5-minute mini-quarter. This dir is the deep-dive companion to [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), which gives the high-level summary; the files here cover each quarter level individually.

## Formal Criteria

The fractal hierarchy:

| Level | Q1 (A) | Q2 (M) | Q3 (D) | Q4 (X) |
|---|---|---|---|---|
| Year | Jan-Mar | Apr-Jun | Jul-Sep | Oct-Dec |
| Month | week 1 | week 2 | week 3 | week 4 |
| Week | Mon | Tue | Wed | Thu (Fri = closing) |
| Day | 18:00–00:00 NY | 00:00–06:00 NY | 06:00–12:00 NY | 12:00–18:00 NY |
| 6-hour session-Q | first 90 min | second 90 min | third 90 min | fourth 90 min |
| 90-min cycle | 22.5 min A | 22.5 min M | 22.5 min D | 22.5 min X |

Roles per quarter:

- **Q1 — Accumulation:** range-building.
- **Q2 — Manipulation:** sweep / Judas swing.
- **Q3 — Distribution:** the true intended move.
- **Q4 — X:** continuation or reversal.

## Formula / Math

```
qt_levels = [yearly, monthly, weekly, daily, 6h_session_q, 90min, 22.5min]
qt_phases = [A, M, D, X]

# Each level splits into 4 sub-periods, each carrying an AMD-X role.
```

## Machine-Readable

```json
{
  "id": "quarterly-theory-overview",
  "category": "22-quarterly-theory",
  "aliases": ["QT-overview", "Quarterly-Theory-primary"],
  "criteria": [
    {"id": "c1", "expr": "fractal time framework with 4-quarter splits"},
    {"id": "c2", "expr": "phases = [A, M, D, X]"},
    {"id": "c3", "expr": "applies at every TF from year down to 22.5-min"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2025",
  "related": ["quarterly-shift-theory","yearly-quarters","monthly-quarters","weekly-quarters","daily-quarters","90-minute-quarters","true-day-open","true-week-open","quarterly-shift-2025","power-of-three"],
  "sources": ["ICT-2023-QUARTERLY-THEORY","ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
   QT fractal hierarchy:

   Yearly:  Jan-Mar | Apr-Jun | Jul-Sep | Oct-Dec
              (A)  |   (M)   |   (D)   |   (X)
                         ↓
   Monthly: week 1 | week 2 | week 3 | week 4
                         ↓
   Weekly:  Mon    | Tue    | Wed    | Thu (Fri close)
                         ↓
   Daily:   18-00  | 00-06  | 06-12  | 12-18 (NY clock)
                         ↓
   90-min:  22.5m  | 22.5m  | 22.5m  | 22.5m
```

## Timeframes

All TFs.

## Examples

**Example 1 — multi-scale QT alignment:**
- It's Wednesday (weekly Q3 = distribution).
- 09:30 NY (daily Q3 = distribution).
- 09:00–10:30 90-min cycle, currently in M-phase (manipulation, sweep just occurred).
- → multi-scale alignment: weekly D + daily D + 90-min M-to-D transition. High-conviction setup window.

## Common Mistakes

- **Single-scale QT reads.** QT's value is multi-scale alignment; a single-scale read misses the bigger picture.
- **Forcing every period into AMD-X.** ~50-60% of periods follow the canonical map; the rest deviate. Use QT as a probabilistic backdrop, not a deterministic prediction.
- **Confusing day quarters with calendar quarters.** Day-Q1 = NY 18:00-00:00 (6-hour block); year-Q1 = Jan-Mar. Same word, different scope.

## Related Concepts

- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md) — high-level companion.
- [yearly-quarters](yearly-quarters.md), [monthly-quarters](monthly-quarters.md), [weekly-quarters](weekly-quarters.md), [daily-quarters](daily-quarters.md), [90-minute-quarters](90-minute-quarters.md) — per-level deep dives.
- [true-day-open](true-day-open.md), [true-week-open](true-week-open.md), [quarterly-shift-2025](quarterly-shift-2025.md).
- [power-of-three](../12-power-of-three/power-of-three.md) — AMD-X source concept.

## Citations

- `ICT-2023-QUARTERLY-THEORY`, `ICT-2025-ADV-LIQUIDITY`.
