# Stop Run into FVG

**Category:** 29-stop-runs
**Aliases:** stop run + FVG entry, FVG-anchored stop run
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** stop-run, fvg, entry

## Definition

A "stop run into FVG" is the high-conviction sequence: stop run sweeps a known liquidity level, then a displacement candle leaves an FVG, providing the entry zone for a position aligned with the post-sweep direction. This is one of ICT's most-traded combinations — the stop run gives the entry the algorithmic anchor (where the institutional position got filled), and the FVG gives the precise retest level.

## Formal Criteria

The full sequence:

1. **Stop run event** — wick takes a known structural level.
2. **Displacement** — wide candle in the post-sweep direction (typically opposite to the sweep direction = Turtle Soup outcome; sometimes same direction = run-and-continue).
3. **FVG forms** — inside or after the displacement.
4. **Entry on FVG retest** at CE (per 2025 default).
5. **SL beyond the swept extreme**.

## Formula / Math

```
stop_run_into_fvg(setup):
    sweep_event_at_known_level
    AND displacement_after_sweep
    AND FVG forms
    AND entry at FVG CE on retest
    AND SL beyond sweep extreme + buffer
```

## Machine-Readable

```json
{
  "id": "stop-run-into-fvg",
  "category": "29-stop-runs",
  "aliases": ["stop-run-FVG-entry", "FVG-anchored-stop-run"],
  "criteria": [
    {"id": "c1", "expr": "sweep + displacement + FVG sequence"},
    {"id": "c2", "expr": "entry at FVG CE"},
    {"id": "c3", "expr": "SL beyond sweep extreme"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["stop-run-definition","stop-run-into-ob","stop-run-into-breaker","fair-value-gap","ce-as-primary-entry","liquidity-sweep","silver-bullet-rules"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish stop run into FVG:

   ─── known SSL ─────
        │
        ▼  ← stop run wick (sweep)
        ╲╱
         ▲▲▲   ← displacement up
        ▲ █▲   ← bullish FVG inside displacement
       ▲ █ ▲
                       ↓
                       retest to FVG CE = entry
```

## Timeframes

M5–H4.

## Examples

**Example 1 — bullish stop run into FVG (London open):**
- HTF bullish; Asian SSL at 1.0850.
- 02:55 NY: M5 wicks 1.0846 (sweep).
- 03:05 NY: M5 18-pip green displacement, FVG at 1.0856–1.0860.
- 03:25 NY: M5 retests CE 1.0858. Long entry.
- SL 1.0844 (sweep low - 2-pip buffer); risk 14 pips.
- TP -1.5 SD or PDH.

## Common Mistakes

- **Pre-positioning at FVG before displacement.** The FVG zone must form *after* the sweep + displacement; entering earlier on a "near miss" is premature.
- **Stop run direction confusion.** Take direction from post-sweep displacement; the sweep direction is misleading.

## Related Concepts

- [stop-run-definition](stop-run-definition.md), [stop-run-into-ob](stop-run-into-ob.md), [stop-run-into-breaker](stop-run-into-breaker.md).
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.
