# Power of Three (PO3 / AMD)

**Category:** 12-power-of-three
**Aliases:** PO3, AMD, AMD doctrine, market-maker model, MMBM/MMSM
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PO3, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** po3, amd, market-maker-model, foundational

## Definition

The Power of Three (PO3), also called the **AMD doctrine**, is ICT's three-phase model for how the algorithm delivers price across any timeframe: **Accumulation → Manipulation → Distribution**. It's both a mental model for reading delivered price and a fractal pattern that repeats at every TF (yearly, monthly, weekly, daily, session, 90-minute). When the model runs to upside distribution, it's called **MMBM** (Market Maker Buy Model); to downside distribution, **MMSM** (Market Maker Sell Model). PO3 is the most foundational ICT framework — every named setup (Silver Bullet, Judas Swing, etc.) is an instance of PO3 at a specific scale.

## Formal Criteria

The three phases:

1. **Accumulation** — quiet, range-bound consolidation while institutions build positions.
2. **Manipulation** — engineered fake-out move (Judas Swing) that sweeps liquidity in the wrong direction, providing counter-flow for institutional fills.
3. **Distribution** — the true intended directional move toward HTF DOL.

Some ICT framings add a 4th phase **X (continuation/reversal)** for the late-cycle behavior — see [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md) for the AMD-X expansion in Quarterly Theory.

## Formula / Math

```
po3_phases = ["accumulation", "manipulation", "distribution"]
po3_x      = "continuation_or_reversal"   # optional 4th in some framings

mmbm := PO3 cycle ending in upward distribution
mmsm := PO3 cycle ending in downward distribution
```

## Machine-Readable

```json
{
  "id": "power-of-three",
  "category": "12-power-of-three",
  "aliases": ["PO3", "AMD", "AMD-doctrine", "market-maker-model", "MMBM", "MMSM"],
  "criteria": [
    {"id": "c1", "expr": "phases = [accumulation, manipulation, distribution]"},
    {"id": "c2", "expr": "fractal — repeats at every TF"},
    {"id": "c3", "expr": "MMBM = upside distribution; MMSM = downside"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["accumulation-phase","manipulation-phase","distribution-phase","intraday-amd","htf-amd","amd-cycle-overview","amd-vs-po3","quarterly-shift-theory","judas-swing","range-contraction","range-expansion"],
  "sources": ["ICT-2016-PO3","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   PO3 / AMD across one trading day:

   Asia (accumulation)        London open (manipulation)       NY AM (distribution)
   ────────────                  /\                                   /\
        /\  /\                  /  \   ← Judas swing                 /  \
       /  \/  \                /    \    (sweeps Asian range)       /    \
      /        \              /      \                             /      \
                                       \                          /
                                        \  ← reversal             /
                                         \                       /
                                          \________→ true delivery
                                                     (distribution toward HTF DOL)
```

## Timeframes

PO3 is fractal. Day-PO3 maps to Asia-London-NY phases; H1-PO3 maps to a 3-hour cycle of accumulation-manipulation-distribution; M5-PO3 maps to ~15-minute mini-cycles inside a session.

## Examples

**Example 1 — daily MMBM (bullish PO3):**
- Asia: 30-pip range, low-volatility accumulation.
- London open: M5 wicks below Asia low (manipulation / Judas), closes back inside.
- NY AM: 60-pip green displacement, takes PDH BSL (distribution).
- → MMBM completed.

**Example 2 — H1 MMSM:**
- H1 range-bound for 6 hours (accumulation).
- 7th hour: H1 wick above the range high (manipulation).
- Next 4 H1 candles: bearish displacement breaking PWL (distribution).
- → H1 MMSM.

## Common Mistakes

- **Forcing every move into PO3.** Some moves are pure expansion or pure consolidation; PO3 isn't always the right read.
- **Mistaking accumulation for trend continuation.** Choppy ranges that look like accumulation may be late-distribution exhaustion instead.
- **Single-TF PO3 read.** PO3 is most useful when read with HTF bias — a daily MMBM aligned with weekly bullish bias is high-conviction; against weekly bias is lower.

## Related Concepts

- [accumulation-phase](accumulation-phase.md), [manipulation-phase](manipulation-phase.md), [distribution-phase](distribution-phase.md), [intraday-amd](intraday-amd.md), [htf-amd](htf-amd.md).
- [amd-cycle-overview](../24-amd-cycle/amd-cycle-overview.md), [amd-vs-po3](../24-amd-cycle/amd-vs-po3.md).
- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [judas-swing](../13-judas-swing/judas-swing.md), [range-contraction](../01-market-structure/range-contraction.md), [range-expansion](../01-market-structure/range-expansion.md).

## Citations

- `ICT-2016-PO3` — original PO3 introduction in 2016 mentorship.
- `ICT-2022-MENTORSHIP-OVERVIEW` — PO3 operational framing refined.
