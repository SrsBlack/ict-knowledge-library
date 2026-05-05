# NY Judas Swing

**Category:** 13-judas-swing
**Aliases:** NY AM Judas, New York Judas
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** judas, ny-am, sweep

## Definition

A NY Judas swing is the smaller-scale session-open Judas at NY AM (08:00 NY) — typically a fake directional move in the first 30–60 minutes of NY AM-KZ that sweeps a known pre-NY pool (London-session high/low, premarket extremes, prior day high/low), then reverses into the actual NY AM delivery. NY Judas is generally **less reliable than London Judas** because NY AM often inherits and continues London's direction rather than reversing it.

## Formal Criteria

- Killzone: NY AM-KZ (08:00–11:00 NY).
- Sweep target: London session high/low, premarket extremes, or PDH/PDL.
- Macro overlap: often sets up via the 08:30 news candle and resolves around the 09:50–10:10 macro.
- Reversal: occurs within the killzone, displaces, leaves FVG, aligns with HTF bias.
- **Lower frequency than London Judas:** when London already delivered the daily direction, NY tends to extend rather than reverse.

## Formula / Math

```
ny_judas := session == NY_AM_KZ [08:00, 11:00] NY
             AND sweeps(london_session_high) OR sweeps(london_session_low) OR sweeps(PDH/PDL)
             AND reverses_in_kz == true
             AND reversal_aligns_with_HTF_bias == true
```

## Machine-Readable

```json
{
  "id": "ny-judas-swing",
  "category": "13-judas-swing",
  "aliases": ["ny-am-judas", "new-york-judas"],
  "criteria": [
    {"id": "c1", "expr": "killzone == ny_am_kz"},
    {"id": "c2", "expr": "sweep_target_is_london_extreme_or_PDH_PDL"},
    {"id": "c3", "expr": "reversal_aligns_with_HTF_bias == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["judas-swing","london-judas-swing","judas-swing-failure","ny-am-killzone","macro-time-0950-1010","silver-bullet-ny-am"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   06:00 ── 08:00 ── 09:30 ── 10:00 ── 11:00 NY
              |       |       │        |
              ──── NY AM KZ ──┼────────
              ↑               │
              ↑  Judas (fake) │
              ↑               │
              ↓  reversal     ↓
              ↓  + macro      │
              ↓  09:50-10:10  │
              ↓               │
              ↓  displacement │
              ↓               │
              ↓  + FVG        │
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — bullish HTF, NY high-side Judas:**
- HTF bullish; London delivered a 50-pip up-move; London-session high 1.0905, current price 1.0890 at 08:00.
- 08:30 NY (news candle): M5 prints a -15-pip red candle, closes 1.0875.
- 09:00: M5 wicks 1.0871 (London-day-low SSL), closes 1.0880.
- 09:55 (macro): M5 displaces 18 pips up, leaves bullish FVG.
- 10:30: 1.0915 (NY HOD).
- → NY Judas down then bullish reversal aligned with HTF.

## Common Mistakes

- **Expecting NY Judas every day.** When London cleanly delivered, NY often continues without a Judas. Don't force a Judas read.
- **Confusing news-driven move with Judas.** The 08:30 news release can produce a real directional move that is NOT a Judas — it's actual delivery. Differentiating requires checking displacement quality and HTF bias alignment.
- **Trading the 08:00–08:30 pre-news window.** Often the cleanest "Judas-looking" move happens before the 08:30 release; trading it pre-news is risky because the news can extend the move rather than reverse it.

## Related Concepts

- [judas-swing](judas-swing.md), [london-judas-swing](london-judas-swing.md), [judas-swing-failure](judas-swing-failure.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [macro-time-0950-1010](../04-time-cycles/macro-time-0950-1010.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
