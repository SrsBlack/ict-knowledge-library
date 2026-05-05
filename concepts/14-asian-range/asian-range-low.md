# Asian Range Low

**Category:** 14-asian-range
**Aliases:** Asian low, AR low, ARL, Asia session low
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** asian-range, ssl, foundational

## Definition

The Asian range low is the lowest price printed during the Asia session window — the mirror of [asian-range-high](asian-range-high.md). Primary sell-side liquidity pool that London delivery often sweeps. Equal-lows along the level make it a particularly dense SSL target.

## Formal Criteria

- Window: 20:00 → 00:00 NY (KZ anchor) or 18:00 prev → 03:00 NY (full session anchor).
- Asian range low = min(low) over window.
- Wick bottom counts.
- Frequently coincides with [equal-lows](../02-liquidity/equal-lows.md).

## Formula / Math

```
asian_range_low = min(low(t)) for t in asian_window
```

## Machine-Readable

```json
{
  "id": "asian-range-low",
  "category": "14-asian-range",
  "aliases": ["asian-low", "ARL", "asia-session-low"],
  "criteria": [
    {"id": "c1", "expr": "level == min_low_during_asian_window"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["asian-range","asian-range-high","asian-range-sweep","sell-side-liquidity","equal-lows","liquidity-pool","judas-swing"],
  "sources": ["ICT-2016-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

See [asian-range-high](asian-range-high.md) — same diagram, lower bound is the ARL.

## Timeframes

M5 / M15 / H1.

## Examples

**Example 1 — bullish-bias Judas-down at ARL:**
- Asian KZ produces low 1.0848 at 23:15 NY (REL with 1.0850 at 22:00).
- HTF bias bullish → ARL is the Judas swing target.
- London open: M5 wicks 1.0846, closes 1.0853. ARL swept.
- Subsequent M5 displaces 18 pips up, leaves bullish FVG; entry zone for the actual long.

## Common Mistakes

- **Wick vs close.** Asian low uses the wick bottom.
- **Treating ARL as support.** It's **SSL liquidity**, designed to be taken.

## Related Concepts

- [asian-range](asian-range.md), [asian-range-high](asian-range-high.md), [asian-range-sweep](asian-range-sweep.md), [sell-side-liquidity](../02-liquidity/sell-side-liquidity.md), [equal-lows](../02-liquidity/equal-lows.md), [liquidity-pool](../02-liquidity/liquidity-pool.md), [judas-swing](../13-judas-swing/judas-swing.md).

## Citations

- `ICT-2016-LIQUIDITY`, `ICT-2022-MENTORSHIP-OVERVIEW`.
