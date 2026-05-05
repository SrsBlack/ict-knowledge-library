# Bullish FVG (BISI)

**Category:** 06-fair-value-gaps
**Aliases:** BISI, buy-side imbalance / sell-side inefficiency, bullish gap, BFVG
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fvg, bullish, bisi, foundational

## Definition

A bullish FVG (BISI) is a 3-candle imbalance produced by an upward displacement candle whose neighbors fail to overlap on the wick range — `L_{n+1} > H_{n-1}`. The unworked region between the two non-overlapping wicks is a buy-side imbalance / sell-side inefficiency: the algorithm went up too fast to deliver two-sided trade, so the unworked zone stays open as a future revisit target. Bullish FVGs are **discount-array references** when sitting below current price.

## Formal Criteria

- Three consecutive candles n-1, n, n+1.
- Candle n is an upward displacement candle (large green body, minimal upper wick relative to body).
- `L_{n+1} > H_{n-1}` strictly.
- Unworked region: `[H_{n-1}, L_{n+1}]`.
- Persists until rebalanced.

## Formula / Math

```
bullish_FVG(n) := L_{n+1} > H_{n-1}

fvg_low  := H_{n-1}
fvg_high := L_{n+1}
fvg_size := fvg_high - fvg_low
ce       := (fvg_low + fvg_high) / 2
```

## Machine-Readable

```json
{
  "id": "bullish-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["BISI", "buy-side-imbalance", "BFVG"],
  "criteria": [
    {"id": "c1", "expr": "L_{n+1} > H_{n-1}"},
    {"id": "c2", "expr": "candle_n_is_bullish_displacement == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["fair-value-gap","bearish-fvg","inversion-fvg","consequent-encroachment","ce-as-primary-entry","discount-array","bullish-order-block","displacement-definition"],
  "sources": ["ICT-2016-FVG-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
         ▲
         █  ← n+1 (low > n-1 high)
         █
       ▲     ← gap region (FVG)
       █
       █  ← n (large green displacement)
       █
       █
     ▲
     █  ← n-1
   ▲
   FVG = [H_{n-1}, L_{n+1}], below candle n+1, above candle n-1.
```

## Timeframes

All TFs.

## Examples

**Example 1 — M15 bullish FVG entry:**
- M15: H_{n-1} = 1.0860, L_{n+1} = 1.0865. FVG = [1.0860, 1.0865], size 5 pips. CE = 1.08625.
- HTF bullish; price returns to 1.0863 (CE).
- Long entry at CE with SL below 1.0858 (FVG low - 2 pip buffer).
- Risk = 5 pips.

## Common Mistakes

- **Bullish-FVG long against bearish HTF bias.** Even a textbook bullish FVG fails frequently when HTF says price should keep falling.
- **Treating BISI as guaranteed support.** It's a *zone of interest*, not a hard floor.
- **Tiny FVG = noise.** Filter by ATR; sub-2-pip FVGs on EURUSD M5 rarely matter.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bearish-fvg](bearish-fvg.md), [inversion-fvg](inversion-fvg.md).
- [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md).
- [discount-array](../05-pd-arrays/discount-array.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md).
- [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
