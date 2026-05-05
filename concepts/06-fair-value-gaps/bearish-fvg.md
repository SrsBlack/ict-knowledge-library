# Bearish FVG (SIBI)

**Category:** 06-fair-value-gaps
**Aliases:** SIBI, sell-side imbalance / buy-side inefficiency, bearish gap, BeFVG
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fvg, bearish, sibi, foundational

## Definition

A bearish FVG (SIBI) is a 3-candle imbalance from a downward displacement candle where `H_{n+1} < L_{n-1}`. Mirror of bullish FVG. Sits as a **premium-array reference** when above current price.

## Formal Criteria

- Three consecutive candles n-1, n, n+1.
- Candle n is a downward displacement candle.
- `H_{n+1} < L_{n-1}` strictly.
- Unworked region: `[H_{n+1}, L_{n-1}]`.

## Formula / Math

```
bearish_FVG(n) := H_{n+1} < L_{n-1}

fvg_low  := H_{n+1}
fvg_high := L_{n-1}
fvg_size := fvg_high - fvg_low
ce       := (fvg_low + fvg_high) / 2
```

## Machine-Readable

```json
{
  "id": "bearish-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["SIBI", "sell-side-imbalance", "BeFVG"],
  "criteria": [
    {"id": "c1", "expr": "H_{n+1} < L_{n-1}"},
    {"id": "c2", "expr": "candle_n_is_bearish_displacement == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["fair-value-gap","bullish-fvg","inversion-fvg","consequent-encroachment","ce-as-primary-entry","premium-array","bearish-order-block","displacement-definition"],
  "sources": ["ICT-2016-FVG-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   ▼
   █  ← n-1
     ▼
     █
     █  ← n (large red displacement)
     █
     █
        ▼   ← gap region (FVG)
          ▼
          █  ← n+1 (high < n-1 low)
          █
          ▼

   FVG = [H_{n+1}, L_{n-1}], above candle n+1, below candle n-1.
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 bearish FVG short:**
- H1: L_{n-1} = 1.0945, H_{n+1} = 1.0938. FVG = [1.0938, 1.0945], size 7 pips. CE = 1.09415.
- HTF bearish; price retraces to CE.
- Short at 1.0941 with SL above 1.0947 (FVG high + 2-pip buffer).
- Risk = 6 pips.

## Common Mistakes

- **Going short into bullish HTF bias.** SIBI alone doesn't defeat bias.
- **Insisting on full fill before expansion.** SIBI often holds at CE without going to far edge.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [inversion-fvg](inversion-fvg.md).
- [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md).
- [premium-array](../05-pd-arrays/premium-array.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md).
- [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
