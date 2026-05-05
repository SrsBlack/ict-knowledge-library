# NY PM Killzone

**Category:** 10-killzones
**Aliases:** NY PM KZ, afternoon killzone
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, ny-pm, afternoon, reversal

## Definition

The NY PM killzone is the 13:30 → 16:00 NY sub-window — effectively the entire NY PM session is one killzone. It contains two macro-time windows (13:50–14:10 and 14:50–15:10) and the NY PM Silver Bullet (14:00–15:00). Behaviorally it is the **secondary delivery window**: continuation of the AM trend OR a reversal that retraces the AM move. The lowest-probability of the three SB windows lives here.

## Formal Criteria

- Time window: 13:30 → 16:00 NY.
- Coincides with NY PM session.
- Contains:
  - Macro 13:50–14:10 NY.
  - NY PM Silver Bullet 14:00–15:00 NY.
  - Macro 14:50–15:10 NY.
- Behavioral profile: continuation OR reversal of AM trend; reversals more common when AM was over-extended.

## Formula / Math

```
ny_pm_kz = [13:30, 16:00] NY
contains_macros = [(13:50, 14:10), (14:50, 15:10)]
contains_sb     = [14:00, 15:00]
```

## Machine-Readable

```json
{
  "id": "ny-pm-killzone",
  "category": "10-killzones",
  "aliases": ["ny-pm-kz", "afternoon-killzone"],
  "criteria": [
    {"id": "c1", "expr": "time_in [13:30, 16:00] NY"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["killzone-overview","ny-pm-session","silver-bullet-ny-pm","macro-time-1350-1410","macro-time-1450-1510","ny-pm-reversal"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   12:00 ── 13:30 ── 14:00 ── 15:00 ── 16:00 NY
   ── lunch ──         |        |        |
                       ──── NY PM KZ ────
                       █                 █
                  macro 13:50         macro 14:50
                       –14:10              –15:10
                       ──── NY PM SB ────
                       14:00 – 15:00
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — PM reversal:**
- AM rallied to HOD 1.0925; lunch consolidated 1.0918–1.0930.
- 13:55 NY (PM macro): M5 sweeps 1.0930 lunch BSL, closes 1.0922.
- 14:10: M5 displaces 18 pips down; bearish FVG.
- 14:30–15:30: trend bearish; takes 1.0900 SSL by 15:30.
- → PM KZ delivers a textbook reversal of AM.

## Common Mistakes

- **Forcing trades when AM has fully delivered.** When AM already produced a wide daily range, PM often consolidates rather than extending; aggressive PM continuation entries chop.
- **Trading 16:00–17:00 close-out.** Brokers may continue trading but volume thins; ICT's KZ ends at 16:00. After-hours moves rarely match KZ probability.

## Related Concepts

- [killzone-overview](killzone-overview.md), [ny-pm-session](../15-sessions/ny-pm-session.md), [silver-bullet-ny-pm](../11-silver-bullet/silver-bullet-ny-pm.md), [macro-time-1350-1410](../04-time-cycles/macro-time-1350-1410.md), [macro-time-1450-1510](../04-time-cycles/macro-time-1450-1510.md), [ny-pm-reversal](../31-models/ny-pm-reversal.md).

## Citations

- `ICT-2016-KILLZONES`, `ICT-2022-MENTORSHIP-OVERVIEW`.
