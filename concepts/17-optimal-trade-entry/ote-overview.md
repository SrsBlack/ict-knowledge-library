# Optimal Trade Entry — Overview

**Category:** 17-optimal-trade-entry
**Aliases:** OTE, optimal entry, OTE zone
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, fibonacci, entry, foundational

## Definition

Optimal Trade Entry (OTE) is ICT's **canonical entry methodology** for taking positions in the direction of HTF bias on a measured pullback. The OTE zone is the **0.62–0.79 retracement** of a clean swing leg, with **0.705 as the optimal mid-point**. Entries within OTE are taken with PD-array confluence (FVG, OB, breaker) at the level. OTE is one of the original ICT setups (2017) and remains a foundational entry tool taught in every mentorship cycle since.

## Formal Criteria

A canonical OTE setup requires:

- A clean **measured swing leg** in the bias direction (start → end, on a structurally significant TF).
- A **retracement** of price back into the 0.62–0.79 zone of that leg.
- A **PD array** present in the OTE zone (FVG, OB, breaker, mitigation) — the entry trigger.
- **HTF bias agreement** — long OTE entries only on bullish bias, short OTE entries on bearish.
- **Invalidation** at or just beyond 0.79 (deep OTE).

## Formula / Math

```
leg_size = leg_end - leg_start

OTE_upper = leg_end - 0.62 * leg_size      # shallowest OTE
OTE_optimal = leg_end - 0.705 * leg_size   # optimal mid-point
OTE_deep = leg_end - 0.79 * leg_size       # deepest OTE / invalidation reference

# Bullish leg 1.0800 → 1.0900:
OTE_zone = [1.0821, 1.0838]    # [0.79, 0.62]
OTE_optimal = 1.08295
```

## Machine-Readable

```json
{
  "id": "ote-overview",
  "category": "17-optimal-trade-entry",
  "aliases": ["OTE", "optimal-entry"],
  "criteria": [
    {"id": "c1", "expr": "retracement_in [0.62, 0.79] of measured leg"},
    {"id": "c2", "expr": "PD_array_present_in_zone == true"},
    {"id": "c3", "expr": "HTF_bias_agrees_with_entry_direction == true"},
    {"id": "c4", "expr": "invalidation_at_or_beyond_0.79 == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ote-62","ote-705","ote-79","ote-rules","ote-failure","ict-fib-overview","fib-62","fib-705","fib-79","fib-vs-ote","standard-deviation-projections","pd-array-definition"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OTE setup:

   leg_end ──────── 0.0  (recent swing high)
   ───────────────  0.50 (EQ)
   ─── 0.62 ────── ┐
                   │ OTE zone
   ─── 0.705 ────  │ ← optimal entry (with PD-array)
                   │
   ─── 0.79 ────── ┘ ← deep entry / invalidation
   leg_start ──── 1.0  (recent swing low)

   Long entry at 0.705 with FVG/OB at the level.
   SL just below 0.79.
   Targets via SD projections (-1.5, -2.0).
```

## Timeframes

Most actionable on M5–H4 entry TFs. Daily OTE setups exist but the swing leg sizes are larger and the SL distances scale up.

## Examples

**Example 1 — bullish H1 OTE entry:**
- HTF bias bullish.
- H1 leg: 1.0800 (LTL) → 1.0900 (recent LTH). 100-pip leg.
- OTE zone = [1.0821, 1.0838], optimal at 1.08295.
- Price retraces; M15 prints bullish FVG at 1.0828–1.0832 (within OTE).
- Long entry at 1.0830 (≈ optimal), SL at 1.0815 (below 0.79 + 6-pip buffer).
- Targets: -1.5 SD = 1.1050 (~220 pips from entry), -2.0 SD = 1.1100 (~270 pips).
- R:R: 15-pip risk vs 220-pip first target = ~14.7R to -1.5 SD; ~18R to -2.0 SD.

## Common Mistakes

- **OTE without PD array.** Pure fib-level entries with no FVG / OB at the level lack the algorithmic anchor; conviction is too low.
- **OTE against HTF bias.** Counter-trend OTE setups need explicit HTF reversal context (CHoCH/MSS). Without it, the trade fights the algorithm.
- **Demanding exact 0.705.** Use a buffer ±0.5–1 pip on FX. Pixel-precision misses fills.
- **Ignoring leg quality.** A choppy, overlapping "leg" produces unreliable retracement levels. Use clean swing legs only.

## Related Concepts

- [ote-62](ote-62.md), [ote-705](ote-705.md), [ote-79](ote-79.md), [ote-rules](ote-rules.md), [ote-failure](ote-failure.md) — per-level and rules deep-dives.
- [ict-fib-overview](../28-fibonacci-levels/ict-fib-overview.md), [fib-62](../28-fibonacci-levels/fib-62.md), [fib-705](../28-fibonacci-levels/fib-705.md), [fib-79](../28-fibonacci-levels/fib-79.md), [fib-vs-ote](../28-fibonacci-levels/fib-vs-ote.md), [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md).
- [pd-array-definition](../05-pd-arrays/pd-array-definition.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
