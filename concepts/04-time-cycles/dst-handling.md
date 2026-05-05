# DST Handling

**Category:** 04-time-cycles
**Aliases:** Daylight Saving Time, DST mismatch, time-conversion gotcha
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** time, dst, conversion, foundational

## Definition

ICT teaches every time-of-day rule in **New York time** (America/New_York: EST in winter, EDT in summer). Daylight Saving Time creates two issues for traders whose charts display server time, broker time, or UTC: (1) a one-hour shift in the NY → UTC mapping at NY's DST transitions (mid-March, early-November), and (2) two brief multi-week windows per year when NY DST and UK BST are misaligned, making London and NY 4 hours apart instead of the usual 5. **All canonical session, killzone, and macro times in this library are NY-clock anchored**; if your chart is in another timezone, convert.

## Formal Criteria

- ICT canonical timezone: America/New_York.
- NY observes DST from second Sunday of March → first Sunday of November.
- UK observes BST from last Sunday of March → last Sunday of October.
- The two **misalignment windows** (when London/NY are 4h apart instead of 5h):
  - **Spring**: 2nd Sunday March → last Sunday March (~2–3 weeks).
  - **Autumn**: last Sunday October → first Sunday November (~1 week).
- During misalignment, ICT-time-anchored windows still work in NY clock; only translations to/from GMT/UTC shift.

## Formula / Math

```
NY_to_UTC_offset(date):
  -4 if NY in DST (EDT)
  -5 if NY non-DST (EST)

london_NY_offset(date):
  +5 if both observe DST or both observe non-DST (most of year)
  +4 during misalignment windows
```

## Machine-Readable

```json
{
  "id": "dst-handling",
  "category": "04-time-cycles",
  "aliases": ["dst", "daylight-saving-time", "time-conversion"],
  "criteria": [
    {"id": "c1", "expr": "ICT_canonical_timezone == America/New_York"},
    {"id": "c2", "expr": "session_killzone_macro_times_anchored_to_NY_clock == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["session-overview","killzone-overview","macro-times-overview","time-of-day-pivots"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

A timezone offset table rather than a chart:

```
Period                  NY → UTC    London → NY    Notes
─────────────────────   ─────────   ────────────   ──────────────────────
mid-Mar → late-Mar      -4 (EDT)    +4             SPRING MISALIGN window
late-Mar → late-Oct     -4 (EDT)    +5             both DST, normal
late-Oct → early-Nov    -4 (EDT)    +4             AUTUMN MISALIGN window
early-Nov → mid-Mar     -5 (EST)    +5             both non-DST, normal
```

## Timeframes

Affects every TF whose rule is time-anchored. Daily and higher TFs aggregate over the entire day so DST mismatch is less perceptible; intraday (M1–H4) is where errors compound.

## Examples

**Example 1 — running an indicator on UTC charts during US DST:**
- ICT NY AM killzone: 08:00–11:00 NY.
- During DST: 08:00 EDT = 12:00 UTC.
- Indicator must use `12:00 ≤ t < 15:00 UTC` to plot the killzone correctly.
- During non-DST: 08:00 EST = 13:00 UTC. Same indicator must shift by an hour.

**Example 2 — broker-time chart at GMT+2:**
- 08:00 NY EDT = 14:00 GMT+2.
- Killzone window in broker time: 14:00–17:00.
- Server-time platforms should be reset to display NY time directly to avoid this conversion.

## Common Mistakes

- **Hard-coded UTC offsets.** Code that assumes "NY = UTC-5 always" silently breaks 8 months of the year. Use a real timezone library (Python `zoneinfo`, JS `Intl.DateTimeFormat`, etc.).
- **Missing the misalignment windows.** Even with proper DST handling, the 2-week London-NY misalignment trips up indicators that compute via UTC and assume a fixed London-NY offset.
- **Naive trading bot scheduling.** A bot scheduled in UTC for "London open killzone" needs the trigger time recomputed twice a year minimum.
- **Server-time charts.** MT4/MT5 servers run on broker timezones (often GMT+2/GMT+3 in summer). Always re-anchor charts to NY time or build conversions explicitly.

## Related Concepts

- [session-overview](../15-sessions/session-overview.md) — every session boundary depends on this.
- [killzone-overview](../10-killzones/killzone-overview.md) — every killzone boundary depends on this.
- [macro-times-overview](macro-times-overview.md) — macros most affected by DST mistakes.
- [time-of-day-pivots](time-of-day-pivots.md) — all anchored to NY clock.

## Citations

- `ICT-2016-KILLZONES` — NY-clock anchoring established in foundational kill-zone teaching.
- `ICT-2022-MENTORSHIP-OVERVIEW` — DST discipline operationalized for live trading.
