# NY AM Killzone

**Category:** 10-killzones
**Aliases:** New York AM KZ, NY morning KZ
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2017-DEFINING-DAILY-RANGE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, ny-am, distribution

## Definition

The NY AM killzone is the 08:00 → 11:00 NY sub-window of the NY AM session — the **highest-volume killzone of the trading day** because of the overlap with London Close (10:00–12:00 NY). NY AM-KZ contains the 09:50–10:10 macro time and the entirety of the NY AM Silver Bullet (10:00–11:00 NY). It is typically where the daily HOD or LOD is established and where the bulk of the daily candle's body is delivered.

⚠ **The April-2017 mentorship gives a different window: 07:00 → 10:00.** "Every day at **7
a.m.** Eastern Standard Time New York begins the New York killzone; every day at **10 a.m.** …
ends the New York killzone" (`ICT-2017-DEFINING-DAILY-RANGE`, 03:57–04:17), taught as "the
**definitive teaching** … if you've seen anything different in the past, **this is the real
one**" (02:13–02:27). That formulation shifts the whole window an hour earlier, so it **ends
where the public window's Silver Bullet begins** and excludes 10:00–11:00 entirely, handing
that hour to the London close killzone. The 08:00–11:00 set below is the public 2016/2022
formulation and is what the rest of this page is built on. Full 2017 set:
[ipda-true-day](../04-time-cycles/ipda-true-day.md).

## Formal Criteria

- Time window: 08:00 → 11:00 NY (public 2016/2022 anchor); **07:00 → 10:00 NY** in the
  April-2017 mentorship.
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
    {"id": "c1", "expr": "time_in [08:00, 11:00] NY (public 2016/2022)"},
    {"id": "c2", "expr": "highest_volume_killzone == true"},
    {"id": "c3", "expr": "time_in [07:00, 10:00] NY (April-2017 mentorship)"},
    {"id": "c4", "expr": "cme_open == 08:20 NY, inside both formulations"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["killzone-overview","ny-am-session","london-close","silver-bullet-ny-am","macro-time-0950-1010","distribution-phase","ipda-true-day","ny-judas-swing"],
  "sources": ["ICT-2016-KILLZONES","ICT-2017-DEFINING-DAILY-RANGE","ICT-2022-MENTORSHIP-OVERVIEW"]
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
- **Mixing the two windows.** Working 2017 mentorship material against an 08:00–11:00 window
  puts the last hour of the session outside ICT's own New York killzone and inside London
  close. Pick a formulation and state it.
- **Ignoring 08:20.** The **CME open** sits inside both windows and is where ICT locates the
  New York protraction — in this lesson's own example "the low that forms in the actual New
  York killzone … **forms at 8:20, CME open**" (`ICT-2017-DEFINING-DAILY-RANGE`, 08:44).

## Related Concepts

- [ipda-true-day](../04-time-cycles/ipda-true-day.md) — the April-2017 time set, where this window is 07:00–10:00.
- [ny-judas-swing](../13-judas-swing/ny-judas-swing.md) — the 08:20 CME-open protraction inside it.
- [killzone-overview](killzone-overview.md), [ny-am-session](../15-sessions/ny-am-session.md), [london-close](../15-sessions/london-close.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [macro-time-0950-1010](../04-time-cycles/macro-time-0950-1010.md), [distribution-phase](../12-power-of-three/distribution-phase.md).

## Citations

- `ICT-2016-KILLZONES`, `ICT-2022-MENTORSHIP-OVERVIEW` — the 08:00–11:00 public formulation.
- `ICT-2017-DEFINING-DAILY-RANGE` (00:14) "**lesson two of the April 2017 ICT mentorship**"; (02:13–02:27) "this is the **definitive teaching** … if you've seen anything different in the past, **this is the real one**"; (03:57–04:17) "the ICT New York killzone — every day at **7 a.m.** Eastern Standard Time New York begins the New York killzone; every day at **10 a.m.** … ends the New York killzone"; (07:17) "I want to add the **8:20 a.m.** New York time — this is the **CME open**"; (08:44) "look at the low that forms in the actual New York killzone — **it forms at 8:20, CME open**".
