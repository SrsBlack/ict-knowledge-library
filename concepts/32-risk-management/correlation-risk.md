# Correlation Risk

**Category:** 32-risk-management
**Aliases:** correlated exposure, multi-pair correlation, basket risk
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, correlation, foundational

## Definition

Correlation risk is the **hidden exposure** that arises when multiple open trades share a common driver — most commonly multiple FX pairs sharing the USD leg, or multiple US indices sharing US-economy correlation. Sizing each trade at 1% individually but having 5 correlated longs open = 5% effective exposure to a single driver. ICT teaches correlation awareness as essential discipline: total open-position risk should account for correlation, not just per-trade risk %.

## Formal Criteria

Common correlation clusters:

| Cluster | Pairs / Instruments | Correlation |
|---|---|---|
| USD-base FX | EURUSD, GBPUSD, AUDUSD, NZDUSD | High positive (all "vs USD") |
| USD-quote FX | USDJPY, USDCHF, USDCAD | High positive |
| US Indices | NQ, ES, YM, RTY | Very high positive |
| Risk-on basket | EURUSD, AUDUSD, indices, oil | Moderate positive |
| Safe-haven cluster | USDJPY (pre-2022), gold, USD index | Variable inverse |

Aggregate exposure to a cluster should be tracked: 4 × 1% longs in EURUSD, GBPUSD, AUDUSD, NZDUSD = effectively 4% on "USD weakness."

## Formula / Math

```
cluster_exposure = sum(position_risk_$ for each correlated_position) / account_equity

# Soft caps:
single_cluster_cap = 2% - 3% effective
total_open_risk_cap = 5% - 6% across all clusters
```

## Machine-Readable

```json
{
  "id": "correlation-risk",
  "category": "32-risk-management",
  "aliases": ["correlated-exposure", "multi-pair-correlation", "basket-risk"],
  "criteria": [
    {"id": "c1", "expr": "track aggregate exposure to common drivers"},
    {"id": "c2", "expr": "soft cap 2-3% per cluster"},
    {"id": "c3", "expr": "soft cap 5-6% total open"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["risk-per-trade","r-multiple","position-sizing","correlated-pairs-smt","index-smt"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

A pre-trade discipline rather than a chart pattern. Mental tracker:

```
   Open positions (each at 1% per-trade risk):

   EURUSD long  ─── 1% (USD-weak cluster)
   GBPUSD long  ─── 1% (USD-weak cluster)
   AUDUSD long  ─── 1% (USD-weak cluster)
   NQ long      ─── 1% (US-equities cluster)
   ES long      ─── 1% (US-equities cluster)

   USD-weak cluster effective exposure: 3%
   US-equities cluster effective exposure: 2%
   Total open risk: ~5% (high — consider closing one)
```

## Timeframes

All TFs.

## Examples

**Example 1 — correlated FX cluster:**
- $50K account, 1% per trade.
- Long EURUSD ($500 risk), long GBPUSD ($500), long AUDUSD ($500).
- All three are "USD-weakness" trades; highly correlated.
- If USD strengthens unexpectedly: all 3 hit SL = $1500 loss = 3% account.
- Effective cluster exposure was 3%, not 1% per trade.

## Common Mistakes

- **Counting only per-trade risk.** Per-trade % matters for any single failure; cluster % matters for systemic moves.
- **Trading the same setup across multiple correlated pairs.** "Diversification" via correlated pairs isn't diversification; it's concentration.
- **Forgetting to close cluster trades together.** If the driver story flips, close the cluster, not just one position.

## Related Concepts

- [risk-per-trade](risk-per-trade.md), [r-multiple](r-multiple.md), [position-sizing](position-sizing.md).
- [correlated-pairs-smt](../16-smt-divergence/correlated-pairs-smt.md), [index-smt](../16-smt-divergence/index-smt.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
