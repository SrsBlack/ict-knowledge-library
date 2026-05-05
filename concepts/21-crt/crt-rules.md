# CRT Rules

**Category:** 21-crt
**Aliases:** CRT setup rules, CRT checklist
**ICT Confidence:** community-attributed
**Year Introduced:** 2024
**Year Refined:** 2024
**Source IDs:** ROMEO-2024-CRT, TTRADES-CRT-EXPLAINER
**Tags:** crt, rules, community-attributed

## Definition

CRT Rules are the operational checklist for taking a CRT setup. Per the [candle-range-theory](candle-range-theory.md) primary file, CRT is community-attributed (not ICT-original). The rules below reflect the most common formalization across Romeo / TTrades / community sources, with the caveat that CRT teaching is **less standardized than ICT**, so variations exist.

## Formal Criteria — The CRT Checklist

A typical CRT entry requires:

1. **HTF reference candle** — H1 / H4 / D / W candle with a clearly defined high and low.
2. **Time-of-day filter** — sweep occurs at a community-specified time (most-cited: 02:00, 03:00, 05:00, 09:00, 13:00 NY, but varies by source).
3. **Sweep event** — future candle wicks above (or below) the reference candle's bound and closes back inside the range.
4. **Entry trigger** — typically on the LTF FVG or wick rejection following the sweep.
5. **SL** — beyond the sweep extreme.
6. **Target** — the opposite bound of the reference candle.

## Formula / Math

```
crt_setup_valid := htf_reference_candle_identified
                    AND in_time_of_day_window
                    AND sweep_event(reference_candle)
                    AND entry_trigger_after_sweep
                    AND SL_beyond_sweep
                    AND target_at_opposite_bound
```

## Machine-Readable

```json
{
  "id": "crt-rules",
  "category": "21-crt",
  "aliases": ["CRT-checklist", "CRT-rules"],
  "criteria": [
    {"id": "c1", "expr": "htf_reference_candle"},
    {"id": "c2", "expr": "time_of_day_filter"},
    {"id": "c3", "expr": "sweep_event_with_close_back_inside"},
    {"id": "c4", "expr": "target_opposite_bound"}
  ],
  "timeframes": ["H1","H4","D","W"],
  "confidence": "community-attributed",
  "year_introduced": "2024",
  "year_refined": "2024",
  "related": ["candle-range-theory","crt-vs-amd","ict-response-to-crt","liquidity-sweep","turtle-soup"],
  "sources": ["ROMEO-2024-CRT","TTRADES-CRT-EXPLAINER"]
}
```

## Visual Pattern

```
   CRT checklist (bearish setup):

   ☐ HTF reference candle with clear high/low?  [H4 candle 1.0860-1.0900]
   ☐ Sweep occurred at a CRT-time?              [03:00 NY wick above 1.0900]
   ☐ Wick closed back inside range?             [close 1.0890]
   ☐ Entry trigger present?                     [bearish FVG forming]
   ☐ SL above sweep + buffer?                   [1.0912]
   ☐ Target at opposite bound?                  [1.0860]
   
   All checked → take entry.
```

## Timeframes

H1+.

## Examples

**Example 1 — bearish CRT pass:**
- H4 reference candle: high 1.0900, low 1.0860 (formed at 04:00 NY).
- 09:00 NY (CRT time): M5 wicks 1.0905 (sweep above H4 high), closes 1.0892.
- 09:15: M5 prints bearish FVG at 1.0888-1.0892.
- 09:25: Short entry at FVG CE 1.0890. SL 1.0912 (above sweep + buffer); risk 22 pips.
- Target 1.0860 (H4 low); reward 30 pips; R:R = 1.36.

## Common Mistakes

- **Skipping the time filter.** CRT teaches time-anchored sweeps; non-time-aligned sweeps are weaker.
- **Using LTF candles as reference.** CRT references HTF candles for setup-grade reliability.
- **Treating CRT as identical to ICT setups.** CRT entries often look superficially similar to ICT Turtle Soup or Silver Bullet but the framework differs — don't blend taxonomies.

## Related Concepts

- [candle-range-theory](candle-range-theory.md), [crt-vs-amd](crt-vs-amd.md), [ict-response-to-crt](ict-response-to-crt.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [turtle-soup](../20-turtle-soup/turtle-soup.md) — ICT analogues.

## Citations

- `ROMEO-2024-CRT`, `TTRADES-CRT-EXPLAINER`.
