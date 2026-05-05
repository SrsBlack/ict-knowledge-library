# Silver Bullet — NY AM

**Category:** 11-silver-bullet
**Aliases:** NY AM SB, 10am SB, premier silver bullet
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-SILVER-BULLET, ICT-2025-MACRO-PRECISION
**Tags:** silver-bullet, ny-am, premier

## Definition

The NY AM Silver Bullet is the **10:00–11:00 NY** Silver Bullet window — ICT's **highest-probability SB** because it sits inside three overlapping high-conviction time contexts simultaneously: the NY AM killzone (08:00–11:00), the London Close killzone (10:00–12:00), and the 09:50–10:10 macro window. The combined volume + algorithmic precision + multi-session institutional participation makes this window the most-cited SB in ICT teaching.

## Formal Criteria

- Time window: 10:00 – 11:00 NY.
- Inside NY AM killzone AND London Close killzone (overlap).
- Contains macro 09:50–10:10 (which spans into 10:10).
- Sequence: liquidity sweep (often pre-NY-AM range or PDH/PDL) → displacement → FVG → CE retest.
- The setup is typically where the **daily HOD or LOD** is established.

## Formula / Math

```
ny_am_sb_window   = [10:00, 11:00] NY
overlapping       = NY_AM_KZ ∩ LDN_Close_KZ ∩ macro_0950_1010
parent_killzones  = NY AM (08:00-11:00), LDN Close (10:00-12:00)
```

## Machine-Readable

```json
{
  "id": "silver-bullet-ny-am",
  "category": "11-silver-bullet",
  "aliases": ["NY-AM-SB", "10am-SB", "premier-silver-bullet"],
  "criteria": [
    {"id": "c1", "expr": "time in [10:00, 11:00] NY"},
    {"id": "c2", "expr": "overlap_NY_AM_KZ_and_LDN_Close_KZ == true"},
    {"id": "c3", "expr": "highest_probability_SB == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["silver-bullet-overview","silver-bullet-rules","ny-am-killzone","london-close-killzone","london-close","macro-time-0950-1010","ce-as-primary-entry"],
  "sources": ["ICT-2022-SILVER-BULLET","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
   08:00 ── 09:50 ─── 10:00 ──── 11:00 ──── 12:00 NY
              ██████ macro 09:50-10:10
                       ██████████████ ← NY AM SB window
   ──── NY AM KZ ──────────────────
                       ──── London Close KZ ──────
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — bullish NY AM SB:**
- HTF bullish; PDH 1.0942 untaken; current 1.0915 at 09:50.
- 09:55 (macro): M5 wicks 1.0908 (London-AM low SSL), closes 1.0918.
- 10:05 (SB window opens): M5 displacement candle 22 pips green, bullish FVG at 1.0930–1.0934.
- 10:25: M5 pulls back to FVG CE 1.0932. Long entry.
- SL below sweep low at 1.0906 (2-pip buffer). Risk = 26 pips.
- Target PDH 1.0942 = ~10 pips → too tight for 26 risk; target -1.5 SD or PWH at 1.0975 = ~43 pips → 1.65R. Better: scale entry deeper (closer to FVG far edge 1.0930) for tighter risk.

## Common Mistakes

- **Force-fitting SB at 10:00 sharp.** The window opens at 10:00; sweep+displacement+FVG can take 5–25 minutes to form. Don't force entries on the opening tick.
- **Ignoring overlap nuances.** The 10:00–11:00 hour participates in NY AM KZ + LDN Close KZ + the tail of macro 09:50-10:10. All three are in your favor.
- **Holding past 12:00.** Lunch begins; SB momentum dies. Take profits or trail SLs before NY AM session ends.

## Related Concepts

- [silver-bullet-overview](silver-bullet-overview.md), [silver-bullet-rules](silver-bullet-rules.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [london-close-killzone](../10-killzones/london-close-killzone.md), [london-close](../15-sessions/london-close.md), [macro-time-0950-1010](../04-time-cycles/macro-time-0950-1010.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md).

## Citations

- `ICT-2022-SILVER-BULLET`, `ICT-2025-MACRO-PRECISION`.
