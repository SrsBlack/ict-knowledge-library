# London Close Reversal

**Category:** 31-models
**Aliases:** LDN close reversal, London close fade, European unwind reversal
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** model, london-close, reversal

## Definition

The London Close Reversal is a named ICT setup where the **London-open direction reverses during the London Close window (10:00–12:00 NY)**. As European desks unwind their morning positions, the directional move from London open often gets faded — particularly when the morning move was extended and HTF bias was less than fully bullish/bearish on the morning side. The reversal frequently produces the day's HOD or LOD.

## Formal Criteria

A London Close Reversal requires:

- The London-open KZ delivered a clear directional move (bullish or bearish).
- That move ran into a known HTF level (PDH/PDL/PWH/PWL or FVG).
- During 10:00–12:00 NY (London Close KZ + NY AM overlap), price reverses.
- The reversal sweeps the London-open extreme as part of the move.
- HTF bias is mixed or transitioning — pure-trend HTF rarely sees full LC reversals.

## Formula / Math

```
london_close_reversal:
    london_open_directional_move_present
    AND move_reached_HTF_level
    AND in [10:00, 12:00] NY window
    AND price_reverses_against_morning_direction
    AND london_open_extreme_eventually_swept
```

## Machine-Readable

```json
{
  "id": "london-close-reversal",
  "category": "31-models",
  "aliases": ["LDN-close-reversal", "London-close-fade"],
  "criteria": [
    {"id": "c1", "expr": "London open delivered move"},
    {"id": "c2", "expr": "reversal during 10:00-12:00 NY"},
    {"id": "c3", "expr": "morning-extreme eventually swept"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["london-close","london-close-killzone","ny-am-killzone","silver-bullet-ny-am","ict-2022-model","liquidity-sweep"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   London Close Reversal (bearish reversal of bullish morning):

   03:00–10:00: London open delivered +60 pips up to HOD 1.0925.
   10:30 NY: M5 wicks 1.0928 (sweeps HOD BSL), closes 1.0918.
   11:00 NY: M5 displaces -25 pips, bearish FVG.
   11:30: M5 retests FVG; short entry.
   12:00–13:30: continues bearish into NY lunch.
```

## Timeframes

M5 / M15 / H1.

## Examples

**Example 1 — bearish reversal of bullish AM:**
- HTF bias mixed; W bullish but D approaching exhaustion.
- 03:00–10:00 NY: London delivered +60 pips, HOD 1.0925 at PDH BSL.
- 10:30 NY: M5 wicks 1.0928 (HOD/PDH BSL swept), closes 1.0918.
- 11:00 NY: M5 displaces 25 pips down, bearish FVG 1.0908–1.0912.
- 11:25 NY: M5 retests CE 1.0910. Short entry.
- SL 1.0930 (above sweep + buffer); risk 20 pips.
- TP NY AM-low SSL or PDL → reasonable 2-3R.

## Common Mistakes

- **Forcing reversal every day.** Many days continue London-open direction through NY AM; LC Reversal isn't guaranteed.
- **Reversing strong-trend days.** When HTF is unambiguously aligned with London-open direction, fading at LC is fighting the algorithm.
- **Missing the swept-extreme requirement.** A reversal that doesn't first sweep the morning extreme isn't a true LC Reversal — it's just a pullback.

## Related Concepts

- [london-close](../15-sessions/london-close.md), [london-close-killzone](../10-killzones/london-close-killzone.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [ict-2022-model](ict-2022-model.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md).

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW`.
