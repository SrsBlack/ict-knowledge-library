# Session vs Killzone — Disambiguation

**Category:** 15-sessions
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** sessions, killzones, disambiguation, terminology

## Definition

This page resolves the most common terminology confusion in ICT time-of-day analysis: **session** vs **killzone**. They are related but not interchangeable.

- A **session** is a broad multi-hour window of the trading day (Asia, London, NY AM, NY Lunch, NY PM, London Close).
- A **killzone** is a stricter, narrower sub-window inside a session where ICT teaches the highest-probability setups occur.

Every killzone is inside a session. Not every session-time is a killzone.

## Formal Criteria

### Sessions (broad, foundational)

- Asia: ~18:00 prev → 03:00 NY (~9 hours).
- London: ~02:00 → 11:00 NY (~9 hours).
- NY AM: ~08:00 → 12:00 NY (~4 hours).
- NY Lunch: 12:00 → 13:30 NY (~1.5 hours).
- NY PM: 13:30 → 16:00 NY (~2.5 hours).
- London Close: 10:00 → 12:00 NY (~2 hours, overlaps NY AM).

### Killzones (narrow, setup-rich)

- Asia killzone: 20:00 → 00:00 NY (~4 hours; not the whole Asia session).
- London Open killzone: 02:00 → 05:00 NY (~3 hours; subset of London).
- NY AM killzone: 08:00 → 11:00 NY (~3 hours; subset of NY AM).
- London Close killzone: 10:00 → 12:00 NY (~2 hours; same as the close window).
- NY PM killzone: 13:30 → 16:00 NY (~2.5 hours; full PM session).

### The Containment Relationship

```
all killzones ⊂ all session-time
```

If you see action inside a killzone, you also see it inside the parent session. The reverse is NOT true: an Asia trade at 21:30 NY is in the Asia killzone, but an Asia trade at 04:30 NY is past the Asia killzone (and also not yet in the London killzone).

## Formula / Math

```
in_session(t, name)  := t falls inside the broad session window
in_killzone(t, name) := t falls inside the strict killzone subset

invariant: in_killzone(t, kz) ⇒ in_session(t, parent_session(kz))
```

## Machine-Readable

```json
{
  "id": "session-vs-killzone",
  "category": "15-sessions",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "every_killzone_subset_of_a_session == true"},
    {"id": "c2", "expr": "killzones_narrower_than_sessions == true"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["session-overview","killzone-overview","asia-session","london-session","ny-am-session","ny-pm-session","london-close"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Asia session ──────────────────────────────────────
       killzone:        ████████████████              ← 20:00 – 00:00 NY
   ──────────────────────────────────────────────────

   London session  ────────────────────
       killzone:   ████████             ← 02:00 – 05:00 NY
   ──────────────────────────────────────

   NY AM session   ────────────────
       killzone:   ████████             ← 08:00 – 11:00 NY
   ──────────────────────────────────────

   (sessions are wider, killzones are narrower)
```

## Timeframes

Both apply on every TF, but the distinction matters most on M5/M15 entry timeframes where being inside vs outside a killzone changes the setup quality.

## Examples

**Example A — inside session, outside killzone:**
- 06:30 NY: still inside London session (02:00–11:00) but past the London Open killzone (which ended at 05:00).
- ICT teaches: lower-probability for new setups; finish what's in flight, don't open new.

**Example B — inside killzone:**
- 09:30 NY: inside NY AM session AND inside NY AM killzone (08:00–11:00).
- ICT teaches: prime time for setup execution.

## Common Mistakes

- **Treating "session" as synonym for "killzone".** The broad session is descriptive (this is what time it is); the killzone is prescriptive (this is when to take setups).
- **Missing the overlap with NY AM Silver Bullet.** The NY AM killzone (08:00–11:00) contains the Silver Bullet window (10:00–11:00) — both apply during that hour.
- **Skipping DST.** Killzone times in NY shift relative to GMT twice a year; always anchor to NY clock.

## Related Concepts

- [session-overview](session-overview.md) — full session map.
- [killzone-overview](../10-killzones/killzone-overview.md) — full killzone map.
- [asia-session](asia-session.md), [london-session](london-session.md), [ny-am-session](ny-am-session.md), [ny-pm-session](ny-pm-session.md), [london-close](london-close.md) — session deep-dives.
- [dst-handling](../04-time-cycles/dst-handling.md) — time-conversion details.

## Citations

- `ICT-2016-KILLZONES` — original killzone teaching that established the inside-the-session relationship.
- `ICT-2022-MENTORSHIP-OVERVIEW` — formal session/killzone separation operationalized for setups.
