# Risk Per Trade

**Category:** 32-risk-management
**Aliases:** risk %, per-trade risk, R-risk
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-SWING-REDUCE-RISK, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, foundational

## Definition

Risk per trade is the **percentage of account equity** the trader is willing to lose on a single setup if the SL is hit. ICT teaches conservative risk discipline: typically **0.5% to 1% per trade** for funded accounts, sometimes up to 2% for personal accounts in high-conviction setups. Risk per trade is the most fundamental position-sizing input — every position size calculation starts from a chosen risk-per-trade percentage and the trade's SL distance.

## Formal Criteria

ICT-recommended ranges:

| Account type | Recommended risk % |
|---|---|
| Funded prop firm (typical) | 0.5% – 1% |
| Personal high-conviction | up to 2% |
| Personal exploratory | 0.25% – 0.5% |
| Recovery / drawdown mode | 0.25% or less |

**Leverage is the other half of the equation** (`ICT-2017-SWING-REDUCE-RISK`, 08:18–09:10,
15:08–16:04). ICT treats available leverage as a trap rather than a resource: "**leverage is
your holy grail in swing trading** — you're going to look to **control** your leverage and
you're **not** trying to maximize it." Concretely:

- Brokers offering 50:1 (US retail FX) or more are offering "unheard of" leverage you do not need.
- The taught working figure is **3:1** — "if you have a $10,000 account, you're only trading
  with three minis."
- Futures run around 10:1 by default, which ICT treats as already sufficient.
- At scale, prime brokerage **de-leverages** you — a million on deposit is often traded as half
  a million — and that is presented as the correct end state, not a constraint.

**Compressing the stop instead of widening the risk** (00:30–07:00). The swing-trading method
frames the *trade* on monthly and weekly PD arrays but takes the *entry* on the **four-hour**
chart. The monthly range supplies a several-hundred-pip objective while the H4 entry keeps the
stop small — "by using the higher timeframe PD arrays… we remove all the necessity to have a
big, huge stop." The trader who instead maximises leverage on a large-range setup has thrown
away the entire advantage.

**Frequency sets the risk budget** (14:25–14:44). Swing setups arrive at roughly **one to two
every four to six weeks**, so per-trade risk does not need to be large to matter over a year.

The risk-per-trade % combined with the SL distance yields position size:

```
position_size = (account_equity * risk_per_trade_pct) / sl_distance_in_$
```

## Formula / Math

```
risk_per_trade_$ = account_equity * risk_per_trade_pct
position_size = risk_per_trade_$ / sl_distance_in_$_per_unit

# Example: $50,000 account, 1% risk, 20-pip SL on EURUSD ($10/pip per std lot):
# risk_$ = $500
# position_size = $500 / ($10 * 20) = $500 / $200 = 2.5 standard lots

# Leverage discipline (ICT-2017-SWING-REDUCE-RISK):
effective_leverage := notional_exposure / account_equity
target_leverage    := ~3        # NOT the 50:1 or 100:1 a broker offers
# $10,000 account at 3:1 => three mini lots
```

## Machine-Readable

```json
{
  "id": "risk-per-trade",
  "category": "32-risk-management",
  "aliases": ["risk-pct", "per-trade-risk", "R-risk"],
  "criteria": [
    {"id": "c1", "expr": "typical range 0.5%-1% for funded"},
    {"id": "c2", "expr": "max 2% for personal high-conviction"},
    {"id": "c3", "expr": "drives position sizing combined with SL distance"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["r-multiple","position-sizing","stop-placement-by-pd-array","partial-takes","correlation-risk"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

A discipline concept rather than a chart pattern. Practical view:

```
   account: $50,000
   risk per trade: 1% = $500

   trade 1 (SL 20 pips):  position = 2.5 lots, risk $500
   trade 2 (SL 12 pips):  position = 4.16 lots, risk $500
   trade 3 (SL 35 pips):  position = 1.43 lots, risk $500

   → equal $-risk, position size adjusts to SL distance.
```

## Timeframes

All TFs.

## Examples

**Example 1 — calibrating risk-per-trade:**
- $50,000 funded account.
- Risk per trade: 1% = $500.
- Setup: bullish OB on H1, SL = 15 pips, EURUSD.
- Position size = $500 / ($10/pip × 15 pips) = 3.33 lots.
- If SL hits, loss = $500 = 1% of account.

## Common Mistakes

- **Fixed lot size regardless of SL.** Same lot size with different SL distances produces wildly different $-risk; always scale lots to SL distance.
- **Risking >2% on any single trade.** Even high-conviction setups can fail; >2% risk recovery requires non-trivial subsequent wins.
- **Ignoring funded-account daily loss limits.** Many prop firms cap daily loss at 4–5%; sizing 2% per trade leaves only 2 trades' worth of buffer. Calibrate to firm rules.

## Related Concepts

- [r-multiple](r-multiple.md), [position-sizing](position-sizing.md), [stop-placement-by-pd-array](stop-placement-by-pd-array.md), [partial-takes](partial-takes.md), [correlation-risk](correlation-risk.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- `ICT-2017-SWING-REDUCE-RISK` (00:30) "lesson 6, February 2017 ICT Mentorship… reducing risk and maximizing potential reward [in] swing setups"; (00:37) "this begins with knowing your maximum risk per set up or trade… you should not allow high risk percent per trade, this equates to gambling"; (00:58–07:00) framing on monthly and weekly PD arrays while entering on the four-hour to compress the stop — "we remove all the necessity to have a big, huge stop"; (03:47–04:16) do not try to double the account monthly; low risk is what sells a fund manager's business model; (08:18–09:10) "leverage is your holy grail in swing trading — you're going to look to control your leverage and you're not trying to maximize it"; (14:25–14:44) "there's typically one to two swing trades every four to six weeks"; (15:08–16:04) "by removing the high leverage, you can actually trade with just 3 to 1 leverage… if you have a $10,000 account, you're only trading with three minis"; (16:04–16:49) prime brokerage de-leveraging as the end state.
