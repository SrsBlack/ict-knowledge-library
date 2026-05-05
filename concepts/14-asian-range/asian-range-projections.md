# Asian Range Projections

**Category:** 14-asian-range
**Aliases:** Asia projections, AR projections, AR extension targets
**ICT Confidence:** medium
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** asian-range, projections, targets

## Definition

Asian range projections are extension targets that use the Asian range size as the unit of measurement and project price levels above and below the range — typically at multiples of 0.5×, 1×, 1.5×, 2× the Asian range size. ICT teaches that London / NY delivery often reaches an integer multiple of the Asian range from the side opposite to the initial sweep. Useful for estimating distance-of-day targets and partial-take levels.

## Formal Criteria

- Asian range size = `asian_high - asian_low`.
- Projections from the **non-swept** side (the side opposite the Judas swing):
  - 0.5× projection = swept_bound ± 0.5 × range
  - 1× projection = swept_bound ± 1 × range
  - 1.5× projection
  - 2× projection
- After a low-side sweep, project upward from `asian_high`. After a high-side sweep, project downward from `asian_low`.

These are **target estimations**, not entries. Combine with HTF DOL.

## Formula / Math

```
range_size = asian_high - asian_low

# After low-side sweep (Judas down → bullish delivery up):
proj_0_5x_up = asian_high + 0.5 * range_size
proj_1x_up   = asian_high + 1.0 * range_size
proj_1_5x_up = asian_high + 1.5 * range_size
proj_2x_up   = asian_high + 2.0 * range_size

# After high-side sweep (Judas up → bearish delivery down):
proj_0_5x_down = asian_low - 0.5 * range_size
proj_1x_down   = asian_low - 1.0 * range_size
proj_1_5x_down = asian_low - 1.5 * range_size
proj_2x_down   = asian_low - 2.0 * range_size
```

## Machine-Readable

```json
{
  "id": "asian-range-projections",
  "category": "14-asian-range",
  "aliases": ["asia-projections", "AR-projections", "extension-targets"],
  "criteria": [
    {"id": "c1", "expr": "projection = swept_bound +/- N * asian_range_size for N in [0.5, 1, 1.5, 2]"}
  ],
  "timeframes": ["M15","H1","H4"],
  "confidence": "medium",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["asian-range","asian-range-sweep","standard-deviation-projections","draw-on-liquidity","ote-overview"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   2x_up  ─────────  ← extension target
   1.5x_up ────────
   1x_up  ─────────  ← common target after Judas-down
   0.5x_up ────────
   asian_high ─────  ← sweep starts here
                /\
               /  \
              /    \   (range)
   asian_low  ─────  ← swept side
```

## Timeframes

M15 / H1 / H4 (project on whichever TF you're trading; Asian range size is small enough that M15 chart-fit works well).

## Examples

**Example 1 — bullish delivery hitting 1× projection:**
- Asian range 1.0848–1.0876, range_size = 28 pips.
- London Judas sweeps 1.0846 (low-side); HTF bullish.
- Targets:
  - 0.5×: 1.0876 + 14 = 1.0890
  - 1×: 1.0876 + 28 = 1.0904
  - 1.5×: 1.0876 + 42 = 1.0918
  - 2×: 1.0876 + 56 = 1.0932
- NY AM tags 1.0905 by 09:30, hits 1.0918 by 10:30 macro, stalls.
- → 1.5× projection delivered the daily HOD.

## Common Mistakes

- **Treating projections as primary targets.** They're estimation tools; HTF DOL (PDH/PWH/etc.) takes precedence when one of those sits closer or farther than a projection.
- **Using projections without bias.** Projections are direction-agnostic; pair with HTF bias and post-sweep displacement direction.
- **Different range definitions.** KZ-anchored range (20:00–00:00) and full-session range (18:00–03:00) produce different sizes; pick one and stick with it.

## Related Concepts

- [asian-range](asian-range.md), [asian-range-sweep](asian-range-sweep.md), [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md) — analogous extension framework.
- [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md), [ote-overview](../17-optimal-trade-entry/ote-overview.md).

## Citations

- `ICT-2017-OTE` — fib-style projection logic that AR projections borrow.
- `ICT-2022-MENTORSHIP-OVERVIEW` — AR projections taught as target tool.

> Confidence is `medium` because the specific multiples (0.5/1/1.5/2) vary across ICT teachings; some references use 1/2/3 or fib ratios. Use as a heuristic, not a fixed rule.
