# Swing Low

**Category:** 01-market-structure
**Aliases:** pivot low, fractal low, short-term low (STL), intermediate-term low (ITL), long-term low (LTL), old low
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2017
**Source IDs:** ICT-2016-MENTORSHIP-OVERVIEW, ICT-2017-CHARTER-OVERVIEW
**Tags:** structure, pivot, fractal, swing, foundational

## Definition

A swing low is a local price trough — a candle whose low is less than the lows of the candles to its immediate left and right. The mirror image of a swing high. Swing lows are the structural anchors below price; ICT references them for bearish BOS, bullish CHoCH, and SSL liquidity pools.

## Formal Criteria

3-bar definition:

- Candle `n` is a swing low iff `L_n < L_{n-1}` AND `L_n < L_{n+1}`.
- Wicks count — uses candle low, not body or close.
- Confirmation requires candle `n+1` to close.

Fractal hierarchy:

- **Short-Term Low (STL):** any 3-bar swing low.
- **Intermediate-Term Low (ITL):** an STL whose adjacent STLs are both higher.
- **Long-Term Low (LTL):** an ITL whose adjacent ITLs are both higher.

## Formula / Math

```
swing_low(n) := L_n < L_{n-1} AND L_n < L_{n+1}

short_term_low(n)        := swing_low(n)
intermediate_term_low(n) := short_term_low(n)
                             AND L_n < L_{prev_STL}
                             AND L_n < L_{next_STL}
long_term_low(n)         := intermediate_term_low(n)
                             AND L_n < L_{prev_ITL}
                             AND L_n < L_{next_ITL}
```

Where `L_n` is the low (including lower wick) of candle at index `n`.

## Machine-Readable

```json
{
  "id": "swing-low",
  "category": "01-market-structure",
  "aliases": ["pivot-low", "fractal-low", "STL", "ITL", "LTL"],
  "criteria": [
    {"id": "c1", "expr": "L_n < L_{n-1}"},
    {"id": "c2", "expr": "L_n < L_{n+1}"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2017",
  "related": ["swing-high","bos-bearish","choch-bearish","internal-structure","external-structure"],
  "sources": ["ICT-2016-MENTORSHIP-OVERVIEW","ICT-2017-CHARTER-OVERVIEW"]
}
```

## Visual Pattern

```
n-1     n+1
 \  |  /
  \ | /
   \|/
    |
    n
```

Middle candle (`n`) has a low strictly less than both neighbors. Body color irrelevant.

## Timeframes

Same as swing-high: applies M1 through MN1. HTF swing lows are structurally heavier.

## Examples

**Example 1 — basic 3-bar pattern:**
- Candle n-1 low = 1.0850
- Candle n low = 1.0830
- Candle n+1 low = 1.0845
- → n is a swing low (STL).

**Example 2 — STL but NOT ITL:**
- Three STLs at 1.0830, 1.0815, 1.0820. The middle STL (1.0815) is the ITL because both neighbors are higher.

## Common Mistakes

- **Body-only comparisons.** Use the candle low (wick bottom), not the close.
- **Calling the live candle a swing low.** Confirmation requires the next candle's close.
- **Equal lows.** Two adjacent equal-priced lows form an [equal-lows](../02-liquidity/equal-lows.md) liquidity pool, not a single swing low.

## Related Concepts

- [swing-high](swing-high.md) — mirror.
- [bos-bearish](bos-bearish.md) — close below a prior swing low.
- [choch-bearish](choch-bearish.md) — first close below a swing low after a bullish leg.
- [equal-lows](../02-liquidity/equal-lows.md) — what two equal-priced lows form.
- [sell-side-liquidity](../02-liquidity/sell-side-liquidity.md) — stops resting below swing lows.

## Citations

- `ICT-2016-MENTORSHIP-OVERVIEW` — 3-bar swing definition.
- `ICT-2017-CHARTER-OVERVIEW` — STL / ITL / LTL hierarchy.
