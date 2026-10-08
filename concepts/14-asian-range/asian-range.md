# Asian Range

**Category:** 14-asian-range
**Aliases:** Asia range, AR, Asian session range
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2017
**Source IDs:** ICT-2017-DEFINING-DAILY-RANGE, ICT-2017-INTRADAY-PROFILES, ICT-2017-AVOID-LONDON, ICT-2017-20-PIPS, ICT-2017-INTRADAY-TOP-DOWN, ICT-2016-PROTRACTION, ICT-2016-MARKET-EFFICIENCY-PARADIGM, ICT-2022-MENTORSHIP-EP18
**Tags:** asian-range, liquidity, foundational

## Definition

The Asian range is first named in the **September-2016** mentorship — "Every day starts with consolidation, Asian range" (`ICT-2016-MARKET-EFFICIENCY-PARADIGM`, 13:56) — a year before the clocked window below is taught. The clocked definition is the price range formed during the Asian killzone, **20:00 → 00:00 New York time** — "every day at 8 p.m. … begins the Asian range every day at midnight … ends the Asian range" (`ICT-2017-DEFINING-DAILY-RANGE`, 02:27–02:41). It is bounded by the **Asian range high** ([asian-range-high](asian-range-high.md)) and **Asian range low** ([asian-range-low](asian-range-low.md)). ICT teaches the Asian range as part of the engineered liquidity setup for London delivery: London's first killzone frequently sweeps one bound (the Judas swing) before expanding toward HTF DOL, though ICT's own sweep description is anchored to the opening price and the CBDR deviations rather than strictly to the Asian bound (see Common Mistakes).

## Formal Criteria

- Time window: **20:00 → 00:00 NY** — this is the only clocked Asian window in either corpus; no "full session" alternative (18:00–03:00 or similar) appears anywhere.
- Bounded by:
  - Asian range high = max(high) over the window.
  - Asian range low = min(low) over the window.
- Equal highs / equal lows along the bounds are common — they make the bounds explicit liquidity pools.
- **Range size is a qualification filter, not a typical range.** "Asian range has to be 20 to 30 pips" (`ICT-2017-INTRADAY-PROFILES`, 03:09); "if the Asian range is greater than 40 pips I'm going to consider the delayed protraction profile" (`ICT-2017-AVOID-LONDON`, 09:26); "many times the Asian range is a lot larger than 20 30 40 pips but many times it's at least enough to get 20 pips out of it" (`ICT-2017-20-PIPS`, 06:59).

## Formula / Math

```
asian_window = [20:00, 00:00] NY

asian_high = max(high(t)) for t in asian_window
asian_low  = min(low(t))  for t in asian_window
asian_range_size = asian_high - asian_low
asian_eq         = (asian_high + asian_low) / 2

# ICT gives no "typical pip" figure — 20-30 pips is a qualification filter,
# >40 pips triggers the delayed-protraction profile, not a disqualification outright.
```

## Machine-Readable

```json
{
  "id": "asian-range",
  "category": "14-asian-range",
  "aliases": ["asia-range", "AR", "asian-session-range"],
  "criteria": [
    {"id": "c1", "expr": "bounds_formed_during_asian_window == true"},
    {"id": "c2", "expr": "high == max_high AND low == min_low"},
    {"id": "c3", "expr": "window == [20:00,00:00] America/New_York; no full-session alternative in corpus"},
    {"id": "c4", "expr": "qualification: 20-30 pips ideal; >40 pips => delayed protraction profile"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2017",
  "related": ["asian-range-high","asian-range-low","asian-range-sweep","asian-session-bias","asian-range-projections","asia-session","asia-killzone","judas-swing","liquidity-pool","range-contraction"],
  "sources": ["ICT-2017-DEFINING-DAILY-RANGE","ICT-2017-INTRADAY-PROFILES","ICT-2017-AVOID-LONDON","ICT-2017-20-PIPS","ICT-2017-INTRADAY-TOP-DOWN","ICT-2016-PROTRACTION","ICT-2016-MARKET-EFFICIENCY-PARADIGM","ICT-2022-MENTORSHIP-EP18"]
}
```

## Visual Pattern

