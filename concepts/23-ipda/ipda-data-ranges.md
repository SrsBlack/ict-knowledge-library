# IPDA Data Ranges

**Category:** 23-ipda
**Aliases:** IPDA lookback ranges, IPDA reference windows, 20/40/60-day windows
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-IPDA-DATA-RANGES, ICT-2017-QUARTERLY-SHIFTS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ipda, lookback, ranges, foundational

## Definition

IPDA data ranges are the **canonical lookback windows** ICT teaches as the algorithm's reference horizon: **20, 40, and 60 trading days**. The algorithm references the highest high and lowest low printed across each window to identify untaken liquidity pools and unmitigated PD arrays. The three windows cover different time horizons:

- **20-day**: ~1 month — short-horizon, intraday-relevant.
- **40-day**: ~2 months — swing-trade horizon.
- **60-day**: ~3 months — quarterly horizon (often coincides with the IPDA quarterly rotation).

⚠ **The windows are not measured from today.** In the originating January 2017 lessons they hang off an anchored vertical line — the first trading day of the previous closed calendar month, re-anchored onto the quarterly market structure shift — and they run **both left and right** of it. The right-hand half ("cast forward") dates the next setup rather than locating liquidity. The full procedure is [ipda-data-range-calibration](ipda-data-range-calibration.md). A trailing-from-today measurement is a common simplification, not ICT's stated method.

## Formal Criteria

For each window, the analyst tracks:

- The highest high over the trailing N trading days.
- The lowest low over the trailing N trading days.
- The freshness (whether the high/low has been swept since formation).
- Whether the level coincides with other reference points (PWH/PWL/PMH/PML, swing highs).

## Formula / Math

```
N_options = [20, 40, 60]   # trading days, not calendar days

for N in N_options:
    ipda_N_high = max(high) over last N trading days
    ipda_N_low  = min(low)  over last N trading days
```

`max` and `min` use wick highs/lows, not closes.

## Machine-Readable

```json
{
  "id": "ipda-data-ranges",
  "category": "23-ipda",
  "aliases": ["IPDA-lookback-ranges", "IPDA-reference-windows"],
  "criteria": [
    {"id": "c1", "expr": "lookbacks = [20, 40, 60] trading days"},
    {"id": "c2", "expr": "tracks_highest_high_and_lowest_low_in_each_window"}
  ],
  "timeframes": ["D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ipda-definition","ipda-20-day-lookback","ipda-40-day-lookback","ipda-60-day-lookback","ipda-reference-points","ipda-data-range-calibration","external-range-liquidity","draw-on-liquidity"],
  "sources": ["ICT-2017-IPDA-DATA-RANGES","ICT-2017-QUARTERLY-SHIFTS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   present day → ───────── current price

     ← 20 days →
   ─── 20-day high (ipda_20_high)  if not swept = active BSL DOL
   ─── 20-day low  (ipda_20_low)   if not swept = active SSL DOL

     ←── 40 days ──→
   ─── 40-day high   (longer horizon BSL)
   ─── 40-day low    (longer horizon SSL)

     ←──── 60 days ────→
   ─── 60-day high   (quarterly horizon ERL)
   ─── 60-day low    (quarterly horizon ERL)
```

## Timeframes

Daily for measurement (each "day" is a trading-day candle); reference at any TF.

## Examples

**Example 1 — IPDA-data-ranges identifying DOL stack:**
- Current price 1.0855 on EURUSD.
- 20-day high = 1.0925 (formed 12 days ago, untaken).
- 40-day high = 1.0950 (formed 32 days ago, untaken).
- 60-day high = 1.0980 (formed 48 days ago, untaken).
- DOL ladder for bullish bias: 1.0925 → 1.0950 → 1.0980. Each is a higher-horizon BSL.

## Common Mistakes

- **Calendar days vs trading days.** ICT teaches trading days (excludes weekends). Calendar-day lookbacks shift the windows by ~30%.
- **Missing the freshness check.** Once a window's high/low is swept, that level stops being an active DOL until a new one forms in the same window.
- **Treating windows as isolated.** The three windows often align (the same level is 20-day high AND 40-day high), making it a higher-conviction DOL.

## Related Concepts

- [ipda-definition](ipda-definition.md), [ipda-20-day-lookback](ipda-20-day-lookback.md), [ipda-40-day-lookback](ipda-40-day-lookback.md), [ipda-60-day-lookback](ipda-60-day-lookback.md), [ipda-reference-points](ipda-reference-points.md).
- [ipda-data-range-calibration](ipda-data-range-calibration.md) — where the windows are anchored and how the forward half is used.
- [external-range-liquidity](../02-liquidity/external-range-liquidity.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md).

## Citations

- `ICT-2017-IPDA-DATA-RANGES` (81:03) — "It's January 12, 2017"; (27:52–28:27) "if you look back 60 days in the past, what was the highest high in the last 60 days? There's going to be buy stops above that high… Inside of the range of 20 days, 40 days, and 60 days."
- `ICT-2017-QUARTERLY-SHIFTS` (00:21) — "the January 2017 ICT Mentorship Long Term Analysis Lesson 1.1"; (22:22–23:41) "60 trading days, 40 trading days, and 20 trading days… and they're all trading days, not calendar days."
- `ICT-2022-MENTORSHIP-OVERVIEW` — the windows re-taught in the 2022 season.
