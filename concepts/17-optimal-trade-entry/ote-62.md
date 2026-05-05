# OTE 0.62

**Category:** 17-optimal-trade-entry
**Aliases:** shallow OTE, OTE 62 entry
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, fibonacci, shallow-entry

## Definition

The OTE 0.62 entry is the **shallowest acceptable OTE entry** — the upper bound of the OTE zone. Used when price retraces only to 0.62 and finds PD-array confluence there without going deeper. R:R is reduced versus 0.705 / 0.79 entries because the SL distance to 0.79 is larger.

## Formal Criteria

- Retracement reaches 0.62 of measured leg.
- PD array (FVG / OB / breaker) present at or near 0.62.
- HTF bias agreement.
- SL placed beyond 0.79 (deep OTE bound).

## Formula / Math

```
OTE_62_entry = leg_end - 0.62 * leg_size
SL_reference = leg_end - 0.79 * leg_size      # plus buffer

# Bullish leg 1.0800 → 1.0900:
OTE_62_entry = 1.08380
SL_below_79  = 1.0815 (1.0821 - 6 pips)
Risk         = 1.0838 - 1.0815 = 23 pips
```

## Machine-Readable

```json
{
  "id": "ote-62",
  "category": "17-optimal-trade-entry",
  "aliases": ["shallow-OTE-entry"],
  "criteria": [
    {"id": "c1", "expr": "entry == leg_end - 0.62 * leg_size"},
    {"id": "c2", "expr": "PD_array_at_or_near_062 == true"},
    {"id": "c3", "expr": "SL beyond 0.79"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ote-overview","ote-705","ote-79","ote-rules","fib-62"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   leg_end ──────── 0.0
   ─────────────── 0.50 EQ
   ─────────────── 0.62  ← entry (shallowest OTE)
   ─────────────── 0.705
   ─────────────── 0.79  ← SL reference
   leg_start ──── 1.0
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 0.62 entry:**
- Leg 1.0800 → 1.0900.
- 0.62 = 1.0838; bullish FVG at 1.0836–1.0840.
- Long at 1.0838, SL 1.0815 (below 0.79 + buffer). Risk = 23 pips.
- TP1 -1.5 SD = 1.1050 → ~9.2R reward potential.

## Common Mistakes

- **Skipping 0.62 because "0.705 is better."** If 0.62 has clean PD-array confluence and 0.705 may not be reached, take the 0.62 entry.
- **Unrealistic R:R expectations.** 0.62 entries have wider SLs; calibrate position size accordingly.

## Related Concepts

- [ote-overview](ote-overview.md), [ote-705](ote-705.md), [ote-79](ote-79.md), [ote-rules](ote-rules.md), [fib-62](../28-fibonacci-levels/fib-62.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
