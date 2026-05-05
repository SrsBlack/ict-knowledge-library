# Macro Time 00:50–01:10 NY (London Early)

**Category:** 04-time-cycles
**Aliases:** London early macro, 1AM macro, pre-London macro
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-MACROS, ICT-2025-MACRO-PRECISION
**Tags:** time, macro, london, early

## Definition

The 00:50–01:10 NY macro window sits at the tail of the Asia session and is the first programmed-delivery moment of the trading day in ICT's framework. It often produces the initial Asia-range manipulation move ahead of the London open killzone. The window centers on the 01:00 NY hour boundary.

## Formal Criteria

- Time window: 00:50 → 01:10 NY (canonical anchor; see [dst-handling](dst-handling.md) for the brief twice-yearly drift windows).
- Inside the late Asia session, before the London open killzone (which begins 02:00).
- Behavior: often a sweep of the early Asia range high or low; sometimes the start of the actual Asia → London sweep that the London open then completes.

## Formula / Math

```
window = [00:50, 01:10] NY
parent_session = Asia
proximate_killzone = London open (begins 02:00)
```

## Machine-Readable

```json
{
  "id": "macro-time-0050-0110",
  "category": "04-time-cycles",
  "aliases": ["london-early-macro", "1am-macro"],
  "criteria": [
    {"id": "c1", "expr": "time_in [00:50, 01:10] NY"}
  ],
  "timeframes": ["M1","M5"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["macro-times-overview","asia-session","asian-range","macro-time-0250-0310"],
  "sources": ["ICT-2022-MACROS","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
00:00 ────── 00:50 ── 01:00 ── 01:10 ────── 02:00 NY
              |        █        |
              |   macro window  |   ── London open killzone begins ──
              ──────────────────
             Asia session continues
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — Asia-low sweep:**
- During Asia, M5 prints an Asian low at 1.0848 around 21:30 NY.
- 00:55 NY: M5 wicks 1.0846, closes 1.0851.
- 01:05 NY: M5 displaces up 12 pips, leaves a small bullish FVG.
- → Asian SSL swept inside the macro; London open continues the up-move.

## Common Mistakes

- **Treating it as the London open.** This macro sits BEFORE the London killzone; behavior often previews London but is not yet London delivery proper.
- **Over-trading.** Volume is still Asian-thin; setups need explicit confluence (PD array + Asian range bound + bias).

## Related Concepts

- [macro-times-overview](macro-times-overview.md) — full macro list.
- [asia-session](../15-sessions/asia-session.md) — parent session.
- [asian-range](../14-asian-range/asian-range.md) — what gets swept.
- [macro-time-0250-0310](macro-time-0250-0310.md) — the next macro (London open).

## Citations

- `ICT-2022-MACROS` — macro-time formalization.
- `ICT-2025-MACRO-PRECISION` — refinement.
