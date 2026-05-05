# Asian Range

**Category:** 14-asian-range
**Aliases:** Asia range, AR, Asian session range
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** asian-range, liquidity, foundational

## Definition

The Asian range is the price range formed during the Asia session (typically 18:00 prev → 03:00 NY, with most-tracked formation 20:00–00:00 NY inside the Asia killzone). It is bounded by the **Asian range high** ([asian-range-high](asian-range-high.md)) and **Asian range low** ([asian-range-low](asian-range-low.md)). ICT teaches the Asian range as the **engineered liquidity setup** for London delivery: London's first killzone almost always sweeps one bound (the Judas swing) and then expands toward the opposite or beyond.

## Formal Criteria

- Time window: most commonly the Asian killzone 20:00 → 00:00 NY (some references use the entire Asia session 18:00–03:00).
- Bounded by:
  - Asian range high = max(high) over the window.
  - Asian range low = min(low) over the window.
- Equal highs / equal lows along the bounds are common — they make the bounds explicit liquidity pools.
- Range size: typically 25–60 pips on EURUSD; varies by instrument and volatility regime.

## Formula / Math

```
asian_window = [20:00, 00:00] NY      # canonical KZ-anchored
# or [18:00 prev, 03:00] NY for full session anchor

asian_high = max(high(t)) for t in asian_window
asian_low  = min(low(t))  for t in asian_window
asian_range_size = asian_high - asian_low
asian_eq         = (asian_high + asian_low) / 2
```

## Machine-Readable

```json
{
  "id": "asian-range",
  "category": "14-asian-range",
  "aliases": ["asia-range", "AR", "asian-session-range"],
  "criteria": [
    {"id": "c1", "expr": "bounds_formed_during_asian_window == true"},
    {"id": "c2", "expr": "high == max_high AND low == min_low"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["asian-range-high","asian-range-low","asian-range-sweep","asian-session-bias","asian-range-projections","asia-session","asia-killzone","judas-swing","liquidity-pool","range-contraction"],
  "sources": ["ICT-2016-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   18:00 prev ─── 20:00 ─── 00:00 ─── 03:00 NY
                  |  ↓ Asia KZ  |
   asian_high ────┼─────────────┼──── ← BSL pool
                  │   /\  /\    │
                  │  /  \/  \   │  (overlapping candles)
                  │ /        \  │
   asian_low  ────┴─────────────┴──── ← SSL pool
                                 ↓
                          London open targets one
                          of these bounds (Judas)
```

## Timeframes

M5 / M15 are the practical TFs for marking bounds. H1 captures the entire range in 4 candles and is too coarse to see equal highs/lows.

## Examples

**Example 1 — typical EURUSD Asian range:**
- 20:00–00:00 NY: M5 prints high 1.0876 at 22:30 NY and low 1.0848 at 23:15 NY.
- Range = 28 pips.
- Two equal lows form at 23:00 and 23:50 around 1.0848.
- → London open is highly likely to sweep 1.0848 first (Judas down) before any move up.

## Common Mistakes

- **Using broker time.** All ICT Asian range references are NY-anchored.
- **Ignoring the killzone-vs-session distinction.** The full Asia session (18:00–03:00) range and the Asian KZ range (20:00–00:00) often differ; specify which you're using. Most ICT references use the KZ window.
- **Treating the range as a pivot, not as liquidity.** The Asian range is not a "support/resistance" zone — it is **engineered liquidity** that London is going to take. Bias should be set by HTF, not by the range alone.

## Related Concepts

- [asian-range-high](asian-range-high.md), [asian-range-low](asian-range-low.md) — bounds.
- [asian-range-sweep](asian-range-sweep.md) — what London does to the bounds.
- [asian-session-bias](asian-session-bias.md) — how to read direction from Asia.
- [asian-range-projections](asian-range-projections.md) — extension targets.
- [asia-session](../15-sessions/asia-session.md), [asia-killzone](../10-killzones/asia-killzone.md) — parent session/KZ.
- [judas-swing](../13-judas-swing/judas-swing.md) — what London does to the range.
- [liquidity-pool](../02-liquidity/liquidity-pool.md), [range-contraction](../01-market-structure/range-contraction.md).

## Citations

- `ICT-2016-LIQUIDITY`, `ICT-2022-MENTORSHIP-OVERVIEW`.
