# Bias Invalidation

**Category:** 25-htf-bias
**Aliases:** bias-flip, bias-invalidated, bias change
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** htf-bias, invalidation, risk

## Definition

Bias invalidation is the structural event that **forces a bias flip** at a given TF — typically a CHoCH/MSS that breaks the prior trend's structure. ICT teaches that bias should be re-read and potentially flipped only when concrete invalidation signals print: a single counter-trend candle isn't enough; an external structure break with displacement is. Without explicit invalidation, the bias from prior analysis stays.

## Formal Criteria

A bias is invalidated at a given TF when:

- A **CHoCH or MSS** prints in the opposite direction (close beyond the trend's recent swing pivot with displacement).
- An **external BOS** in the opposite direction (close beyond the dealing range bound).
- Crucially, on the **same TF** being analyzed (a daily CHoCH doesn't invalidate weekly bias).

Levels at which invalidation matters most: D, W, MN. H4/H1 invalidations are intraday-only.

## Formula / Math

```
bias_invalidated(tf, direction):
    if direction == "bullish":
        bearish_CHoCH_or_MSS_at_tf == true OR
        bearish_external_BOS_at_tf == true
    if direction == "bearish":
        bullish_CHoCH_or_MSS_at_tf == true OR
        bullish_external_BOS_at_tf == true
```

## Machine-Readable

```json
{
  "id": "bias-invalidation",
  "category": "25-htf-bias",
  "aliases": ["bias-flip", "bias-invalidated"],
  "criteria": [
    {"id": "c1", "expr": "structural_break_in_opposite_direction_at_tf"},
    {"id": "c2", "expr": "either_CHoCH/MSS_or_external_BOS"},
    {"id": "c3", "expr": "must_occur_at_the_same_TF_being_analyzed"}
  ],
  "timeframes": ["H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","bias-confluence","monthly-bias","weekly-bias","daily-bias","mss","choch-bullish","choch-bearish","external-structure"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   daily bullish bias invalidation:

   prior bullish leg: ▲▲▲▲
                       \
                        \  pullback
                         \
                          ─── prior daily swing low (key level)
                            ↓
                            ▼  CLOSE BELOW the swing low with displacement
                            ▼  → daily CHoCH-bear
                            ▼     daily bias INVALIDATED bullish
                                  → bias flips bearish until further notice
```

## Timeframes

Same as bias being invalidated: H1 → MN.

## Examples

**Example 1 — daily bias invalidation:**
- Daily bullish for 2 weeks; pullback approaches recent D swing low at 1.0820.
- D candle closes 1.0810 (below 1.0820) with bearish displacement and bearish FVG.
- → daily bias invalidated bullish; flips bearish.
- Action: stop taking long setups; re-evaluate weekly/monthly to see if multi-TF bias is shifting.

## Common Mistakes

- **Calling intraday invalidations "HTF flips."** A H1 CHoCH doesn't flip daily bias.
- **Wick-only invalidation.** Use closes, not wicks. Wicks can be sweeps or stop runs without changing structure.
- **Refusing to flip.** Holding a stale bias against confirmed structural shift = trading against the algorithm.

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [bias-confluence](bias-confluence.md), [monthly-bias](monthly-bias.md), [weekly-bias](weekly-bias.md), [daily-bias](daily-bias.md).
- [mss](../01-market-structure/mss.md), [choch-bullish](../01-market-structure/choch-bullish.md), [choch-bearish](../01-market-structure/choch-bearish.md), [external-structure](../01-market-structure/external-structure.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
