# ICT Fibonacci — Overview

**Category:** 28-fibonacci-levels
**Aliases:** ICT fib, ICT-specific fib levels, OTE fib, ICT retracement levels
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fibonacci, fib, ote, retracement, projection

## Definition

ICT teaches a **specific subset of fibonacci ratios** for measured retracements and projections — not the full classical fib set used by other technical-analysis traditions. The ICT fib retracement set is **0.62 / 0.705 / 0.79** (the OTE zone), with 0.50 (equilibrium) and 0.79 as the deepest entry. The ICT fib projection set is **−1.5 / −2.0 / −2.5 / −4.0** standard-deviation levels (negative ratios indicate price extending beyond the measured leg). Other classical levels (0.382, 0.618 alone, 1.272, 1.618) are NOT primary ICT references.

## Formal Criteria

ICT fib levels:

| Type | Level | ICT name |
|---|---|---|
| Retracement | 0.50 | Equilibrium (EQ) |
| Retracement | 0.62 | upper OTE bound |
| Retracement | 0.705 | OTE optimal entry |
| Retracement | 0.79 | lower OTE bound (deep entry) |
| Projection | -1.5 | first SD target |
| Projection | -2.0 | second SD target |
| Projection | -2.5 | third SD target |
| Projection | -4.0 | extreme SD target |

The fib tool is anchored to a **measured swing leg**: from leg start to leg end. Retracements measure pullback into the leg; projections measure extensions beyond the leg's destination.

## Formula / Math

```
leg_start = price at start of measured leg
leg_end   = price at end of measured leg
leg_size  = leg_end - leg_start          # signed by direction

retrace(level) = leg_end - level * leg_size
project(level) = leg_end - level * leg_size  # works the same with negative levels

# Example, bullish leg from 1.0800 (start) to 1.0900 (end):
EQ_0_50 = 1.0900 - 0.50 * 100 = 1.0850
OTE_0_705 = 1.0900 - 0.705 * 100 = 1.08295
OTE_0_79 = 1.0900 - 0.79 * 100 = 1.0821
SD_-1_5  = 1.0900 - (-1.5) * 100 = 1.1050
SD_-2_0  = 1.0900 + 200 = 1.1100
```

## Machine-Readable

```json
{
  "id": "ict-fib-overview",
  "category": "28-fibonacci-levels",
  "aliases": ["ICT-fib", "OTE-fib"],
  "criteria": [
    {"id": "c1", "expr": "retracement_levels = [0.50, 0.62, 0.705, 0.79]"},
    {"id": "c2", "expr": "projection_levels = [-1.5, -2.0, -2.5, -4.0]"},
    {"id": "c3", "expr": "anchored_to_measured_swing_leg == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["fib-62","fib-705","fib-79","standard-deviation-projections","symmetrical-price-projections","fib-vs-ote","ote-overview","equilibrium-definition"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish leg (start → end, then retracement):

   leg_end ─────────  ← 0.0 (no retracement)
                                  ── -1.5 SD projection target
                                  ── -2.0
                                  ── -2.5
                                  ── -4.0
   ─── 0.50 (EQ) ────
   ─── 0.62 (upper OTE) ─
   ─── 0.705 (OTE optimal entry) ───
   ─── 0.79 (deep OTE) ─
   leg_start ─────────  ← 1.0 (full retrace)
```

## Timeframes

All TFs.

## Examples

**Example 1 — bullish leg + OTE entry:**
- Leg: 1.0800 → 1.0900 (100 pips bullish).
- OTE zone: 0.62 = 1.08380, 0.705 = 1.08295, 0.79 = 1.0821.
- Long entry at 0.705 (1.08295) on retest with bullish FVG + HTF bias.
- SL below 0.79 (1.0821) plus buffer.
- Targets: -1.5 SD = 1.1050 (extension), -2.0 SD = 1.1100.

## Common Mistakes

- **Using classical fib set.** 0.382, 0.50, 0.618, 1.272, 1.618 are common but NOT ICT's primary set. Use 0.62 / 0.705 / 0.79 / SD ratios instead.
- **Anchoring poorly.** Anchor to a clean swing leg with structural significance (a confirmed swing high to swing low, not a random pivot).
- **Ignoring HTF.** Fib levels alone are not entries; require PD-array + HTF confluence at the level.

## Related Concepts

- [fib-62](fib-62.md), [fib-705](fib-705.md), [fib-79](fib-79.md) — per-level deep dives.
- [standard-deviation-projections](standard-deviation-projections.md) — projection side.
- [symmetrical-price-projections](symmetrical-price-projections.md) — alternative projection method.
- [fib-vs-ote](fib-vs-ote.md) — disambiguation page.
- [ote-overview](../17-optimal-trade-entry/ote-overview.md) — application of the retracement set.
- [equilibrium-definition](../27-equilibrium/equilibrium-definition.md) — 0.50 = EQ.

## Citations

- `ICT-2017-OTE` — ICT fib levels introduced.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use refined.
