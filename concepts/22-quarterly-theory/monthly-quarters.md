# Monthly Quarters

**Category:** 22-quarterly-theory
**Aliases:** monthly weeks, weeks-of-month
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-QUARTERLY-THEORY
**Tags:** quarterly-theory, monthly

## Definition

Monthly Quarters split each month into **four weekly periods**, each carrying an AMD-X phase: week 1 (A), week 2 (M), week 3 (D), week 4 (X). Monthly quarters are particularly useful for swing-trading bias because most months have a recognizable weekly-rhythm pattern: range/manipulation → distribution → late-month consolidation/reversal.

## Formal Criteria

The monthly map:

| Quarter | Week | Phase | Character |
|---|---|---|---|
| Q1 | week 1 | Accumulation | first week of month, range-building |
| Q2 | week 2 | Manipulation | mid-month sweeps, NFP often falls here (manipulation context) |
| Q3 | week 3 | Distribution | major monthly directional move |
| Q4 | week 4 | X | end-of-month rebalancing / continuation |

Practical note: **first NFP** of a month falls in monthly week 1 (Q1) — i.e., during accumulation. The post-NFP move (typically week 1 Friday or week 2 Monday) often kicks off the manipulation phase.

## Formula / Math

```
monthly_quarters(month):
    week_1 (Q1, A): days 1-7
    week_2 (Q2, M): days 8-14
    week_3 (Q3, D): days 15-21
    week_4 (Q4, X): days 22-end_of_month
```

## Machine-Readable

```json
{
  "id": "monthly-quarters",
  "category": "22-quarterly-theory",
  "aliases": ["monthly-weeks", "weeks-of-month"],
  "criteria": [
    {"id": "c1", "expr": "Q1=week1, Q2=week2, Q3=week3, Q4=week4"},
    {"id": "c2", "expr": "AMD-X phase mapping per quarter"}
  ],
  "timeframes": ["D","W"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["quarterly-theory-overview","yearly-quarters","weekly-quarters","htf-amd"],
  "sources": ["ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   monthly AMD-X:

   Wk 1   |   Wk 2   |   Wk 3   |   Wk 4
   Q1 (A)    Q2 (M)     Q3 (D)     Q4 (X)
   range     sweep      delivery   continuation
   build     liquidity              / reversal
```

## Timeframes

D / W.

## Examples

**Example 1 — typical monthly MMBM:**
- Week 1: tight 60-pip range (accumulation).
- Week 2: NFP Friday wicks below week-1 low (manipulation).
- Week 3: 200-pip rally (distribution).
- Week 4: consolidates 50% retracement of week-3 leg (X).

## Common Mistakes

- **Off-cycle months.** Some months break the pattern entirely (Fed pivots, geopolitical shocks).
- **Confusing month-of-year with monthly-Q.** Year-Q1 = Jan-Mar; monthly-Q1 = first week of any month. Same naming, different scope.

## Related Concepts

- [quarterly-theory-overview](quarterly-theory-overview.md), [yearly-quarters](yearly-quarters.md), [weekly-quarters](weekly-quarters.md), [htf-amd](../12-power-of-three/htf-amd.md).

## Citations

- `ICT-2023-QUARTERLY-THEORY`.
