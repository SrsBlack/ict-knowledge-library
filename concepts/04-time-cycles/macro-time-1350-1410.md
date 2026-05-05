# Macro Time 13:50–14:10 NY (NY First Afternoon)

**Category:** 04-time-cycles
**Aliases:** NY 2PM macro, NY first afternoon macro, post-lunch macro
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-MACROS, ICT-2025-MACRO-PRECISION
**Tags:** time, macro, ny-pm

## Definition

The 13:50–14:10 NY macro brackets the 14:00 hour boundary at the start of the NY PM session. It is the first programmed-delivery window after [ny-lunch](../15-sessions/ny-lunch.md) ends and frequently produces the PM session's opening direction — either continuation of NY AM or the start of an afternoon reversal. This macro overlaps the start of the NY PM Silver Bullet (14:00–15:00).

## Formal Criteria

- Time window: 13:50 → 14:10 NY.
- Inside the NY PM session.
- Coincides with the start of NY PM Silver Bullet.
- Behavior: often sweeps the lunch range bounds (12:00–13:30) and starts the afternoon move.

## Formula / Math

```
window = [13:50, 14:10] NY
parent_session = NY PM
overlapping_setup = NY PM Silver Bullet [14:00, 15:00]
```

## Machine-Readable

```json
{
  "id": "macro-time-1350-1410",
  "category": "04-time-cycles",
  "aliases": ["ny-2pm-macro", "post-lunch-macro"],
  "criteria": [
    {"id": "c1", "expr": "time_in [13:50, 14:10] NY"}
  ],
  "timeframes": ["M1","M5"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["macro-times-overview","ny-pm-session","ny-lunch","silver-bullet-ny-pm","macro-time-1450-1510"],
  "sources": ["ICT-2022-MACROS","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
   12:00 ── 13:30 ── 13:50 ── 14:00 ── 14:10 ──── 15:00 NY
   ── lunch ────                 █
                    ──── macro ──
                            ──── NY PM Silver Bullet ────
                                  14:00 – 15:00
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — PM reversal:**
- NY AM rallied to HOD 1.0925; lunch consolidated 1.0918–1.0930.
- 13:55 NY: M5 wicks 1.0931 (lunch BSL swept), closes 1.0922.
- 14:05 NY: M5 displaces 18 pips down, leaves bearish FVG.
- → macro-window PM reversal entry; trend bearish for the rest of the session.

## Common Mistakes

- **Trading lunch breakouts at 13:30.** That's still inside lunch low-volume; wait for the macro window 13:50+ for actual delivery.
- **Skipping bias check.** PM macros amplify both directions equally; bias filters which side of the lunch sweep is the entry side.

## Related Concepts

- [macro-times-overview](macro-times-overview.md), [ny-pm-session](../15-sessions/ny-pm-session.md), [ny-lunch](../15-sessions/ny-lunch.md), [silver-bullet-ny-pm](../11-silver-bullet/silver-bullet-ny-pm.md), [macro-time-1450-1510](macro-time-1450-1510.md).

## Citations

- `ICT-2022-MACROS`, `ICT-2025-MACRO-PRECISION`.
