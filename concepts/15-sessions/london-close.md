# London Close

**Category:** 15-sessions
**Aliases:** London close window, European close, LDN close
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** sessions, london-close, overlap, reversal

## Definition

London Close is the 10:00 → 12:00 NY window during which the European institutional book unwinds for the day. It overlaps the NY AM session and is one of the **highest-volume windows of the trading day** because both London and NY traders are active simultaneously. ICT teaches London Close as a window where European positions are squared — frequently producing reversals against the London-open direction (see [london-close-reversal](../31-models/london-close-reversal.md)).

## Formal Criteria

- Time window: 10:00 → 12:00 NY (DST) / 11:00 → 13:00 NY (non-DST).
- Overlaps NY AM (08:00 → 12:00) — high volume.
- Behavior: often a reversal of London-open's direction as European books unwind, OR an acceleration when NY agrees with London's direction.
- Window closes into NY Lunch — final London prints often coincide with NY AM-window peaks.

## Formula / Math

```
london_close_window = [10:00, 12:00] NY (DST)

overlaps with ny_am_window = [08:00, 12:00] NY     # 10:00–12:00 overlap
```

## Machine-Readable

```json
{
  "id": "london-close",
  "category": "15-sessions",
  "aliases": ["london-close-window", "european-close", "ldn-close"],
  "criteria": [
    {"id": "c1", "expr": "time_in [10:00, 12:00] NY"},
    {"id": "c2", "expr": "overlaps_ny_am == true"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["london-session","ny-am-session","session-overlaps","london-close-reversal","silver-bullet-ny-am"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   08:00 ── 10:00 ──────── 12:00 NY
                |          |
   NY AM ───────── ████████ ────  high-volume overlap
   London ────── ██████████ ───   (London close)
                |          |
                ↑          ↑
        London close      Lunch begins
        starts            (London closed,
                           NY continues)
```

## Timeframes

M5 / M15 / H1. The 10:00–11:00 NY window is also the **NY AM Silver Bullet** — these two ICT concepts overlap and reinforce each other.

## Examples

**Example 1 — London-close reversal:**
- London-open delivered a 60-pip rally on EURUSD; HOD 1.0925 set at 09:30 NY.
- 10:00–11:00 NY: M5 sweeps 1.0925 BSL, closes 1.0918.
- 11:30: M5 displaces 30 pips down, leaves bearish FVG.
- → London-close reversal; rest of NY AM trends back into Asian range.

## Common Mistakes

- **Confusing London close with London session close.** "London Close" in ICT means the 10:00–12:00 NY window where the close-out happens — not the moment London exchange physically closes.
- **Trading the overlap as one window.** London close (10–12) and NY AM Silver Bullet (10–11) overlap; the SB rules apply specifically to that hour, not to the full close window.
- **Ignoring DST.** London-close clock-time vs NY shifts twice a year; always anchor to NY clock.

## Related Concepts

- [london-session](london-session.md) — the broader window London close is the tail of.
- [ny-am-session](ny-am-session.md) — overlapping session.
- [session-overlaps](session-overlaps.md) — disambiguation of overlap windows.
- [london-close-reversal](../31-models/london-close-reversal.md) — named setup model.
- [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md) — overlapping SB window.

## Citations

- `ICT-2016-KILLZONES` — London close window referenced in foundational killzone teaching.
- `ICT-2022-MENTORSHIP-OVERVIEW` — London-close-reversal logic and overlap framing.
