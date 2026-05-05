# Fib 0.62

**Category:** 28-fibonacci-levels
**Aliases:** 62 retracement, upper OTE bound, shallow OTE
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fibonacci, fib, ote, retracement

## Definition

The 0.62 fib retracement is the **upper bound of ICT's OTE zone** — the shallowest acceptable retracement level for an OTE entry. It marks the start of the "premium retracement zone" relative to a bullish leg (or the discount zone for a bearish leg's retracement). Entries at 0.62 are less optimal than 0.705 / 0.79 but acceptable when deeper retracements aren't reached.

## Formal Criteria

- Anchor: a measured swing leg (start → end).
- 0.62 = 62% retracement of the leg's range, measured from the leg's destination back toward its origin.
- Functions as the **first** acceptable OTE entry level on a return.

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
    {"id": "c1", "expr": "level == leg_end - 0.62 * leg_size"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ict-fib-overview","fib-705","fib-79","ote-62","ote-overview","equilibrium-definition"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
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
- If bullish FVG at 1.0838 + HTF bias bullish: long entry valid at 0.62 with SL below 0.79 (1.0821).
- This is a less-optimal entry than 0.705 but acceptable when 0.705 isn't reached.

## Common Mistakes

- **Treating 0.62 as a hard support.** It's a level of interest, not a guaranteed bounce point.
- **Skipping deeper levels.** Often 0.62 holds and price runs without reaching 0.705 / 0.79; chasing a deeper entry that never came is a missed setup.

## Related Concepts

- [ict-fib-overview](ict-fib-overview.md), [fib-705](fib-705.md), [fib-79](fib-79.md), [ote-62](../17-optimal-trade-entry/ote-62.md), [ote-overview](../17-optimal-trade-entry/ote-overview.md), [equilibrium-definition](../27-equilibrium/equilibrium-definition.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
