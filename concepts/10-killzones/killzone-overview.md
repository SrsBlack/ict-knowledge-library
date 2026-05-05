# Killzone Overview

**Category:** 10-killzones
**Aliases:** ICT killzones, KZ overview, prime windows
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, time, foundational

## Definition

A killzone is a precise multi-hour sub-window of a trading session during which ICT teaches the highest-probability setups occur — defined in NY time. Killzones are stricter than the broad sessions ([session-overview](../15-sessions/session-overview.md)) they sit inside; trading inside a killzone is when ICT operators are "live." Five canonical killzones cover the trading day. Wider context: killzones < sessions ([session-vs-killzone](../15-sessions/session-vs-killzone.md)). Narrower context: killzones contain macro times and silver-bullet windows.

## Formal Criteria

The five canonical killzones (NY time):

| Killzone | Window | Parent session |
|---|---|---|
| Asia | 20:00 – 00:00 (prev → cur) | Asia |
| London Open | 02:00 – 05:00 | London |
| NY AM | 08:00 – 11:00 | NY AM |
| London Close | 10:00 – 12:00 | London (overlaps NY AM) |
| NY PM | 13:30 – 16:00 | NY PM |

Behavioral signatures:

- High-volume injection at killzone start.
- Frequent sweeps + displacement + FVG sequences.
- Common HOD/LOD formation inside one of the killzones.
- Outside killzones (e.g. mid-morning Asia, 06:30 NY post-London-open, NY Lunch): low-probability for new setups.

## Formula / Math

```
killzones_NY = {
  "asia":          (20:00, 00:00),
  "london_open":   (02:00, 05:00),
  "ny_am":         (08:00, 11:00),
  "london_close":  (10:00, 12:00),
  "ny_pm":         (13:30, 16:00),
}

is_in_killzone(t) := any(start <= t < end for start, end in killzones_NY.values())
```

(Asia killzone wraps midnight; treat as `[20:00, 24:00] ∪ [00:00, 00:00]`.)

## Machine-Readable

```json
{
  "id": "killzone-overview",
  "category": "10-killzones",
  "aliases": ["ICT-killzones", "prime-windows"],
  "criteria": [
    {"id": "c1", "expr": "time falls in any of the 5 canonical KZ windows"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["asia-killzone","london-open-killzone","ny-am-killzone","london-close-killzone","ny-pm-killzone","killzone-times-table","killzone-vs-session","session-overview","macro-times-overview"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
NY clock 24h:

00 ─ 02 ─ 05 ─ 08 ─ 10 ─ 11 ─ 12 ─ 13:30 ─ 16 ─ 18 ─ 20 ─ 24

█           │   │   │       │
└Asia KZ────┘   │   │       │     ──── NY PM KZ ────
                │   │       │     13:30 – 16:00
   ───── London Open KZ ────│
   02:00 – 05:00            │
                ──── NY AM KZ ────
                08:00 – 11:00
                    ──── London Close KZ ────
                    10:00 – 12:00
                    (overlaps NY AM 10:00–11:00)
```

## Timeframes

M1 / M5 / M15 — killzone windows are too short to read meaningfully on H4+.

## Examples

**Example 1 — full-day KZ utilization:**
- 02:30 NY (London Open KZ): swept Asian high, displaced down 30 pips, FVG at 1.0858.
- 09:55 NY (NY AM KZ): swept lunch-eve highs from prior session, displaced up 25 pips.
- 14:10 NY (NY PM KZ): swept lunch low, no follow-through, reversed back into AM range.
- → all three KZs delivered actionable setups; outside-KZ time was avoided.

## Common Mistakes

- **Treating outside-KZ chop as setup.** ICT's discipline: setups belong in killzones. If you're trading 06:00 NY (after London Open KZ ended, before NY AM KZ began), you're outside ICT's prescribed windows.
- **Confusing killzone with session.** See [killzone-vs-session](../15-sessions/session-vs-killzone.md).
- **Confusing killzone with macro window.** Macros (20-min) are precision sub-windows inside killzones (2–3 hours).

## Related Concepts

- Per-killzone deep dives: [asia-killzone](asia-killzone.md), [london-open-killzone](london-open-killzone.md), [ny-am-killzone](ny-am-killzone.md), [london-close-killzone](london-close-killzone.md), [ny-pm-killzone](ny-pm-killzone.md).
- [killzone-times-table](killzone-times-table.md) — quick reference card.
- [killzone-vs-session](killzone-vs-session.md) / [session-vs-killzone](../15-sessions/session-vs-killzone.md) — disambiguation.
- [session-overview](../15-sessions/session-overview.md) — broader window.
- [macro-times-overview](../04-time-cycles/macro-times-overview.md) — narrower precision windows.

## Citations

- `ICT-2016-KILLZONES` — original killzone framework.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational refinements for setup selection.
