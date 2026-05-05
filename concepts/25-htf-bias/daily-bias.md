# Daily Bias

**Category:** 25-htf-bias
**Aliases:** D bias, daily direction, daily setup bias
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** htf-bias, daily, foundational

## Definition

Daily bias is the directional read from the **daily chart** — the primary bias-setting TF for ICT day-traders. While weekly and monthly provide context, daily bias is what most intraday setups align against. It changes faster than weekly but slower than H4, and a fresh daily CHoCH/MSS frequently signals the start of a new multi-day swing.

## Formal Criteria

Daily bias is bullish when:

- Most recent daily external BOS was up OR a daily CHoCH-up has just printed.
- Current price below daily EQ (in daily discount).
- Daily DOL is upside (PDH/PWH ahead).

Bearish when symmetric. Neutral when conflicting.

Common signals:

- True Day Open (00:00 NY) above prior day's range = mild bullish lean.
- Daily candle closed strongly directional yesterday = momentum continuation expected today.
- Daily wicked one bound = sweep + reversal possible.

## Formula / Math

```
daily_dealing_range = [LTL_d, LTH_d]
d_eq = (LTL_d + LTH_d) / 2

daily_bias :=
  "bullish" if last_daily_external == bullish AND price < d_eq AND upside_DOL
  "bearish" if last_daily_external == bearish AND price > d_eq AND downside_DOL
  "neutral" otherwise
```

## Machine-Readable

```json
{
  "id": "daily-bias",
  "category": "25-htf-bias",
  "aliases": ["D-bias", "daily-direction"],
  "criteria": [
    {"id": "c1", "expr": "uses_daily_external_structure"},
    {"id": "c2", "expr": "considers_price_vs_daily_eq"},
    {"id": "c3", "expr": "considers_PDH_PDL_DOL"}
  ],
  "timeframes": ["D","H4","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["htf-bias-framework","monthly-bias","weekly-bias","bias-confluence","top-down-analysis","true-day-open","time-of-day-pivots"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Daily chart bullish bias:

   PDH ───────────  (yesterday's high — potential BSL target today)
       /\
      /  \   today's price near discount of D range
   ──────── D_EQ
            \
   PDL ────── (yesterday's low — already swept = manipulation)
```

## Timeframes

D / H4 / H1.

## Examples

**Example 1 — bullish daily bias:**
- D LTH 1.0950 (yesterday); D LTL 1.0820 (3 days ago).
- D_EQ = 1.0885.
- Today's price 1.0855 = discount.
- Today's TDO 1.0860 above PDH 1.0860? → mild bullish lean.
- DOL: PDH BSL above 1.0950 (today's target).
- → bullish daily bias; intraday setups long-aligned.

## Common Mistakes

- **Stale daily bias.** Once today's session confirms a structural shift on D, refresh the bias.
- **Single-candle daily reads.** A daily CHoCH on a thin-volume day may not stick — wait for confirmation in the next 1-2 sessions.
- **Conflict ignorance.** When weekly and daily disagree, the conflict itself is the signal — reduce conviction or wait.

## Related Concepts

- [htf-bias-framework](htf-bias-framework.md), [monthly-bias](monthly-bias.md), [weekly-bias](weekly-bias.md), [bias-confluence](bias-confluence.md), [top-down-analysis](top-down-analysis.md).
- [true-day-open](../22-quarterly-theory/true-day-open.md), [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
