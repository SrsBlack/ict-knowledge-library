# London Session

**Category:** 15-sessions
**Aliases:** London hours, European session, London trading hours
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-DEFINING-DAILY-RANGE, ICT-2017-BOND-SPLIT-SESSION, ICT-2017-INTRADAY-PROFILES, ICT-2017-CBDR, ICT-2016-MARKET-EFFICIENCY-PARADIGM, ICT-2022-MENTORSHIP-EP20, ICT-2022-MENTORSHIP-EP21
**Tags:** sessions, london, manipulation, expansion, foundational

## Definition

⚠ **No source in either corpus defines a continuous "02:00–11:00 NY London session."** Searched `london.{0,80}(2 a.m|2 o'clock|11 (a.m|o'clock))` in the raw packets and `london` + clock in the 2022 episodes: nothing defines that span. What exists instead is a set of discrete London windows: the **London killzone** — 01:00–05:00 NY in the 2017 mentorship, 02:00–05:00 NY in 2021/2022 (see [killzone-times-table](../10-killzones/killzone-times-table.md) for the full ERA-SPLIT) — "2 o'clock in the morning to 5 AM, we understand that is the traditional London session" (`ICT-2017-BOND-SPLIT-SESSION`, 06:20); and the **London close killzone** — 10:00–12:00 NY in 2017, narrowed to 10:00–11:00 NY in 2022 (see [london-close](london-close.md)). This page treats "London session" as the informal span bracketed by those two windows, not as a window ICT himself clocks end-to-end.

ICT teaches that London frequently begins with a manipulation phase — a [judas-swing](../13-judas-swing/judas-swing.md) — and then expands in the *opposite* direction toward HTF DOL, and that London frequently establishes the day's high or low: "we're looking for the low of the day to form predominantly in the London session" (`ICT-2017-CBDR`, 06:56).

## Formal Criteria

- No single clocked "session" window — see the Definition warning. Use the two killzones directly.
- Volatility: high. ATR substantially exceeds Asia.
- **London open killzone**: 01:00–05:00 NY (2017) / 02:00–05:00 NY (2021–2022). Most setup-rich.
- **London close killzone**: 10:00–12:00 NY (2017) / 10:00–11:00 NY (2022); overlap with NY AM.
- Asian range bounds are the typical first targets for the London-open sweep, though ICT's own Judas description is anchored to the **midnight opening price**, not to a 02:00 killzone start (see Common Mistakes).

## Formula / Math

```
# No "london_window" constant — ICT gives no single session span.
london_open_kz_2017  = [01:00, 05:00] NY
london_open_kz_2022  = [02:00, 05:00] NY
london_close_kz_2017 = [10:00, 12:00] NY
london_close_kz_2022 = [10:00, 11:00] NY
```

## Machine-Readable

```json
{
  "id": "london-session",
  "category": "15-sessions",
  "aliases": ["london-hours", "european-session"],
  "criteria": [
    {"id": "c1", "expr": "no_single_clocked_session_window_in_corpus == true"},
    {"id": "c2", "expr": "london_open_kz: [01:00,05:00] (2017) or [02:00,05:00] (2021-2022)"},
    {"id": "c3", "expr": "london_close_kz: [10:00,12:00] (2017) or [10:00,11:00] (2022)"},
    {"id": "c4", "expr": "judas_anchor == midnight_NY_opening_price, not killzone_start"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["london-open-killzone","london-close","ny-am-session","asia-session","judas-swing","manipulation-phase","range-expansion"],
  "sources": ["ICT-2017-DEFINING-DAILY-RANGE","ICT-2017-BOND-SPLIT-SESSION","ICT-2017-INTRADAY-PROFILES","ICT-2017-CBDR","ICT-2016-MARKET-EFFICIENCY-PARADIGM","ICT-2022-MENTORSHIP-EP20","ICT-2022-MENTORSHIP-EP21"]
}
```

## Visual Pattern

```
   00:00        02:00    03:00         05:00           10:00   11:00/12:00 NY
   ──────────────────────────────────────────────────────────────────────
   | manipulation (normal) | manip.  |   expansion     |  close   |
   | from midnight open     | (delayed)|  (killzone)    |  reversal|
   | (INTRADAY-PROFILES     | case     |                 |  / overlap|
   |  12:04, 18:42)         | (21:25)  |                 |          |
   ──────────────────────────────────────────────────────────────────────
   midnight open = Judas anchor; killzone (01:00/02:00 start) brackets
   expansion, it does not mark where the manipulation begins.
```

## Timeframes

