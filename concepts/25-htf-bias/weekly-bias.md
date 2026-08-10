# Weekly Bias

**Category:** 25-htf-bias
**Aliases:** W bias, weekly direction
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-INTERMEDIATE-TOP-DOWN, ICT-2022-MENTORSHIP-OVERVIEW
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

**ICT's own weekly routine** (`ICT-2017-INTERMEDIATE-TOP-DOWN`) — tier 2 of [top-down-analysis](top-down-analysis.md), run at the start of each new week. The three inputs that opened the monthly tier are **replaced, not repeated**: "there's a couple things missing here that we saw in the monthly that is not in the weekly portion… we had three different things that started off the monthly" (04:38).

1. **Relative strength**, run first — and deliberately so, as the fallback when the monthly tier was inconclusive: "the reason why I start with relative strength is I may not have a clear picture from the monthly" (02:52). Markets that **lead in strength fail to make lower lows**; markets that **lead in weakness fail to make higher highs** — "I determine what markets **lead in strength** by failing to make lower lows and **lead in weakness** by failing to make higher highs" (08:23). Both are leadership: one long-side, one short-side. *Leaders vs laggards* is a separate axis run on top — "I look for leadership and laggards, so I want to know **what the strongest is and the weakest**" (09:23). Equities are screened through IBD's **top 30 industry groups** (08:50). The mechanic itself is defined in full on [relative-strength-analysis](../03-order-flow/relative-strength-analysis.md).
2. **Commitment of traders** — commercials at a **12-month or 6-month extreme** in net holdings, additionally sorted for **2-year and 4-year extremes** (10:28). The boundary is the recentred line, not the printed zero: take the commercial net line's 12-month high and low and "split that in half — above it would be buying and below it would be selling" (19:05).
3. **Market sentiment**, from three readings that must agree before it counts:
   - **Headlines faded** — IBD, Barron's, the Wall Street Journal, Bloomberg; ICT looks for "real big descriptive adjectives" and rising story frequency, not the news itself (12:02–12:58).
   - **Retail forums**, read for the consensus position (13:04).
   - **Williams %R on the weekly**, at period **20, 14 or 10** — pick whichever "most accurately depict[s] or overlaps with the previous important highs and lows" on that chart (13:52). **Ideal long at the 80 reading, ideal short at 20** (40:01). ICT calibrates to **14** in the worked example: "14 periods in my opinion would have been optimal, it gives you a little bit more time filter" (41:17).
   - The point of all three is opposition: "ideally you want to be diametrically opposed to that in an alignment with what smart money is doing" (05:33).
4. Then the shared spine, with **institutional order flow** folded into the structure step — in a bull, "down-close candles supporting price and up-close candles being broken"; mirrored in a bear (06:39).
5. Output the bias, then **transpose it onto the daily chart** (08:02).

**Timeframe hygiene:** time-of-day analysis is excluded at this tier by design — "it's not required on these timeframes, monthly and weekly" (46:44).

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
    {"id": "c3", "expr": "considers_weekly_DOL"},
    {"id": "c4", "expr": "tier-2 input order == [relative_strength, COT, sentiment] then shared spine"},
    {"id": "c5", "expr": "tier-1 inputs (seasonal, quarterly_shift, rate_differentials) are NOT repeated here"},
    {"id": "c6", "expr": "leads_in_strength := fails to make lower low; leads_in_weakness := fails to make higher high (BOTH are leadership, not leader-vs-laggard)"},
    {"id": "c6b", "expr": "leaders_vs_laggards is a separate ranking axis: strongest vs weakest of the group"},
    {"id": "c7", "expr": "COT extremes checked at 12m, 6m, 2y and 4y"},
    {"id": "c8", "expr": "sentiment := faded_headlines AND forums AND weekly Williams %R in {20,14,10}"},
    {"id": "c9", "expr": "percent_R ideal_long == 80, ideal_short == 20; period 14 preferred"},
    {"id": "c10", "expr": "time_of_day analysis excluded at W and MN"}
  ],
  "timeframes": ["W","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","monthly-bias","daily-bias","bias-confluence","top-down-analysis","htf-amd","dealing-range","commitment-of-traders","relative-strength-analysis","sentiment-effect","institutional-order-flow","pd-array-matrix"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2017-INTERMEDIATE-TOP-DOWN","ICT-2022-MENTORSHIP-OVERVIEW"]
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
- **Carrying the monthly inputs down.** Seasonals, quarterly shifts and rate differentials are tier-1 only; substituting them for relative strength / COT / sentiment skips the entire weekly input set.
- **Fitting the %R period to the current swing.** The period is calibrated against the chart's **past** important highs and lows, then left alone. ICT names the temptation as he does it — "this does look like form fitting, I know, but you'll see what I'm doing here" (13:34) — and rejects the shortest setting because "the smallest one will always generally give you a good reading regardless, and that sometimes is a little too sugar-coated" (40:59).
- **Treating one sentiment reading as sentiment.** Headlines, forums and the oscillator are three inputs; the signal is their agreement.
- **Reading the printed COT zero line.** The weekly tier uses the recentred 12-month midpoint. See [commitment-of-traders](../03-order-flow/commitment-of-traders.md).

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [monthly-bias](monthly-bias.md), [daily-bias](daily-bias.md), [bias-confluence](bias-confluence.md), [top-down-analysis](top-down-analysis.md), [htf-amd](../12-power-of-three/htf-amd.md), [dealing-range](../05-pd-arrays/dealing-range.md).
- [commitment-of-traders](../03-order-flow/commitment-of-traders.md) — tier-2 input 2, including the recentred zero line.
- [relative-strength-analysis](../03-order-flow/relative-strength-analysis.md) — tier-2 input 1, defined in full.
- [sentiment-effect](../31-models/sentiment-effect.md) — the intraday counterpart of tier-2 input 3.
- [institutional-order-flow](../03-order-flow/institutional-order-flow.md) — the up/down-close-candle read folded into the structure step.
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md) — where the weekly key levels are calibrated.

## Citations

- `ICT-2017-INTERMEDIATE-TOP-DOWN` (00:22) "this teaching is ICT intermediate term top-down analysis, weekly to daily"; (02:46–02:52) relative strength first, "because I may not have a clear picture from the monthly"; (03:13–04:25) COT then sentiment; (05:33) "ideally you want to be diametrically opposed to that in an alignment with what smart money is doing"; (04:38–05:13) the three monthly inputs named as absent from this tier; (06:39–06:55) institutional order flow on down- and up-close candles; (08:02–08:20) "I come to a weekly bias… and transpose that to the daily chart"; (08:23) "I determine what markets **lead in strength** by failing to make lower lows and **lead in weakness** by failing to make higher highs" — both leadership, not leader-vs-laggard; (08:50) IBD top 30 industry groups; (09:23) "I look for leadership and laggards, so I want to know what the strongest is and the weakest" — the separate ranking axis; (10:28–10:58) commercials at 12-month, 6-month, 2-year and 4-year extremes; (12:02–13:11) headlines faded, "real big descriptive adjectives", forums haunted for retail thinking; (13:34–14:24) "I use a percent R on a weekly chart in periods of 20, 14, period, and 10… I look for which one is the most accurately depicting or overlaps with the previous important highs and lows"; (19:05–19:42) the 12-month high/low split in half replacing the zero line; (40:01–41:23) ideal long at 80 and short at 20, the 10-period rejected as "too sugar-coated", 14 optimal; (46:44) time-of-day analysis not required on monthly and weekly.
- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW` — the general weekly-context restatement in later years.
