# Weekly Quarters

**Category:** 22-quarterly-theory
**Aliases:** weekly days, days-of-week QT
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-QUARTERLY-THEORY
**Tags:** quarterly-theory, weekly

## Definition

Weekly Quarters split each trading week into **four day-periods** mapped to AMD-X: Monday (Q1, A), Tuesday (Q2, M), Wednesday (Q3, D), Thursday (Q4, X), with Friday treated as a closing/continuation day outside the canonical 4-quarter map. This is the **most-traded QT scale for day-traders** — many setups gain conviction from being aligned with weekly-Q3 (Wednesday distribution).

## Formal Criteria

The weekly map:

| Day | Quarter | Phase | Typical character |
|---|---|---|---|
| Monday | Q1 | Accumulation | tight range; PWL/PWH often respected; "Monday range" forms |
| Tuesday | Q2 | Manipulation | sweep PWL or PWH (which one depends on weekly bias); week's manipulation move |
| Wednesday | Q3 | Distribution | major directional move; weekly HOD/LOD often set |
| Thursday | Q4 | X | continuation or reversal |
| Friday | (closing) | profit-taking | week's structure often resolves |

Common adage: "Tuesday lows on bullish weeks, Tuesday highs on bearish weeks" — referring to the manipulation-direction sweep.

## Formula / Math

```
weekly_quarters:
    Monday    (Q1, A)
    Tuesday   (Q2, M)
    Wednesday (Q3, D)
    Thursday  (Q4, X)
    Friday    (closing, separate)
```

## Machine-Readable

```json
{
  "id": "weekly-quarters",
  "category": "22-quarterly-theory",
  "aliases": ["weekly-days", "days-of-week-QT"],
  "criteria": [
    {"id": "c1", "expr": "Mon=Q1(A), Tue=Q2(M), Wed=Q3(D), Thu=Q4(X)"},
    {"id": "c2", "expr": "Friday closing day, separate from QT structure"}
  ],
  "timeframes": ["H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["quarterly-theory-overview","monthly-quarters","daily-quarters","htf-amd"],
  "sources": ["ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   weekly AMD-X:

   Mon   | Tue   | Wed   | Thu   | Fri
   Q1(A) | Q2(M) | Q3(D) | Q4(X) | close
   range   sweep   major   cont/   week
   build   PWL/H   move    rev     resolve
```

## Timeframes

H1 / H4 / D.

## Examples

**Example 1 — clean weekly MMBM:**
- Mon: 50-pip range, tight (Q1, A).
- Tue: wicks 1.0815 (PWL SSL swept) at London open, reverses (Q2, M).
- Wed: 130-pip rally, takes PWH 1.0985 (Q3, D).
- Thu: extends to 1.1010, then consolidates (Q4, X).
- Fri: closes 1.0995 (closing day).

## Common Mistakes

- **Forcing every week into Mon-Tue-Wed-Thu pattern.** ~50% of weeks follow it; macro events / news shift the rhythm.
- **Skipping Tuesday context.** A clean Tuesday manipulation is often the highest-conviction setup window of the week.

## Related Concepts

- [quarterly-theory-overview](quarterly-theory-overview.md), [monthly-quarters](monthly-quarters.md), [daily-quarters](daily-quarters.md), [htf-amd](../12-power-of-three/htf-amd.md).

## Citations

- `ICT-2023-QUARTERLY-THEORY`.
