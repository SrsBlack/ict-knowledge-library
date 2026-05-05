# Yearly Quarters

**Category:** 22-quarterly-theory
**Aliases:** annual quarters, calendar quarters
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-QUARTERLY-THEORY
**Tags:** quarterly-theory, yearly, calendar

## Definition

Yearly Quarters are the **four 3-month calendar periods** of the trading year mapped to AMD-X phases per Quarterly Theory: Q1=Jan-Mar (A), Q2=Apr-Jun (M), Q3=Jul-Sep (D), Q4=Oct-Dec (X). The yearly fractal is the largest unit ICT teaches; it sets the broadest backdrop for swing-and-position-trading bias. Yearly quarters typically shift slowly — yearly distribution often runs 3+ months before transitioning.

## Formal Criteria

The yearly map:

| Quarter | Months | Phase | Typical character |
|---|---|---|---|
| Q1 | Jan-Mar | Accumulation | range-building, "January effect" volatility, low directional conviction |
| Q2 | Apr-Jun | Manipulation | sweeps prior-year extremes, sets up annual reversal |
| Q3 | Jul-Sep | Distribution | major directional moves, often "summer rally" or selloff |
| Q4 | Oct-Dec | X (continuation/reversal) | year-end rallies or sharp corrections |

The phase assignment is **typical not guaranteed** — yearly behavior varies substantially by macro regime.

## Formula / Math

```
yearly_q1 = [Jan 1, Mar 31]
yearly_q2 = [Apr 1, Jun 30]
yearly_q3 = [Jul 1, Sep 30]
yearly_q4 = [Oct 1, Dec 31]
```

## Machine-Readable

```json
{
  "id": "yearly-quarters",
  "category": "22-quarterly-theory",
  "aliases": ["annual-quarters", "calendar-quarters"],
  "criteria": [
    {"id": "c1", "expr": "Q1 = Jan-Mar (A)"},
    {"id": "c2", "expr": "Q2 = Apr-Jun (M)"},
    {"id": "c3", "expr": "Q3 = Jul-Sep (D)"},
    {"id": "c4", "expr": "Q4 = Oct-Dec (X)"}
  ],
  "timeframes": ["W","MN"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["quarterly-theory-overview","monthly-quarters","quarterly-shift-2025","htf-amd","htf-bias-framework"],
  "sources": ["ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   yearly AMD-X:

   Jan ── Mar  |  Apr ── Jun  |  Jul ── Sep  |  Oct ── Dec
      Q1 (A)         Q2 (M)         Q3 (D)         Q4 (X)
   accumulation   manipulation    distribution   continuation
                                                  / reversal
```

## Timeframes

W / MN (yearly is too coarse for daily-and-below).

## Examples

**Example 1 — yearly distribution context:**
- It's August: yearly Q3 = distribution phase.
- Weekly + monthly bias both bullish.
- → swing-trading setups in the bullish direction get yearly-Q3 conviction bonus.

## Common Mistakes

- **Treating yearly QT as deterministic.** Macro shocks (recessions, Fed pivots) override calendar mapping.
- **Day-trading on yearly QT alone.** Yearly is backdrop; setup execution is daily-and-below.

## Related Concepts

- [quarterly-theory-overview](quarterly-theory-overview.md), [monthly-quarters](monthly-quarters.md), [quarterly-shift-2025](quarterly-shift-2025.md), [htf-amd](../12-power-of-three/htf-amd.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2023-QUARTERLY-THEORY`.
