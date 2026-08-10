# 30% Capital Allocation

**Category:** 32-risk-management
**Aliases:** 30 percent rule, allocation base, tradeable equity, reserve capital, 1% of 30%
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-HTF-MONEY-MANAGEMENT
**Tags:** risk, allocation, position-trading, drawdown, managed-funds

## Definition

ICT's allocation rule caps the **base on which risk percentage is computed** at **30% of total
account equity**. The remaining 70% is never allocated. "I limit my allocation to only 30% of my
total equity. That may be shocking to some of you, but it's the truth"
(`ICT-2017-HTF-MONEY-MANAGEMENT`, 04:18–04:25).

Risk-per-trade then compounds against the smaller base: "if I'm going to be doing a percentage
basis of my equity and let's just say, for instance, that I'm going to be using the standard in
the industry of 2%, that means I'm going to be using 2% of 30,000, not 2% of 100,000" (04:44).

⚠ This changes the meaning of the familiar 1% figure. 1% under this rule is **0.3% of total
equity**, not 1%. See [risk-per-trade](risk-per-trade.md).

## Formal Criteria

- **Allocation base** = 30% of total equity. Stated for a $100k account: "that means I'm only
  going to be using $30,000 to meet whatever margin requirements or trade parameters" (04:34).
- **Risk per trade** = 1% of the allocation base, i.e. 0.3% of total equity. Worked for a $10k
  account: "your account trading is going to be based on $3,000, not $10,000… 1% of that is going
  to be $30. So $30 is your total maximum risk per trade" (06:41–07:12).
- **Minimum reward-to-risk** = 3:1 on higher-timeframe setups (07:25).
- **Drawdown ceiling** = 15% annually as the objective, 20% tolerable, 25% the point most
  investors "start to cringe" (02:03–02:23).
- **Target annual return** = 18–25%, "which is like an industry standard for managed funds"
  (09:27).
- **Expected setup frequency** = 2 position trades a year, 3 if fortunate: "I look personally for
  two, and if I'm lucky, three good position trade setups a year… Generally, rarely have I seen
  four setups in a full January to December" (24:17–24:55).

**Stated reasons for the 70% reserve** (05:01–05:47):

1. No margin calls, no over-leverage, no wild equity dips.
2. Spare capital for an opportunity that would otherwise be unaffordable — "you always have an
   opportunity to take something that may otherwise not have been on your radar screen."
3. It is what allocators want to see: "they like to see that you're not 100% exposed."

**The correlated-pair workaround.** The reserve also funds trades that offset open-profit
drawdown on the long-term position, since US retail traders cannot hedge: "while we cannot in the
US trade like a hedger… we can trade markets that are closely correlated or inversely correlated
with the long term positions that we are holding" (12:11–12:27). Worked example: short USDJPY
retracing against you → short EURUSD or GBPUSD with reserve capital (13:11–13:57). "So that's one
way you can beat the North American hedging rule" (13:57).

## Formula / Math

```
allocation_base := total_equity * 0.30
risk_$          := allocation_base * risk_pct        # risk_pct = 0.01 taught default
effective_risk_pct_of_total_equity := risk_pct * 0.30

# ICT's worked numbers
total_equity = 100_000 -> allocation_base = 30_000
total_equity =  10_000 -> allocation_base =  3_000 -> risk_$ = 30

# targets
min_RR              = 3.0
max_annual_drawdown = 0.15   (tolerable to 0.20)
target_annual_return= 0.18 .. 0.25
position_setups_per_year = 2 .. 3
```

## Machine-Readable

```json
{
  "id": "capital-allocation-30-percent",
  "category": "32-risk-management",
  "aliases": ["30-percent-rule", "allocation-base", "1-percent-of-30-percent"],
  "criteria": [
    {"id": "c1", "expr": "allocation_base == total_equity * 0.30"},
    {"id": "c2", "expr": "risk_per_trade == 0.01 * allocation_base == 0.003 * total_equity"},
    {"id": "c3", "expr": "min_reward_to_risk >= 3.0"},
    {"id": "c4", "expr": "target_max_annual_drawdown <= 0.15"},
    {"id": "c5", "expr": "target_annual_return in [0.18, 0.25]"},
    {"id": "c6", "expr": "expected_position_setups_per_year in [2, 3]"},
    {"id": "c7", "expr": "reserve funds correlated-pair offsets in place of hedging"}
  ],
  "timeframes": ["D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["risk-per-trade","position-sizing","r-multiple","correlation-risk","partial-takes","ipda-trailing-stop","quarterly-market-structure-shift"],
  "sources": ["ICT-2017-HTF-MONEY-MANAGEMENT"]
}
```

