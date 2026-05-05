# Intraday AMD

**Category:** 12-power-of-three
**Aliases:** intraday PO3, daily AMD, session AMD
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PO3, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** amd, intraday, foundational

## Definition

Intraday AMD is the application of the PO3 / AMD doctrine at the **single-trading-day scale** — the canonical Asia-London-NY mapping. It's the most-traded scale of PO3 because every day the cycle restarts and the Asia-London-NY phase structure repeats. Intraday AMD is the framework most ICT day-traders use to plan a session.

## Formal Criteria

The standard intraday-AMD mapping (NY time):

| Phase | Window | Session |
|---|---|---|
| Accumulation (A) | 18:00 prev → 03:00 NY | Asia |
| Manipulation (M) | 02:00 → 05:00 NY (London open KZ) | London open / Judas swing |
| Distribution (D) | 08:00 → 12:00 NY | NY AM |
| (X — continuation/reversal) | 13:30 → 16:00 NY | NY PM |

This is the **typical** mapping; not every day follows it cleanly. Some days skip the Judas (manipulation), others reverse during distribution into NY PM.

## Formula / Math

```
intraday_amd_canonical = {
  A: [18:00 prev, 03:00 NY],   # Asia
  M: [02:00, 05:00 NY],        # London open KZ
  D: [08:00, 12:00 NY],        # NY AM
  X: [13:30, 16:00 NY],        # NY PM
}
```

## Machine-Readable

```json
{
  "id": "intraday-amd",
  "category": "12-power-of-three",
  "aliases": ["intraday-PO3", "daily-AMD", "session-AMD"],
  "criteria": [
    {"id": "c1", "expr": "A=Asia, M=London open KZ, D=NY AM, X=NY PM"},
    {"id": "c2", "expr": "canonical typical_only_not_required"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["power-of-three","accumulation-phase","manipulation-phase","distribution-phase","htf-amd","amd-cycle-overview","asia-session","london-open-killzone","ny-am-session","ny-pm-session","quarterly-shift-theory"],
  "sources": ["ICT-2016-PO3","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   intraday AMD timeline (NY clock):

   18:00 ─── 00:00 ─── 03:00 ─── 05:00 ─── 08:00 ─── 12:00 ─── 13:30 ─── 16:00 NY
   ──── A ──────────────────                                                
                          ── M ─                                            
                                            ──── D ───────                  
                                                              ── X ────────
   Asia                  LDN open               NY AM             NY PM
   (accumulation)        (manipulation)         (distribution)    (X)
```

## Timeframes

M5 / M15 / H1.

## Examples

**Example 1 — clean MMBM day:**
- Asia (A): 30-pip range, low volatility, 2 equal lows at 1.0848.
- London open (M): 02:55 wicks 1.0846 (Asian SSL swept), reverses up.
- NY AM (D): 60-pip rally, takes PDH 1.0925 by 09:30, prints HOD 1.0945 by 10:30 (NY AM SB delivery).
- NY PM (X): pulls back into NY AM range, consolidates to 16:00.
- → textbook intraday MMBM.

## Common Mistakes

- **Forcing every day into the canonical map.** ~50–60% of days follow AMD cleanly; the rest show variations (no manipulation, reversal during distribution, etc.).
- **Sticking to A-M-D-X labels rigidly.** The phases blur at boundaries; volume and behavior matter more than clock-time labels.
- **Single-instrument bias.** Different instruments may run AMD on slightly shifted clocks (e.g., commodity-related FX during commodity-market hours).

## Related Concepts

- [power-of-three](power-of-three.md), [accumulation-phase](accumulation-phase.md), [manipulation-phase](manipulation-phase.md), [distribution-phase](distribution-phase.md), [htf-amd](htf-amd.md), [amd-cycle-overview](../24-amd-cycle/amd-cycle-overview.md).
- [asia-session](../15-sessions/asia-session.md), [london-open-killzone](../10-killzones/london-open-killzone.md), [ny-am-session](../15-sessions/ny-am-session.md), [ny-pm-session](../15-sessions/ny-pm-session.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md).

## Citations

- `ICT-2016-PO3`, `ICT-2022-MENTORSHIP-OVERVIEW`.
