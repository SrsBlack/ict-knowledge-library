# Macro Time 14:50–15:10 NY (NY Mid-Afternoon)

**Category:** 04-time-cycles
**Aliases:** NY 3PM macro, NY mid-afternoon macro, last macro
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-MACROS, ICT-2025-MACRO-PRECISION
**Tags:** time, macro, ny-pm

## Definition

The 14:50–15:10 NY macro is the final programmed-delivery window of the trading day. It brackets the 15:00 NY hour boundary and frequently produces the PM session's continuation thrust or a final reversal before the NY close. This macro sits inside the NY PM Silver Bullet (14:00–15:00) and overlaps with the 15:00 hourly close — the last macro before equities close at 16:00 NY.

## Formal Criteria

- Time window: 14:50 → 15:10 NY.
- Inside NY PM session.
- The end of the NY PM Silver Bullet window.
- Behavior: often resolves the daily range with a final move to HOD/LOD or a reversal that defines the daily candle.

## Formula / Math

```
window = [14:50, 15:10] NY
parent_session = NY PM
parent_setup    = NY PM Silver Bullet [14:00, 15:00] (this macro at the tail)
```

## Machine-Readable

```json
{
  "id": "macro-time-1450-1510",
  "category": "04-time-cycles",
  "aliases": ["ny-3pm-macro", "ny-mid-afternoon-macro", "last-macro"],
  "criteria": [
    {"id": "c1", "expr": "time_in [14:50, 15:10] NY"}
  ],
  "timeframes": ["M1","M5"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["macro-times-overview","ny-pm-session","silver-bullet-ny-pm","macro-time-1350-1410"],
  "sources": ["ICT-2022-MACROS","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
   14:00 ── 14:50 ── 15:00 ── 15:10 ──── 16:00 NY (close)
              |       █        |
              ──── macro ──────
              ──── NY PM Silver Bullet ────
                   14:00 – 15:00
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — final continuation thrust:**
- PM trend has been bullish since the 13:50 macro; 1.0942 hit at 14:30, slight pullback to 1.0935 by 14:50.
- 14:55 NY: M5 prints a green displacement candle.
- 15:00 NY: macro hour-boundary; M5 takes 1.0942 BSL with 12-pip extension to 1.0954.
- 15:10 NY: pulls back to FVG; final HOD set.
- → macro delivers the day's high before 16:00 close.

## Common Mistakes

- **Holding past 16:00.** Many ICT setups exit by 16:00 NY. After the close, Asia begins rebuilding low-volume noise — held positions tend to give back.
- **Forcing trades after a clean PM.** If the 13:50 macro already delivered the PM move, 14:50 often consolidates instead of extending; take only with confluence.

## Related Concepts

- [macro-times-overview](macro-times-overview.md), [ny-pm-session](../15-sessions/ny-pm-session.md), [silver-bullet-ny-pm](../11-silver-bullet/silver-bullet-ny-pm.md), [macro-time-1350-1410](macro-time-1350-1410.md).

## Citations

- `ICT-2022-MACROS`, `ICT-2025-MACRO-PRECISION`.
