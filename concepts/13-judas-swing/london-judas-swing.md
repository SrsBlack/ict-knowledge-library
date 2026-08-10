# London Judas Swing

**Category:** 13-judas-swing
**Aliases:** London Judas, LDN Judas, London-open Judas
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2016-PROTRACTION
**Tags:** judas, london, sweep

## Definition

The London Judas swing is the canonical session-open Judas — the deceptive directional move at the start of London (02:00 NY) that sweeps the [asian-range](../14-asian-range/asian-range.md) on the wrong side before the algorithm reverses and delivers the true HTF-bias-aligned move. This is the most-frequent Judas pattern in ICT's framework and the highest-quality version because the Asian range is a clean, well-defined liquidity setup overnight.

⚠ **Dating corrected 2026-08-09** from 2018. The September-2016 protraction lecture describes
this exact instance — a counter-directional move after midnight New York / 4 GMT — and names it
a Judas swing (`ICT-2016-PROTRACTION`, 04:04–04:44, 06:32–06:49). See
[market-protraction](market-protraction.md).

## Formal Criteria

- Killzone: London Open KZ (02:00–05:00 NY).
- Sweep target: Asian range high (high-side Judas) or low (low-side Judas).
- Macro overlap: 02:50–03:10 NY macro window often contains the sweep.
- Reversal: occurs in the same killzone, displaces, leaves an FVG.
- Direction post-reversal: aligns with HTF bias.

## Formula / Math

```
london_judas := session == London_Open_KZ [02:00, 05:00] NY
                 AND sweeps(asian_range_high) OR sweeps(asian_range_low)
                 AND reverses_in_kz == true
                 AND reversal_aligns_with_HTF_bias == true
```

## Machine-Readable

```json
{
  "id": "london-judas-swing",
  "category": "13-judas-swing",
  "aliases": ["london-judas", "ldn-judas"],
  "criteria": [
    {"id": "c1", "expr": "killzone == london_open_kz"},
    {"id": "c2", "expr": "sweep_target == asian_range_bound"},
    {"id": "c3", "expr": "reversal_aligns_with_HTF_bias == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["judas-swing","ny-judas-swing","judas-swing-failure","london-open-killzone","asian-range","asian-range-sweep","macro-time-0250-0310"],
  "sources": ["ICT-2016-PROTRACTION", "ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   00:00 ── 02:00 ── 03:00 ── 05:00 NY
              |      |        |
   asian_high ──────────────  ← swept here on high-side Judas
              ↑
              ↑  initial Judas-up
              ↑  (FAKE direction, often
              ↑   first ~30 min of KZ)
              │
              ↓  reversal down
              ↓  displacement + FVG
              ↓
   asian_low  ──────────────
                 ↑
                 ↑ (low-side Judas variant
                    swept here, then reversal up)
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — bullish HTF, low-side Judas:**
- HTF bullish; Asian range 1.0848–1.0876.
- 02:25 NY: M5 wicks 1.0846 (Asian SSL swept), closes 1.0852.
- 02:55–03:10 (macro): M5 prints 18-pip green displacement; FVG at 1.0858–1.0862.
- 03:20: pulls back to FVG; long entry.
- 04:30: 1.0905 reached (PDH).
- → textbook bullish-aligned London Judas.

**Example 2 — bearish HTF, high-side Judas:**
- HTF bearish; Asian range 1.0848–1.0876.
- 02:30 NY: M5 wicks 1.0879 (Asian BSL swept), closes 1.0871.
- 03:00 (macro): M5 prints 16-pip red displacement; FVG at 1.0867–1.0863.
- 03:25: pulls back to FVG; short entry.
- 05:00: 1.0840 reached.
- → textbook bearish-aligned London Judas.

## Common Mistakes

- **Trading both sides.** The Judas is one direction; pick the side based on HTF bias and don't fade your own bias when the fake-out comes through.
- **Late entry on extended displacement.** If displacement extends 30+ pips before retracing to FVG, the FVG often holds but the R:R degrades.
- **Wrong macro alignment.** A Judas that sweeps before 02:50 (pre-macro) sometimes plays out cleaner; one that hasn't swept by 03:30 may not be a Judas at all — could be direct delivery.

## Related Concepts

- [judas-swing](judas-swing.md), [ny-judas-swing](ny-judas-swing.md), [judas-swing-failure](judas-swing-failure.md), [london-open-killzone](../10-killzones/london-open-killzone.md), [asian-range](../14-asian-range/asian-range.md), [asian-range-sweep](../14-asian-range/asian-range-sweep.md), [macro-time-0250-0310](../04-time-cycles/macro-time-0250-0310.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- `ICT-2016-PROTRACTION` (04:04–04:44) the counter-directional move right after midnight New York, "designed to fake out the individuals that chase that initial move"; (06:32–06:49) the same window given as "after 4 GMT" and named a Judas swing.
