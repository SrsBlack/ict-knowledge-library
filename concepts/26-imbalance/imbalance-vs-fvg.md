# Imbalance vs FVG — Disambiguation

**Category:** 26-imbalance
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** imbalance, fvg, disambiguation, terminology

## Definition

This page resolves a common terminology confusion: when ICT (and the ICT community) says **"imbalance"** vs **"Fair Value Gap (FVG)"**.

**Short version:** every FVG is an imbalance, but not every imbalance is an FVG.

- **Imbalance** = umbrella term for any region where two-sided trade didn't happen (FVGs, volume imbalances, liquidity voids — all forms of imbalance).
- **FVG** = a specific imbalance pattern: a 3-candle wick-based gap where the middle candle's range fails to overlap with the candles before and after.

Use "FVG" when you mean the specific 3-candle pattern. Use "imbalance" when you mean the broader phenomenon (or when the specific form doesn't matter).

## Formal Criteria

### Imbalance (umbrella)

- Any region of price where consecutive candles' ranges do not overlap.
- Includes: FVGs, volume imbalances, multi-candle voids.

### Fair Value Gap (specific)

- 3 candles with `L_{n+1} > H_{n-1}` (bullish) or `H_{n+1} < L_{n-1}` (bearish).
- The middle candle (n) is the displacement candle.
- The imbalance is the price region between H_{n-1} and L_{n+1} (or L_{n-1} and H_{n+1}).
- Wick-based (not body-based).

### The Containment Relationship

```
all FVGs ⊂ all imbalances
```

A volume imbalance (body-vs-body gap that doesn't satisfy the wick rule) IS an imbalance but is NOT an FVG.

## Formula / Math

```
is_imbalance(region) := consecutive_candle_ranges_dont_overlap(region)

is_FVG(n)            := is_imbalance(n)
                         AND L_{n+1} > H_{n-1}    # bullish form
                            OR H_{n+1} < L_{n-1}  # bearish form
                         AND involves_3_candles == true
```

## Machine-Readable

```json
{
  "id": "imbalance-vs-fvg",
  "category": "26-imbalance",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "every_fvg_is_imbalance == true"},
    {"id": "c2", "expr": "fvg_requires_3_candle_wick_pattern == true"},
    {"id": "c3", "expr": "imbalance_is_broader_umbrella == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["imbalance-definition","inefficiency","fair-value-gap","volume-imbalance-detail","liquidity-void"],
  "sources": ["ICT-2016-FVG-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   FVG (specific 3-candle pattern):           Volume imbalance (NOT an FVG):

        ▲                                              ▲
        █  ← n+1 (low > n-1 high)                      █  ← body opens above
        █                                              █     prior body close
      ▲                                                       (no wick gap)
      █  ← n (displacement)                          ▲
      █                                              █  ← prior body
    ▲
    █  ← n-1 (high)
   wick gap = FVG                              body gap = volume imbalance
                                                (wicks may overlap; not an FVG)
```

## Timeframes

All TFs.

## Examples

**Example A — FVG and imbalance both apply:**
- M5: H_{n-1}=1.0860, L_{n+1}=1.0865.
- → 5-pip bullish FVG (specific) AND 5-pip imbalance (umbrella). Both terms valid.

**Example B — imbalance but NOT FVG:**
- M5: candle n-1 closes at 1.0855, candle n opens at 1.0860 (5-pip body gap), but wicks of n-1 (high 1.0858) and n (low 1.0856) overlap.
- → Volume imbalance (body gap), NOT an FVG (wicks overlap so the 3-candle FVG criterion fails). Calling this "FVG" is incorrect; calling it "imbalance" is correct.

## Common Mistakes

- **Calling every body gap an FVG.** Body-only gaps without the wick-non-overlap rule are volume imbalances, not FVGs.
- **Treating the terms as interchangeable.** They overlap but FVG is the stricter case.
- **Insisting on FVGs for entries.** Volume imbalances and broader voids also qualify as ICT entry references at lower conviction.

## Related Concepts

- [imbalance-definition](imbalance-definition.md), [inefficiency](inefficiency.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [volume-imbalance-detail](volume-imbalance-detail.md), [liquidity-void](../02-liquidity/liquidity-void.md).

## Citations

- `ICT-2016-FVG-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
