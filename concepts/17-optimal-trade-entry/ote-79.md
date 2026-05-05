# OTE 0.79

**Category:** 17-optimal-trade-entry
**Aliases:** deep OTE, OTE 79 entry, last-chance OTE
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, fibonacci, deep-entry

## Definition

The OTE 0.79 entry is the **deepest acceptable OTE entry** — also serves as the OTE invalidation reference. R:R is improved versus 0.705 (smaller SL distance) but the entry is later in the retracement so probability of having reached it is lower. SL placement is just a few pips below 0.79.

## Formal Criteria

- Retracement reaches 0.79.
- PD array at the level.
- HTF bias agreement.
- SL just beyond 0.79 (5–10 pip buffer on FX).

## Formula / Math

```
OTE_79_entry = leg_end - 0.79 * leg_size
SL_buffer    = 5 pips      # tune by instrument

SL = OTE_79_entry - SL_buffer       # for longs

# Bullish leg 1.0800 → 1.0900:
OTE_79_entry = 1.0821
SL           = 1.0816
Risk         = 5 pips
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
    {"id": "c3", "expr": "SL just beyond 0.79"}
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
   ─────────────── 0.79  ← entry (deep)
                          SL just below
   leg_start ──── 1.0
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 0.79 entry (last-chance):**
- Leg 1.0800 → 1.0900.
- 0.79 = 1.0821; bullish OB at 1.0820–1.0822.
- Long at 1.0821, SL 1.0816 (5-pip buffer). Risk = 5 pips.
- TP1 -1.5 SD = 1.1050 → ~46R potential (extreme R:R because of tight SL).

## Common Mistakes

- **Below-0.79 entries.** Past 0.79 is OTE-invalidated; don't commit deeper.
- **Insufficient SL buffer.** Pixel-precise SLs at exactly 0.79 get stopped on noise.
- **Assuming 0.79 will hit.** Many setups stop at 0.62 or 0.705; if the trade plan requires 0.79, you may miss the move waiting.

## Related Concepts

- [ote-overview](ote-overview.md), [ote-62](ote-62.md), [ote-705](ote-705.md), [ote-rules](ote-rules.md), [ote-failure](ote-failure.md), [fib-79](../28-fibonacci-levels/fib-79.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
