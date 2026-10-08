# Fib 0.62

**Category:** 28-fibonacci-levels
**Aliases:** 62 retracement, upper OTE bound, shallow OTE
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2020-OTE-VOL09, ICT-2021-OTE-SCALPING-EXERCISE, ICT-2021-OTE-PRICE-ACTION-LESSON, ICT-2016-EQUILIBRIUM-DISCOUNT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fibonacci, fib, ote, retracement

## Definition

The 0.62 fib retracement is the **upper bound of ICT's OTE zone** — the shallowest level of the 0.62–0.79 retracement band. It marks the start of the "deep discount" zone relative to a bullish leg (or the premium zone for a bearish leg's retracement) — "the 62% to 79% of the tradesman [levels]… that's the deep discount that we look for in bullish conditions and why Fibonacci 62% to 79% of the tradesman levels work" (`ICT-2016-EQUILIBRIUM-DISCOUNT`, 41:36–41:48).

> ⚠ **Era-split, corrected 2026-10-08 — the depth-vs-fill-risk framing was collapsed the wrong way.** This page previously called 0.62 "less optimal than 0.705 / 0.79." The 2017 Primer *does* prefer depth — "I want to get as deep as I can… into that 70.5 level" (`ICT-2017-OTE`, 18:46–18:52) — but the 2020–21 applied material makes **0.62 the rule, not the fallback**: "keeping with the rules of this model we're using the 62% retracement level" (`ICT-2020-OTE-VOL09`, 02:41); "don't try to do the 70.5, don't look for the 79, use 62" (`ICT-2021-OTE-SCALPING-EXERCISE`, 13:32–13:40). The reason is fill probability and spread, not setup quality — see [ote-62](../17-optimal-trade-entry/ote-62.md), which already records 0.62 as the default executable entry in the applied material. This page previously contradicted that sibling page; it no longer does.

## Formal Criteria

- Anchor: a measured swing leg (start → end).
- 0.62 = 62% retracement of the leg's range, measured from the leg's destination back toward its origin.
- **Era-split role:** the shallowest geometric bound of the zone (Primer framing), AND the default executable entry in the 2020–21 applied material (fill-probability framing). See [ote-62](../17-optimal-trade-entry/ote-62.md).

## Formula / Math

```
leg_size = leg_end - leg_start
fib_62  = leg_end - 0.62 * leg_size

# Bullish leg from 1.0800 to 1.0900:
fib_62 = 1.0900 - 0.62 * 100 = 1.08380
```

## Machine-Readable

```json
{
  "id": "fib-62",
  "category": "28-fibonacci-levels",
  "aliases": ["62-retracement", "upper-OTE-bound", "shallow-OTE"],
  "criteria": [
    {"id": "c1", "expr": "level == leg_end - 0.62 * leg_size"},
    {"id": "c2", "expr": "role == shallowest geometric bound (Primer) AND default executable entry (2020-21 applied material)", "strength": "era-fork"},
    {"id": "c3", "expr": "SL == leg_origin_extreme (fib 1.0), exactly — never a 0.79-based stop"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["ict-fib-overview","fib-705","fib-79","ote-62","ote-overview","equilibrium-definition"],
  "sources": ["ICT-2017-OTE","ICT-2020-OTE-VOL09","ICT-2021-OTE-SCALPING-EXERCISE","ICT-2021-OTE-PRICE-ACTION-LESSON","ICT-2016-EQUILIBRIUM-DISCOUNT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   leg_end ──────── 0.0
   ─────────────── 0.50 (EQ)
   ─────────────── 0.62 ← shallowest OTE
   ─────────────── 0.705 (optimal)
   ─────────────── 0.79 (deepest OTE)
   leg_start ──── 1.0
```

## Timeframes

All TFs.

## Examples

**Example 1 — bullish leg shallow OTE:**
- Leg 1.0800 → 1.0900 (100 pips).
- fib_62 = 1.08380.
- If bullish FVG at 1.0838 + HTF bias bullish: long entry valid at 0.62, **SL at 1.0800 — the leg-origin low, exactly.** Risk = 38 pips.
- ⚠ *Corrected 2026-10-08: this example previously placed the stop "below 0.79 (1.0821)." No source anywhere in the OTE corpus references the stop to 0.79; ICT states it flatly for the Primer's own worked example — "my stop will be exactly at this low… not 10 pips or five pips below that" (`ICT-2017-OTE`, 12:32–12:39). The same correction was already applied to [ote-62](../17-optimal-trade-entry/ote-62.md), [ote-705](../17-optimal-trade-entry/ote-705.md), and [ote-79](../17-optimal-trade-entry/ote-79.md) on 2026-08-05; this page had not been updated to match.*
- In the 2020–21 applied material this is the **default** entry depth, not a fallback — see the era-split note above.

## Common Mistakes

- **Treating 0.62 as a hard support.** It's a level of interest, not a guaranteed bounce point.
- **Skipping deeper levels in the Primer framing.** In the 2017 Primer, 0.62 holds and price can run without reaching 0.705 / 0.79; chasing a deeper entry that never came is a missed setup there. ⚠ In the 2020–21 applied material this is inverted — 0.62 is the entry to take, and waiting for 0.705/0.79 risks a missed fill.
- ⚠ **Putting the stop below 0.79.** The taught stop is the leg-origin extreme, exactly — never a level referenced to 0.79. See the Example above.

## Related Concepts

- [ict-fib-overview](ict-fib-overview.md), [fib-705](fib-705.md), [fib-79](fib-79.md), [ote-62](../17-optimal-trade-entry/ote-62.md), [ote-overview](../17-optimal-trade-entry/ote-overview.md), [equilibrium-definition](../27-equilibrium/equilibrium-definition.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.

Added 2026-10-08:

- `ICT-2016-EQUILIBRIUM-DISCOUNT` (29:25) — "so that's where the optimal trade entry idea came from when I was using the 62% to 79% tradesmen levels" (Year Introduced correction); (41:36–41:48) "the 62% to 79% of the tradesman… that's the deep discount that we look for in bullish conditions and why Fibonacci 62% to 79% of the tradesman levels work."
- `ICT-2017-OTE` (18:46–18:52) — "I want to get as deep as I can… into that 70.5 level" (Primer's depth preference).
- `ICT-2020-OTE-VOL09` (02:41) — "keeping with the rules of this model we're using the 62% retracement level" (2020-series rule).
- `ICT-2021-OTE-SCALPING-EXERCISE` (13:32–13:40) — "don't try to do the 70.5, don't look for the 79, use 62."
- `ICT-2021-OTE-PRICE-ACTION-LESSON` (04:07–04:15) — "that's your 62% retracement level, that's your minimum level to reach for for shorting."
