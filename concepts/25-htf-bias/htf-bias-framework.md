# HTF Bias Framework

**Category:** 25-htf-bias
**Aliases:** HTF bias, bias framework, top-down bias
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** htf-bias, framework, foundational

## Definition

The HTF Bias Framework is ICT's **directional decision system** for live trading: a structured, top-down process that produces a single directional bias (bullish / bearish / neutral) by reading market structure and PD-array context across the monthly / weekly / daily / H4 / H1 timeframe stack. The bias drives setup-side selection — long setups only on bullish bias, short setups on bearish, no-trade on neutral. Without a clear HTF bias, ICT teaches that no entry is taken: bias is the prerequisite, not the consequence, of setup analysis.

## Formal Criteria

The standard top-down read:

1. **Monthly:** identify dealing range (LTH/LTL), current side of EQ, most recent monthly external BOS direction.
2. **Weekly:** same checks; most recent CHoCH/MSS direction.
3. **Daily:** same; most recent BOS/CHoCH; current draw on liquidity.
4. **H4:** confirms or refines the daily read; identifies the active HTF PD array.
5. **H1:** entry-bias confirmation.

Bias output:

- **Bullish:** majority of TFs in bullish structure with clear upside DOL.
- **Bearish:** majority in bearish structure with clear downside DOL.
- **Neutral / conflicting:** TFs disagree, OR price sits at EQ of dealing range, OR external structure in transition.

## Formula / Math

```
htf_bias_inputs = {
  monthly: {bias, dealing_range, side_of_eq, most_recent_external_break},
  weekly:  {same fields},
  daily:   {same fields},
  h4:      {same fields},
  h1:      {same fields},
}

htf_bias_output := majority_vote(monthly, weekly, daily, h4, h1)
                    weighted_by_TF (higher TFs heavier)

# When monthly + weekly + daily all agree: high-conviction bias
# When daily disagrees with monthly+weekly: bias-flip in progress; reduce conviction
# When all 5 disagree: neutral; no trade
```

## Machine-Readable

```json
{
  "id": "htf-bias-framework",
  "category": "25-htf-bias",
  "aliases": ["HTF-bias", "bias-framework", "top-down-bias"],
  "criteria": [
    {"id": "c1", "expr": "top_down_read_across_MN_W_D_H4_H1"},
    {"id": "c2", "expr": "output: bullish | bearish | neutral"},
    {"id": "c3", "expr": "higher_TFs_weighted_more_heavily"}
  ],
  "timeframes": ["H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["monthly-bias","weekly-bias","daily-bias","bias-confluence","bias-invalidation","top-down-analysis","htf-pd-array-hierarchy","draw-on-liquidity","dealing-range"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   top-down bias read:

   Monthly  ──── bullish (last external BOS up; price in discount)
   Weekly   ──── bullish (last CHoCH up; recent BOS continuation)
   Daily    ──── bullish (price below EQ; targeting weekly BSL above)
   H4       ──── confirms (most recent BOS up)
   H1       ──── confirms

   → high-conviction bullish HTF bias
```

## Timeframes

H1 → MN. Daily and weekly do most of the work; H4/H1 refine.

## Examples

**Example 1 — clean bullish bias:**
- MN: dealing range 1.0500–1.1200; current price 1.0850 = discount; last external BOS up.
- W: range 1.0750–1.1000; current 1.0850 = mid-discount; last CHoCH up.
- D: range 1.0820–1.0950; current 1.0850; last D BOS up; targeting W high 1.1000.
- H4 / H1: confirm.
- → bullish bias. All long setups valid; shorts disfavored.

## Common Mistakes

- **Reading bias from a single TF.** Single-TF bias misses HTF structure and produces frequent reversals.
- **Bias flipping on every CHoCH.** Day-to-day CHoCH happens often; treat HTF bias changes as significant only when MULTIPLE TFs flip.
- **Force-fitting neutral into directional.** When TFs conflict, the correct call is neutral / no-trade — don't pick a side just to be active.

## Related Concepts

- [monthly-bias](monthly-bias.md), [weekly-bias](weekly-bias.md), [daily-bias](daily-bias.md), [bias-confluence](bias-confluence.md), [bias-invalidation](bias-invalidation.md), [top-down-analysis](top-down-analysis.md).
- [htf-pd-array-hierarchy](../05-pd-arrays/htf-pd-array-hierarchy.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md), [dealing-range](../05-pd-arrays/dealing-range.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
