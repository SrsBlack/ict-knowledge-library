# OTE Failure

**Category:** 17-optimal-trade-entry
**Aliases:** failed OTE, broken OTE, OTE invalidation
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, failure, invalidation, risk

## Definition

An OTE failure is when an entered OTE setup invalidates — ultimately by price **taking out the leg-origin extreme** (fib 1.0), which is where the taught stop sits. A close beyond **0.79** is the earlier warning: once price closes past the deepest acceptable entry, the leg's structural premise is in doubt and the algorithm may be shifting bias.

> ⚠ **Corrected 2026-08-05: two distinct events, previously conflated.** This page treated a close below 0.79 as *the* invalidation because it assumed the stop sat beyond 0.79. The dedicated OTE material places the stop at the **leg-origin extreme, exactly** (`ICT-2017-OTE`), so a close past 0.79 **warns**; the leg extreme **invalidates**. Traders using the community 0.79-buffer stop experience the two as the same event — that is a property of their stop choice, not of the setup. See [ote-79](ote-79.md), [ote-overview](ote-overview.md).

## Formal Criteria

For a long OTE failure:

- Entry was taken inside [0.62, 0.79] of a measured bullish leg.
- **Warning:** price closes **below 0.79** — out of the zone, premise weakening.
- **Invalidation:** price takes out **leg_start** (fib 1.0) — the structural low that defined the leg is gone; the stop is hit and the leg is void.
- *(Invalidation semantics — whether a body close beyond the level is required, and on which timeframe — are NOT specified in the primary material. Any mechanical implementation must pin its own convention and say so.)*
- Optional confirmation: bearish FVG / displacement forms after the close-below.

For a short OTE failure: symmetric.

When failure occurs:

- **Don't fight it.** Don't add to a losing OTE expecting a deeper reversal.
- **Reassess HTF bias.** A close below 0.79 often signals HTF bias is flipping or the dealing range is being broken.
- **Look for counter-bias setups.** If HTF bias appears to be flipping, the next setups belong in the new direction.

## Formula / Math

```
long_ote_failure  := close < (leg_end - 0.79 * leg_size)
short_ote_failure := close > (leg_end - 0.79 * leg_size)     # leg_size negative for bearish leg
```

## Machine-Readable

```json
{
  "id": "ote-failure",
  "category": "17-optimal-trade-entry",
  "aliases": ["failed-OTE", "OTE-invalidation"],
  "criteria": [
    {"id": "c1", "expr": "close beyond 0.79 of measured leg in invalidation direction", "role": "warning"},
    {"id": "c2", "expr": "leg_origin_extreme (fib 1.0) taken out", "role": "invalidation"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ote-overview","ote-79","ote-rules","fib-79","htf-bias-framework"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   OTE failure (bullish setup invalidated):

   leg_end ──────── 0.0
   ─────────────── 0.50 EQ
   ─── 0.62 ────── (entry zone)
   ─── 0.705 ────  (entry tried here)
   ─── 0.79 ────── ← invalidation trigger
   ─── close ────── ← bearish close BELOW 0.79
                     → setup invalidated; leg structure broken
   leg_start ──── 1.0
```

## Timeframes

All TFs.

## Examples

**Example 1 — failed bullish OTE:**
- Leg 1.0800 → 1.0900.
- 0.79 = 1.0821; entry at 1.0830 (0.705).
- Price extends down, closes M15 candle at 1.0815 (below 0.79) — **warning: out of the zone**, premise weakening, but the stop at 1.0800 is still intact.
- Price continues and takes out 1.0800, the leg-origin low → **SL hit; setup invalidated.** HTF bias reassessed: D1 just printed CHoCH down. The bullish leg is being violated; bias is flipping.
- Action: stand aside; wait for new structure to define the next setup direction.

## Common Mistakes

- **"It'll come back."** Adding to an invalidated OTE based on hope/anchoring loses bigger.
- **No HTF reassessment.** OTE failures often herald HTF bias change. Failing to re-read HTF after a failure leads to repeated same-direction failures.
- **Over-tight SL leading to false failures.** A 1-pip overshoot of 0.79 is not a real failure on FX; require a closing print.

## Related Concepts

- [ote-overview](ote-overview.md), [ote-79](ote-79.md), [ote-rules](ote-rules.md), [fib-79](../28-fibonacci-levels/fib-79.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
