# Bias Confluence

**Category:** 25-htf-bias
**Aliases:** multi-TF bias, bias agreement, multi-TF alignment
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** htf-bias, confluence, multi-tf

## Definition

Bias confluence is the **alignment of bias direction across multiple TFs**. ICT teaches that bias confluence is a primary conviction modifier: when monthly + weekly + daily all agree, intraday setups in that direction are highest-conviction; when daily disagrees with monthly+weekly, conviction is reduced and signals a possible bias-flip in progress.

## Formal Criteria

The standard 3-TF confluence read:

| MN | W | D | Conviction |
|---|---|---|---|
| bull | bull | bull | **A+ confluence**: highest-conviction longs |
| bull | bull | neutral | medium-high: longs preferred, wait for D bullish trigger |
| bull | bull | bear | mixed: D bias-flip in progress; reduce size |
| bull | bear | bear | weak bull MN, strong bear W+D: shorts more likely |
| (mirror cases for bearish) | | | |

5-TF expansion adds H4 and H1, weighted lower than D/W/MN.

## Formula / Math

```
confluence_score = sum_weighted([
  monthly_bias_direction * 5,
  weekly_bias_direction  * 4,
  daily_bias_direction   * 3,
  h4_bias_direction      * 2,
  h1_bias_direction      * 1,
])

# Bias direction: bullish=+1, bearish=-1, neutral=0
# Score range: [-15, +15]
# A+ confluence: |score| >= 12
# Medium: |score| in [6, 11]
# Low / conflict: |score| <= 5
```

## Machine-Readable

```json
{
  "id": "bias-confluence",
  "category": "25-htf-bias",
  "aliases": ["multi-tf-bias", "bias-agreement"],
  "criteria": [
    {"id": "c1", "expr": "alignment_of_bias_across_TFs"},
    {"id": "c2", "expr": "higher_TFs_weighted_more_heavily"},
    {"id": "c3", "expr": "score_drives_setup_conviction"}
  ],
  "timeframes": ["H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","monthly-bias","weekly-bias","daily-bias","bias-invalidation","top-down-analysis","pd-array-confluence"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bias confluence ladder (bullish example):

   MN   ──── bullish ✓
   W    ──── bullish ✓
   D    ──── bullish ✓
   H4   ──── bullish ✓
   H1   ──── bullish ✓

   → all 5 TFs aligned: A+ confluence; full size on long setups.
```

## Timeframes

H1 → MN.

## Examples

**Example 1 — A+ confluence:**
- MN bullish (+5), W bullish (+4), D bullish (+3), H4 bullish (+2), H1 bullish (+1).
- score = +15. A+ confluence.
- Long setups: full size, expect distribution-day character.

**Example 2 — bias-flip in progress:**
- MN bullish (+5), W bullish (+4), D bearish (-3), H4 bearish (-2), H1 bearish (-1).
- score = +3. Weak / conflicting.
- Daily/H4/H1 transitioning bearish; reduce or skip.

## Common Mistakes

- **Treating any confluence as A+.** Score 6 ≠ score 14; calibrate position size to confluence strength.
- **Ignoring HTF veto.** A mixed-confluence setup against monthly bias should reduce, not maintain, full conviction.
- **Forcing 5-TF reads.** When a TF is genuinely neutral, count it as 0; don't force a direction.

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [monthly-bias](monthly-bias.md), [weekly-bias](weekly-bias.md), [daily-bias](daily-bias.md), [bias-invalidation](bias-invalidation.md), [top-down-analysis](top-down-analysis.md), [pd-array-confluence](../05-pd-arrays/pd-array-confluence.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
