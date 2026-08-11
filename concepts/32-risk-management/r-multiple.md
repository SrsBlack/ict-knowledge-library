# R-Multiple

**Category:** 32-risk-management
**Aliases:** R, R:R, R-multiple, risk-reward
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2016-GROWING-SMALL-ACCOUNTS, ICT-2016-NO-FEAR-LOSING, ICT-2017-CHARTER-OVERVIEW, ICT-2017-SWING-ELEMENTS, ICT-2017-SWING-REDUCE-RISK, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, r-multiple, foundational

## Definition

R-multiple (R, or R:R) is the **ratio of profit to risk** expressed as a multiple of the original SL distance. **R = 1** means the profit equals the risked amount; **R = 3** means the profit is 3× the risk. ICT teaches R-multiple as the universal trade-quality measurement: a 5R win is a "5R win" regardless of pips, $-amount, or instrument. Setups with target/risk ratios below 1.5R are typically deprioritized; ICT setups commonly target 3R+, with high-conviction setups (Unicorn, A+ confluence) targeting 8R+.

## Formal Criteria

For any trade:

```
R = profit_$ / risk_$
  = (TP_distance / SL_distance) for symmetric position size

# At entry:
projected_R = (target_price - entry_price) / abs(entry_price - sl_price)    # for longs

# Realized after exit:
realized_R = (exit_price - entry_price) / abs(entry_price - sl_price)
```

ICT-recommended baseline R ratios:

| Setup quality | Target R |
|---|---|
| Standard 2022/2023 model | 2R-4R |
| Silver Bullet | 3R-5R |
| OTE 0.705 with PD-array confluence | 5R-10R |
| Unicorn / A+ confluence | 8R-15R |

**Why R is the lever, not accuracy.** Raising R lowers the win rate needed to break even, so
ICT's whole risk argument runs on the ratio rather than on being right more often: 3:1 lets
you make money "when you're **wrong 66 % of the time**" (`ICT-2017-SWING-ELEMENTS`,
12:35–13:33). He calls 3:1 only *marginally* profitable and prefers **5×**, which "endures
losses much easier"; the setups with the most movement potential are the ones that offer the
better ratios.

**The working assumption is 30 %, and it is modelled, not asserted.** **30 %** recurs — the
whole of `ICT-2016-NO-FEAR-LOSING` plus `ICT-2017-SWING-REDUCE-RISK` 07:29 — and **34 %**
appears once (`ICT-2017-SWING-ELEMENTS` 12:38). 30 % is the convention ICT works to when he
builds a P&L model.

⚠ **Corrected 2026-08-11 on reading the primary source.** This page previously stated that the
corpus contains only three accuracy figures and that "every figure ICT quotes sits above" the
arithmetic breakeven of 25 % at R=3. **Both claims were wrong.**
`ICT-2016-GROWING-SMALL-ACCOUNTS` (07:40–09:08) enumerates a **six-row table**, not a stray
33 %, and its last row is exactly the arithmetic breakeven:

| Accuracy | Minimum reward:risk | `1/(1+R)` |
|---|---|---|
| 75 % | "very low" — no ratio given | — |
| 60 % | lower still — no ratio given | — |
| 50 % | **1:1** | 50.0 % |
| 40 % | **1.5:1** | 40.0 % |
| 33 % | **2:1** | 33.3 % |
| **25 %** | **3:1** | **25.0 %** |

"At 25 % accuracy… If 75 % of the trades that you take are losing trades, the minimum ratio for
profitability is you have to look for trades that pay out 3 to 1" (08:51–09:08). The table *is*
the breakeven curve, taught as a floor. The 33 % row is not a one-off phrasing of 30 %; it is
the 2:1 row of that curve. See [six-percent-monthly-model](six-percent-monthly-model.md).

The two facts coexist: ICT teaches the breakeven curve as the **minimum**, and then models
expected P&L at **30 %** — above the R=3 minimum, which is what makes those models show a profit
rather than a wash.