## Visual Pattern

```
   TOTAL EQUITY  $100,000
   ┌──────────────────────────────────────────────────────────┐
   │ ████████████ 30% allocated  │      70% reserve           │
   │   $30,000                   │      $70,000               │
   └──────────────────────────────────────────────────────────┘
        │                                    │
        │  1% of $30,000 = $300 risk/trade   │ funds correlated-pair
        │  = 0.3% of total equity            │ offsets + missed
        │  3:1 minimum RR                    │ opportunities
        v                                    v
   2-3 position setups/year          no margin call, ever
```

## Timeframes

Written for position / long-term trading off the daily chart with monthly and weekly context. ICT
contrasts the stop sizing directly: intraday he uses ~35 pips ("if it's 100 pip daily range
average… a third of that would be 33%. So I round it to 35 pips", 15:53–16:10); a daily-chart
setup may need 200 pips, and "just because it's a 200 pip stop loss… assume for a moment that
you're aiming for a 600 pip win. That's still a three to one reward to risk ratio" (17:11–17:24).

## Examples

**Example 1 — the $10,000 account (`ICT-2017-HTF-MONEY-MANAGEMENT`, 06:41–07:12):**
- Total equity $10,000 → allocation base $3,000.
- Risk per trade 1% of $3,000 = **$30**.
- ICT's own comment on the outcome: "Michael, I can't get rich doing this. And that's right,
  you're not going to get rich right now."

**Example 2 — the return arithmetic ICT pre-empts (24:55–26:20):**
- Two setups a year at 3:1 on 1% risk = 6% for the year, which ICT concedes is correct as far as
  it goes: "That's not attractive, Michael. That's only if you're taking one setup."
- His answer is compounding plus reserve deployment: "if you have a setup that's moved into
  profitability, now you have new equity. So that equity can be put to work as well on new trade
  setups."

## Common Mistakes

- **Computing risk % on total equity.** The whole point of the rule is that the base is 30% of
  equity. Applying 1% to the full account triples the intended exposure.
- **Reading 30% as a maximum open-position size.** It is the margin/parameter base, not a
  per-trade cap; risk-per-trade is a separate, smaller number layered on top.
- **Moving the stop to break-even.** Explicitly forbidden on this timeframe: "resist the impulse
  to move your stop loss to break even or even reducing the risk… break even on long-term trading
  is just the worst thing" (17:45–18:04).
- **Judging skill by stop size.** "Stop loss orders are not a measure of ability… that doesn't
  belong in any way, shape or form in long term trading" (14:55–15:32).
- **Expecting velocity.** "You are not going to see velocity for your money trading these higher
  time frames. It just isn't there" (20:47–21:08).

## Related Concepts

- [risk-per-trade](risk-per-trade.md) — the percentage this rule re-bases.
- [position-sizing](position-sizing.md) — the lot calculation that consumes the $-risk.
- [r-multiple](r-multiple.md) — the 3:1 minimum expressed as R.
- [correlation-risk](correlation-risk.md) — the correlated-pair offset is the same correlation structure used deliberately.
- [ipda-trailing-stop](ipda-trailing-stop.md) — the stop discipline that pairs with this allocation.
- [quarterly-market-structure-shift](../01-market-structure/quarterly-market-structure-shift.md) — the event that generates the 2–3 setups a year.

## Citations

- `ICT-2017-HTF-MONEY-MANAGEMENT` (00:00) — "Welcome back folks, this is lesson 5 of January 2017 ICT Mentorship… money management and higher timeframe analysis"; (02:03–02:23) 15% drawdown objective, 20% acceptable, 25% the cringe point; (04:18–04:44) the 30% allocation and "2% of 30,000, not 2% of 100,000"; (05:01–05:47) the three reasons for the reserve; (06:41–07:12) the $10,000 → $3,000 → $30 worked example; (07:25) "targeting 3 to 1 reward to risk for higher setups"; (09:27) "18% to 25% a year, which is like an industry standard for managed funds"; (12:11–13:57) the correlated-pair workaround for the North American hedging rule; (14:55–15:32) stop-loss size is not a measure of ability; (15:53–16:10) the 35-pip intraday rule of thumb; (17:11–17:24) 200-pip stop against a 600-pip target; (17:45–18:04) do not move to break-even; (20:47–21:08) no velocity on this timeframe; (24:17–24:55) two setups a year, three if lucky; (24:55–26:20) the 6%-a-year objection and its answer.
