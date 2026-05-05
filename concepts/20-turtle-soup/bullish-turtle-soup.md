# Bullish Turtle Soup

**Category:** 20-turtle-soup
**Aliases:** bullish TS, BTS, failed bearish breakout
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** turtle-soup, bullish

## Definition

A bullish Turtle Soup is a **failed bearish breakout**: price wicks below a known SSL level, closes back above, and rallies. The pattern documents the failure of breakdown traders' shorts and the trapping of breakout sellers — providing the buy-side counter-flow that institutions need to fill long positions. Functions as a high-conviction long entry signal at known SSL levels.

## Formal Criteria

- A known SSL level (swing low, EQL, PWL/PDL, session low) is being approached.
- Price wicks below the SSL.
- Close (same candle or within 1–3 bars) is back above the SSL.
- Post-event displacement is up; bullish FVG often forms.
- HTF bias should be bullish or transitioning bullish.

## Formula / Math

```
bullish_ts(level, n):
    low(n) < level
    AND close(n+k) > level   for some k in [0, 3]
    AND subsequent displacement_up
    AND ideally bullish_FVG forms in displacement
```

## Machine-Readable

```json
{
  "id": "bullish-turtle-soup",
  "category": "20-turtle-soup",
  "aliases": ["bullish-TS", "BTS", "failed-bearish-breakout"],
  "criteria": [
    {"id": "c1", "expr": "wick_below_known_SSL"},
    {"id": "c2", "expr": "close_back_above_within_few_bars"},
    {"id": "c3", "expr": "displacement_up_with_FVG"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["turtle-soup","bearish-turtle-soup","stop-hunt-pattern","sell-side-liquidity","liquidity-sweep","bullish-rejection-block"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish Turtle Soup at SSL:

   ─── known SSL (e.g. PWL or EQL) ──
       │
       ╲  ← wick down through SSL
        ╲╱
         ▲  ← close back above SSL
        ▲▲  ← next candle: green displacement
       ▲▲▲   leaves bullish FVG
```

## Timeframes

M5+.

## Examples

**Example 1 — bullish TS at PWL on H1:**
- PWL = 1.0850.
- H1 wicks 1.0846, closes 1.0858.
- Next H1: 22-pip green displacement, FVG at 1.0855–1.0859.
- → confirmed bullish TS.
- Entry at FVG CE 1.0857; SL 1.0844 (sweep low - 2-pip buffer); risk 13 pips.

## Common Mistakes

- **No HTF context.** Bullish TS during a clean bearish HTF distribution often fails — the wick is a continuation, not a reversal.
- **Tight reversal expectation.** Some TS patterns produce only a small bounce before continuing down; require displacement + FVG to confirm.

## Related Concepts

- [turtle-soup](turtle-soup.md), [bearish-turtle-soup](bearish-turtle-soup.md), [stop-hunt-pattern](stop-hunt-pattern.md), [sell-side-liquidity](../02-liquidity/sell-side-liquidity.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [bullish-rejection-block](../19-rejection-blocks/bullish-rejection-block.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
