# Macro Time 02:50–03:10 NY (London Open)

**Category:** 04-time-cycles
**Aliases:** London open macro, 3AM macro
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-MACROS, ICT-2025-MACRO-PRECISION
**Tags:** time, macro, london, open

## Definition

The 02:50–03:10 NY macro spans the actual London open (03:00 NY). It is the canonical "Judas swing" delivery window — the moment when the algorithm typically sweeps one side of the [asian-range](../14-asian-range/asian-range.md) and begins London's expansion phase. It sits inside the London open killzone (02:00–05:00 NY).

## Formal Criteria

- Time window: 02:50 → 03:10 NY.
- Inside London open killzone.
- Behavior: high-probability for Asian-range sweep + opposite-direction displacement; the foundational [judas-swing](../13-judas-swing/judas-swing.md) macro.

## Formula / Math

```
window = [02:50, 03:10] NY
parent_killzone = London open killzone [02:00, 05:00]
```

## Machine-Readable

```json
{
  "id": "macro-time-0250-0310",
  "category": "04-time-cycles",
  "aliases": ["london-open-macro", "3am-macro"],
  "criteria": [
    {"id": "c1", "expr": "time_in [02:50, 03:10] NY"}
  ],
  "timeframes": ["M1","M5"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["macro-times-overview","london-session","london-open-killzone","judas-swing","asian-range","silver-bullet-london"],
  "sources": ["ICT-2022-MACROS","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
02:00 ────── 02:50 ── 03:00 ── 03:10 ────── 05:00 NY
   |          |        █        |             |
   ────── London open killzone ────────────────
              ──── macro ────
             (Judas swing zone)
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — Judas-swing-down then bullish reversal:**
- HTF bias bullish; Asian range 1.0845–1.0875.
- 02:55 NY: M5 wicks 1.0843, closes 1.0851 (Asian SSL swept).
- 03:05 NY: M5 displaces 18 pips up, leaves a 4-pip bullish FVG.
- 03:30 NY: returns to FVG, then continues to PDH BSL by 04:30.
- → textbook macro-window Judas swing.

## Common Mistakes

- **Trading the first wick blindly.** The macro often produces a fake-out then a real move; don't enter on the wick — wait for the displacement.
- **Missing the bias filter.** Macros amplify both directions; bias decides which side of the sweep is the entry side.

## Related Concepts

- [macro-times-overview](macro-times-overview.md), [london-open-killzone](../10-killzones/london-open-killzone.md), [judas-swing](../13-judas-swing/judas-swing.md), [asian-range](../14-asian-range/asian-range.md), [silver-bullet-london](../11-silver-bullet/silver-bullet-london.md).

## Citations

- `ICT-2022-MACROS`, `ICT-2025-MACRO-PRECISION`.