Highest-yield analysis on M5 / M15 (entry refinement) with H1 / H4 for bias. Daily candles often have their high or low established during the London window.

## Examples

**Example 1 — classic Judas-swing-up day:**
- HTF bias bullish.
- 00:00 NY: midnight open — ICT's Judas anchor point.
- 02:30 NY (London open KZ, 2022 set): M5 prints a 12-pip dip below Asian low (SSL sweep), closes back inside Asian range.
- 03:15 NY: M5 displaces up, leaves bullish FVG, prints first higher-high above Asian range.
- 04:30 NY: extends through PDH BSL, retraces to FVG.
- → London-open sweep + expansion, classic textbook delivery.

## Common Mistakes

- **Citing a "02:00–11:00 canonical London session."** Not in either corpus; use the discrete killzones above.
- **Anchoring the Judas swing to the killzone open.** ICT anchors it to the **midnight NY opening price**, not to 02:00: "we're looking at 12 a.m. for a classic London protraction or Judas swing" (`ICT-2017-INTRADAY-PROFILES`, 18:42); "if we do not see an immediate decline from 12 a.m. New York down into 2 a.m. New York, this is not going to be a London normal protraction buy day" (12:04); the delayed case runs "between 2 o'clock and 3 a.m." (21:25). 2016: "right after midnight New York time, there's a drop down in price. That's the manipulation" (`ICT-2016-MARKET-EFFICIENCY-PARADIGM`, 15:49). 2022 ties the same opening price (the NY midnight open, established at [12:41]–[13:14]) to the 02:00–05:00 killzone instead: "this price is useful for trading the london session that's two o'clock and five o'clock in the morning new york local time" (`ICT-2022-MENTORSHIP-EP21`, 13:14). A window anchored at 02:00 misses the 00:00–02:00 protraction window both eras teach.
- **Claiming "first 15–30 minutes are typically manipulation."** Not in corpus — searched `15 minutes|first hour|first 30|thirty minutes|60 minutes` within 120 characters of `judas|protraction` in both corpora: zero hits.
- **Ignoring the DST shift.** London open clock-time relative to NY changes twice a year. Track DST explicitly.
- **Treating London as one block.** Open killzone and close killzone have different profiles and different ERA-SPLIT clocks; analyze them separately.

## Related Concepts

- [london-open-killzone](../10-killzones/london-open-killzone.md) — the highest-priority sub-window.
- [london-close](london-close.md) — the close window and its overlap with NY AM.
- [ny-am-session](ny-am-session.md) — what overlaps London close.
- [asia-session](asia-session.md) — produces the targets London takes.
- [judas-swing](../13-judas-swing/judas-swing.md) — classic London-open pattern, anchored to the midnight open.
- [manipulation-phase](../12-power-of-three/manipulation-phase.md) — AMD equivalent.
- [range-expansion](../01-market-structure/range-expansion.md) — what follows the manipulation.
- [killzone-times-table](../10-killzones/killzone-times-table.md) — full ERA-SPLIT reference for both London windows.

## Citations

- `ICT-2017-DEFINING-DAILY-RANGE` (03:06–03:24) London killzone 1 a.m. → 5 a.m.; (04:31–04:39) London close killzone 10 a.m. → 12 noon.
- `ICT-2017-BOND-SPLIT-SESSION` (06:20) "2 o'clock in the morning to 5 AM, we understand that is the traditional London session."
- `ICT-2017-INTRADAY-PROFILES` (18:42) "we're looking at 12 a.m. for a classic London protraction or Judas swing"; (12:04) "if we do not see an immediate decline from 12 a.m. New York down into 2 a.m. New York, this is not going to be a London normal protraction buy day"; (21:25) delayed Judas "between 2 o'clock and 3 a.m."
- `ICT-2017-CBDR` (06:56) "we're looking for the low of the day to form predominantly in the London session."
- `ICT-2016-MARKET-EFFICIENCY-PARADIGM` (15:49) "right after midnight New York time, there's a drop down in price. That's the manipulation, making the false move for the low"; (16:11) expansion "into 5 o'clock in the morning New York time."
- `ICT-2022-MENTORSHIP-EP20` (08:09) "london open that's our kill zone that i teach here on the youtube channel it's two o'clock in the morning to five o'clock in the morning new york local time."
- `ICT-2022-MENTORSHIP-EP21` (13:14) "this price is useful for trading the london session that's two o'clock and five o'clock in the morning new york local time and it helps me frame the power 3 for the daily range" — "this price" = the NY midnight opening price, established in the preceding lines [12:41]–[13:14].
