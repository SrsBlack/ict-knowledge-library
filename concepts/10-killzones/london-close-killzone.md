# London Close Killzone

**Category:** 10-killzones
**Aliases:** London Close KZ, LC killzone
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, london, close, overlap

## Definition

The London Close killzone is the 10:00 → 12:00 NY sub-window where the European institutional book unwinds for the day. It is identical in time to the [london-close](../15-sessions/london-close.md) session window — for ICT operators the entire close window IS the killzone (no narrower sub-window). Critically, it overlaps the NY AM killzone from 10:00–11:00 NY, producing the day's combined-volume peak. Frequently delivers a reversal of the London-open direction or accelerates it when NY agrees.

## Formal Criteria

- Time window: 10:00 → 12:00 NY.
- Overlaps NY AM killzone 10:00 → 11:00 NY.
- Coincides with NY AM Silver Bullet 10:00 → 11:00 NY.
- Behavioral profile: high volume; reversal of London-open direction common; OR continuation acceleration when NY agrees.

## Formula / Math

```
london_close_kz = [10:00, 12:00] NY
overlap_with_ny_am_kz = [10:00, 11:00] NY
```

## Machine-Readable

```json
{
  "id": "london-close-killzone",
  "category": "10-killzones",
  "aliases": ["london-close-kz", "lc-killzone"],
  "criteria": [
    {"id": "c1", "expr": "time_in [10:00, 12:00] NY"},
    {"id": "c2", "expr": "overlaps_ny_am_kz == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["killzone-overview","london-close","ny-am-killzone","silver-bullet-ny-am","session-overlaps","london-close-reversal"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   08:00 ─── 10:00 ─── 11:00 ─── 12:00 NY
              |          |          |
              ── London Close KZ ───
                      ▒▒▒▒▒
              ── NY AM KZ ──
              08:00 – 11:00
                         ↓
                 overlap (10–11)
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — London-open reversal at LC-KZ:**
- 03:00–05:00 LO-KZ: London delivered a 60-pip rally; HOD 1.0925.
- 10:30 NY (LC-KZ): M5 sweeps 1.0925, closes 1.0918.
- 11:00 NY: M5 displaces 25 pips down, leaves bearish FVG.
- → London-close-driven reversal of the morning move.

## Common Mistakes

- **Treating LC-KZ as separate from NY AM-KZ.** The 10:00–11:00 hour is in both; setups during that hour often satisfy both frameworks simultaneously.
- **Holding past 12:00.** After 12:00 NY, lunch begins; positions held into lunch typically chop.

## Related Concepts

- [killzone-overview](killzone-overview.md), [london-close](../15-sessions/london-close.md), [ny-am-killzone](ny-am-killzone.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [session-overlaps](../15-sessions/session-overlaps.md), [london-close-reversal](../31-models/london-close-reversal.md).

## Citations

- `ICT-2016-KILLZONES`, `ICT-2022-MENTORSHIP-OVERVIEW`.
