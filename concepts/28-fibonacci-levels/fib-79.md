# Fib 0.79

**Category:** 28-fibonacci-levels
**Aliases:** 79 retracement, deep OTE, lower OTE bound, OTE invalidation reference
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fibonacci, fib, ote, deep-entry

## Definition

The 0.79 fib retracement is the **deepest acceptable OTE entry level** — and the canonical **invalidation reference** for OTE setups. Entries deeper than 0.79 are not OTE; they are last-chance fades that ICT teaches as much lower probability. SLs for OTE entries typically sit just beyond 0.79 (with a small buffer) so the trade is invalidated cleanly if the market overshoots the OTE zone.

## Formal Criteria

- 0.79 = 79% retracement of the measured leg.
- Functions as the **deep OTE entry** AND the OTE invalidation level.
- Beyond 0.79 = OTE setup invalidated; expect the leg's origin to be retested or broken.

## Formula / Math

```
fib_79 = leg_end - 0.79 * leg_size

# Bullish leg from 1.0800 to 1.0900:
fib_79 = 1.0900 - 0.79 * 100 = 1.0821
```

## Machine-Readable

```json
{
  "id": "fib-79",
  "category": "28-fibonacci-levels",
  "aliases": ["79-retracement", "deep-OTE", "OTE-invalidation-reference"],
  "criteria": [
    {"id": "c1", "expr": "level == leg_end - 0.79 * leg_size"},
    {"id": "c2", "expr": "functions_as_deep_entry_and_SL_reference == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ict-fib-overview","fib-62","fib-705","ote-79","ote-overview","ote-failure"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   leg_end ──────── 0.0
   ─────────────── 0.50 (EQ)
   ─────────────── 0.62 (shallow OTE)
   ─────────────── 0.705 (optimal)
   ─────────────── 0.79  ← DEEP / INVALIDATION
   ─────────────── beyond 0.79 = OTE invalidated
   leg_start ──── 1.0
```

## Timeframes

All TFs.

## Examples

**Example 1 — 0.79 entry as last-chance:**
- Leg 1.0800 → 1.0900.
- fib_79 = 1.0821.
- HTF bullish; price retraces past 0.62, past 0.705, hits 0.79 with bullish OB nearby.
- Long entry at 0.79 with SL below 1.0815 (buffer below 0.79).
- Tight risk; conviction reduced versus 0.705 entry but still valid.

**Example 2 — 0.79 invalidation:**
- Leg 1.0800 → 1.0900.
- Price retraces to 1.0820, then closes 1.0815 (below 0.79).
- → OTE setup invalidated. Don't fight it; reassess for a counter-bias setup or wait for new structure.

## Common Mistakes

- **Entering deeper than 0.79.** Below 0.79 is past OTE; entries here are no longer ICT-valid OTE setups.
- **No SL buffer.** SL exactly at 0.79 gets stopped on small spikes. Add a few pips of buffer.
- **Forgetting depth context.** A 0.79 entry on a 30-pip leg has tiny risk; a 0.79 entry on a 200-pip leg has much larger risk. Position-size accordingly.

## Related Concepts

- [ict-fib-overview](ict-fib-overview.md), [fib-62](fib-62.md), [fib-705](fib-705.md), [ote-79](../17-optimal-trade-entry/ote-79.md), [ote-overview](../17-optimal-trade-entry/ote-overview.md), [ote-failure](../17-optimal-trade-entry/ote-failure.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
