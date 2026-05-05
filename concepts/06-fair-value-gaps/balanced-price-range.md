# Balanced Price Range (BPR)

**Category:** 06-fair-value-gaps
**Aliases:** BPR, balanced range, mirror FVG zone, opposing FVG overlap
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fvg, bpr, balance, ranging

## Definition

A Balanced Price Range is a price zone where a **bullish FVG and a bearish FVG overlap or share the same price region** — typically because both formed during a recent two-sided trade in the same area. ICT teaches BPR as a **decision zone**: price entering BPR can react in either direction with significant probability. Trading inside a BPR without HTF bias support is low-conviction; well-defined HTF bias is required to pick a side. BPRs often form at session highs/lows and during consolidation phases.

## Formal Criteria

A BPR exists when:

- A bullish FVG zone `[fvg_bull_low, fvg_bull_high]` and a bearish FVG zone `[fvg_bear_low, fvg_bear_high]` overlap.
- Overlap region = intersection of the two ranges.
- Both FVGs are unmitigated.
- Typically forms near range bounds during contraction / consolidation.

## Formula / Math

```
overlap = max(fvg_bull_low, fvg_bear_low), min(fvg_bull_high, fvg_bear_high)
is_bpr = overlap[0] < overlap[1]      # non-empty intersection
```

## Machine-Readable

```json
{
  "id": "balanced-price-range",
  "category": "06-fair-value-gaps",
  "aliases": ["BPR", "balanced-range", "mirror-FVG-zone"],
  "criteria": [
    {"id": "c1", "expr": "bullish_FVG and bearish_FVG share overlapping price region"},
    {"id": "c2", "expr": "both_FVGs_unmitigated == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["fair-value-gap","bullish-fvg","bearish-fvg","range-contraction","htf-bias-framework","pd-array-confluence"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   ▒▒▒▒  ← bearish FVG zone
   ▒▓▒▒
   ▓▓▓▓  ← BPR overlap (decision zone)
   ░▓░░
   ░░░░  ← bullish FVG zone
```

## Timeframes

M15+. M5 BPRs are too noisy.

## Examples

**Example 1 — H1 BPR at session high:**
- H1 bearish FVG forms at 1.0945–1.0955 after a sweep of PDH.
- Hours later, an H1 bullish FVG forms at 1.0942–1.0952 during the next push down's reversal.
- Overlap: [1.0945, 1.0952].
- HTF bearish → BPR likely resolves bearish on retest; short setup at the bearish-FVG side of BPR.

## Common Mistakes

- **Trading BPR without HTF bias.** Both directions can fire from BPR; HTF bias is the tiebreaker.
- **Calling overlapping wicks "BPR."** Both ranges must be valid 3-candle FVGs; wick-overlap alone doesn't qualify.
- **Stale BPR.** Once one of the FVGs is mitigated, the BPR character is gone — only the surviving FVG matters.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md).
- [range-contraction](../01-market-structure/range-contraction.md) — BPRs commonly form during contraction.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [pd-array-confluence](../05-pd-arrays/pd-array-confluence.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
