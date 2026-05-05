# Silver Bullet — NY PM

**Category:** 11-silver-bullet
**Aliases:** NY PM SB, 2pm SB, afternoon SB
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-SILVER-BULLET, ICT-2025-MACRO-PRECISION
**Tags:** silver-bullet, ny-pm, lowest-probability

## Definition

The NY PM Silver Bullet is the **14:00–15:00 NY** SB window — the **lowest-probability** of the three SB windows. ICT teaches it explicitly with the caveat that it should only be taken when the prior AM session did not cleanly deliver the daily move and the trend remains intact. PM SB sits inside NY PM killzone, between the 13:50–14:10 and 14:50–15:10 macro windows. Often produces continuation moves to final HOD/LOD or reversals against the morning trend.

## Formal Criteria

- Time window: 14:00 – 15:00 NY.
- Inside NY PM killzone (13:30–16:00).
- Borders macro 13:50–14:10 (start) and 14:50–15:10 (end).
- Sequence: lunch-range sweep or AM-extreme retest → displacement → FVG → entry.
- Lower probability than London / NY AM SB; ICT recommends conservative position sizing.

## Formula / Math

```
ny_pm_sb_window  = [14:00, 15:00] NY
bordering_macros = [(13:50, 14:10), (14:50, 15:10)]
parent_killzone  = NY PM (13:30, 16:00)
```

## Machine-Readable

```json
{
  "id": "silver-bullet-ny-pm",
  "category": "11-silver-bullet",
  "aliases": ["NY-PM-SB", "2pm-SB", "afternoon-SB"],
  "criteria": [
    {"id": "c1", "expr": "time in [14:00, 15:00] NY"},
    {"id": "c2", "expr": "lowest_probability_SB == true"},
    {"id": "c3", "expr": "AM_did_not_cleanly_deliver_preferred_context"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["silver-bullet-overview","silver-bullet-rules","silver-bullet-failure-modes","ny-pm-killzone","ny-pm-session","macro-time-1350-1410","macro-time-1450-1510","ny-pm-reversal"],
  "sources": ["ICT-2022-SILVER-BULLET","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
   13:30 ── 13:50 ─── 14:00 ─── 14:10 ── 14:50 ─── 15:00 ── 15:10 ── 16:00 NY
              ██████ macro                        ██████ macro
                       ████████████████████ ← NY PM SB window
   ────── NY PM KZ ───────────────────────────────────────
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — PM continuation SB:**
- AM was choppy; current trend bearish; lunch consolidated 1.0920–1.0935.
- 13:55 NY: M5 wicks 1.0936 (lunch BSL swept), closes 1.0925.
- 14:10 NY: M5 displacement candle 18 pips red, bearish FVG at 1.0918–1.0922.
- 14:25 NY: M5 retraces to FVG CE 1.0920. Short entry.
- SL above sweep high at 1.0938 (2-pip buffer). Risk = 18 pips.
- Target PDL 1.0890 = 30 pips → 1.7R.

## Common Mistakes

- **Taking PM SB after a clean AM delivery.** When AM has already produced the daily range, PM tends to consolidate or reverse weakly — SB pattern fires but follow-through is poor.
- **Full-size PM trades.** ICT teaches reduced sizing on PM SBs because of the lower probability.
- **Holding past 16:00.** PM SBs should resolve before equities close at 16:00; held positions into Asia rebuild noise risk.

## Related Concepts

- [silver-bullet-overview](silver-bullet-overview.md), [silver-bullet-rules](silver-bullet-rules.md), [silver-bullet-failure-modes](silver-bullet-failure-modes.md), [ny-pm-killzone](../10-killzones/ny-pm-killzone.md), [ny-pm-session](../15-sessions/ny-pm-session.md), [macro-time-1350-1410](../04-time-cycles/macro-time-1350-1410.md), [macro-time-1450-1510](../04-time-cycles/macro-time-1450-1510.md), [ny-pm-reversal](../31-models/ny-pm-reversal.md).

## Citations

- `ICT-2022-SILVER-BULLET`, `ICT-2025-MACRO-PRECISION`.
