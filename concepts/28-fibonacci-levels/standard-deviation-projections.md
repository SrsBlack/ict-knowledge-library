# Standard Deviation Projections

**Category:** 28-fibonacci-levels
**Aliases:** SD projections, fib projection targets, ICT projection levels
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2020-OTE-VOL10, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fibonacci, projections, targets, sd

## Definition

Standard Deviation projections are ICT's measured-leg extension targets — price levels **beyond** the original swing leg's destination, calculated as multiples of the leg's size. ICT uses negative fib ratios (−1.5, −2.0, −2.5, −4.0) to denote extension beyond the leg. These are **target levels**, not entries: when an OTE entry is taken, SD projections answer "where might price reach?" The most-cited targets are −1.5 SD (first extension) and −2.0 SD (typical full-delivery target).

## Formal Criteria

- Anchor: the same swing leg used for retracement (start → end), on **candle bodies** — see [fib-anchoring](fib-anchoring.md).
- Each negative fib ratio extends past `leg_end` by that multiple of `leg_size`.
- Standard projection set: −1.5, −2.0, −2.5, −4.0.
- Extreme: −4.0 used for major reversal-anchor targets (rarely reached in a single trade).

⚠ **Two different SD sets are taught, and the OTE series uses the shallower one.** In the 2020 *OTE Pattern Recognition Series* the fib preset carries **half / full / one-and-a-half / two** standard deviations — i.e. **−0.5, −1.0, −1.5, −2.0** — with ICT walking the preset's levels directly: "you can add a negative 1.5 level… so that way you have your half standard deviation, full standard deviation, one and a half standard deviation and two standard deviations" (`ICT-2020-OTE-VOL10`, 01:39–02:00). The −0.5 and −1.0 levels are the routine scaling targets in that series (`ICT-2020-OTE-VOL04`–`VOL09`, `VOL12`, `VOL15`); −2.5 and −4.0 do not appear in it. Treat −1.5/−2.0/−2.5/−4.0 as the wider-context set and −0.5/−1.0/−1.5/−2.0 as the OTE-series set; state which one an implementation uses. *(Recorded 2026-08-09.)*

## Formula / Math

```
leg_size = leg_end - leg_start

project(level) = leg_end - level * leg_size      # negative level extends past leg_end

# Bullish leg 1.0800 → 1.0900 (leg_size = 100):
SD_-1_5 = 1.0900 - (-1.5) * 100 = 1.0900 + 150 = 1.1050
SD_-2_0 = 1.0900 + 200 = 1.1100
SD_-2_5 = 1.0900 + 250 = 1.1150
SD_-4_0 = 1.0900 + 400 = 1.1300
```

## Machine-Readable

```json
{
  "id": "standard-deviation-projections",
  "category": "28-fibonacci-levels",
  "aliases": ["SD-projections", "fib-projection-targets", "ICT-projection-levels"],
  "criteria": [
    {"id": "c1", "expr": "projection_levels = [-1.5, -2.0, -2.5, -4.0]"},
    {"id": "c2", "expr": "anchored_to_same_leg_as_retracement == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ict-fib-overview","symmetrical-price-projections","fib-62","fib-705","fib-79","draw-on-liquidity","external-range-liquidity"],
  "sources": ["ICT-2017-OTE","ICT-2020-OTE-VOL10","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
                              ─── -4.0 SD (extreme)
                              ─── -2.5 SD
                              ─── -2.0 SD (typical full-delivery)
                              ─── -1.5 SD (first extension)
   leg_end ─────────  ← 0.0
   ─── 0.50 (EQ) ──
   ─── 0.62 ────── (OTE retracement zone)
   ─── 0.705 ────
   ─── 0.79 ────
   leg_start ─────  ← 1.0
```

## Timeframes

All TFs. HTF SD projections often align with HTF DOL (PWH, PMH, etc.) — when an SD level coincides with an existing liquidity pool, conviction increases.

## Examples

**Example 1 — partial-take ladder using SD projections:**
- Leg 1.0800 → 1.0900.
- OTE entry at 0.705 = 1.08295.
- TP ladder:
  - TP1: -1.5 SD = 1.1050 (~22.7R from a 15-pip risk)
  - TP2: -2.0 SD = 1.1100
  - Final: -2.5 SD = 1.1150 if extended delivery
- Often coincides with PWH (e.g., 1.1095) → confirms TP2 zone as a real liquidity destination.

## Common Mistakes

- **Using full classical projection set.** Classical 1.272, 1.618, 2.618 don't map to ICT's −1.5/−2.0/−2.5/−4.0. Pick one framework.
- **Treating SD targets as guarantees.** They are areas of interest. Some setups never reach -1.5; others fly past -4.0 on news.
- **Ignoring HTF DOL.** A nearby HTF liquidity pool often resolves before the SD target; check for collisions.

## Related Concepts

- [ict-fib-overview](ict-fib-overview.md), [symmetrical-price-projections](symmetrical-price-projections.md).
- [fib-62](fib-62.md), [fib-705](fib-705.md), [fib-79](fib-79.md).
- [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md), [external-range-liquidity](../02-liquidity/external-range-liquidity.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
