# Position Sizing

**Category:** 32-risk-management
**Aliases:** size calc, lot sizing, contract sizing
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2016-GROWING-SMALL-ACCOUNTS, ICT-2022-MENTORSHIP-EP01, ICT-2022-MENTORSHIP-EP40, ICT-2022-MENTORSHIP-EP41, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, position-sizing, foundational

## Definition

Position sizing is the **calculation of how many lots/contracts to enter** based on account equity, risk-per-trade %, and SL distance. Correct position sizing is the operational implementation of [risk-per-trade](risk-per-trade.md): same $-risk per trade regardless of SL distance. ICT walks the full arithmetic live: "ten thousand dollars is equity, you want to take one percent risk per trade… that's going to give you a figure of one hundred… that's one hundred dollars… that's what one percent of ten thousand dollars is" (`ICT-2022-MENTORSHIP-EP41`, 22:18–22:45); "so we take nine, divide that into one hundred, that gives us eleven… if we're going to trade a mini or e-mini futures contract on the S&P, the multiplier per contract is 50 bucks — divide 50 into 11, you can't, so you right away know you can't trade a mini… you have to drop down into the micros" (23:16–23:52). ⚠ *Corrected 2026-10-08: this page previously said ICT teaches sizing "never sized retroactively"; no such statement is in the corpus. Removed as invented.*

## Formal Criteria

The standard formula, as ICT works it:

```
position_size = risk_$ / sl_distance_$
              = (account_equity * risk_pct) / (sl_pips * pip_value)
```

ICT-confirmed per-instrument figures (S&P e-mini / micro only — `ICT-2022-MENTORSHIP-EP41`, `ICT-2022-MENTORSHIP-EP01`):

| Instrument | Pip/point value | Source |
|---|---|---|
| ES (e-mini S&P) | $50 / point per contract | EP41, 23:16 |
| MES (micro e-mini S&P) | $5 / point per contract | EP41, 23:52 |
| ES tick | $12.50 / tick (4 ticks = 1 point = $50) | EP01, 24:14 |

⚠ *Corrected 2026-10-08: this page previously listed EURUSD, GBPUSD, USDJPY, XAUUSD, and NQ pip/point values as if ICT-sourced. None of those rows is a quote from either corpus — they are generic contract specifications, not ICT teachings. Kept below for reference only, clearly marked as not primary-sourced:*

| Instrument | Pip value (per std lot, $-quote) | Status |
|---|---|---|
| EURUSD | $10 / pip | generic reference, not ICT-sourced |
| GBPUSD | $10 / pip | generic reference, not ICT-sourced |
| USDJPY | ~$6.7 / pip (varies with rate) | generic reference, not ICT-sourced |
| XAUUSD | $1 / 0.01 ($10 per "pip" if pip = 0.10) | generic reference, not ICT-sourced |
| NQ futures | $20 / point per contract | generic reference, not ICT-sourced |

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
    {"id": "c2", "expr": "calculated_before_entry"},
    {"id": "c3", "expr": "scales_to_keep_$_risk_constant_per_trade"},
    {"id": "c4", "expr": "round DOWN when the exact contract count is unreachable; drop to micros rather than round up", "strength": "ICT-confirmed, EP41"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["risk-per-trade","r-multiple","stop-placement-by-pd-array","partial-takes","correlation-risk"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2016-GROWING-SMALL-ACCOUNTS","ICT-2022-MENTORSHIP-EP01","ICT-2022-MENTORSHIP-EP40","ICT-2022-MENTORSHIP-EP41","ICT-2022-MENTORSHIP-OVERVIEW"]
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

**Example 1 — full pre-trade sizing (illustrative, generic pip values, not ICT-sourced):**
- Account: $50,000.
- Setup: H1 bullish OB, EURUSD, entry 1.0930, SL 1.0908. SL distance = 22 pips. *(Renamed 2026-10-08 from "NY AM SB" — "Silver Bullet" as a named setup post-dates this corpus; see [r-multiple](r-multiple.md).)*
- Risk %: 1%.
- risk_$ = $500.
- position_lots = $500 / ($10 × 22) = 2.27 standard lots.
- Round to 2 lots (slight under-risk): actual risk = 2 × $10 × 22 = $440 = 0.88%.

**Example 2 — ICT's own worked arithmetic (`ICT-2022-MENTORSHIP-EP41`, 22:18–23:52):**
- Account: $10,000 equity, 1% risk per trade.
- risk_$ = $10,000 × 0.01 = $100.
- Hypothetical ES entry 37.54¾, stop 45¾ → SL distance = 9 points.
- contracts = $100 / 9 points = 11 (as a $-per-point budget, before applying the contract multiplier).
- ES multiplier = $50/point; 11 / 50 is not a whole mini contract, so ICT drops to micros ($5/point): 11 / 5 = 2 micro contracts.
- "so you have to drop down into the micros" — ICT's reasoning is that the mini contract size *can't* be traded at this risk budget ("you can't"), not an explicit "never round up" rule; the effect is the same (round down to the nearest tradable size).

## Common Mistakes

- **Fixed lot size on every trade.** Same lots × different SL distances = wildly different $-risk.
- **Forgetting pip-value differences.** USDJPY pip value varies with rate; XAUUSD requires "pip" definition convention; futures use point × contract spec. ⚠ Only the ES/MES figures above are ICT-confirmed; the others are generic reference data.
- **Over-rounding.** Rounding 2.27 lots to 3 lots over-risks; round down or use micro lots — ICT does exactly this when a mini contract doesn't fit the risk budget (Example 2).

## Related Concepts

- [risk-per-trade](risk-per-trade.md), [r-multiple](r-multiple.md), [stop-placement-by-pd-array](stop-placement-by-pd-array.md), [partial-takes](partial-takes.md), [correlation-risk](correlation-risk.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.

Added 2026-10-08:

- `ICT-2016-GROWING-SMALL-ACCOUNTS` (17:04) "now account with $1,000, your risk per trade is going to be 1.5% or $15" — the earliest located worked sizing arithmetic (Oct-2016; Year Introduced correction).
- `ICT-2022-MENTORSHIP-EP41` (22:18–23:52) the full ES/micro sizing walkthrough quoted in Example 2 above.
- `ICT-2022-MENTORSHIP-EP01` (24:14) — "every one tick is twelve dollars and fifty cents" (ES tick value, 4 ticks = 1 point).
- `ICT-2022-MENTORSHIP-EP40` (14:50) — "that's one of the benefits of forex, it's very scalable, whereas if you're trading futures you're kind of stuck to whatever the contract size is."
