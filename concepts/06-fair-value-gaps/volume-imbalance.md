# Volume Imbalance (FVG-side)

**Category:** 06-fair-value-gaps
**Aliases:** VI, body imbalance, volume gap
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-REINFORCED, ICT-2016-LIQUIDITY-VOIDS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fvg, volume-imbalance, body-gap

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018` sourced
only to the generic `ICT-2017-DISPLACEMENT` and `ICT-2022-MENTORSHIP-OVERVIEW` placeholders. The
**December-2016** mentorship lecture *ICT Fair Value Gaps FVG* teaches this exact geometry — "we
gap from this candle's close, 104.72, to an opening on this candle of 104.70 … now it's only two
pips difference, but that creates a what? A gap" [12:26–12:41], and then "**the wick trades
through the body, but the bodies of the candle completely close in here** … so this gap between
these two candles … this gap in between the bodies have perfectly been filled in with this up
candle" [13:19–13:33] (`ICT-2016-FVG-REINFORCED`). The companion lecture *Liquidity Voids* names
the same two-candle body gap a **common gap** [12:37] (`ICT-2016-LIQUIDITY-VOIDS`). Re-dated to
2016. ⚠ The *label* "volume imbalance" does not appear anywhere in the 153-packet local corpus;
it is later (2022-mentorship-era) terminology for a 2016 concept, which is why `Year Refined`
stays 2022.

## Definition

A volume imbalance (in the FVG family) is a **body-vs-body gap** between two consecutive candles — open of candle n is strictly above (bullish VI) or below (bearish VI) the close of candle n-1, but their **wicks may overlap**. It is **not** a strict 3-candle FVG (which requires non-overlapping wicks across 3 candles), but it IS an imbalance and serves as a softer FVG-like reference. See [volume-imbalance-detail](../26-imbalance/volume-imbalance-detail.md) for the deeper imbalance-side treatment; this file documents how VIs are treated alongside FVGs in ICT entry logic.

## Formal Criteria

For a bullish VI:

- Candle n-1 closes at `C_{n-1}`.
- Candle n opens at `O_n > C_{n-1}` (body gap up).
- Wicks of n-1 and n may overlap (this is what differentiates VI from FVG).
- Body gap = `[C_{n-1}, O_n]` (the unworked body region).

For a bearish VI: symmetric.

VIs often nest near or inside an FVG; when a VI sits inside the same zone as a 3-candle FVG, conviction stacks.

## Formula / Math

```
bullish_vi(n) := O_n > C_{n-1}
vi_low        := C_{n-1}
vi_high       := O_n
vi_size       := vi_high - vi_low
```

## Machine-Readable

```json
{
  "id": "volume-imbalance",
  "category": "06-fair-value-gaps",
  "aliases": ["VI", "body-imbalance", "volume-gap"],
  "criteria": [
    {"id": "c1", "expr": "open_n != close_{n-1}"},
    {"id": "c2", "expr": "wicks_may_overlap == true (NOT a strict FVG)"},
    {"id": "c3", "expr": "vi_size_meaningful relative to ATR"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["fair-value-gap","imbalance-vs-fvg","volume-imbalance-detail","imbalance-definition","displacement-definition"],
  "sources": ["ICT-2016-FVG-REINFORCED","ICT-2016-LIQUIDITY-VOIDS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish volume imbalance:

       ▲
       █  ← candle n: opens above prior close
       █
       O_n
       ──────────────  ← body gap (volume imbalance)
       C_{n-1}
       █
       █  ← candle n-1
       ▼
   (wicks may overlap visually; bodies do not)
```

## Timeframes

M5+. M1 VIs are micro-noise.

## Examples

**Example 1 — bullish VI inside displacement:**
- M15: candle n-1 close 1.0852, high 1.0855.
- Candle n open 1.0858, low 1.0856.
- Body gap = 6 pips at [1.0852, 1.0858]; wicks overlap [1.0855, 1.0856].
- → bullish VI, not a 3-candle FVG. Treat as a softer support reference inside ongoing bullish displacement.

## Common Mistakes

- **Calling VI an FVG.** They're different patterns; VIs have overlapping wicks.
- **Tiny gaps from feed noise.** Sub-tick VIs are not real; filter by ATR.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [imbalance-vs-fvg](../26-imbalance/imbalance-vs-fvg.md), [volume-imbalance-detail](../26-imbalance/volume-imbalance-detail.md), [imbalance-definition](../26-imbalance/imbalance-definition.md), [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-REINFORCED` — "Month 04 — ICT Fair Value Gaps FVG", `FgacYSN9QEo` (Dec 2016). Close-to-open body gap at [12:26–12:41]; wick-through-body / bodies-fill-the-gap at [13:19–13:33].
- `ICT-2016-LIQUIDITY-VOIDS` — "Month 04 — Liquidity Voids", `HTQgH11W37o` (Dec 2016). "That little space right there where the bodies don't close in … this is a gap" [10:34–10:43]; named a **common gap** at [12:37]; body-only fill is sufficient at [13:03].
- `ICT-2022-MENTORSHIP-OVERVIEW` — retained for the 2022 refinement, which is where the *name* "volume imbalance" originates.
