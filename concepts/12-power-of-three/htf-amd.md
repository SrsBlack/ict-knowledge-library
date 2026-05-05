# HTF AMD

**Category:** 12-power-of-three
**Aliases:** HTF PO3, weekly AMD, monthly AMD, swing-scale AMD
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2023
**Source IDs:** ICT-2016-PO3, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2023-QUARTERLY-THEORY
**Tags:** amd, htf, weekly, monthly

## Definition

HTF AMD is the application of the PO3 / AMD doctrine at **higher timeframes** — weekly, monthly, quarterly, yearly. Weekly AMD maps to a Mon-Tue-Wed-Thu phase structure; monthly AMD splits into 4 weekly quarters; yearly AMD splits into 4 calendar quarters. ICT teaches HTF AMD as the **bias-setting** layer for intraday execution: a weekly MMBM in progress means intraday setups should bias bullish.

## Formal Criteria

Mapping (per [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md)):

| TF | A (Q1) | M (Q2) | D (Q3) | X (Q4) |
|---|---|---|---|---|
| Yearly | Jan-Mar | Apr-Jun | Jul-Sep | Oct-Dec |
| Monthly | week 1 | week 2 | week 3 | week 4 |
| Weekly | Mon | Tue | Wed | Thu (Fri = closing) |

The HTF AMD phase you're in **biases lower-TF setups** in the corresponding direction.

## Formula / Math

```
htf_amd_phases:
  yearly:   {Q1: Jan-Mar, Q2: Apr-Jun, Q3: Jul-Sep, Q4: Oct-Dec}
  monthly:  {Q1: week_1, Q2: week_2, Q3: week_3, Q4: week_4}
  weekly:   {Q1: Mon, Q2: Tue, Q3: Wed, Q4: Thu}

current_htf_phase(date) → bias_for_lower_tf
```

## Machine-Readable

```json
{
  "id": "htf-amd",
  "category": "12-power-of-three",
  "aliases": ["HTF-PO3", "weekly-AMD", "monthly-AMD", "swing-AMD"],
  "criteria": [
    {"id": "c1", "expr": "applies AMD to weekly/monthly/yearly TFs"},
    {"id": "c2", "expr": "Mon=A, Tue=M, Wed=D, Thu=X for weekly"}
  ],
  "timeframes": ["D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2023",
  "related": ["power-of-three","accumulation-phase","manipulation-phase","distribution-phase","intraday-amd","amd-cycle-overview","quarterly-shift-theory","htf-bias-framework"],
  "sources": ["ICT-2016-PO3","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   weekly AMD (typical bullish week):

   Mon (A): tight range, low volatility
   Tue (M): wicks below Mon's low (manipulation)
   Wed (D): 100-pip rally, takes PWH (distribution)
   Thu (X): consolidation or extension
   Fri:    week's closing print
```

## Timeframes

D / W / MN.

## Examples

**Example 1 — weekly MMBM:**
- Mon: EURUSD ranges 1.0850–1.0900.
- Tue: wicks 1.0838 (Mon low SSL swept), reverses up.
- Wed: 130-pip rally, takes PWH 1.0985 by Wed close.
- Thu: extends to 1.1010, then consolidates.
- Fri: closes 1.0995.
- → weekly MMBM. Intraday bias bullish all week; counter-trend setups disfavored.

## Common Mistakes

- **Ignoring HTF AMD phase.** Trading intraday setups against a clear weekly distribution in the opposite direction is fighting the algorithm.
- **Forcing every week into A-M-D-X.** ~40-50% of weeks follow the canonical map; the rest deviate. Bias-set with HTF AMD; don't predict every detail.
- **Confusing day quarters with week quarters.** Different scopes; specify which.

## Related Concepts

- [power-of-three](power-of-three.md), [accumulation-phase](accumulation-phase.md), [manipulation-phase](manipulation-phase.md), [distribution-phase](distribution-phase.md), [intraday-amd](intraday-amd.md), [amd-cycle-overview](../24-amd-cycle/amd-cycle-overview.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2016-PO3`, `ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2023-QUARTERLY-THEORY`.