`ICT-2016-NO-FEAR-LOSING` builds the whole case arithmetically on a $5,000 account, 10 trades
a month, **30 % accuracy** (7 losses in 10):

| Risk/trade | R | Wins | Losses | Net | Monthly return |
|---|---|---|---|---|---|
| 1 % | **3:1** | 3 × $150 = $450 | 7 × $50 = $350 | **+$100** | **2 %** — "marginally eke out a net positive" |
| 1 % | **5:1** | 3 × $250 = $750 | 7 × $50 = $350 | **+$400** | **8 %** |
| 2 % | **5:1** | 3 × $500 = $1,500 | 7 × $100 = $700 | **+$800** | **16 %** |

The point ICT draws is about fund management, not size: 2 % a month compounded "is an
absolutely amazing return for managed funds" (06:40–07:21).

⚠ The **arithmetic** breakeven at R=3 is **25 %**, and ICT quotes that figure directly (see the
table above). Treat 25 % at R=3 as the taught *minimum* and 30 % as the figure his worked P&L
models assume.

`ICT-2017-SWING-REDUCE-RISK` also sets the practical expectation for swing setups framed on
monthly/weekly arrays with four-hour entries: 3:1 is the floor and hard to find, "many times
it's going to be five to one, ten to one is not unheard of", and higher-timeframe ranges of
**200–500 pips can yield up to 10R** (07:00–07:29, 11:41–12:22).

## Formula / Math

```
R = abs(target - entry) / abs(entry - sl)

# Example: long entry 1.0830, SL 1.0815, TP 1.0885
# risk = 1.0830 - 1.0815 = 15 pips
# reward = 1.0885 - 1.0830 = 55 pips
# R = 55 / 15 = 3.67R

# Breakeven accuracy required at a given R:
breakeven_win_rate(R) = 1 / (1 + R)
#   R = 1   -> 50.0%   <- ICT: 50% accuracy needs 1:1
#   R = 1.5 -> 40.0%   <- ICT: 40% accuracy needs 1.5:1
#   R = 2   -> 33.3%   <- ICT: 33% accuracy needs 2:1
#   R = 3   -> 25.0%   <- ICT: 25% accuracy needs 3:1   (quoted verbatim, 08:51)
#   R = 5   -> 16.7%
# ICT teaches this curve as the MINIMUM (ICT-2016-GROWING-SMALL-ACCOUNTS, 07:40-09:08)
# and separately models expected P&L at a 30% accuracy convention.
```

## Machine-Readable

```json
{
  "id": "r-multiple",
  "category": "32-risk-management",
  "aliases": ["R", "R:R", "risk-reward"],
  "criteria": [
    {"id": "c1", "expr": "R = abs(target - entry) / abs(entry - sl)"},
    {"id": "c2", "expr": "minimum target typically 1.5R-2R"},
    {"id": "c3", "expr": "high-conviction targets 5R+"},
    {"id": "c4", "expr": "breakeven_win_rate(R) == 1/(1+R); ICT teaches this curve as the MINIMUM and quotes 25% at 3:1 verbatim"},
    {"id": "c5", "expr": "HTF ranges of 200-500 pips with H4 entries can yield up to 10R"},
    {"id": "c6", "expr": "taught minimum-R table: 50%->1:1, 40%->1.5:1, 33%->2:1, 25%->3:1"},
    {"id": "c7", "expr": "worked P&L models assume a 30% accuracy convention, above the R=3 minimum"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["risk-per-trade","position-sizing","stop-placement-by-pd-array","partial-takes","swing-trading-hallmarks","six-percent-monthly-model","loss-mitigation-half-size-reentry"],
  "sources": ["ICT-2016-GROWING-SMALL-ACCOUNTS","ICT-2016-NO-FEAR-LOSING","ICT-2017-CHARTER-OVERVIEW","ICT-2017-SWING-ELEMENTS","ICT-2017-SWING-REDUCE-RISK","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   R-multiple visualization:

   target ──────  + 5R     <- target at 5R level (5× SL distance above entry)
                 |
                 |
   entry  ──────  0R       <- entry
                 |
   SL     ──────  -1R      <- SL = 1R loss
                 |
   1R unit = SL distance
```

