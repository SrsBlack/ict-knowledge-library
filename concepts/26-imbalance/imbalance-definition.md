# Imbalance — Definition

**Category:** 26-imbalance
**Aliases:** imbalance, market imbalance, price imbalance
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** imbalance, foundational

## Definition

An imbalance is **any region of price where one side of the order book did not get filled** — a pocket where buyers traded through sellers (or vice versa) without two-sided auction. ICT uses imbalance as the umbrella term that includes Fair Value Gaps, volume imbalances, and broader liquidity voids. Imbalances are inefficiencies the algorithm tends to revisit in order to **rebalance** — provide the missing two-sided trade.

## Formal Criteria

An imbalance has:

- A measurable price region where consecutive candles failed to overlap (the geometric definition: candle wicks don't touch).
- Strong directional intent (one side dominated).
- Typically forms during displacement.
- Frequently gets visited by price later as the algorithm "rebalances" the inefficiency.

ICT-canonical imbalance variants:

- **Fair Value Gap (FVG)** — 3-candle imbalance where mid-candle's wick range doesn't overlap with adjacent candle ranges.
- **Volume imbalance** — small body-vs-body gap (no overlap of bodies) that may not qualify as a 3-candle FVG.
- **Liquidity void** — multi-candle wider region with displacement and minimal pullback.

## Formula / Math

Generic imbalance test:

```
imbalance(n, n+1) := body_or_range(n) does NOT overlap body_or_range(n+1)
```

Type-specific definitions:

```
bullish_FVG(n)        := L_{n+1} > H_{n-1}                # 3-candle wick gap
bearish_FVG(n)        := H_{n+1} < L_{n-1}
volume_imbalance(n)   := close_n vs open_{n+1} body gap
```

## Machine-Readable

```json
{
  "id": "imbalance-definition",
  "category": "26-imbalance",
  "aliases": ["imbalance", "market-imbalance"],
  "criteria": [
    {"id": "c1", "expr": "consecutive_price_regions_dont_overlap == true"},
    {"id": "c2", "expr": "formed_during_displacement == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["inefficiency","imbalance-vs-fvg","imbalance-rebalance","volume-imbalance-detail","fair-value-gap","liquidity-void","displacement-definition"],
  "sources": ["ICT-2016-FVG-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish 3-candle imbalance (= FVG):

         ▲
         █  ← candle n+1 (low > candle n-1 high)
         █
       ▲
       █  ← candle n (the displacement candle)
       █
       █
     ▲
     █  ← candle n-1
   ▲
   wick_top of n-1   < wick_bottom of n+1

   The price region between H_{n-1} and L_{n+1} is the imbalance / FVG.
```

## Timeframes

All TFs.

## Examples

**Example 1 — bullish FVG imbalance:**
- M5: candle n-1 high = 1.0860, candle n+1 low = 1.0865.
- → 5-pip imbalance from 1.0860–1.0865.
- Algorithm tendency: revisit the imbalance later to rebalance (often within hours on M5).

## Common Mistakes

- **Treating imbalance and FVG as identical.** FVG is a specific 3-candle imbalance pattern. The umbrella term includes other forms (volume imbalance, void).
- **Over-finding imbalances.** Tiny imbalances of 1–2 pips on M1 are noise; filter by size proportional to ATR.
- **Expecting full rebalance.** Most imbalances rebalance to CE (50% midpoint) or just past, not to the far edge. Expecting full fill is too literal.

## Related Concepts

- [inefficiency](inefficiency.md) — ICT's broader synonym.
- [imbalance-vs-fvg](imbalance-vs-fvg.md) — disambiguation.
- [imbalance-rebalance](imbalance-rebalance.md) — what happens when price returns.
- [volume-imbalance-detail](volume-imbalance-detail.md) — body-vs-body imbalances.
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) — the canonical 3-candle pattern.
- [liquidity-void](../02-liquidity/liquidity-void.md) — wider multi-candle imbalance.
- [displacement-definition](../09-displacement/displacement-definition.md) — what creates imbalances.

## Citations

- `ICT-2016-FVG-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
