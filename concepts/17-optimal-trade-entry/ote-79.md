# OTE 0.79

**Category:** 17-optimal-trade-entry
**Aliases:** deep OTE, OTE 79 entry, last-chance OTE
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, fibonacci, deep-entry

## Definition

The OTE 0.79 entry is the **deepest acceptable OTE entry** — the lower bound of the zone. It offers the tightest stop distance of the three depths, but the entry is later in the retracement so the probability of price reaching it at all is lower. ICT does not demand it: "at or very close to the 62%… I'm not going to demand 79%" (`ICT-2017-OTE`).

> ⚠ **Corrected 2026-08-05: 0.79 is an ENTRY bound, not the stop.** This file previously described 0.79 as "the OTE invalidation reference" with an SL a few pips beyond it. The dedicated OTE material places the stop at the **leg-origin extreme (fib 1.0), exactly** — "my stop will be exactly at this low, not 10 pips [or] 5 to 10 pips below that" (`ICT-2017-OTE`); Vol.01's worked example did the same. A "just beyond 0.79 + buffer" stop is a widespread community and backtesting variant with **no primary-source quote behind it**; it produces a structurally different trade (much tighter risk, far higher stop-out rate on ordinary noise). Use it if you want, but label it as the variant it is. See [ote-overview](ote-overview.md).

## Formal Criteria

- Retracement reaches 0.79.
- PD array at the level.
- HTF bias agreement.
- **SL at the leg-origin extreme (fib 1.0).** *(Variant, community-attributed: just beyond 0.79 with a 5–10 pip buffer on FX.)*

## Formula / Math

```
OTE_79_entry = leg_end - 0.79 * leg_size
SL           = leg_start                    # fib 1.0, exactly — the taught stop

# Bullish leg 1.0800 → 1.0900:
OTE_79_entry = 1.0821
SL           = 1.0800
Risk         = 21 pips
# first target 1.0900 (fib 0.0) = 79 pips ≈ 3.8R — the deepest entry carries the best
# R:R of the three depths, at the cost of a lower chance of ever being filled.

# community variant (NOT primary-sourced):
SL_variant   = 1.0816     # 0.79 minus a 5-pip buffer; risk 5 pips
```

## Machine-Readable

```json
{
  "id": "ote-79",
  "category": "17-optimal-trade-entry",
  "aliases": ["deep-OTE", "last-chance-OTE"],
  "criteria": [
    {"id": "c1", "expr": "entry == leg_end - 0.79 * leg_size"},
    {"id": "c2", "expr": "PD_array_at_079 == true"},
    {"id": "c3", "expr": "SL == leg_origin_extreme (fib 1.0)"},
    {"id": "c4", "expr": "SL just beyond 0.79", "strength": "community-variant", "primary_sourced": false}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ote-overview","ote-62","ote-705","ote-rules","ote-failure","fib-79"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   leg_end ──────── 0.0
   ─────────────── 0.50 EQ
   ─────────────── 0.62
   ─────────────── 0.705
   ─────────────── 0.79  ← entry (deepest acceptable)
   leg_start ──── 1.0    ← SL sits HERE (fib 1.0, exactly)
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 0.79 entry (last-chance):**
- Leg 1.0800 → 1.0900.
- 0.79 = 1.0821; bullish OB at 1.0820–1.0822.
- Long at 1.0821, **SL 1.0800 (the leg-origin low). Risk = 21 pips.**
- TP1 = 1.0900 (fib 0.0, prior extreme) → 79 pips ≈ 3.8R; then 1.0927 / 1.0962 / 1.1000.
- *(Community variant: SL 1.0816 on a 5-pip buffer → 5 pips risk and a ~16R first target. The arithmetic is seductive and the stop-out rate is the reason ICT does not teach it.)*

## Common Mistakes

- **Below-0.79 entries.** Past 0.79 the setup is out of the zone; don't commit deeper.
- ⚠ **Reading 0.79 as the invalidation level.** It bounds the *entry*, not the risk. The taught stop is the leg origin; an entry that trades past 0.79 has left the zone but has not yet hit the stop.
- **Insufficient SL buffer (variant only).** If you do use the community 0.79-based stop, pixel-precise SLs at exactly 0.79 get stopped on noise.
- **Assuming 0.79 will hit.** Many setups stop at 0.62 or 0.705; if the trade plan requires 0.79, you may miss the move waiting.

## Related Concepts

- [ote-overview](ote-overview.md), [ote-62](ote-62.md), [ote-705](ote-705.md), [ote-rules](ote-rules.md), [ote-failure](ote-failure.md), [fib-79](../28-fibonacci-levels/fib-79.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