## Timeframes

All TFs.

## Examples

**Example 1 — computing R for a setup:**
- Entry 1.0830, SL 1.0815, TP1 1.0860, TP2 1.0890.
- 1R = 15 pips.
- TP1 = 30 pips = 2R.
- TP2 = 60 pips = 4R.
- → setup has 2R/4R partial-take structure.

## Common Mistakes

- **Mixing $-amount with R.** Always think in R; $ amounts vary by account size and position.
- **Targeting 1R or less.** Setups with TP ≤ 1R have no edge after slippage and commission.
- **Stretching for big R without confluence.** Aiming for 10R when the setup only justifies 4R produces frequent missed targets.

## Related Concepts

- [risk-per-trade](risk-per-trade.md), [position-sizing](position-sizing.md), [stop-placement-by-pd-array](stop-placement-by-pd-array.md), [partial-takes](partial-takes.md).
- [six-percent-monthly-model](six-percent-monthly-model.md) — the primary source for the accuracy/minimum-R table above.
- [loss-mitigation-half-size-reentry](loss-mitigation-half-size-reentry.md) — where R2 at half size becomes the recovery threshold.

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- `ICT-2016-GROWING-SMALL-ACCOUNTS` (00:23) "This is month two of the ICT Mentorship. This is **teaching one of eight of the second month of twelve**"; (05:23–05:40) "Identify trade setups that permit **three reward multiples to one risk or higher**"; (07:20–07:33) "accuracy is not even necessary in terms of high end accuracy to make money… but you do need **time**"; (07:40–09:08) ⚠ **the accuracy → minimum-ratio table** — 75 %, 60 %, then 50 % → "you got to start risking $1 for $1", 40 % → "$1.50 for every $1", 33 % → "$2 for every $1 risk", and **25 % → "the minimum ratio for profitability is you have to look for trades that pay out 3 to 1"**; (09:08–09:41) "we can be wrong 75 % of the time and still be net profitable"; (15:26–15:48) the 6 %/month model at 1.5 % risk and 1:1; (28:04–28:07) the worked example is "a five to one setup". ⚠ Previously referenced on this page as an unlinked italic mention with the ID missing from both header and JSON — corrected 2026-08-11 along with the "every figure sits above 25 %" claim it was cited to support.
- `ICT-2017-SWING-ELEMENTS` (12:35–13:33) "probabilities reward diligence… limiting setups to three to one reward risk permits as low as 34 % accuracy to be net profitable… that means you're making money when you're wrong 66 % of the time"; 5× risk preferred as it "endures losses much easier"; "the setups that we have the most movement potential offer the better risk to reward ratios."
- `ICT-2017-SWING-REDUCE-RISK` (07:00–07:29) "use nothing less than three to one reward to risk ratios… many times it's going to be five to one, ten to one is not unheard of"; (07:29–07:54) "when you trade with reward to risk ratio conditions, you only need to be accurate 30 % of the time to be profitable… you can lose 70 % of the time if you're trading with three to one"; (11:41–12:22) R-multiple defined as reward on the risk associated with the trade, with professionals putting "very little money at risk to get huge price moves"; (12:14–12:26) "higher time frame levels that offer ranges of 200 to 500 pips, they can yield up to 10 R wins".
- `ICT-2016-NO-FEAR-LOSING` (00:30) "the fourth installment of month two of the ICT Mentorship… why losing on trades won't affect your profitability"; (04:42–06:32) the $5,000 / 10-trade / **30 % accuracy** model at 3:1 and 1 % risk — three wins of $150 against seven losses of $50, "you still can marginally eke out a net positive profit"; (06:40–07:21) 2 % a month "is an astronomical return for managed funds"; (07:21–08:33) the same 30 % accuracy at 5:1 returning 8 %; (08:40–09:28) 5:1 at 2 % risk. ⚠ Classified NOT-A-CONCEPT in the distillation backlog (trading psychology) and correctly so — it is cited here only for the arithmetic, which is not psychology.
