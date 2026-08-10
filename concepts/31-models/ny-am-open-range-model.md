# NY AM Open Range Model

**Category:** 31-models
**Aliases:** NY AM open range, NY opening range, OR model
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** model, ny-am, opening-range

## Definition

The NY AM Open Range Model uses the **first 30 to 60 minutes of NY AM (08:00–08:30 or 08:00–09:00 NY)** as the day's opening range. ICT teaches that this opening range often gets swept on one side during the NY AM killzone and the daily delivery extends in the opposite direction. The Open Range high and low function as intra-day BSL/SSL pools that the algorithm targets during the NY AM Silver Bullet hour.

## Formal Criteria

- Time window: 08:00 → 08:30 NY (short OR) or 08:00 → 09:00 NY (long OR).
- OR_high = max(high) over the window.
- OR_low = min(low) over the window.
- Sweep of OR_high or OR_low during 09:00–11:00 NY is the trigger event.
- HTF bias filters which sweep direction is the entry side.

## Formula / Math

```
or_window = [08:00, 08:30] NY    # or [08:00, 09:00] for long OR
or_high = max(high) over or_window
or_low  = min(low)  over or_window

trigger:
    if HTF bullish AND OR_low_swept post-window: long bias on reversal
    if HTF bearish AND OR_high_swept post-window: short bias on reversal
```

## Machine-Readable

```json
{
  "id": "ny-am-open-range-model",
  "category": "31-models",
  "aliases": ["NY-AM-OR", "NY-opening-range", "OR-model"],
  "criteria": [
    {"id": "c1", "expr": "OR window = [08:00, 08:30] or [08:00, 09:00] NY"},
    {"id": "c2", "expr": "OR-bound sweep + HTF-bias-aligned reversal"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["ict-2022-model","silver-bullet-ny-am","ny-am-killzone","ny-am-session","liquidity-sweep","htf-bias-framework"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   NY AM Open Range Model:

   08:00 ─── 08:30 ─── 09:00 ─── 11:00 NY
   ──── OR window ──────
   |          |
   OR_high (BSL pool)            ← sweep during NY AM SB
   OR_low  (SSL pool)
   |          |
                          ↓
              09:55–10:30: sweep one OR bound, reverse, displace.
              Long if SSL swept on bullish bias; short if BSL swept on bearish.
```

## Timeframes

M5–H1.

## Examples

**Example 1 — bullish NY AM OR sweep:**
- HTF bullish.
- 08:00–08:30: OR formed at 1.0900–1.0915.
- 09:55: M5 wicks 1.0896 (OR_low swept), closes 1.0908.
- 10:08: M5 displacement +18 pips, FVG up at 1.0918–1.0922.
- 10:25: M5 retests CE 1.0920. Long entry.
- SL 1.0894 (sweep low - 2-pip buffer); risk 26 pips.
- Target PDH 1.0950 → 30 pips → 1.15R; or extended -1.5 SD ~1.0975 → 55 pips → 2.1R.

## Common Mistakes

- **OR sweep without HTF context.** Counter-bias OR sweeps frequently fail.
- **Single OR window.** Some traders use 08:00–08:30; others 08:00–09:00; pick one and apply consistently.
- **Trading the OR breakout itself.** The model is "sweep + reverse," not "OR breakout buy/sell." Sweeps are entries; clean breakouts often lack reversal confirmation.

## Related Concepts

- [ict-2022-model](ict-2022-model.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [ny-am-session](../15-sessions/ny-am-session.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).
- [futures-opening-range](../15-sessions/futures-opening-range.md) — the June-2017 futures form of the same construct: **08:00–09:00 NY for the 30-year bond** and **09:30–10:30 NY for the index futures**, each anchored to that market's own volume peak. It is the earliest opening-range teaching located in the corpus, and it also carries the range-size rules (≤12 ticks = squeeze; extended range = expect a return) that this page does not.

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW`.
