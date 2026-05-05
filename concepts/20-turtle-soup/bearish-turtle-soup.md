# Bearish Turtle Soup

**Category:** 20-turtle-soup
**Aliases:** bearish TS, BeTS, failed bullish breakout
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** turtle-soup, bearish

## Definition

A bearish Turtle Soup is a **failed bullish breakout**: price wicks above a known BSL level, closes back below, and sells off. Mirror of [bullish-turtle-soup](bullish-turtle-soup.md). Functions as a high-conviction short entry signal at BSL levels.

## Formal Criteria

- A known BSL level (swing high, EQH, PWH/PDH, session high) is being approached.
- Price wicks above the BSL.
- Close (same candle or within 1–3 bars) is back below the BSL.
- Post-event displacement is down; bearish FVG often forms.
- HTF bias should be bearish or transitioning bearish.

## Formula / Math

```
bearish_ts(level, n):
    high(n) > level
    AND close(n+k) < level   for some k in [0, 3]
    AND subsequent displacement_down
    AND ideally bearish_FVG forms in displacement
```

## Machine-Readable

```json
{
  "id": "bearish-turtle-soup",
  "category": "20-turtle-soup",
  "aliases": ["bearish-TS", "BeTS", "failed-bullish-breakout"],
  "criteria": [
    {"id": "c1", "expr": "wick_above_known_BSL"},
    {"id": "c2", "expr": "close_back_below_within_few_bars"},
    {"id": "c3", "expr": "displacement_down_with_FVG"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["turtle-soup","bullish-turtle-soup","stop-hunt-pattern","buy-side-liquidity","liquidity-sweep","bearish-rejection-block"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bearish Turtle Soup at BSL:

       ╲╱  ← wick up through BSL, close back below
       ▼   ← close below BSL
   ─── known BSL (e.g. PWH or EQH) ──
        │
        ▼  ← next candle: red displacement
        ▼▼  leaves bearish FVG
```

## Timeframes

M5+.

## Examples

**Example 1 — bearish TS at PDH on H1:**
- PDH = 1.0942.
- H1 wicks 1.0948, closes 1.0935.
- Next H1: 28-pip red displacement, FVG at 1.0928–1.0932.
- → confirmed bearish TS.
- Entry at FVG CE 1.0930; SL 1.0950 (sweep high + 2-pip buffer); risk 20 pips.

## Common Mistakes

- **No HTF context.** Bearish TS during clean bullish HTF distribution often fails.
- **Confusing TS with BSL sweep without confirmation.** TS requires the close-back-below; without it, the wick may extend to a higher BSL.

## Related Concepts

- [turtle-soup](turtle-soup.md), [bullish-turtle-soup](bullish-turtle-soup.md), [stop-hunt-pattern](stop-hunt-pattern.md), [buy-side-liquidity](../02-liquidity/buy-side-liquidity.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [bearish-rejection-block](../19-rejection-blocks/bearish-rejection-block.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