```
   20:00 ─── 00:00 NY
          ↓ Asia KZ
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
- Range = 28 pips — inside the 20–30 pip qualification band.
- Two equal lows form at 23:00 and 23:50 around 1.0848.
- → London open is highly likely to sweep 1.0848 first (Judas down) before any move up.

## Common Mistakes

- **Using broker time.** All ICT Asian range references are NY-anchored.
- **Citing an 18:00–03:00 "full session" alternative.** Not in either corpus — searched `(asia|asian).{0,80}(7 p|6 p|5 p|7 o'clock|6 o'clock|3 a.m|3 o'clock)` and the reverse: zero hits for an 18:00 or 03:00 bound. The only clocked window is 20:00–00:00.
- **Treating 25–60 pips as "typical."** ICT's numbers are a filter (20–30 pips ideal, >40 triggers the delayed-protraction profile), not a described typical range.
- **Treating the range as a pivot *before* it is swept.** Going into London, the Asian range is not a "support/resistance" zone — it is **engineered liquidity** that London is going to take. Bias should be set by HTF, not by the range alone.
  ⚠ **Scoped 2026-08-10.** This warning previously denied the pivot reading outright, which contradicted ICT. **After** the sweep, he uses the bound as a pivot by name: "if I'm bullish I expect the **Asian range high to be retested for entry as support**, or adding to open positions for long" (`ICT-2017-INTRADAY-TOP-DOWN` [11:14–11:20]); "sometimes during the New York open the Asian range high, when it's been bullish, will be retreated to and **retested as support**" [11:49]; bearish mirror at [12:08–12:20]. The two readings are sequential, not opposed — liquidity first, pivot after the flip. A reader following the unscoped version would refuse the New-York add ICT explicitly teaches.
- **Overstating London's sweep as "of the Asian bound" specifically.** ICT's own description ties the Judas to the CBDR deviations: "protractionary stage for Judas swing will be one to two standard deviations of the central bank dealer's range" (`ICT-2017-INTRADAY-PROFILES`, 03:29) — not strictly "the Asian range bound."
- **Calling the 2022 model's silence on Asian range a "refinement."** The 2022 mentorship drops it rather than updating it: "I wouldn't worry about doing anything with Asian range" (`ICT-2022-MENTORSHIP-EP18`, 06:22). The 2016 view is similarly muted: "I don't believe Asian is that influential initially" (`ICT-2016-PROTRACTION`, 03:58). This page's `Year Refined` is left at 2017 (not advanced to 2022) because no 2022 source refines the concept — it is deprioritized, not redefined.

## Related Concepts

- [asian-range-high](asian-range-high.md), [asian-range-low](asian-range-low.md) — bounds.
- [asian-range-sweep](asian-range-sweep.md) — what London does to the bounds.
- [asian-session-bias](asian-session-bias.md) — how to read direction from Asia.
- [asian-range-projections](asian-range-projections.md) — extension targets.
- [asia-session](../15-sessions/asia-session.md), [asia-killzone](../10-killzones/asia-killzone.md) — parent session/KZ.
- [judas-swing](../13-judas-swing/judas-swing.md) — what London does to the range.
- [central-bank-dealers-range](../15-sessions/central-bank-dealers-range.md) — the window that precedes and feeds the Judas-swing depth.
- [liquidity-pool](../02-liquidity/liquidity-pool.md), [range-contraction](../01-market-structure/range-contraction.md).

## Citations

- `ICT-2017-DEFINING-DAILY-RANGE` (02:27–02:41) "every day at 8 p.m. … begins the Asian range every day at midnight … ends the Asian range."
- `ICT-2017-INTRADAY-PROFILES` (03:09) "Asian range has to be 20 to 30 pips"; (03:29) "protractionary stage for Judas swing will be one to two standard deviations of the central bank dealer's range."
- `ICT-2017-AVOID-LONDON` (09:26) "if the Asian range is greater than 40 pips I'm going to consider the delayed protraction profile."
- `ICT-2017-20-PIPS` (06:59) "Many times the Asian range is a lot larger than 20 30 40 pips but many times it's at least enough to get 20 pips out of it."
- `ICT-2017-INTRADAY-TOP-DOWN` (11:14) "if I'm bullish I expect the Asian range high to be retested for entry as support"; (11:49) "sometimes during the New York open the Asian range high, when it's been bullish, will be retreated to and retested as support"; bearish mirror (12:08–12:20).
- `ICT-2016-PROTRACTION` (03:58) "I don't believe Asian is that influential initially."
- `ICT-2016-MARKET-EFFICIENCY-PARADIGM` (13:56) "Every day starts with consolidation, Asian range" — the earliest located use of the term, Sep-2016.
- `ICT-2022-MENTORSHIP-EP18` (06:22) "I wouldn't worry about doing anything with Asian range."
