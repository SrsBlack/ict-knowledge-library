# Index SMT

**Category:** 16-smt-divergence
**Aliases:** US index SMT, NQ-ES SMT, indices divergence
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-INDEX-SMT-AM-TREND, ICT-2017-INDEX-TRADE-SETUPS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** smt, indices, nq, es

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018` sourced only to
the placeholder IDs `ICT-2017-CHARTER-OVERVIEW` and `ICT-2022-MENTORSHIP-OVERVIEW`. The **Month 10**
lecture *Index Futures — AM Trend* (`ICT-2017-INDEX-SMT-AM-TREND`), which self-identifies at **[00:20]**
as "June 2017, ICT Mentorship, ICT Index Trading, Lesson 2, The AM Trend", teaches equity-index SMT in
full at **[08:05]** — "when institutional order flow is bullish … we have to be comparing relative lows
across the three indices; one index will fail to confirm a lower low … that's your bullish confirmation
for trading the AM trend." Re-dated to **2017**. (The 2016 `index SMT` hits elsewhere in the corpus are
*dollar-index* SMT — see [smt-divergence](smt-divergence.md) — not equity indices.)

## Definition

Index SMT is the application of SMT divergence to **US equity indices**: NQ (Nasdaq 100), ES (S&P 500), YM (Dow Jones), RTY (Russell 2000). All four are highly correlated and routinely diverge at structural extremes. ICT teaches index SMT as one of the most reliable confirmation signals because the indices are deeply correlated by economic fundamentals (rate-sensitive, sector-weighted) and intermarket flows. NQ-vs-ES is the most-cited pairing.

## Formal Criteria

The four US indices and their typical SMT pairings:

| Pairing | Reliability | Notes |
|---|---|---|
| NQ vs ES | Highest | Most-cited pairing. Tech-heavy NQ vs broad ES. |
| ES vs YM | High | Both broad-market; YM more rate-sensitive. |
| RTY vs ES | Medium-High | Small-cap vs large-cap divergence. |
| NQ vs RTY | High | Tech vs small-cap. |

SMT logic same as [smt-divergence](smt-divergence.md): one index makes new extreme, the other does not.

⚠ **Source scope.** The 2017 primary sources teach index SMT across **three** indices only — NASDAQ, Dow
and E-mini S&P ("we're going to be comparing the index SMT divergences at the lows comparably against the
Dow and NASDAQ with the S&P mini", `ICT-2017-INDEX-TRADE-SETUPS` 16:09). RTY does not appear in them, and
the per-pairing reliability ranks in the table above are not attributable to a located source.
`ICT-2017-INDEX-SMT-AM-TREND` also brackets the comparison to a **5:00 a.m.–9:30 a.m. New York window**
[07:57], a constraint this page does not currently carry.

## Formula / Math

```
us_indices = [NQ, ES, YM, RTY]

bullish_index_smt(idx_A, idx_B, t):
    idx_A.low_at(t) < idx_A.prior_low
    AND idx_B.low_at(t) > idx_B.prior_low

# Same logic for bearish (with highs)
```

## Machine-Readable

```json
{
  "id": "index-smt",
  "category": "16-smt-divergence",
  "aliases": ["US-index-SMT", "NQ-ES-SMT", "indices-divergence"],
  "criteria": [
    {"id": "c1", "expr": "indices in [NQ, ES, YM, RTY]"},
    {"id": "c2", "expr": "high correlation typically > 0.85"},
    {"id": "c3", "expr": "structural-level divergence is the signal"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["smt-divergence","correlated-pairs-smt","smt-confirmation","smt-failure"],
  "sources": ["ICT-2017-INDEX-SMT-AM-TREND","ICT-2017-INDEX-TRADE-SETUPS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

Same as [smt-divergence](smt-divergence.md) — two charts side-by-side, e.g., NQ printing new low while ES holds higher low.

## Timeframes

M1 / M5 / M15 are intraday-tradeable; H1 / H4 for setup conviction.

## Examples

**Example 1 — NQ-ES bullish SMT at session low (intraday):**
- 09:00 NY: NQ M5 wicks new session low at 17500.
- Same M5: ES wicks 4880, but ES's prior low this session was 4878 — ES did NOT make a new low.
- → bullish SMT (NQ took new low, ES did not). Long NQ or ES on bullish setup.

## Common Mistakes

- **Cross-asset divergence (e.g., NQ vs gold).** Gold is not US-index-correlated for SMT purposes; the framework is intra-index-class.
- **Ignoring time alignment.** NQ trades on different exchanges; align to the same NY-time minute.
- **Single-bar SMT.** Use a clear structural extreme (session low/high), not random bar comparisons.

## Related Concepts

- [smt-divergence](smt-divergence.md), [correlated-pairs-smt](correlated-pairs-smt.md), [smt-confirmation](smt-confirmation.md), [smt-failure](smt-failure.md).

## Citations

- `ICT-2017-INDEX-SMT-AM-TREND` (00:20) "June 2017, ICT Mentorship, ICT Index Trading, Lesson 2, The AM Trend" — self-dates the lecture; (07:57) "between 5 a.m. and 9:30 a.m. New York time, relative highs and lows should be compared"; (08:13) "one index will fail to confirm a lower low … when that occurs, that's your bullish confirmation for trading the AM trend"; (13:13) "it will show you that crack in correlation where otherwise the indices should be moving in tandem." Earliest equity-index SMT teaching located in the corpus, which is why this page is dated 2017 rather than 2018.
- `ICT-2017-INDEX-TRADE-SETUPS` (16:09) "we're going to be comparing the index SMT divergences at the lows comparably against the Dow and NASDAQ with the S&P mini" — the same-month setup lecture; fixes the three-index scope.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use in the 2022 re-teaching.
