# NY AM Session

**Category:** 15-sessions
**Aliases:** New York morning session, NY morning, NY open, NY AM hours
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2022-MACROS
**Tags:** sessions, ny-am, distribution, foundational

## Definition

The NY AM session covers 08:00 → 12:00 NY and overlaps the London close window from 10:00 onward. It is the **highest-volume part of the trading day** and the period where US institutional flow combines with the unwinding European book. ICT treats NY AM as the **distribution / second-delivery phase** of the daily AMD: London established direction, NY AM delivers the bulk of the daily range, often setting the day's high or low and establishing the daily candle's body.

## Formal Criteria

- Time window: 08:00 → 12:00 NY.
- Major US news embedded: 08:30 (CPI, NFP, retail sales), 10:00 (some Fed/ISM releases).
- Two key sub-windows:
  - **NY Open killzone** (~08:00–11:00 NY): primary setup-rich window.
  - **NY AM Silver Bullet** (10:00–11:00 NY): ICT's highest-probability silver-bullet window (see [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md)).
- Macro time windows fall inside NY AM (09:50–10:10) — see [macro-times-overview](../04-time-cycles/macro-times-overview.md).

## Formula / Math

```
ny_am_window       = [08:00, 12:00] NY
ny_open_kz         = [08:00, 11:00] NY
ny_am_silver_bullet = [10:00, 11:00] NY
```

## Machine-Readable

```json
{
  "id": "ny-am-session",
  "category": "15-sessions",
  "aliases": ["ny-morning", "ny-am-hours"],
  "criteria": [
    {"id": "c1", "expr": "time_in [08:00, 12:00] NY"},
    {"id": "c2", "expr": "overlaps_london_close_after_10:00 == true"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["ny-am-killzone","ny-lunch","ny-pm-session","london-close","silver-bullet-ny-am","macro-times-overview","distribution-phase"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2022-MACROS"]
}
```

## Visual Pattern

```
   08:00     09:30      10:00       11:00       12:00 NY
   ────────────────────────────────────────────────────
   |  open  | NY Open  | macro       | continuation/  |
   |        |  KZ      | 09:50-10:10 | reversal       |
   |        |          | + Silver    |                |
   |        |          | Bullet 10-11|                |
   ────────────────────────────────────────────────────
   ↑                                          ↑
   London Close overlaps from 10:00          → Lunch begins 12:00
```

## Timeframes

M1–H1 most actionable. The 08:30 news candle and the 09:50–10:10 macro window often print displacement that defines the daily range; H1 / H4 candles around NY AM often set HOD/LOD.

## Examples

**Example 1 — bullish NY AM continuation:**
- London-open Judas swept Asian SSL, displaced 50 pips up.
- NY opens at 08:00 with a bullish gap-up; 08:30 news (positive surprise) prints a wide green M5 candle that takes PDH BSL.
- 10:00–11:00 NY AM Silver Bullet retraces to the 08:30 candle's FVG and pushes higher.
- → NY AM extends London's direction; daily candle prints a wide bullish body.

## Common Mistakes

- **Trading 08:00–08:30 blindly.** The pre-news window is volatile and frequently produces fake breakouts before 08:30.
- **Ignoring news.** NY AM has more economic-release windows than any other session. Always check the calendar.
- **Skipping macro times.** ICT treats 09:50–10:10 as a programmed delivery moment; trades placed against macro times often get stopped before the move.

## Related Concepts

- [ny-am-killzone](../10-killzones/ny-am-killzone.md) — the high-priority sub-window.
- [ny-lunch](ny-lunch.md) — what follows.
- [ny-pm-session](ny-pm-session.md) — afternoon session.
- [london-close](london-close.md) — overlapping window from 10:00.
- [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md) — ICT's premier setup window.
- [macro-times-overview](../04-time-cycles/macro-times-overview.md) — programmed delivery windows.
- [distribution-phase](../12-power-of-three/distribution-phase.md) — AMD-cycle equivalent.

## Citations

- `ICT-2016-KILLZONES` — NY AM kill zone defined.
- `ICT-2022-MENTORSHIP-OVERVIEW` — NY AM as distribution phase.
- `ICT-2022-MACROS` — macro-time windows inside NY AM.
