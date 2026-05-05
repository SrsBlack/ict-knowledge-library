# NY PM Session

**Category:** 15-sessions
**Aliases:** New York afternoon, NY PM hours, afternoon session
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2022-MACROS
**Tags:** sessions, ny-pm, reversal, foundational

## Definition

NY PM runs from 13:30 → 16:00/17:00 NY. It is ICT's **secondary delivery** window — after London and NY AM have done the heavy lifting, NY PM either continues the day's trend toward final HOD/LOD or reverses against the AM move. PM reversals are common and are one of ICT's named setups (see [ny-pm-reversal](../31-models/ny-pm-reversal.md)). The PM Silver Bullet (14:00–15:00 NY) is the lower-probability third silver-bullet window.

## Formal Criteria

- Time window: 13:30 → 16:00 NY (some traders extend to 17:00).
- Sub-windows:
  - **PM Silver Bullet** (14:00–15:00 NY): see [silver-bullet-ny-pm](../11-silver-bullet/silver-bullet-ny-pm.md).
  - **Macro times** at 13:50–14:10 and 14:50–15:10.
- Behavior: continuation OR reversal of the AM move; reversal is more common when AM was over-extended.

## Formula / Math

```
ny_pm_window         = [13:30, 16:00] NY      # 17:00 alternate close
ny_pm_silver_bullet  = [14:00, 15:00] NY
macro_times_in_pm    = [[13:50, 14:10], [14:50, 15:10]]
```

## Machine-Readable

```json
{
  "id": "ny-pm-session",
  "category": "15-sessions",
  "aliases": ["ny-afternoon", "ny-pm-hours"],
  "criteria": [
    {"id": "c1", "expr": "time_in [13:30, 16:00] NY"},
    {"id": "c2", "expr": "post_lunch_delivery_window == true"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["ny-am-session","ny-lunch","silver-bullet-ny-pm","macro-times-overview","ny-pm-reversal","distribution-phase"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2022-MACROS"]
}
```

## Visual Pattern

```
   13:30 ──── 14:00 ──── 15:00 ──── 16:00 NY
   ─────────────────────────────────────────
   |  open  | macro      | macro    | close |
   |        | 13:50-14:10| 14:50-   |       |
   |        | + Silver   | 15:10    |       |
   |        | Bullet     |          |       |
   ─────────────────────────────────────────
```

## Timeframes

M5 / M15 for entries; H1 for context (does the H1 candle finalize HOD/LOD here?).

## Examples

**Example 1 — PM reversal (textbook):**
- NY AM rallied to a HOD of 1.0925 by 11:30.
- Lunch consolidated 1.0918–1.0930.
- 14:00 PM: M5 sweeps 1.0930 lunch BSL on a wick, closes 1.0922.
- 14:30: M5 displaces down 30 pips, leaves bearish FVG.
- → PM reversal of AM move; bearish bias for the rest of the session, often closing near LOD.

## Common Mistakes

- **Forcing trades after a clean AM.** When AM has already delivered the daily range, PM often consolidates or reverses; aggressive PM continuation entries get chopped.
- **Ignoring 16:00 close behavior.** Many ICT setups end well before 16:00; positions held through close into Asia rebuild risk for less reward.
- **Over-relying on PM Silver Bullet.** It's the **lowest** probability of the three SB windows; ICT acknowledges this and recommends only taking it when AM and London context support continuation/reversal cleanly.

## Related Concepts

- [ny-am-session](ny-am-session.md) — what PM continues or reverses.
- [ny-lunch](ny-lunch.md) — what precedes PM.
- [silver-bullet-ny-pm](../11-silver-bullet/silver-bullet-ny-pm.md) — the PM SB window.
- [macro-times-overview](../04-time-cycles/macro-times-overview.md) — PM macro windows.
- [ny-pm-reversal](../31-models/ny-pm-reversal.md) — named reversal model.
- [distribution-phase](../12-power-of-three/distribution-phase.md) — AMD-cycle phase.

## Citations

- `ICT-2016-KILLZONES` — NY PM kill zone foundational.
- `ICT-2022-MENTORSHIP-OVERVIEW` — PM reversal vs continuation framing.
- `ICT-2022-MACROS` — PM macro times.
