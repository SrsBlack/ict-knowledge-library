# R-Multiple

**Category:** 32-risk-management
**Aliases:** R, R:R, R-multiple, risk-reward
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-SWING-ELEMENTS, ICT-2022-MENTORSHIP-OVERVIEW
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

**Why R is the lever, not accuracy** (`ICT-2017-SWING-ELEMENTS`, 12:35–13:33). Raising R
lowers the win rate needed to break even: "limiting setups to **three to one** reward risk
permits as low as **34 % accuracy** to be net profitable… that means you're making money
when you're **wrong 66 % of the time**." ICT calls 3:1 only *marginally* profitable and
prefers **5×** risk, which "endures losses much easier". The setups with the most movement
potential are the ones that offer the better ratios.

## Formula / Math

```
R = abs(target - entry) / abs(entry - sl)

# Example: long entry 1.0830, SL 1.0815, TP 1.0885
# risk = 1.0830 - 1.0815 = 15 pips
# reward = 1.0885 - 1.0830 = 55 pips
# R = 55 / 15 = 3.67R

# Breakeven accuracy required at a given R:
breakeven_win_rate(R) = 1 / (1 + R)
#   R = 1  -> 50.0%
#   R = 3  -> 25.0%   (ICT quotes 34% as the net-profitable floor once costs are carried)
#   R = 5  -> 16.7%
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
    {"id": "c4", "expr": "breakeven_win_rate(R) == 1/(1+R); R=3 quoted as ~34% net-profitable floor"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["risk-per-trade","position-sizing","stop-placement-by-pd-array","partial-takes"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
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

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- `ICT-2017-SWING-ELEMENTS` (12:35–13:33) "probabilities reward diligence… limiting setups to three to one reward risk permits as low as 34 % accuracy to be net profitable… that means you're making money when you're wrong 66 % of the time"; 5× risk preferred as it "endures losses much easier"; "the setups that we have the most movement potential offer the better risk to reward ratios."
