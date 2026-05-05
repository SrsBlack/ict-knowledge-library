# Macro Time 09:50–10:10 NY (NY Pre-Open)

**Category:** 04-time-cycles
**Aliases:** NY 10AM macro, NY pre-open macro, NY AM macro
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-MACROS, ICT-2025-MACRO-PRECISION
**Tags:** time, macro, ny-am

## Definition

The 09:50–10:10 NY macro is the pre-10AM programmed-delivery window inside the NY AM session. It overlaps the start of the NY AM Silver Bullet (10:00–11:00) and the London Close × NY AM session overlap (10:00–12:00). For ICT-style intraday traders this macro is one of the highest-density setup windows of the day: the algorithm injects volatility 10 minutes before and after the 10:00 NY hour boundary, often producing the day's HOD or LOD.

## Formal Criteria

- Time window: 09:50 → 10:10 NY.
- Inside NY AM session and NY AM killzone.
- Coincides with the start of NY AM Silver Bullet (10:00–11:00).
- Behavior: high-probability for displacement, sweeps of pre-10AM range bounds, and reversals.

## Formula / Math

```
window = [09:50, 10:10] NY
parent_session = NY AM
parent_killzone = NY AM killzone [08:00, 11:00]
overlapping_setup = NY AM Silver Bullet [10:00, 11:00]
```

## Machine-Readable

```json
{
  "id": "macro-time-0950-1010",
  "category": "04-time-cycles",
  "aliases": ["ny-10am-macro", "ny-pre-open-macro"],
  "criteria": [
    {"id": "c1", "expr": "time_in [09:50, 10:10] NY"}
  ],
  "timeframes": ["M1","M5"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["macro-times-overview","ny-am-session","ny-am-killzone","silver-bullet-ny-am","london-close"],
  "sources": ["ICT-2022-MACROS","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
   08:00 ──── 09:50 ── 10:00 ── 10:10 ── 11:00 NY
              |         █         |
              ──── macro ────────
                          ──── NY AM Silver Bullet ────
                                10:00 – 11:00
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — bullish macro extension:**
- HTF bias bullish; PDH 1.0925 untaken; current 1.0915 at 09:45.
- 09:55: M5 wicks down to 1.0911, closes 1.0918.
- 10:00: M5 prints a 16-pip green displacement, takes 1.0925 BSL.
- 10:05: leaves a bullish FVG at 1.0922; pulls back; continues to 1.0942.
- → macro-window delivery; same setup is also a textbook Silver Bullet entry.

## Common Mistakes

- **Confusing macro with Silver Bullet.** They overlap from 10:00–10:10 but the macro is 09:50–10:10 (earlier start). The 09:50–10:00 window is macro-only.
- **Overtrading the macro.** Wait for confluence (HTF bias + PD array + macro start). Random macro-window trades have no edge.

## Related Concepts

- [macro-times-overview](macro-times-overview.md), [ny-am-session](../15-sessions/ny-am-session.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [london-close](../15-sessions/london-close.md).

## Citations

- `ICT-2022-MACROS`, `ICT-2025-MACRO-PRECISION`.
