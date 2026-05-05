# NY AM Killzone

**Category:** 10-killzones
**Aliases:** New York AM KZ, NY morning KZ
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, ny-am, distribution

## Definition

The NY AM killzone is the 08:00 → 11:00 NY sub-window of the NY AM session — the **highest-volume killzone of the trading day** because of the overlap with London Close (10:00–12:00 NY). NY AM-KZ contains the 09:50–10:10 macro time and the entirety of the NY AM Silver Bullet (10:00–11:00 NY). It is typically where the daily HOD or LOD is established and where the bulk of the daily candle's body is delivered.

## Formal Criteria

- Time window: 08:00 → 11:00 NY (canonical anchor).
- Sits inside NY AM session (08:00–12:00).
- Major US news embedded: 08:30 economic releases (CPI, NFP, retail sales).
- Contains macro time 09:50–10:10 NY.
- Contains NY AM Silver Bullet 10:00–11:00 NY.
- Overlaps London Close 10:00–11:00 NY (highest combined volume).

## Formula / Math

```
ny_am_kz       = [08:00, 11:00] NY
contains_macro = [09:50, 10:10] NY
contains_sb    = [10:00, 11:00] NY
overlaps_london_close = [10:00, 11:00] NY
```

## Machine-Readable

```json
{
  "id": "ny-am-killzone",
  "category": "10-killzones",
  "aliases": ["ny-am-kz", "ny-morning-kz"],
  "criteria": [
    {"id": "c1", "expr": "time_in [08:00, 11:00] NY"},
    {"id": "c2", "expr": "highest_volume_killzone == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["killzone-overview","ny-am-session","london-close","silver-bullet-ny-am","macro-time-0950-1010","distribution-phase"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   06:00 ─── 08:00 ─── 09:30 ─── 10:00 ─── 11:00 NY
              |          ↑         █         |
              ──── NY AM KZ ─────────────────
                              ────macro────
                                09:50–10:10
                                   ↓
                              ──── NY AM Silver Bullet ────
                              10:00 – 11:00
```

## Timeframes

M1 / M5 / M15. The 08:30 news candle and the 10:00 macro/SB candles often print displacement that defines the daily range.

## Examples

**Example 1 — bullish NY AM KZ delivery:**
- HTF bias bullish; PDH BSL at 1.0925; current 1.0900.
- 08:30 NY: positive news; M5 prints 25-pip green displacement, closes 1.0922.
- 09:50–10:10 macro: pulls back to 08:30 candle's FVG, then takes 1.0925.
- 10:30 NY: extends to 1.0942 (NY AM Silver Bullet continuation).
- → NY AM KZ delivers ~40 pips, sets daily HOD.

## Common Mistakes

- **Pre-08:30 over-trading.** The pre-news window (08:00–08:30) is volatile and often produces fake breakouts that resolve only after the 08:30 release.
- **Ignoring news calendar.** NY AM has more high-impact releases than any other killzone; skipping the calendar = trading blind.
- **Treating 11:00 as a hard end.** Some NY AM setups finalize 11:00–11:30 (post-SB extension); the killzone window is a guideline, not a halt.

## Related Concepts

- [killzone-overview](killzone-overview.md), [ny-am-session](../15-sessions/ny-am-session.md), [london-close](../15-sessions/london-close.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [macro-time-0950-1010](../04-time-cycles/macro-time-0950-1010.md), [distribution-phase](../12-power-of-three/distribution-phase.md).

## Citations

- `ICT-2016-KILLZONES`, `ICT-2022-MENTORSHIP-OVERVIEW`.
