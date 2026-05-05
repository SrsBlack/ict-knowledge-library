# AMD on HTF

**Category:** 24-amd-cycle
**Aliases:** HTF AMD cycle, weekly/monthly/yearly AMD
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2023
**Source IDs:** ICT-2016-PO3, ICT-2023-QUARTERLY-THEORY
**Tags:** amd, htf, weekly, monthly

## Definition

AMD on higher timeframes — the same cycle, scaled to weekly / monthly / yearly. HTF AMD sets bias for intraday execution; lower-TF setups should be aligned with the current HTF AMD phase. This file is the cycle-side companion to [htf-amd](../12-power-of-three/htf-amd.md), which covers the same ground from the PO3 / market-maker angle.

## Formal Criteria

Same mapping as [htf-amd](../12-power-of-three/htf-amd.md):

- Yearly: Q1=Jan-Mar (A), Q2=Apr-Jun (M), Q3=Jul-Sep (D), Q4=Oct-Dec (X).
- Monthly: week 1 (A), week 2 (M), week 3 (D), week 4 (X).
- Weekly: Mon (A), Tue (M), Wed (D), Thu/Fri (X / closing).

When the current HTF phase is **manipulation**, expect the LTF setups inside the manipulation to fade quickly (you're inside the engineered fake-out).
When the current HTF phase is **distribution**, intraday continuation setups have the highest base rates.

## Formula / Math

```
htf_amd_phase(now) = lookup(now, htf_amd_canonical_table)

intraday_setup_quality_modifier(setup, htf_phase):
  if htf_phase == "distribution" AND setup_aligned: bonus
  if htf_phase == "manipulation": fade quickly / counter-bias likely fails
  if htf_phase == "accumulation": expect chop, low conviction
```

## Machine-Readable

```json
{
  "id": "amd-on-htf",
  "category": "24-amd-cycle",
  "aliases": ["HTF-AMD-cycle", "weekly-monthly-yearly-AMD"],
  "criteria": [
    {"id": "c1", "expr": "AMD applied at week/month/year scales"},
    {"id": "c2", "expr": "current HTF phase biases intraday execution"}
  ],
  "timeframes": ["D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2023",
  "related": ["amd-cycle-overview","amd-on-intraday","amd-vs-po3","htf-amd","power-of-three","quarterly-shift-theory","htf-bias-framework"],
  "sources": ["ICT-2016-PO3","ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   monthly AMD example:

   Week 1 (A): ──────  range build, low vol.
   Week 2 (M):    ▼▼   sweep month-1 low (manipulation).
   Week 3 (D):       ▲▲▲▲  major bullish leg (distribution).
   Week 4 (X):           ─── consolidation or extension.
```

## Timeframes

D / W / MN.

## Examples

**Example 1 — monthly MMBM context for a daily setup:**
- Currently in week 3 of the month → monthly Q3 = distribution phase.
- HTF (W, MN) bullish.
- Daily setup: bullish OB at H4 = high-conviction long because monthly distribution is in progress.

## Common Mistakes

- **Ignoring HTF AMD when reading intraday.** A bearish-side intraday setup during a clean monthly bullish distribution often fails.
- **Forcing the calendar map.** The Mon/Tue/Wed/Thu weekly map is typical; some weeks deviate (Thursday distribution, Friday X, etc.).

## Related Concepts

- [amd-cycle-overview](amd-cycle-overview.md), [amd-on-intraday](amd-on-intraday.md), [amd-vs-po3](amd-vs-po3.md), [htf-amd](../12-power-of-three/htf-amd.md), [power-of-three](../12-power-of-three/power-of-three.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2016-PO3`, `ICT-2023-QUARTERLY-THEORY`.
