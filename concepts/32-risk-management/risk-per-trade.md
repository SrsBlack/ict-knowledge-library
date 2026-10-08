# Risk Per Trade

**Category:** 32-risk-management
**Aliases:** risk %, per-trade risk, R-risk
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-OTE, ICT-2017-SWING-REDUCE-RISK, ICT-2016-GROWING-SMALL-ACCOUNTS, ICT-2016-NO-FEAR-LOSING, ICT-2016-MITIGATE-LOSING-TRADES, ICT-2017-HTF-MONEY-MANAGEMENT, ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP07, ICT-2022-MENTORSHIP-EP41, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, foundational

## Definition

Risk per trade is the **percentage of account equity** the trader is willing to lose on a single setup if the SL is hit. ⚠ For long-term position trading ICT re-bases this: the percentage is taken on **30% of total equity**, not on the full account, so his taught 1% is 0.3% of the account — see [capital-allocation-30-percent](capital-allocation-30-percent.md). Risk per trade is the most fundamental position-sizing input — every position size calculation starts from a chosen risk-per-trade percentage and the trade's SL distance.

> ⚠ **Corrected 2026-10-08 (EMBELLISHED).** This page previously gave a four-row "account type" table (funded / personal high-conviction / personal exploratory / recovery) with ranges 0.25%–2%. ICT never classifies risk by account type; that table is invented. His actual stated figures, across years, are:

- "two percent ideally if you're a new trader, but no more than two percent on an average" (`ICT-2016-GROWING-SMALL-ACCOUNTS`, 03:45).
- "we're not talking about 2% which is the industry standard here — we're talking about 1%. 1% makes millionaires" (`ICT-2016-NO-FEAR-LOSING`, 14:33–14:38); "what if you were to drop that risk per trade down to a half a percent" (15:43).
- "we'll say it's a half a percent" (`ICT-2017-OTE`, 16:01, 2017 Primer).
- "ideally set 1% as the most risk per trade. That means 1% of 30% of your total equity base" (`ICT-2017-HTF-MONEY-MANAGEMENT`, 06:30–06:36).
- "if you're risking one and a half percent on your equity per trade" for swing setups (`ICT-2017-SWING-REDUCE-RISK`, 17:13; "six trades risking one and a half percent using three to one leverage and about a 50 pip stop", 18:54).
- 2022: "you should be risking less than 1% — about a half percent or a quarter percent, because if you don't know what you're doing…" (`ICT-2022-MENTORSHIP-EP07`, 04:44). ICT's own, stated in the same breath as not a recommendation: "I like 3 and a half% — I'm not telling you to use 3 and a half%" (`ICT-2022-MENTORSHIP-EP07`, 04:44); "my maximum risk on a trade if I'm trading competitively is four and a half percent per trade" (`ICT-2022-MENTORSHIP-EP03`, 48:47).
- "ten thousand dollars is equity, you want to take one percent risk per trade" (`ICT-2022-MENTORSHIP-EP41`, 22:18); "eventually getting to the point where you can risk two percent" as an experience-gated ceiling, not a day-one figure (28:50).

There is no single number; the figure varies by year, trading horizon (swing/position vs intraday), and the trader's stated experience level — not by "account type," which was the wrong second axis this page previously named. 1% and "a half a percent" recur most often as the baseline.

## Formal Criteria

ICT's own stated risk-per-trade figures (no account-type table; see Definition for sources):

