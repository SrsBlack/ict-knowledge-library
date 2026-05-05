# Monthly Bias

**Category:** 25-htf-bias
**Aliases:** MN bias, monthly direction
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** htf-bias, monthly

## Definition

Monthly bias is the directional read derived from the **monthly chart** — the broadest tradeable HTF in standard ICT analysis. Monthly bias sets the structural backdrop for every lower-TF bias read; it changes slowly and rarely, but when it flips, all lower-TF biases should be re-evaluated. Most day-traders defer to weekly / daily bias for execution but reference monthly for context.

## Formal Criteria

Monthly bias is bullish when:

- Most recent monthly external BOS was up.
- Current price below monthly EQ (in monthly discount).
- Monthly draw on liquidity is upside (BSL ahead).

Monthly bias is bearish when symmetric down-side conditions hold.

Monthly is **neutral** when at EQ ± buffer, or external structure in transition.

## Formula / Math

```
mn_dealing_range = [LTL_mn, LTH_mn]
mn_eq = (LTL_mn + LTH_mn) / 2

mn_bias :=
  "bullish" if last_external_break == bullish AND price < mn_eq AND DOL_upside_present
  "bearish" if last_external_break == bearish AND price > mn_eq AND DOL_downside_present
  "neutral" otherwise
```

## Machine-Readable

```json
{
  "id": "monthly-bias",
  "category": "25-htf-bias",
  "aliases": ["MN-bias", "monthly-direction"],
  "criteria": [
    {"id": "c1", "expr": "uses_monthly_external_structure"},
    {"id": "c2", "expr": "considers_current_price_vs_monthly_eq"},
    {"id": "c3", "expr": "considers_monthly_DOL"}
  ],
  "timeframes": ["MN","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","weekly-bias","daily-bias","bias-confluence","top-down-analysis","dealing-range"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Monthly chart:

   LTH_mn ─────────  monthly LTH (recently broken UP for bullish bias)
                /\
               /  \
   ──────────── MN_EQ
              ↓
              price (below EQ → discount)
   LTL_mn ─────────  prior monthly LTL
```

## Timeframes

MN — analyze on monthly candles.

## Examples

**Example 1 — bullish monthly bias:**
- Monthly LTH 1.1200 (broken up 3 months ago).
- Monthly LTL 1.0500 (4 months ago).
- MN_EQ = 1.0850; current price 1.0820 = discount.
- Upside DOL: monthly BSL above 1.1200 (already taken; new ATH BSL ahead).
- → bullish monthly bias.

## Common Mistakes

- **Reacting to single monthly candle.** Monthly bias changes slowly; one mixed monthly candle isn't a flip.
- **Ignoring monthly when day-trading.** Monthly bias provides backdrop conviction; setups against monthly are lower-probability even when daily aligns.

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [weekly-bias](weekly-bias.md), [daily-bias](daily-bias.md), [bias-confluence](bias-confluence.md), [top-down-analysis](top-down-analysis.md), [dealing-range](../05-pd-arrays/dealing-range.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
