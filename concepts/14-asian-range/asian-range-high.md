# Asian Range High

**Category:** 14-asian-range
**Aliases:** Asian high, AR high, ARH, Asia session high
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** asian-range, bsl, foundational

## Definition

The Asian range high is the highest price printed during the Asia session window — typically the Asia killzone (20:00–00:00 NY). It is a primary buy-side liquidity pool that London delivery routinely sweeps. When equal highs print at this level, it becomes a particularly dense BSL target.

## Formal Criteria

- Window: 20:00 → 00:00 NY (KZ anchor) or 18:00 prev → 03:00 NY (full session anchor).
- Asian range high = max(high) over window.
- The wick top counts (not the close).
- Frequently coincides with equal-highs ([equal-highs](../02-liquidity/equal-highs.md)) along the bound.

## Formula / Math

```
asian_range_high = max(high(t)) for t in asian_window
```

## Machine-Readable

```json
{
  "id": "asian-range-high",
  "category": "14-asian-range",
  "aliases": ["asian-high", "ARH", "asia-session-high"],
  "criteria": [
    {"id": "c1", "expr": "level == max_high_during_asian_window"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["asian-range","asian-range-low","asian-range-sweep","buy-side-liquidity","equal-highs","liquidity-pool","judas-swing"],
  "sources": ["ICT-2016-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   asian_range_high ─────────────────── ← BSL pool
                /\  /\    /\  /\
               /  \/  \  /  \/  \
              /        \/        \
   asian_range_low ──────────────────── ← SSL pool
```

## Timeframes

M5 / M15 / H1.

## Examples

**Example 1 — Asian high becomes BSL target:**
- Asian KZ produces high 1.0876 at 22:30 NY with a second touch at 23:00 (REH).
- HTF bias bullish → 1.0876 is intermediate BSL; PDH BSL above is at 1.0900.
- London open: M5 wicks 1.0879, closes 1.0871. Asian BSL swept; bias-aligned setup is to enter long on the FVG.
- Bullish bias targets PDH next.

## Common Mistakes

- **Using close instead of wick.** Asian high uses the candle high (wick top).
- **Wrong window.** Specify killzone-anchored vs full-session-anchored; results differ when extra-session moves print bigger highs/lows.
- **Treating the high as resistance.** It's **liquidity**, not resistance. Algorithm wants to take it, not respect it.

## Related Concepts

- [asian-range](asian-range.md), [asian-range-low](asian-range-low.md), [asian-range-sweep](asian-range-sweep.md), [buy-side-liquidity](../02-liquidity/buy-side-liquidity.md), [equal-highs](../02-liquidity/equal-highs.md), [liquidity-pool](../02-liquidity/liquidity-pool.md), [judas-swing](../13-judas-swing/judas-swing.md).

## Citations

- `ICT-2016-LIQUIDITY`, `ICT-2022-MENTORSHIP-OVERVIEW`.