| Figure | Context |
|---|---|
| 2% (ceiling, "no more than") | new trader, `ICT-2016-GROWING-SMALL-ACCOUNTS` |
| 1% | standing baseline — "1% makes millionaires", `ICT-2016-NO-FEAR-LOSING`; also `ICT-2017-HTF-MONEY-MANAGEMENT`, `ICT-2022-MENTORSHIP-EP41` |
| 0.5% ("a half a percent") | `ICT-2016-NO-FEAR-LOSING`; `ICT-2017-OTE` Primer |
| 1.5% | swing setups, `ICT-2017-SWING-REDUCE-RISK`; also the 2016 6%/month model, `ICT-2016-GROWING-SMALL-ACCOUNTS` (15:39, 17:04) |
| 0.5% or 0.25% | 2022, "if you don't know what you're doing", `ICT-2022-MENTORSHIP-EP07` |
| 3.5% / 4.5% (ICT's own, not a recommendation) | `ICT-2022-MENTORSHIP-EP07`, `ICT-2022-MENTORSHIP-EP03` |
| 2% (experience-gated ceiling) | `ICT-2022-MENTORSHIP-EP41`, 28:50 |

**Loss-mitigation halving rule, added 2026-10-08.** On a stopped-out trade, the next trade's risk is halved, not held constant: "if we took a[n] initial loss of 2% on the first trade, we have to go down to 1%. If we were trading with 1%… drop down to one half of 1%" (`ICT-2016-MITIGATE-LOSING-TRADES`, 05:26–05:33). The 2022 mentorship restates the floor: "risking a half of one percent and that trade gets knocked out to a loss, what size do you use on your next trade — one quarter of one percent, and that's obviously the lowest you can go with" (`ICT-2022-MENTORSHIP-EP41`, 32:04). Restoration back to full risk is gated on recovery, not time: "you have to make back fifty percent of what you lost… before you can go back to your full one percent risk" (`ICT-2022-MENTORSHIP-EP41`, 31:37–32:04).

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
    {"id": "c1", "expr": "no single ICT-stated figure; 1% and 0.5% recur most often as baselines across years"},
    {"id": "c2", "expr": "no account-type table; figures vary by year, trading horizon (swing/position vs intraday), and stated trader experience — not account purpose"},
    {"id": "c3", "expr": "drives position sizing combined with SL distance"},
    {"id": "c4", "expr": "post-loss risk halves (2%->1%->0.5%->0.25% floor); restored only after recovering 50% of the loss"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["r-multiple","position-sizing","stop-placement-by-pd-array","partial-takes","correlation-risk","capital-allocation-30-percent","ipda-trailing-stop","loss-mitigation-half-size-reentry"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2017-OTE","ICT-2017-SWING-REDUCE-RISK","ICT-2016-GROWING-SMALL-ACCOUNTS","ICT-2016-NO-FEAR-LOSING","ICT-2016-MITIGATE-LOSING-TRADES","ICT-2017-HTF-MONEY-MANAGEMENT","ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP07","ICT-2022-MENTORSHIP-EP41","ICT-2022-MENTORSHIP-OVERVIEW"]
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
- $50,000 account (illustrative; "funded" dropped 2026-10-08 to avoid echoing the removed account-type framing).
- Risk per trade: 1% = $500.
- Setup: bullish OB on H1, SL = 15 pips, EURUSD.
- Position size = $500 / ($10/pip × 15 pips) = 3.33 lots.
- If SL hits, loss = $500 = 1% of account.

## Common Mistakes

- **Fixed lot size regardless of SL.** Same lot size with different SL distances produces wildly different $-risk; always scale lots to SL distance.
- ⚠ **Inventing an account-type table.** ICT never classifies risk by "funded" vs. "personal" vs. "recovery" account type. His figures vary by year and stated trader experience — quote a specific figure with its source, not a table.
- **Risking >2% without the halving discipline after a loss.** ICT's own figures (3.5%, 4.5%) are explicitly not a recommendation for others. Whatever baseline is chosen, the taught response to a loss is to halve the next trade's risk, not hold it constant — see the loss-mitigation rule above.
- **Treating the daily-loss-limit figure as ICT's.** A "prop firms cap daily loss at 4–5%" claim was previously on this page; it is not in either corpus (it is a generic community/2023-era fact about funded-account rules, not an ICT teaching). Removed 2026-10-08.

## Related Concepts

- [r-multiple](r-multiple.md), [position-sizing](position-sizing.md), [stop-placement-by-pd-array](stop-placement-by-pd-array.md), [partial-takes](partial-takes.md), [correlation-risk](correlation-risk.md).
- [capital-allocation-30-percent](capital-allocation-30-percent.md) — the 30%-of-equity base ICT applies this percentage to for position trading.
- [ipda-trailing-stop](ipda-trailing-stop.md) — the trailing rule that governs risk once the position is open.
- [loss-mitigation-half-size-reentry](loss-mitigation-half-size-reentry.md) — the halving/recovery mechanism cited above.

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- `ICT-2017-SWING-REDUCE-RISK` (00:30) "lesson 6, February 2017 ICT Mentorship… reducing risk and maximizing potential reward [in] swing setups"; (00:37) "this begins with knowing your maximum risk per set up or trade… you should not allow high risk percent per trade, this equates to gambling"; (00:58–07:00) framing on monthly and weekly PD arrays while entering on the four-hour to compress the stop — "we remove all the necessity to have a big, huge stop"; (03:47–04:16) do not try to double the account monthly; low risk is what sells a fund manager's business model; (08:18–09:10) "leverage is your holy grail in swing trading — you're going to look to control your leverage and you're not trying to maximize it"; (14:25–14:44) "there's typically one to two swing trades every four to six weeks"; (15:08–16:04) "by removing the high leverage, you can actually trade with just 3 to 1 leverage… if you have a $10,000 account, you're only trading with three minis"; (16:04–16:49) prime brokerage de-leveraging as the end state; (17:13) "if you're risking one and a half percent on your equity per trade."

Added 2026-10-08 (account-type table removed; actual risk figures and halving rule):

- `ICT-2016-GROWING-SMALL-ACCOUNTS` (00:23) "this is month two of the ICT Mentorship" — Year Introduced correction (Oct-2016); (03:45) "two percent ideally if you're a new trader, but no more than two percent on an average."
- `ICT-2016-NO-FEAR-LOSING` (14:33–14:38) "we're not talking about 2% which is the industry standard here — we're talking about 1%. 1% makes millionaires"; (15:43) "what if you were to drop that risk per trade down to a half a percent."
- `ICT-2016-MITIGATE-LOSING-TRADES` (05:26–05:33) "if we took a[n] initial loss of 2% on the first trade, we have to go down to 1%. If we were trading with 1%… drop down to one half of 1%" (transcript: "a initial loss").
- `ICT-2017-HTF-MONEY-MANAGEMENT` (06:30–06:36) "ideally set 1% as the most risk per trade. That means 1% of 30% of your total equity base."
- `ICT-2017-OTE` (16:01) "we'll say it's a half a percent uh whatever half percent of your account" — the Primer's own figure, previously not carried to this page.
- `ICT-2022-MENTORSHIP-EP07` (04:44) "you should be risking less than 1% — about a half percent or a quarter percent"; same timestamp, ICT's own: "I like 3 and a half% — I'm not telling you to use 3 and a half%."
- `ICT-2022-MENTORSHIP-EP03` (48:47) "my maximum risk on a trade if I'm trading competitively is four and a half percent per trade."
- `ICT-2022-MENTORSHIP-EP41` (22:18) "ten thousand dollars is equity, you want to take one percent risk per trade"; (28:50) "eventually getting to the point where you can risk two percent"; (31:37–32:04) "you have to make back fifty percent of what you lost… before you can go back to your full one percent risk"; (32:04) "risking a half of one percent and that trade gets knocked out to a loss, what size do you use on your next trade — one quarter of one percent, and that's obviously the lowest you can go with."
