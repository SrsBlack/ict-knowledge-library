# SMT Divergence

**Category:** 16-smt-divergence
**Aliases:** SMT, Smart Money Technique, smart money divergence, intermarket divergence
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-USDX-SMT, ICT-2017-HIGH-REWARD-SETUPS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** smt, divergence, intermarket, foundational

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018` sourced only to
the placeholder IDs `ICT-2017-CHARTER-OVERVIEW` and `ICT-2022-MENTORSHIP-OVERVIEW`. The **Month 03**
lecture *Institutional Market Structure* (`ICT-2016-USDX-SMT`, Nov 2016) defines the acronym and the
signal outright at **[02:21]** — "stands for smart money tool or smart money technique and we're going
to be looking for a divergence between closely correlated or inversely correlated assets" — and the
**Month 02** lecture *The Secrets To Selecting High Reward Setups* (`ICT-2017-HIGH-REWARD-SETUPS`,
Oct 2016) already teaches it a month earlier at **[39:44]**. Re-dated to **2016**.

## Definition

**SMT (Smart Money Technique) Divergence** is a price-action divergence between **two correlated assets**: when one asset makes a new high (or low) but the correlated asset fails to confirm with its own new high (or low), the divergence signals that institutional flow is differentiated and a reversal often follows. Common SMT pairings: EURUSD vs GBPUSD, NQ vs ES (US indices), gold vs silver, EURUSD vs DXY (inverse). SMT is one of ICT's most-relied-upon confirmation signals — entering a setup with SMT confluence is significantly higher conviction than without.

## Formal Criteria

For a bullish SMT (signaling possible bullish reversal):

- Two correlated assets are trending bearishly.
- Asset A makes a new low (continuation).
- Asset B does NOT make a new low — it makes a higher low (divergence).
- The divergence is the SMT signal: institutional buying is differential.

For a bearish SMT: symmetric (Asset A new high, Asset B lower high).

## Formula / Math

```
correlated_pair = (asset_A, asset_B)         # e.g., EURUSD, GBPUSD

bullish_smt(t):
    asset_A.makes_new_low_at(t)
    AND asset_B.does_not_confirm_new_low(t)  # higher-low instead

bearish_smt(t):
    asset_A.makes_new_high_at(t)
    AND asset_B.does_not_confirm_new_high(t) # lower-high instead
```

## Machine-Readable

```json
{
  "id": "smt-divergence",
  "category": "16-smt-divergence",
  "aliases": ["SMT", "smart-money-technique", "intermarket-divergence"],
  "criteria": [
    {"id": "c1", "expr": "two_correlated_assets_used"},
    {"id": "c2", "expr": "one asset makes new extreme; other does not confirm"},
    {"id": "c3", "expr": "divergence_signals_likely_reversal"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["correlated-pairs-smt","index-smt","smt-confirmation","smt-failure","liquidity-sweep","htf-bias-framework"],
  "sources": ["ICT-2016-USDX-SMT","ICT-2017-HIGH-REWARD-SETUPS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish SMT (correlated pair, both bearish):

   Asset A (e.g. EURUSD):                 Asset B (e.g. GBPUSD):
        ▼                                       ▼
       ▼▼                                      ▼▼
      ▼▼▼  ← prior low                        ▼▼▼  ← prior low
      
            ▼                                       ▼
           ▼▼                                      ▼▼  ← higher low
          ▼▼▼  ← NEW LOW                          ▼▼  (failed to confirm)
   
   → bullish SMT divergence: A made new low, B did not.
```

## Timeframes

M5–D. HTF SMT (D, W) is most reliable; LTF SMT (M5) noisier but useful for entry timing.

## Examples

**Example 1 — bullish SMT on EURUSD/GBPUSD H1:**
- 09:00 NY: EURUSD prints H1 low at 1.0840 (new low for the day).
- Same hour: GBPUSD's matching low at 1.2650, but the GBPUSD H1 candle's low is 1.2655 (higher than its prior low 1.2645 from earlier).
- → bullish SMT. EURUSD made new low; GBPUSD did not.
- High-conviction long setup: enter on next bullish FVG / OB on EURUSD.

## Common Mistakes

- **Wrong pair correlation.** Use truly correlated pairs. EURUSD vs GBPUSD: positive correlation. EURUSD vs DXY: strong negative (inverse SMT logic applies). EURUSD vs USDJPY: weaker correlation, less reliable.
- **Single-bar SMT.** Compare the same swing event across the two assets, not random bars.
- **No confluence.** SMT alone is a confirmation signal, not a setup. Pair with PD-array + bias.

## Related Concepts

- [correlated-pairs-smt](correlated-pairs-smt.md), [index-smt](index-smt.md), [smt-confirmation](smt-confirmation.md), [smt-failure](smt-failure.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2016-USDX-SMT` (02:21) "stands for smart money tool or smart money technique and we're going to be looking for a divergence between closely correlated or inversely correlated assets"; (05:28) "when the dollar index makes a lower low in the foreign currency fails to trade higher than a previous high — this is US dollar index SMT or USDX SMT; this does not confirm current price action and the underlying trend is likely not to continue"; (08:28) "do we see a lower low form in the dollar index? No — that's a USDX SMT bullish divergence". The earliest dedicated SMT teaching located in the corpus, which is why this page is dated 2016 rather than 2018.
- `ICT-2017-HIGH-REWARD-SETUPS` (39:44, Oct-2016 lecture despite the ID's year token) "the dollar index SMT analysis is basically just looking at the relationship between the dollar making higher highs … if the British pound versus the dollar fails to make lower lows, that's a crack in correlation" — earliest mention in the corpus.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational SMT use in the 2022 re-teaching (basis for `Year Refined`).
