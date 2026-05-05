# NY PM Reversal

**Category:** 31-models
**Aliases:** NY PM fade, afternoon reversal, PM trend-fade
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** model, ny-pm, reversal

## Definition

The NY PM Reversal is a named ICT setup where **the NY AM direction reverses during NY PM (13:30–16:00 NY)**. Common pattern: AM extended to a daily extreme, lunch consolidated near the extreme, then PM session sweeps the lunch range and reverses back through NY AM range. ICT teaches PM Reversals as the typical "afternoon fade" that retraces the morning move; they're reliable but lower-frequency than continuation patterns.

## Formal Criteria

A NY PM Reversal requires:

- NY AM delivered a clear directional move that reached a daily extreme (HOD or LOD).
- Lunch (12:00–13:30 NY) consolidated near the extreme.
- 13:30–14:30 NY: lunch range bound is swept.
- 14:00–16:00 NY: displacement opposite the AM direction; PM SB window often produces the entry.
- NY AM extreme is eventually swept during the reversal.

## Formula / Math

```
ny_pm_reversal:
    ny_am_delivered_directional_move
    AND ny_am_reached_daily_extreme
    AND lunch_consolidation_near_extreme
    AND in [13:30, 16:00] NY
    AND lunch_bound_swept
    AND opposite-direction displacement
    AND eventual sweep of NY AM extreme
```

## Machine-Readable

```json
{
  "id": "ny-pm-reversal",
  "category": "31-models",
  "aliases": ["NY-PM-fade", "afternoon-reversal", "PM-trend-fade"],
  "criteria": [
    {"id": "c1", "expr": "NY AM moved to daily extreme"},
    {"id": "c2", "expr": "PM session reverses, sweeps AM extreme"},
    {"id": "c3", "expr": "PM SB window often the entry"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["ny-pm-session","ny-pm-killzone","silver-bullet-ny-pm","ny-lunch","macro-time-1350-1410","macro-time-1450-1510","liquidity-sweep","ict-2022-model"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   NY PM Reversal (bearish reversal of bullish AM):

   08:00-12:00: NY AM rallies to HOD 1.0925.
   12:00-13:30: lunch consolidates 1.0918-1.0930.
   13:55: M5 wicks 1.0931 (lunch BSL swept).
   14:10: M5 displaces -18 pips, bearish FVG.
   14:25-15:30: continues down to PDL 1.0890.
```

## Timeframes

M5 / M15 / H1.

## Examples

**Example 1 — PM reversal example:**
- HTF: W bullish but D nearly at upper bound (tired).
- 08:00–11:30: NY AM rallies +50 pips to HOD 1.0925 at PDH BSL.
- 12:00–13:30: lunch range 1.0918–1.0930.
- 13:55 NY: M5 wicks 1.0931 (lunch high + PDH BSL swept), closes 1.0922.
- 14:10 NY (PM macro): M5 displaces -18 pips, bearish FVG 1.0908–1.0912.
- 14:25 NY: M5 retests CE 1.0910. Short entry.
- SL 1.0933 (above sweep + buffer); risk 23 pips.
- TP NY AM range bottom 1.0875 → 35 pips → ~1.5R.

## Common Mistakes

- **Forcing PM reversal on every clean AM.** When HTF is strongly trending, NY PM often continues; reversal is more typical when AM was over-extended.
- **Lunch fade.** Don't trade the lunch consolidation itself; wait for the PM macro window 13:50+ for the actual reversal trigger.

## Related Concepts

- [ny-pm-session](../15-sessions/ny-pm-session.md), [ny-pm-killzone](../10-killzones/ny-pm-killzone.md), [silver-bullet-ny-pm](../11-silver-bullet/silver-bullet-ny-pm.md), [ny-lunch](../15-sessions/ny-lunch.md).
- [macro-time-1350-1410](../04-time-cycles/macro-time-1350-1410.md), [macro-time-1450-1510](../04-time-cycles/macro-time-1450-1510.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [ict-2022-model](ict-2022-model.md).

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW`.
