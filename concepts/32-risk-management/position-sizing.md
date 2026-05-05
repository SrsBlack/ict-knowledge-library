# Position Sizing

**Category:** 32-risk-management
**Aliases:** size calc, lot sizing, contract sizing
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, position-sizing, foundational

## Definition

Position sizing is the **calculation of how many lots/contracts to enter** based on account equity, risk-per-trade %, and SL distance. Correct position sizing is the operational implementation of [risk-per-trade](risk-per-trade.md): same $-risk per trade regardless of SL distance. ICT teaches position-size calculation as a discipline executed before every entry — never sized retroactively.

## Formal Criteria

The standard formula:

```
position_size = risk_$ / sl_distance_$
              = (account_equity * risk_pct) / (sl_pips * pip_value)
```

Per-instrument pip values:

| Instrument | Pip value (per std lot, $-quote) |
|---|---|
| EURUSD | $10 / pip |
| GBPUSD | $10 / pip |
| USDJPY | ~$6.7 / pip (varies with rate) |
| XAUUSD | $1 / 0.01 ($10 per "pip" if pip = 0.10) |
| NQ futures | $20 / point per contract |
| ES futures | $50 / point per contract |

## Formula / Math

```
# FX example: EURUSD, $50,000 account, 1% risk, SL = 20 pips
risk_$ = 50000 * 0.01 = 500
position_lots = 500 / (20 * 10) = 2.5 standard lots

# Index futures example: NQ, $100,000 account, 0.5% risk, SL = 30 points
risk_$ = 100000 * 0.005 = 500
contracts = 500 / (30 * 20) = 0.83 → round to 1 contract (slight over-risk)
       OR  use micro contracts (M2K, MNQ) for finer granularity
```

## Machine-Readable

```json
{
  "id": "position-sizing",
  "category": "32-risk-management",
  "aliases": ["size-calc", "lot-sizing", "contract-sizing"],
  "criteria": [
    {"id": "c1", "expr": "position_size = risk_$ / sl_distance_$"},
    {"id": "c2", "expr": "calculated_before_entry_not_after"},
    {"id": "c3", "expr": "scales_to_keep_$_risk_constant_per_trade"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["risk-per-trade","r-multiple","stop-placement-by-pd-array","partial-takes","correlation-risk"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

A pre-trade calculation, not a chart pattern. Mental model:

```
   account: $50,000, risk 1% = $500

   SL = 10 pips → lots = $500 / ($10 × 10) = 5 lots
   SL = 20 pips → lots = $500 / ($10 × 20) = 2.5 lots
   SL = 50 pips → lots = $500 / ($10 × 50) = 1 lot

   $ risk constant = $500 across all three.
```

## Timeframes

All TFs.

## Examples

**Example 1 — full pre-trade sizing:**
- Account: $50,000.
- Setup: NY AM SB, EURUSD, entry 1.0930, SL 1.0908. SL distance = 22 pips.
- Risk %: 1%.
- risk_$ = $500.
- position_lots = $500 / ($10 × 22) = 2.27 standard lots.
- Round to 2 lots (slight under-risk): actual risk = 2 × $10 × 22 = $440 = 0.88%.

## Common Mistakes

- **Fixed lot size on every trade.** Same lots × different SL distances = wildly different $-risk.
- **Forgetting pip-value differences.** USDJPY pip value varies with rate; XAUUSD requires "pip" definition convention; futures use point × contract spec.
- **Over-rounding.** Rounding 2.27 lots to 3 lots over-risks; round down or use micro lots.

## Related Concepts

- [risk-per-trade](risk-per-trade.md), [r-multiple](r-multiple.md), [stop-placement-by-pd-array](stop-placement-by-pd-array.md), [partial-takes](partial-takes.md), [correlation-risk](correlation-risk.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
