# Session Overlaps

**Category:** 15-sessions
**Aliases:** overlap windows, session intersection, double-session windows
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** sessions, overlap, volume

## Definition

Session overlaps are the time windows when two trading sessions are both active simultaneously, producing the highest combined volume of the 24-hour cycle. The most consequential overlap for ICT analysis is **London Close × NY AM** (10:00–12:00 NY), which combines European book-closing flow with US institutional opening flow. Overlaps are not separate sessions — they are intersections. Understanding the overlap window prevents mis-classifying a setup as belonging to only one of the two sessions.

## Formal Criteria

The two notable overlaps:

| Overlap | Window (NY time) | Component sessions |
|---|---|---|
| Asia × London (early) | 02:00 – 03:00 | end of Asia + London open |
| London Close × NY AM | 10:00 – 12:00 | tail of London + body of NY AM |

Behavioral characteristics:

- **Asia × London overlap (~1 hour):** typically marks the [judas-swing](../13-judas-swing/judas-swing.md). Volume jumps as London desks come online while Asia winds down.
- **London Close × NY AM overlap (~2 hours):** highest volume of the day. Often resolves the daily HOD/LOD; NY AM Silver Bullet (10:00–11:00 NY) sits inside this overlap.

## Formula / Math

```
asia_london_overlap     = [02:00, 03:00] NY
london_close_ny_overlap = [10:00, 12:00] NY
```

## Machine-Readable

```json
{
  "id": "session-overlaps",
  "category": "15-sessions",
  "aliases": ["overlap-windows", "session-intersection"],
  "criteria": [
    {"id": "c1", "expr": "time inside two simultaneous session windows"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["asia-session","london-session","london-close","ny-am-session","silver-bullet-ny-am","judas-swing"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   00 ── 02 ── 03 ── 08 ── 10 ── 12 ── 13:30 ── 16 ── 18 NY

   Asia ─────────                                ─────  (next day Asia)
        London ──────────────────
                              NY AM ───────────
                                  NY Lunch ──
                                              NY PM ─

   ↑           ↑              ↑         ↑
   Asia×LDN    LDN open KZ    LDN-CL ×  Lunch
   overlap     (no overlap)   NY AM     (NY only)
   (1h)                       overlap
                              (2h, biggest)
```

## Timeframes

M5–H1. Daily-and-up TFs already aggregate over the overlap and don't show its character distinctly.

## Examples

**Example 1 — London-close × NY-AM overlap delivery:**
- 10:00 NY: London Close starts, NY AM continues.
- The next 60 minutes (10:00–11:00) is also the NY AM Silver Bullet window.
- M5 sweeps PDH BSL at 10:15, leaves FVG, retraces to FVG by 10:35, displaces upward into 11:00.
- → overlap-window setup, three concepts (London close, NY AM, NY AM Silver Bullet) firing simultaneously.

## Common Mistakes

- **Single-label thinking.** Calling 10:30 NY "NY AM only" or "London Close only" misses that both contexts apply.
- **Counting both volumes.** Total volume at the overlap is *combined*, not double — don't double-count institutional participation.
- **Asia × London over-reading.** The 02:00–03:00 overlap is short and noisy. Don't try to micro-analyze a 1-hour window with multiple session influences; treat it as a transitional period.

## Related Concepts

- [asia-session](asia-session.md), [london-session](london-session.md), [london-close](london-close.md), [ny-am-session](ny-am-session.md) — the overlapping sessions themselves.
- [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md) — sits inside the LDN-Close × NY-AM overlap.
- [judas-swing](../13-judas-swing/judas-swing.md) — typical Asia × London overlap pattern.

## Citations

- `ICT-2016-KILLZONES` — overlap volume noted in original kill-zone lectures.
- `ICT-2022-MENTORSHIP-OVERVIEW` — overlap framed for setup selection.
