# Session Overview

**Category:** 15-sessions
**Aliases:** trading sessions, FX sessions, session map
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** sessions, time, foundational

## Definition

ICT divides the 24-hour FX trading day into discrete sessions defined in **New York time** (EST/EDT). Sessions are not arbitrary — each one carries a characteristic delivery profile (accumulation, manipulation, expansion, distribution) that the algorithm uses repeatedly. ICT's broader killzone concept overlays specific sub-windows inside these sessions where the highest-probability setups occur (see [killzone-overview](../10-killzones/killzone-overview.md)). All times below are NY time and follow DST — see [dst-handling](../04-time-cycles/dst-handling.md).

## Formal Criteria

The ICT canonical session map (NY time):

| Session | Start | End | Notes |
|---|---|---|---|
| Asia | 18:00 (prev day) / 19:00 (DST) | 03:00 / 04:00 | low volatility, range-building |
| London | 02:00 / 03:00 | 11:00 / 12:00 | high volatility, often sets daily direction |
| NY AM | 08:00 / 09:00 | 12:00 | major US news, NY Open displacement |
| NY Lunch | 12:00 | 13:30 | low volatility, consolidation |
| NY PM | 13:30 | 16:00 / 17:00 | secondary delivery, reversals common |
| London Close | 10:00 | 12:00 | overlaps NY AM; European book unwinds |

Two start times reflect DST: the earlier time is during DST (mid-March–early-November NY); the later time is non-DST.

## Formula / Math

Session membership for any timestamp `t` (NY time):

```
session(t) :=
  if 18:00_prev_day <= t < 03:00:        Asia
  elif 02:00 <= t < 08:00:               London (early)
  elif 08:00 <= t < 12:00:               NY AM (overlaps London Close)
  elif 12:00 <= t < 13:30:               NY Lunch
  elif 13:30 <= t < 17:00:               NY PM
```

(Some ICT references use 17:00 NY as the daily close; check broker. The boundary times shift by one hour during DST transitions.)

## Machine-Readable

```json
{
  "id": "session-overview",
  "category": "15-sessions",
  "aliases": ["trading-sessions", "fx-sessions"],
  "criteria": [
    {"id": "c1", "expr": "all_session_times_in_NY_time == true"},
    {"id": "c2", "expr": "DST_transitions_handled == true"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["asia-session","london-session","ny-am-session","ny-lunch","ny-pm-session","london-close","killzone-overview","dst-handling"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
NY time 24-hour layout (DST):

00 ──── 03 ──── 07 ── 09 ── 12 ── 13:30 ── 16 ──── 18 ──── 24
  Asia       London       NY AM    NY     NY PM       Asia
                          (overlap Lunch              (next
                           London Close)               day)
```

## Timeframes

Session boundaries are most relevant on M5 / M15 / H1; daily and higher TFs aggregate across sessions. Lower TFs (M1) show session transitions clearly but are noise-dominated.

## Examples

**Example 1 — full daily cycle:**
- Asia (18:00 prev → 03:00): EURUSD ranges 30 pips.
- London (03:00 → 08:00): sweeps Asian SSL, displaces 60 pips up.
- NY AM (08:00 → 12:00): continues with NY Open displacement candle, prints PDH.
- Lunch (12:00 → 13:30): tight 12-pip consolidation.
- NY PM (13:30 → 17:00): reversal back into NY AM range.

## Common Mistakes

- **Using broker time, not NY time.** Many brokers display server time (often GMT+2 / GMT+3); ICT analysis requires explicit NY-time conversion. DST mismatch is the #1 killzone error.
- **Treating session boundaries as hard.** Volatility transitions are gradual; the first/last 15 minutes of any session can behave like the adjacent one.
- **Ignoring overlaps.** NY AM and London Close overlap (10:00–12:00 NY); this overlap is the highest-volume window of the day.

## Related Concepts

- [asia-session](asia-session.md), [london-session](london-session.md), [ny-am-session](ny-am-session.md), [ny-lunch](ny-lunch.md), [ny-pm-session](ny-pm-session.md), [london-close](london-close.md) — session deep-dives.
- [session-overlaps](session-overlaps.md) — where two sessions co-fire.
- [killzone-overview](../10-killzones/killzone-overview.md) — ICT's stricter sub-windows inside sessions.
- [session-vs-killzone](session-vs-killzone.md) — disambiguation.
- [dst-handling](../04-time-cycles/dst-handling.md) — time-conversion details.

## Citations

- `ICT-2016-KILLZONES` — original session/killzone delineation.
- `ICT-2022-MENTORSHIP-OVERVIEW` — sessions as cycle-of-day reference.
