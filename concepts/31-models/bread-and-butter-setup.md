# Bread-and-Butter Setup

**Category:** 31-models
**Aliases:** B&B setup, bread and butter, B&B model
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-BREAD-AND-BUTTER
**Tags:** model, bread-and-butter, 2023

## Definition

The **Bread-and-Butter Setup** is ICT's name for the **recurring, dependable daily delivery sequence** that day-traders can repeatedly execute: PM-of-prior-day-or-Asia liquidity raid → London raid → NY delivery. Named for its day-in-day-out reliability — not the highest-conviction setup, but the most-frequent. Most ICT day-traders' workflow is built around catching the B&B sequence each day with the standard 2022/2023 model rules applied.

## Formal Criteria

The B&B daily sequence:

1. **Prior session's PM range** (yesterday's NY PM, ending 16:00 NY) creates BSL/SSL pools.
2. **Asian session** consolidates and extends those pools (may sweep one side).
3. **London open** raids one Asian-range bound (Judas swing) → reverses into bias direction.
4. **NY AM** delivers the bulk of the daily move (distribution toward HTF DOL).

The trader catches the **London or NY AM segments** of the sequence each day with standard 2022/2023 model rules.

## Formula / Math

```
bread_and_butter_day :=
    prior_pm_range_present
    AND asian_extension_present
    AND london_open_judas_swing
    AND ny_am_distribution_to_DOL

# Captured by:
trader_executes := standard_2022_model_at(london_open_KZ)
                    OR standard_2022_model_at(ny_am_KZ)
```

## Machine-Readable

```json
{
  "id": "bread-and-butter-setup",
  "category": "31-models",
  "aliases": ["B&B-setup", "bread-and-butter", "B&B-model"],
  "criteria": [
    {"id": "c1", "expr": "PM-Asia-London-NY sequence"},
    {"id": "c2", "expr": "execute via 2022 model in London open or NY AM KZ"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["ict-2022-model","ict-2023-model","silver-bullet-overview","intraday-amd","judas-swing","asian-range-sweep","london-open-killzone","ny-am-killzone"],
  "sources": ["ICT-2023-BREAD-AND-BUTTER"]
}
```

## Visual Pattern

```
   B&B daily sequence (NY clock):

   13:30-16:00 (prior day): NY PM range
                ↓ creates BSL/SSL pools for next day
   18:00-03:00: Asia consolidation, may extend pools
                ↓
   02:00-05:00: London open Judas raids one bound
                ↓ reverses into bias direction
   08:00-12:00: NY AM distribution to HTF DOL
                ↓
   16:00:       day closes; cycle restarts.
```

## Timeframes

M5–H1.

## Examples

**Example 1 — clean B&B day:**
- Yesterday: PDH 1.0925, PDL 1.0830.
- Asia: range 1.0850–1.0875 (within prior PM range).
- 02:55 NY (London open Judas): wicks 1.0846 (Asian SSL swept), reverses up.
- 03:10–11:00: London-open KZ + NY AM KZ deliver 80 pips up to PDH 1.0925.
- Trader caught the move with the 2022 model on London-open SB.

## Common Mistakes

- **Forcing B&B every day.** Roughly 50–60% of days follow B&B cleanly; the rest break pattern. Don't force the read.
- **Treating B&B as a single specific entry.** B&B is the **sequence**; entries within it use the standard 2022/2023 model rules.

## Related Concepts

- [ict-2022-model](ict-2022-model.md), [ict-2023-model](ict-2023-model.md), [silver-bullet-overview](../11-silver-bullet/silver-bullet-overview.md), [intraday-amd](../12-power-of-three/intraday-amd.md), [judas-swing](../13-judas-swing/judas-swing.md), [asian-range-sweep](../14-asian-range/asian-range-sweep.md), [london-open-killzone](../10-killzones/london-open-killzone.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md).

## Citations

- `ICT-2023-BREAD-AND-BUTTER`.
