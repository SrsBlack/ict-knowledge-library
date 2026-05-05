# Asia Killzone

**Category:** 10-killzones
**Aliases:** Asian KZ, Asia kill zone, Tokyo KZ
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, asia, accumulation

## Definition

The Asia killzone is the 20:00 → 00:00 NY sub-window of the broader Asia session — the period most associated with the **engineered Asian range** (BSL/SSL pools at the Asian session high and low). Asia killzone behavior is predominantly low-volatility, range-building, and accumulation; the ICT trader uses it less for taking setups and more for **identifying the levels** that London will attack.

## Formal Criteria

- Time window: 20:00 → 00:00 NY (DST canonical anchor; see [dst-handling](../04-time-cycles/dst-handling.md)).
- Sits inside the broader Asia session (~18:00 prev → 03:00 NY).
- Behavioral profile: low ATR, overlapping candles, equal highs / equal lows along the range bounds.
- Output: Asian range high (BSL pool), Asian range low (SSL pool) — these become the next session's primary draw targets.

## Formula / Math

```
asia_kz = [20:00, 24:00] NY    # wraps midnight as the Asia session continues to 03:00

asian_kz_high = max(high) over asia_kz
asian_kz_low  = min(low)  over asia_kz
```

## Machine-Readable

```json
{
  "id": "asia-killzone",
  "category": "10-killzones",
  "aliases": ["asian-kz", "tokyo-kz"],
  "criteria": [
    {"id": "c1", "expr": "time_in [20:00, 24:00] NY"},
    {"id": "c2", "expr": "low_volatility_range_building == true"}
  ],
  "timeframes": ["M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["killzone-overview","asia-session","asian-range","asian-range-high","asian-range-low","accumulation-phase","range-contraction"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   18:00 ── 20:00 ── 24:00 ── 03:00 NY
            |        |
            ── Asia KZ ──
            ▒▒▒▒▒▒▒▒▒
            (range-building, low vol)
                     ↓
                     Asian high / low
                     pools formed
```

## Timeframes

M5 / M15 most useful for marking the killzone bounds and observing range structure.

## Examples

**Example 1 — Asia KZ produces the day's range bounds:**
- 21:00–23:30 NY: EURUSD M5 oscillates between 1.0852 and 1.0876 in 32-pip range with overlapping candles.
- 23:45 NY: equal-low cluster at 1.0852–1.0853 (SSL pool).
- → London open will likely target the 1.0852 SSL OR sweep above 1.0876 BSL as Judas swing.

## Common Mistakes

- **Trading mean-reversion blindly inside Asia KZ.** Setups need explicit confluence; without HTF bias and PD-array support, Asia chop has no edge.
- **Late-Asia breakout entries.** A late-session push in the last hour (02:00–03:00 NY) can be a real continuation move, but is volatile and often the start of London's Judas swing — not a clean continuation entry.

## Related Concepts

- [killzone-overview](killzone-overview.md), [asia-session](../15-sessions/asia-session.md), [asian-range](../14-asian-range/asian-range.md), [asian-range-high](../14-asian-range/asian-range-high.md), [asian-range-low](../14-asian-range/asian-range-low.md), [accumulation-phase](../12-power-of-three/accumulation-phase.md), [range-contraction](../01-market-structure/range-contraction.md).

## Citations

- `ICT-2016-KILLZONES`, `ICT-2022-MENTORSHIP-OVERVIEW`.
