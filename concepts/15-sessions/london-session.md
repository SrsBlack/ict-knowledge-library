# London Session

**Category:** 15-sessions
**Aliases:** London hours, European session, London trading hours
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** sessions, london, manipulation, expansion, foundational

## Definition

The London session runs from 02:00 NY to 11:00 NY (canonical NY-time anchor — minor shifts in the brief DST/BST mismatch windows; see [dst-handling](../04-time-cycles/dst-handling.md)). It is the **first major liquidity-delivery session** of the trading day. ICT teaches that London almost always begins with a manipulation phase — a [judas-swing](../13-judas-swing/judas-swing.md) that sweeps one side of the [asian-range](../14-asian-range/asian-range.md) — and then expands in the *opposite* direction toward HTF DOL. London frequently establishes the day's high or low.

## Formal Criteria

- Time window: 02:00 → 11:00 NY (canonical anchor).
- Volatility: high. ATR substantially exceeds Asia.
- Two characteristic phases:
  - **London open killzone** (~02:00–05:00 NY): manipulation + initial expansion. Most setup-rich.
  - **London continuation / close window** (~10:00–12:00 NY): overlap with NY AM; either continuation or reversal of London open's move.
- Asian range bounds are the typical first targets for the London-open sweep.

## Formula / Math

```
london_window      = [02:00, 11:00] NY
london_open_kz     = [02:00, 05:00] NY
london_close_kz    = [10:00, 12:00] NY
```

## Machine-Readable

```json
{
  "id": "london-session",
  "category": "15-sessions",
  "aliases": ["london-hours", "european-session"],
  "criteria": [
    {"id": "c1", "expr": "time_in [02:00, 11:00] NY"},
    {"id": "c2", "expr": "manipulation_then_expansion_typical == true"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["london-open-killzone","london-close","ny-am-session","asia-session","judas-swing","manipulation-phase","range-expansion"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   02:00          05:00              10:00       12:00 NY
   ─────────────────────────────────────────────────
   |   manipulation  |   continuation  |  close   |
   |   (judas swing) |   (expansion)   |  reversal|
   |                 |                 |  / overlap|
   ─────────────────────────────────────────────────
                                       ↑ NY AM begins 08:00
```

## Timeframes

Highest-yield analysis on M5 / M15 (entry refinement) with H1 / H4 for bias. Daily candles often have their high or low established during the London window.

## Examples

**Example 1 — classic Judas-swing-up day:**
- HTF bias bullish.
- 02:30 NY: London open. M5 prints a 12-pip dip below Asian low (SSL sweep), closes back inside Asian range.
- 03:15 NY: M5 displaces up, leaves bullish FVG, prints first higher-high above Asian range.
- 04:30 NY: extends through PDH BSL, retraces to FVG.
- → London-open sweep + expansion, classic textbook delivery.

## Common Mistakes

- **Taking London opens at face value.** The first 15–30 minutes are typically manipulation, not direction. Resist trading the opening candles direction.
- **Ignoring the DST shift.** London open clock-time relative to NY changes twice a year. Track DST explicitly.
- **Treating London as one block.** Open killzone (02:00–05:00) and close killzone (10:00–12:00) have different profiles; analyze them separately.

## Related Concepts

- [london-open-killzone](../10-killzones/london-open-killzone.md) — the highest-priority sub-window.
- [london-close](london-close.md) — the close window and its overlap with NY AM.
- [ny-am-session](ny-am-session.md) — what overlaps London close.
- [asia-session](asia-session.md) — produces the targets London takes.
- [judas-swing](../13-judas-swing/judas-swing.md) — classic London-open pattern.
- [manipulation-phase](../12-power-of-three/manipulation-phase.md) — AMD equivalent.
- [range-expansion](../01-market-structure/range-expansion.md) — what follows the manipulation.

## Citations

- `ICT-2016-KILLZONES` — London open killzone foundational lecture.
- `ICT-2022-MENTORSHIP-OVERVIEW` — London-as-manipulation-then-expansion framing.
