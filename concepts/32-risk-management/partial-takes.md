# Partial Takes

**Category:** 32-risk-management
**Aliases:** scaling out, partial profit, ladder TP
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, partial-takes, foundational

## Definition

Partial takes are the discipline of **closing portions of a position at progressive R-targets** rather than holding the full position to a single TP. ICT teaches partial takes as a primary trade-management tool: secure realized R early to derisk the trade, then let the runner pursue extended targets. A typical schedule: take 1/3 to 1/2 at 1R-2R (locks in break-even+ on the trade as a whole), trail SL on remainder, target HTF DOL with the runner.

## Formal Criteria

Common partial-take schedules:

| Schedule | TP1 | TP2 | TP3 / runner |
|---|---|---|---|
| Conservative | 50% at 1R | 25% at 2R | 25% trail to HTF DOL |
| Standard | 33% at 2R | 33% at 4R | 33% to HTF DOL or -1.5/-2.0 SD |
| Runner | 25% at 1R | 25% at 3R | 50% to HTF DOL |

After TP1 fills, **move SL to break-even** on the remaining position (some traders move to entry +1R for extra cushion).

## Formula / Math

```
partial_take_schedule = [
  (fraction_1, R_target_1),
  (fraction_2, R_target_2),
  (fraction_remaining, runner_target),
]

after_tp1_fill: move_sl_to_breakeven_or_better
after_tp2_fill: trail_sl_to_recent_pd_array
```

## Machine-Readable

```json
{
  "id": "partial-takes",
  "category": "32-risk-management",
  "aliases": ["scaling-out", "partial-profit", "ladder-TP"],
  "criteria": [
    {"id": "c1", "expr": "scale out at 2-3 progressive R targets"},
    {"id": "c2", "expr": "first partial typically at 1R-2R"},
    {"id": "c3", "expr": "move SL to BE after TP1"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["r-multiple","risk-per-trade","stop-placement-by-pd-array","standard-deviation-projections","draw-on-liquidity"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   3-tier partial-take ladder:

   runner target HTF DOL  ─────── 25% remaining position
                                       (SL trailed to recent structure)
   TP2 4R                 ───────── close 33%
   TP1 2R                 ─── close 33%, move SL to BE
   entry                   ── 100% open
   SL                     ─── 1R risk
```

## Timeframes

All TFs.

## Examples

**Example 1 — standard 33/33/33 ladder:**
- Setup: 3.33-lot position, entry 1.0830, SL 1.0815 (15 pips).
- TP1 (2R = 30 pips above): 1.0860 → close 1.11 lots.
- After TP1: SL → 1.0830 (BE).
- TP2 (4R = 60 pips above): 1.0890 → close 1.11 lots.
- After TP2: SL → 1.0855 (recent FVG / +1.5R).
- Runner (1.11 lots) targets PWH at 1.0950 = 8R; trails SL up structure.

## Common Mistakes

- **All-or-nothing TP.** Single TP misses the optionality to derisk early and run a portion.
- **Forgetting to move SL after TP1.** Letting a partial-filled trade go back through entry into loss is psychologically and structurally wrong — move SL to BE+.
- **Too many partials.** Splitting into 5+ partials produces noise and over-management. 2–3 partials cover most setup scales.

## Related Concepts

- [r-multiple](r-multiple.md), [risk-per-trade](risk-per-trade.md), [stop-placement-by-pd-array](stop-placement-by-pd-array.md), [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
