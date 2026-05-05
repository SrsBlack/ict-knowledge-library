# Inversion FVG (IFVG)

**Category:** 06-fair-value-gaps
**Aliases:** IFVG, inverted FVG, flipped FVG, polarity-flip FVG
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2025
**Source IDs:** ICT-2018-IFVG, ICT-2024-IFVG-FORMALIZED
**Tags:** fvg, ifvg, inversion, polarity-flip

## Definition

An **Inversion FVG** is a previously-formed FVG that has been **traded through** (price violated the far edge with displacement) and now **flips polarity**: a bullish FVG that was traded through and broken becomes a bearish IFVG (now functions as resistance), and vice versa. The IFVG concept was introduced in 2018 and formalized in 2024 as a standard ICT structural reference. The principle: an FVG that fails to act as support/resistance in its original polarity often serves the opposite role on the retest.

## Formal Criteria

A bullish FVG flips to bearish IFVG when:

- The original bullish FVG (`L_{n+1} > H_{n-1}`) was formed.
- A later candle closes **below** the original FVG's low (`H_{n-1}` of the original — the lower bound of the bullish FVG zone).
- The displacement that broke the FVG is decisive (not a wick + recovery).
- Price subsequently retests the original FVG zone from below.
- On retest, the original bullish FVG zone now acts as **resistance** (bearish IFVG).

Bearish-to-bullish IFVG: symmetric.

## Formula / Math

```
# Original bullish FVG, low = H_{n-1}_orig, high = L_{n+1}_orig
# Inversion trigger:
inversion_break := close_t < H_{n-1}_orig    # for bull→bear inversion

# After inversion, retest from below:
ifvg_act_as_resistance := high_retest reaches L_{n+1}_orig (FVG high)
                           AND price rejects with displacement down
```

## Machine-Readable

```json
{
  "id": "inversion-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["IFVG", "inverted-FVG", "flipped-FVG"],
  "criteria": [
    {"id": "c1", "expr": "original_FVG_was_traded_through == true"},
    {"id": "c2", "expr": "close_breaks_far_edge_with_displacement == true"},
    {"id": "c3", "expr": "retest_acts_with_opposite_polarity == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2025",
  "related": ["fair-value-gap","bullish-fvg","bearish-fvg","fvg-mitigation","breaker-block","consequent-encroachment"],
  "sources": ["ICT-2018-IFVG","ICT-2024-IFVG-FORMALIZED"]
}
```

## Visual Pattern

```
   bullish FVG → bearish IFVG transformation:

   Step 1: Original bullish FVG forms
          ▲
          █  ← n+1
        ▲
        █  ← n
        █
       ▲
       █  ← n-1
   Step 2: Later, price breaks BELOW the FVG with displacement
          (FVG fails as support)
   Step 3: Price retraces UP into the original FVG zone
          → zone now acts as RESISTANCE (bearish IFVG)
```

## Timeframes

M5+ practical. Lower TFs noise-dominate IFVG identification.

## Examples

**Example 1 — bullish→bearish IFVG:**
- M15 bullish FVG forms at 1.0860–1.0865 (CE 1.08625).
- Three hours later, M15 closes at 1.0855 (below 1.0860 with bearish displacement).
- Original FVG is now a candidate IFVG.
- Price rallies, retests up to 1.0863 inside the original FVG zone.
- Bearish reaction with displacement down → confirmed bearish IFVG.
- Short entry on rejection; SL above 1.0866 (above original FVG high + buffer).

## Common Mistakes

- **Calling every wick-through an inversion.** Inversion requires a CLOSE beyond the FVG's far edge with displacement, not just a wick.
- **Confusing IFVG with breaker.** Breakers are based on swing high/low breaks; IFVG is based on FVG-zone breaks. They're related but distinct.
- **Missing retest-with-displacement.** Just touching the IFVG zone isn't enough; require post-touch displacement confirming the new polarity.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md).
- [fvg-mitigation](fvg-mitigation.md), [consequent-encroachment](consequent-encroachment.md).
- [breaker-block](../08-breaker-blocks/breaker-block.md) — analogous polarity-flip on swings.

## Citations

- `ICT-2018-IFVG` — IFVG concept introduced.
- `ICT-2024-IFVG-FORMALIZED` — formal definition + standardized rules.
