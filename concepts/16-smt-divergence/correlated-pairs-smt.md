# Correlated Pairs SMT

**Category:** 16-smt-divergence
**Aliases:** FX SMT, currency-pair SMT, cross-pair divergence
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-HIGH-REWARD-SETUPS, ICT-2016-USDX-SMT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** smt, fx, correlated-pairs

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018` sourced only to
the placeholder IDs `ICT-2017-CHARTER-OVERVIEW` and `ICT-2022-MENTORSHIP-OVERVIEW`. The **Month 02**
lecture *The Secrets To Selecting High Reward Setups* (`ICT-2017-HIGH-REWARD-SETUPS`, Oct 2016 — the
ID's `2017` token is a registry error, see note below) names and teaches the concept at **[40:10]**:
"the other correlation analysis concept that I use is correlated pair SMT analysis, where we look at
closely correlated pairs like, for instance, the euro dollar and the British pound dollar." Re-dated to
**2016**.

## Definition

Correlated-pairs SMT is the application of SMT divergence to **FX pair pairings** that share a common currency leg. The most-cited pairings: **EURUSD vs GBPUSD** (both have USD as quote, both broadly track European-USD strength), **AUDUSD vs NZDUSD** (Aussie pairing), **USDJPY vs USDCHF** (USD-base pairs). The shared currency leg means the pairs move similarly but rarely identically — the divergences ICT teaches as actionable usually occur at extreme price levels (tested SSL/BSL pools).

## Formal Criteria

A correlated-pair SMT requires:

- Two FX pairs with **strong positive correlation** (typical: EUR vs GBP majors, AUD vs NZD, USD-bases, etc.).
- Both pairs are reaching a known structural level (sweep, swing extreme).
- One pair confirms (makes new high/low); the other fails to confirm (lower high or higher low).
- Confirmation requires inspecting the **same time-of-day candle** on both charts (don't compare 09:00 EURUSD with 10:00 GBPUSD).

## Formula / Math

```
positive_correlation_pair = (asset_A, asset_B) where corr_60d > 0.7

bullish_smt(asset_A, asset_B, t):
    A.low_at(t) < A.prior_low_in_session
    AND B.low_at(t) > B.prior_low_in_session     # divergence

bearish_smt(asset_A, asset_B, t):
    A.high_at(t) > A.prior_high_in_session
    AND B.high_at(t) < B.prior_high_in_session
```

## Machine-Readable

```json
{
  "id": "correlated-pairs-smt",
  "category": "16-smt-divergence",
  "aliases": ["FX-SMT", "currency-pair-SMT", "cross-pair-divergence"],
  "criteria": [
    {"id": "c1", "expr": "positive correlation > 0.7 typical"},
    {"id": "c2", "expr": "same time-of-day candle compared"},
    {"id": "c3", "expr": "one confirms new extreme, other does not"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["smt-divergence","index-smt","smt-confirmation","smt-failure"],
  "sources": ["ICT-2017-HIGH-REWARD-SETUPS","ICT-2016-USDX-SMT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

Same as [smt-divergence](smt-divergence.md) — two charts side-by-side, one confirms the new low, the other doesn't.

## Timeframes

M5–D. Most-traded on H1 and H4.

## Examples

**Example 1 — EURUSD vs GBPUSD bullish SMT at session low:**
- Asia: EURUSD low 1.0848, GBPUSD low 1.2645.
- London open: EURUSD wicks 1.0843 (new low), closes 1.0855.
- Same M5: GBPUSD wicks 1.2648 (HIGHER than 1.2645).
- → bullish SMT. EURUSD took new low, GBPUSD did not.
- Long EURUSD or GBPUSD on next bullish FVG.

## Common Mistakes

- **Comparing weakly-correlated pairs.** EURUSD vs USDJPY has weaker / inconsistent correlation — SMT logic becomes unreliable, not inverted. Inverse SMT applies only to strong-negative pairings (e.g. EURUSD vs DXY).
- **Wrong time alignment.** Compare 03:00 NY EURUSD with 03:00 NY GBPUSD, not adjacent candles.
- **Ignoring the structural level.** SMT at a random pair of M1 candles is noise; SMT at a known SSL/BSL is the signal.

## Related Concepts

- [smt-divergence](smt-divergence.md), [index-smt](index-smt.md), [smt-confirmation](smt-confirmation.md), [smt-failure](smt-failure.md).

## Citations

- `ICT-2017-HIGH-REWARD-SETUPS` (40:10) "the other correlation analysis concept that I use is correlated pair SMT analysis, where we look at closely correlated pairs like, for instance, the euro dollar and the British pound dollar, because usually they move in general same direction"; (40:27) "generally, when there's a symmetrical market … correlated pairs move in tandem. When they do not move in tandem, that obviously gives us a lot of insight." Earliest teaching of this concept located in the corpus.
  ⚠ **Registry note:** this Source ID carries a `2017` year token, but the lecture is **Month 02 of the mentorship = October 2016** under the verified month→year map (Month 04 self-identifies as "the December 2016 content" at 00:30). The ID is stable and append-only, so it is cited as-is; the year token should not be read as the teaching date.
- `ICT-2016-USDX-SMT` (02:21) defines SMT as "a divergence between closely correlated or inversely correlated assets" — the parent definition this page specialises to FX pairings.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use in the 2022 re-teaching (basis for `Year Refined`).
