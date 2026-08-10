# Asian Range Projections

**Category:** 14-asian-range
**Aliases:** Asia projections, AR projections, AR extension targets
**ICT Confidence:** medium
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-DAYTRADE-HIGH-PROBABILITY, ICT-2017-FILLING-NUMBERS
**Tags:** asian-range, projections, targets

## Definition

Asian range projections are extension targets that use the Asian range size as the unit of measurement and project price levels above and below the range — typically at multiples of 0.5×, 1×, 1.5×, 2× the Asian range size. ICT teaches that London / NY delivery often reaches an integer multiple of the Asian range from the side opposite to the initial sweep. Useful for estimating distance-of-day targets and partial-take levels.

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018` sourced to
`ICT-2017-OTE` (a fib-leg teaching that never mentions the Asian range) and the placeholder
`ICT-2022-MENTORSHIP-OVERVIEW`. The **Month 08** lecture *High Probability Daytrade Setups*
(Apr 2017) already projects off the Asian range as the unit — "I'm looking for two or one standard
deviation drops of the Asian range, total range down" [11:12], and "scale something off every two
standard deviations of the Asian range or central bank dealer's range" [16:38]. The **Month 09**
lecture *Filling The Numbers* (May 2017) gives the target ladder explicitly: "utilizing the Asian
range, when you're buying the market, buying below the Asian range, you count the high of the Asian
range as **level one of four to fill**" [10:47]. Re-dated to 2017. ⚠ Note that ICT counts the
*opposite bound itself* as level 1 and each further range-multiple as levels 2–4; the 0.5× and 1.5×
half-multiples below are a later community reading, which is part of why confidence is `medium`.

⚠ **ICT states a hard 1–2 standard-deviation ceiling, and states it as a contrast class.** Setting the
Asian range against the flout, which is unbounded: "there isn't a rule-based idea like there is for
central bank dealers range or Asian range — **Asian range can go up one or two standard deviations and
create a high, or down one or two standard deviations created a low of the day.** Flout can be many
standard deviations" (`ICT-2017-INTRADAY-TOP-DOWN` [15:01–15:22]). So the ICT-sourced ladder is
**1× and 2× only, with no half-steps** — which corroborates the `medium` confidence above rather than
conflicting with it. Treat 0.5× and 1.5× as community additions, not as taught levels.

⚠ **Entry-zone rule, previously uncaptured.** Bullish: "the best scenario is to go long **below the
Asian range low**, but as long as I'm **below the Asian range high** I'll still take what I consider
high probability longs" [10:48–11:00]; bearish mirror at [11:01–11:13]. And the confluence claim —
Asian-range deviations overlapping CBDR deviations *and* a PD array put you "very close to the high or
low of the day" [12:23–12:47].

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
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["asian-range","asian-range-sweep","standard-deviation-projections","draw-on-liquidity","ote-overview"],
  "sources": ["ICT-2017-DAYTRADE-HIGH-PROBABILITY","ICT-2017-FILLING-NUMBERS"]
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

- `ICT-2017-DAYTRADE-HIGH-PROBABILITY` — the Asian range used as a standard-deviation unit for both
  entry and exit: "one to two standard deviations in the Asian range coupled with discount PD array"
  [11:05], "two or one standard deviation drops of the Asian range, total range down" [11:12],
  "scale something off every two standard deviations of the Asian range" [16:38].
- `ICT-2017-FILLING-NUMBERS` — the four-level target ladder: "utilizing the Asian range ... you count
  the high of the Asian range as level one of four to fill" [10:47–10:57]; the Asian range named as
  one of four interchangeable projection bases alongside pivots, CBDR and the open float [19:18].

> Confidence is `medium` because the specific multiples (0.5/1/1.5/2) vary across ICT teachings; some references use 1/2/3 or fib ratios. Use as a heuristic, not a fixed rule.
