# Weekly Bias

**Category:** 25-htf-bias
**Aliases:** W bias, weekly direction
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** htf-bias, weekly

## Definition

Weekly bias is the directional read from the **weekly chart**. ICT teaches weekly bias as the **primary HTF anchor for swing traders** and a major confluence input for day-traders. Weekly structure changes more slowly than daily but more quickly than monthly; it's the practical "where is the algorithm headed this week" read.

## Formal Criteria

Weekly bias is bullish when:

- Most recent weekly external BOS was up.
- Price below weekly EQ.
- Weekly DOL is upside (PWH-area BSL ahead).

Bearish when symmetric. Neutral when conflicting / at EQ.

Common time-of-week tendency: PWL (previous week low) often gets swept early in the week (Mon/Tue) before the weekly direction asserts (Wed-Thu distribution).

## Formula / Math

```
weekly_dealing_range = [LTL_w, LTH_w]
w_eq = (LTL_w + LTH_w) / 2

weekly_bias :=
  "bullish" if last_w_external == bullish AND price < w_eq AND upside_DOL
  "bearish" if last_w_external == bearish AND price > w_eq AND downside_DOL
  "neutral" otherwise
```

## Machine-Readable

```json
{
  "id": "weekly-bias",
  "category": "25-htf-bias",
  "aliases": ["W-bias", "weekly-direction"],
  "criteria": [
    {"id": "c1", "expr": "uses_weekly_external_structure"},
    {"id": "c2", "expr": "considers_price_vs_weekly_eq"},
    {"id": "c3", "expr": "considers_weekly_DOL"}
  ],
  "timeframes": ["W","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","monthly-bias","daily-bias","bias-confluence","top-down-analysis","htf-amd","dealing-range"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Weekly chart bullish bias example:

   PWH ─────────── (last week's high; targeting)
       /\
      /  \  ← this week's price drift below PWH
   ──────── W_EQ
            (price retraced to discount)
   PWL ──────── (last week's low; recently swept = manipulation phase done)
```

## Timeframes

W / D.

## Examples

**Example 1 — Tue weekly-bias confirmation:**
- W LTH 1.1000, W LTL 1.0750. W_EQ = 1.0875.
- Mon: tight range above 1.0820 (Q1 / accumulation).
- Tue: M15 wicks 1.0815 (PWL SSL swept = manipulation), reverses up.
- → weekly bias bullish; Wed onwards expect distribution toward W LTH.

## Common Mistakes

- **Late-week bias change.** A weekly CHoCH near Friday may reverse on Sunday/Monday open; wait for a fresh week's confirmation.
- **Day-trading weekly bias only.** Weekly is backdrop; daily-and-below structures the actual entries.

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [monthly-bias](monthly-bias.md), [daily-bias](daily-bias.md), [bias-confluence](bias-confluence.md), [top-down-analysis](top-down-analysis.md), [htf-amd](../12-power-of-three/htf-amd.md), [dealing-range](../05-pd-arrays/dealing-range.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
