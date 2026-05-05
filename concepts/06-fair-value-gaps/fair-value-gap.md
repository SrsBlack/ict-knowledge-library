# Fair Value Gap (FVG)

**Category:** 06-fair-value-gaps
**Aliases:** FVG, 3-candle imbalance, gap, fair value gap, ICT FVG
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2025
**Source IDs:** ICT-2016-FVG-INTRO, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2024-FVG-CLASSIFICATION, ICT-2025-CE-PRIMARY-ENTRY
**Tags:** fvg, imbalance, foundational, pd-array

## Definition

A Fair Value Gap is a **3-candle imbalance pattern** where the middle candle's range is so directional that the wicks of the candles before and after fail to overlap with each other. The unworked region between candle n-1's wick and candle n+1's wick is the FVG itself — a price zone where the market did not trade in both directions and where ICT teaches the algorithm tends to return to "rebalance" the inefficiency. FVGs are ICT's most-cited PD array and the primary entry zone in most setups.

## Formal Criteria

For a **bullish FVG** (BISI — buy-side imbalance / sell-side inefficiency):

- Three consecutive candles n-1, n, n+1.
- Candle n is a strong upward (displacement) candle.
- The low of candle n+1 is **strictly greater than** the high of candle n-1: `L_{n+1} > H_{n-1}`.
- The unworked region is `[H_{n-1}, L_{n+1}]`.

For a **bearish FVG** (SIBI — sell-side imbalance / buy-side inefficiency):

- Candle n is a strong downward displacement.
- `H_{n+1} < L_{n-1}`.
- The unworked region is `[H_{n+1}, L_{n-1}]`.

Wicks are used (not closes). The FVG persists until rebalanced.

## Formula / Math

```
bullish_FVG(n) := L_{n+1} > H_{n-1}
fvg_low        := H_{n-1}
fvg_high       := L_{n+1}
fvg_size       := fvg_high - fvg_low
ce             := (fvg_low + fvg_high) / 2     # consequent encroachment

bearish_FVG(n) := H_{n+1} < L_{n-1}
fvg_low        := H_{n+1}
fvg_high       := L_{n-1}
```

## Machine-Readable

```json
{
  "id": "fair-value-gap",
  "category": "06-fair-value-gaps",
  "aliases": ["FVG", "3-candle-imbalance", "ICT-FVG"],
  "criteria": [
    {"id": "c1", "expr": "bullish: L_{n+1} > H_{n-1}"},
    {"id": "c2", "expr": "bearish: H_{n+1} < L_{n-1}"},
    {"id": "c3", "expr": "candle_n_displacement_present == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2025",
  "related": ["bullish-fvg","bearish-fvg","inversion-fvg","consequent-encroachment","ce-as-primary-entry","balanced-price-range","volume-imbalance","immediate-rebalance-fvg","delayed-rebalance-fvg","fvg-classification-2025","liquidity-void-vs-fvg","fvg-mitigation","nested-fvg","imbalance-definition","displacement-definition"],
  "sources": ["ICT-2016-FVG-INTRO","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2024-FVG-CLASSIFICATION","ICT-2025-CE-PRIMARY-ENTRY"]
}
```

## Visual Pattern

```
   bullish FVG (BISI):                    bearish FVG (SIBI):

         ▲                                    ▼
         █  ← n+1 (low > n-1 high)            ▼  ← n+1 (high < n-1 low)
         █                                    ▼
       ▲                                    █
       █  ← n (displacement up)              █  ← n (displacement down)
       █                                    █
       █                                    █
     ▲                                    ▼
     █  ← n-1                              ▼  ← n-1
   ▲                                      ▼
                                            
   FVG region:                              FVG region:
   [H_{n-1}, L_{n+1}]                       [H_{n+1}, L_{n-1}]
   below n+1, above n-1                     above n+1, below n-1
```

## Timeframes

All TFs. HTF FVGs (H4, D) carry more conviction; LTF FVGs (M5) are entry-trigger size.

## Examples

**Example 1 — bullish M15 FVG:**
- M15 candle n-1 high = 1.0860.
- M15 candle n is a 22-pip green displacement (open 1.0859, close 1.0878, low 1.0858, high 1.0879).
- M15 candle n+1 low = 1.0865.
- → bullish FVG at 1.0860–1.0865 (5 pips). CE = 1.08625.
- Long entry zone on retest at CE; SL below 1.0858 with buffer.

## Common Mistakes

- **Body-only FVG.** Some practitioners use bodies (open/close) instead of wicks (high/low) — that's a different pattern (volume imbalance), not a strict FVG.
- **Tiny FVGs.** A 1–2 pip FVG on M5 is noise; filter by ATR.
- **Forgetting displacement.** A 3-candle wick gap with no displacement on candle n is structurally weak — the algorithm leaves "real" FVGs only when delivery is forceful.
- **Treating every FVG as fillable.** Many FVGs partially fill (to CE) and continue; demanding full fill misses entries.

## Related Concepts

- [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md) — directional variants.
- [inversion-fvg](inversion-fvg.md) — flipped FVG after rebalance + reversal.
- [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md) — CE entry framework.
- [balanced-price-range](balanced-price-range.md) — overlapping bullish + bearish FVG.
- [volume-imbalance](volume-imbalance.md) — body-vs-body imbalance variant.
- [immediate-rebalance-fvg](immediate-rebalance-fvg.md), [delayed-rebalance-fvg](delayed-rebalance-fvg.md), [fvg-classification-2025](fvg-classification-2025.md).
- [liquidity-void-vs-fvg](liquidity-void-vs-fvg.md), [fvg-mitigation](fvg-mitigation.md), [nested-fvg](nested-fvg.md).
- [imbalance-definition](../26-imbalance/imbalance-definition.md), [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-INTRO` — original FVG introduction.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational refinements.
- `ICT-2024-FVG-CLASSIFICATION` — immediate vs delayed rebalance.
- `ICT-2025-CE-PRIMARY-ENTRY` — CE elevated to primary entry.
