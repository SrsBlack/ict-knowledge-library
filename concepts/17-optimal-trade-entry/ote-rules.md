# OTE Rules

**Category:** 17-optimal-trade-entry
**Aliases:** OTE setup rules, OTE checklist
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, rules, checklist

## Definition

OTE rules are the operational checklist for taking an OTE entry — the discipline that distinguishes a high-probability OTE from a low-probability fib-level fade. ICT teaches OTE not as "buy at 0.705" but as a **multi-condition checklist**.

## Formal Criteria — The OTE Checklist

A valid OTE entry requires ALL of:

1. **HTF bias direction confirmed.** Long OTEs only on bullish bias; shorts only on bearish.
2. **Clean measured leg** (leg_start and leg_end are confirmed swing pivots, ideally with displacement).
3. **Retracement enters [0.62, 0.79]**.
4. **PD array at the entry level** (FVG / OB / breaker / mitigation).
5. **Entry trigger** — typically a lower-TF MSS / CHoCH / FVG forming inside the OTE zone confirms the reversal.
6. **SL beyond 0.79** with appropriate buffer.
7. **Targets defined** — at minimum -1.5 SD and -2.0 SD, optionally aligned with HTF DOL.

Missing any of (1)–(6) significantly reduces conviction. (7) is for trade management; missing it doesn't invalidate the entry but does compromise execution.

## Formula / Math

```
ote_entry_valid := htf_bias_agree
                    AND clean_measured_leg
                    AND retracement_in [0.62, 0.79]
                    AND pd_array_at_entry_level
                    AND entry_trigger_present
                    AND sl_beyond_079_with_buffer
```

## Machine-Readable

```json
{
  "id": "ote-rules",
  "category": "17-optimal-trade-entry",
  "aliases": ["OTE-checklist", "OTE-rules"],
  "criteria": [
    {"id": "c1", "expr": "all six core checks pass"},
    {"id": "c2", "expr": "checks: htf_bias, clean_leg, retracement_zone, pd_array, entry_trigger, sl_placement"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ote-overview","ote-62","ote-705","ote-79","ote-failure","htf-bias-framework","pd-array-definition"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   OTE entry checklist (bullish example):

   ☐ HTF bias bullish?                           [check D / W]
   ☐ Clean leg (start = LTL, end = recent LTH)?  [structural confirmation]
   ☐ Retracement entered [0.62, 0.79]?           [fib measurement]
   ☐ FVG / OB / breaker at entry level?          [PD-array check]
   ☐ M5 / M15 MSS or FVG trigger formed inside?  [entry confirmation]
   ☐ SL set beyond 0.79 + 5-pip buffer?          [risk control]
   ☐ Targets at -1.5 SD, -2.0 SD, HTF DOL?       [trade management]

   All checked → take the entry.
   Missing any of 1-6 → skip or reduce conviction.
```

## Timeframes

All TFs.

## Examples

**Example 1 — full checklist pass:**
- Daily bias bullish ✓.
- H1 leg 1.0800 → 1.0900 (clean, displacement-anchored) ✓.
- Retracement reaches 1.0830 (0.705) ✓.
- M15 bullish FVG at 1.0828–1.0832 ✓.
- M5 prints bullish CHoCH inside the FVG zone ✓.
- SL at 1.0815 (below 0.79 + 6-pip buffer) ✓.
- Targets: -1.5 SD = 1.1050 (no nearby HTF DOL conflict) ✓.
- → take the entry.

**Example 2 — checklist fails on PD array:**
- All conditions met EXCEPT no FVG/OB at the OTE level.
- → skip; entry has no algorithmic anchor. Wait for fresh structure.

## Common Mistakes

- **Skipping the leg-quality check.** Choppy "legs" produce unreliable retracement levels.
- **Skipping the entry trigger.** Pre-positioning at the fib level without a lower-TF confirmation candle invites SL hits on overshoots.
- **Force-fitting OTEs onto every chart.** Not every retracement is OTE-grade; some moves don't pull back into 0.62–0.79 at all (price runs without retest).

## Related Concepts

- [ote-overview](ote-overview.md), [ote-62](ote-62.md), [ote-705](ote-705.md), [ote-79](ote-79.md), [ote-failure](ote-failure.md).
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [pd-array-definition](../05-pd-arrays/pd-array-definition.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
