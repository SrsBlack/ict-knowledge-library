# Macro Times Overview

**Category:** 04-time-cycles
**Aliases:** macros, ICT macro windows, programmed-delivery times
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-MACROS, ICT-2025-MACRO-PRECISION
**Tags:** time, macros, programmed-delivery, foundational

## Definition

Macro times are precise short windows within the trading day during which ICT teaches the algorithm reliably executes "instructions" — programmed delivery moments characterized by high-probability displacement, sweeps, and reversals. There are five canonical macro windows, each ~20 minutes wide, all anchored in NY time. Macros are inside larger sessions (London / NY AM / NY PM) and overlap with killzones; trading INSIDE a macro window with PD-array confluence is one of ICT's highest-probability setups.

## Formal Criteria

The five canonical macro windows (NY time):

| Macro | Window | Parent session |
|---|---|---|
| London early | 00:50 – 01:10 | late Asia / pre-London |
| London open | 02:50 – 03:10 | London open killzone |
| NY pre-open | 09:50 – 10:10 | NY AM killzone |
| NY first afternoon | 13:50 – 14:10 | NY PM open + macro |
| NY mid-afternoon | 14:50 – 15:10 | NY PM continuation |

Behavior inside a macro:

- Wider candle ranges and faster delivery than surrounding bars.
- Common to print displacement that takes liquidity and leaves an FVG.
- Setups that align with HTF bias + macro window + PD array = highest-confluence trades.

## Formula / Math

```
macros_NY = [
  (00:50, 01:10),   # London early
  (02:50, 03:10),   # London open
  (09:50, 10:10),   # NY pre-open
  (13:50, 14:10),   # NY first afternoon
  (14:50, 15:10),   # NY mid-afternoon
]

is_macro_window(t) := any(start <= t < end for (start, end) in macros_NY)
```

ICT teaches a typical macro is the **20 minutes around a "10-minutes-before to 10-minutes-after" hour boundary** (or half-hour boundary). The pattern: macros bracket :00 and :30 times where the algorithm injects volatility.

## Machine-Readable

```json
{
  "id": "macro-times-overview",
  "category": "04-time-cycles",
  "aliases": ["macros", "ICT-macro-windows", "programmed-delivery-times"],
  "criteria": [
    {"id": "c1", "expr": "time_in any of [00:50-01:10, 02:50-03:10, 09:50-10:10, 13:50-14:10, 14:50-15:10] NY"}
  ],
  "timeframes": ["M1","M5"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["macro-time-0050-0110","macro-time-0250-0310","macro-time-0950-1010","macro-time-1350-1410","macro-time-1450-1510","90-minute-cycle","killzone-overview","quarterly-shift-theory"],
  "sources": ["ICT-2022-MACROS","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
NY clock, 24h timeline (DST):

00 ─ 01 ─ 02 ─ 03 ─ 04 ─ 05 ─ 06 ─ 07 ─ 08 ─ 09 ─ 10 ─ 11 ─ 12 ─ 13 ─ 14 ─ 15 ─ 16
       █                █                                 █                █     █
       00:50–01:10     02:50–03:10                       09:50–10:10      13:50  14:50
      "London early"   "London open"                     "NY pre-open"    -14:10 -15:10
                                                                          "NY 1st" "NY mid"
```

## Timeframes

M1 / M5 are the actionable TFs. M15 candles span almost the entire macro window so don't carry the same micro-structure information. Daily and higher are irrelevant for macro-window trading.

## Examples

**Example 1 — NY pre-open macro (09:50–10:10) bullish:**
- HTF bias bullish; PDH BSL at 1.0925 untaken; current price 1.0905.
- 09:50: M5 prints a 6-pip wick down into prior FVG, then a 22-pip green displacement candle.
- 09:55: takes 1.0925 BSL, leaves a 5-pip bullish FVG.
- 10:00: extends to 1.0935 before pulling back to FVG.
- → textbook macro-window delivery: sweep, displacement, FVG, continuation. Entry on FVG retest.

## Common Mistakes

- **Trading macros against HTF bias.** Macro windows amplify movement in either direction; without bias filter, macros cut both ways.
- **Wrong timezone.** Macros are NY-time anchors. Server-time charts will misalign by hours.
- **Confusing macros with killzones.** Killzones are 2–3 hour session sub-windows; macros are 20-minute precision windows inside (or sometimes outside) killzones. See [killzone-vs-session](../15-sessions/session-vs-killzone.md) for the broader hierarchy.
- **Stale list.** ICT has refined macro precision over 2023–2025 (`ICT-2025-MACRO-PRECISION`); some older sources cite slightly different windows. Use the canonical five listed here.

## Related Concepts

- [macro-time-0050-0110](macro-time-0050-0110.md), [macro-time-0250-0310](macro-time-0250-0310.md), [macro-time-0950-1010](macro-time-0950-1010.md), [macro-time-1350-1410](macro-time-1350-1410.md), [macro-time-1450-1510](macro-time-1450-1510.md) — per-window deep dives.
- [90-minute-cycle](90-minute-cycle.md) — broader time-cycle concept.
- [killzone-overview](../10-killzones/killzone-overview.md) — session sub-windows that contain or border macros.
- [quarterly-shift-theory](quarterly-shift-theory.md) — fractal-time framing in which macros sit.

## Citations

- `ICT-2022-MACROS` — original macro-time formalization in 2022 mentorship.
- `ICT-2025-MACRO-PRECISION` — 2025 refinement; precision and indicator tools updated.
