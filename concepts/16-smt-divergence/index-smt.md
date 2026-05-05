# Index SMT

**Category:** 16-smt-divergence
**Aliases:** US index SMT, NQ-ES SMT, indices divergence
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** smt, indices, nq, es

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
  "year_introduced": "2018",
  "year_refined": "2023",
  "related": ["smt-divergence","correlated-pairs-smt","smt-confirmation","smt-failure"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
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

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
