# Swing Trading Hallmarks

**Category:** 31-models
**Aliases:** elements of successful swing trading, swing trade validity checklist, swing hallmarks
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-SWING-ELEMENTS
**Tags:** models, swing-trading, checklist, filtering, rule-based, risk-management

## Definition

Swing trading hallmarks are ICT's **seven-item checklist for judging whether a swing trade
is valid**, taught as lesson 2 of the February 2017 swing-trading month. The list is
explicitly **cumulative and not all-required**: "there's going to be times where you don't
have every one of these things on the list in your favour, but the trade will still be
viable… the larger amount of things on this list that I can accumulate to build the idea
that my trade is valid, the more likely the trade does pan out"
(`ICT-2017-SWING-ELEMENTS`, 02:07–02:28).

⚠ **Not the same list as [explosive-market-selection](explosive-market-selection.md).** That
page is lesson 7 of the *same month* and asks a different question — *which market will move
explosively* — with numeric gates (recentred COT line, 10–15 % open-interest change,
15-period Williams %R). This page asks *is this trade valid at all*. The two overlap on COT,
seasonals and intermarket analysis and are otherwise distinct.

## Formal Criteria

**The seven hallmarks** (00:19–01:55)

1. **Obvious trend on the higher-timeframe charts** — the market has left consolidation and
   is moving, or clearly wants to move, in one direction.
2. **Institutional order flow on HTF must be clear** — unambiguous indication of higher or
   lower.
3. **Interest-rate markets support the trade** — rates rising or falling, or a **divergence
   in the yields** signalling an imminent shift.
4. **COT data confirming** — *"not required or necessary, but this can enhance the
   probabilities"* (01:13).
5. **Opposing premium-to-discount arrays are obvious** on the monthly, weekly and daily.
6. **Seasonal tendency aligned** — again *"not required, but it does enhance the probability"* (01:36).
7. **Supporting intermarket analysis confirms the idea.**

**Institutional sponsorship, measured by relative strength** (04:08–04:52)

- Buying: EURUSD makes a **lower low** while the **dollar index fails to make a higher high**
  — dollar weakness, and the pair's lower low ran sell stops before the move up.
- Shorting: USDCHF makes a **lower high** while the **dollar index makes a higher high**.
- ICT names this directly: "it would be **SMT divergence** ideas to measure institutional
  sponsorship" (04:44).

**Bank accumulation and distribution, read off the candles** (04:52–06:41)

- **Bullish:** every **down candle** becomes support and is followed by higher prices; broken
  swing highs are followed by higher highs. Banks "have to buy when the algorithm permits
  them an opportunity to buy at a lower price" — they do not buy at premium.
- **Bearish:** every **up candle** becomes resistance and is followed by lower prices; broken
  swing lows are followed by lower lows.
- Summary rule: "we measure accumulation from the banks by buying at down candles and we
  measure bank distribution at up candles as resistance" (06:28).

**Setup quality — demand clean price action** (06:42–09:30)

- PD arrays above and below current price must be **obvious and easy to identify**: liquidity
  voids, mitigation blocks, breakers, fair value gaps, rejection blocks, order blocks, old
  highs and lows.
- **Price not traded at in recent weeks or months leaves an imbalance on the monthly and
  weekly — a high draw on price.** At equilibrium, expect a move to an imbalance: out of
  consolidation to a premium if rising, to a deep discount if falling.
- **The self-argument test:** "if you're having to convince yourself, chances are it's
  probably not a good trade. **Pass on it**" (09:17). The trades that "literally leap off the
  chart" are the high-probability ones.
- Price should be respecting **institutional levels**: the big-figure 00 levels, the 50
  mid-figure, the 80 and 20 levels, and the smaller 30s and 70s.

**Rule-based filtering** (09:38–11:04)

- Rules are **standardized and static** — the same procedure on every setup, no per-trade
  variation.
- A setup that **fails** the filter is passed on, **period, no exceptions**.
- The rule outranks the mentor: "if your rule-based idea says you can't take that trade and
  you hear me say I like to take that trade, **you don't side with ICT, you side with your
  rule-based ideas**" (10:23).
- A setup that **passes** is executed **only if risk and equity management permit**. An open
  risk allocation that is already full means the new setup is passed on, or an existing
  position is closed to make room — the money-management rule is never broken to take a
  setup (10:42–12:21).

**Reward-to-risk arithmetic** (12:35–13:33)

- **3:1 permits as low as 34 % accuracy to be net profitable** — "marginally profitable…
  you're making money when you're wrong 66 % of the time".
- **5:1 raises the odds further and makes losses easier to endure.**
- Setups with the most movement potential offer the better ratios.

## Formula / Math

```
# --- the checklist ---
hallmarks := [ obvious_HTF_trend
             , HTF_institutional_order_flow_clear
             , interest_rate_market_supports        # incl. yield divergence
             , COT_confirms                         # optional, enhancing
             , opposing_PD_arrays_obvious_on(M, W, D)
             , seasonal_tendency_aligned            # optional, enhancing
             , intermarket_analysis_confirms
             ]
validity := count(true in hallmarks)                # cumulative; no threshold taught

# --- sponsorship via relative strength (SMT) ---
long_sponsorship  := pair makes lower_low  AND DXY fails to make higher_high
short_sponsorship := pair makes lower_high AND DXY makes higher_high

# --- bank accumulation / distribution ---
accumulation := for each down_candle: acts_as_support AND higher_prices_follow
distribution := for each up_candle:   acts_as_resistance AND lower_prices_follow

# --- the execution gate ---
execute := passes_static_rule_filter AND risk_and_equity_management_permits
# failing either => pass on the trade, no exception

# --- breakeven accuracy ---
breakeven_win_rate(R) = 1 / (1 + R)
   R = 3  ->  0.25 ;  ICT quotes 34% as the net-profitable floor after costs
   R = 5  ->  0.167
```

## Machine-Readable

```json
{
  "id": "swing-trading-hallmarks",
  "category": "31-models",
  "aliases": ["elements-of-successful-swing-trading", "swing-trade-validity-checklist"],
  "criteria": [
    {"id": "c1", "expr": "obvious_trend_on_HTF == true"},
    {"id": "c2", "expr": "HTF_institutional_order_flow_clear == true"},
    {"id": "c3", "expr": "interest_rate_market_supports_direction == true"},
    {"id": "c4", "expr": "COT_confirms == optional_enhancing"},
    {"id": "c5", "expr": "opposing_premium_discount_arrays_obvious_on(M,W,D) == true"},
    {"id": "c6", "expr": "seasonal_tendency_aligned == optional_enhancing"},
    {"id": "c7", "expr": "intermarket_analysis_confirms == true"},
    {"id": "c8", "expr": "sponsorship measured via SMT divergence vs dollar_index"},
    {"id": "c9", "expr": "accumulation := down_candles act as support; distribution := up_candles act as resistance"},
    {"id": "c10", "expr": "if trader must argue himself into the setup => pass"},
    {"id": "c11", "expr": "rules static; failing setup passed with no exception; mentor opinion does not override"},
    {"id": "c12", "expr": "execution additionally gated by risk_and_equity_management"},
    {"id": "c13", "expr": "R>=3 permits ~34% accuracy to be net profitable; R>=5 preferred"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["explosive-market-selection", "mega-trade", "smt-divergence", "institutional-order-flow", "commitment-of-traders", "seasonal-tendency", "bond-yield-analysis", "r-multiple", "risk-per-trade", "pd-array-hierarchy"],
  "sources": ["ICT-2017-SWING-ELEMENTS"]
}
```

## Visual Pattern

```
  THE SEVEN HALLMARKS (cumulative — more met, higher probability)

    1 obvious HTF trend            ▓▓▓
    2 HTF order flow clear         ▓▓▓
    3 interest rates support       ▓▓▓
    4 COT confirms                 ░░░   optional, enhancing
    5 opposing PD arrays obvious   ▓▓▓   on M, W and D
    6 seasonal aligned             ░░░   optional, enhancing
    7 intermarket confirms         ▓▓▓

  BANK ACCUMULATION vs DISTRIBUTION — read off the candles

    bullish:   ▼ becomes support      bearish:   ▲ becomes resistance
        ╱‾╲  ▼  ╱‾‾╲  ▼  ╱‾‾‾              ╲__ ▲ ╲___ ▲ ╲___
        every down candle held             every up candle capped

  THE TWO GATES BEFORE EXECUTION

    setup ──► [ static rule filter ] ──► [ risk & equity permit? ] ──► execute
                    │ fail                      │ no
                    ▼                           ▼
                  PASS                    PASS or close something first
```

## Timeframes

Daily, weekly and monthly. This is a swing-trade validity check; it has no intraday form.

## Examples

The lecture is deliberately theory-only — "there's not a lot of charts in this one, it's all
theory" (03:52). Two worked illustrations are given verbally:

**Example 1 — sponsorship by relative strength (04:15–04:44):**
- Buying EURUSD on a **lower low** while the **dollar index makes a lower high**.
- The dollar's failure to make a higher high is the weakness; the pair's lower low ran the
  sell stops that fund the move up.
- Shorting mirror: USDCHF on a **lower high** while the dollar index makes a **higher high**.

**Example 2 — the risk-allocation trade-off (11:13–12:21):**
- Position open: long gold, expecting 1240.
- Competing setup: soybeans, expecting a full-dollar move.
- Decision: soybeans may pay more and faster ("more velocity with your money"), so the
  choice is to **switch**, not to add. Taking both when risk limits are full is not an option.

**Homework (pedagogy, not criteria, 13:46–22:12):** students were required to write a **mock
trading plan** before lesson 3 — opportunity definition, setup framing, profit objectives,
risk management, and the filter process — so their pre-existing understanding was on record
before the model was given.

## Common Mistakes

- **Treating the list as all-required.** It is cumulative; COT and seasonals are explicitly
  optional enhancers.
- **Confusing it with [explosive-market-selection](explosive-market-selection.md).** Same
  month, different lesson, different question, different (numeric) criteria.
- **Arguing yourself into a setup.** ICT's own test: if you have to convince yourself, pass.
- **Breaking risk rules for a good setup.** The setup being valid is *necessary*, not
  sufficient — equity management is a separate gate.
- **Overriding your own rules because ICT liked a trade.** Named explicitly as the wrong move.
- **Reading "34 % accuracy" as a target.** It is the *floor* at which 3:1 stops losing money,
  and ICT calls the result only marginally profitable.
- **Reading down-candle-as-support as an order-block definition.** Here it is a *diagnostic*
  of ongoing bank accumulation across a swing, not the single-candle criterion.

## Related Concepts

- [explosive-market-selection](explosive-market-selection.md) — the eight-hallmark market-selection list from lesson 7 of the same month.
- [mega-trade](mega-trade.md) — the position-scale expression of the same qualification stack.
- [smt-divergence](../16-smt-divergence/smt-divergence.md) — the sponsorship measurement named in the lecture.
- [institutional-order-flow](../03-order-flow/institutional-order-flow.md) — hallmark 2.
- [bond-yield-analysis](../03-order-flow/bond-yield-analysis.md) — how hallmark 3 is judged.
- [commitment-of-traders](../03-order-flow/commitment-of-traders.md), [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — the two optional enhancers.
- [pd-array-hierarchy](../05-pd-arrays/pd-array-hierarchy.md) — hallmark 5's premium/discount reading.
- [r-multiple](../32-risk-management/r-multiple.md) — where the 3:1 / 34 % arithmetic is recorded.
- [risk-per-trade](../32-risk-management/risk-per-trade.md) — the equity-management gate.

## Citations

- `ICT-2017-SWING-ELEMENTS` (00:00) "this is February 2017, Swing Trading Lesson Number 2, The Elements to Successful Swing Trading"; (00:19–01:55) the seven hallmarks, with COT and seasonals flagged "not required… but this can enhance the probabilities"; (02:07–02:35) the list is cumulative — "the larger amount of things on this list that I can accumulate… the more likely the trade does pan out"; (03:52) "there's not a lot of charts in this one, it's all theory"; (04:08–04:52) institutional sponsorship via relative strength, "it would be SMT divergence ideas to measure institutional sponsorship"; (04:52–06:41) bank accumulation at down candles and distribution at up candles, "they do not buy at premium prices"; (06:42–07:38) demand obvious PD arrays above and below; (07:38–08:18) untraded price leaves a monthly/weekly imbalance that is a high draw on price; (08:18–09:25) "the cleanest price action are the most favorable markets to trade in" and "if you're having to convince yourself, chances are it's probably not a good trade — pass on it"; (09:28–09:38) institutional levels — big figures, 50s, 80s, 20s, 30s and 70s; (09:51–10:35) rule-based conceptual methods, static rules, "you don't side with ICT, you side with your rule-based ideas"; (10:42–12:21) the risk- and equity-management gate and the gold-versus-soybeans allocation example; (12:35–13:33) "limiting setups to three to one reward risk permits as low as 34 % accuracy to be net profitable… you're making money when you're wrong 66 % of the time", and 5× risk as the better frame; (13:46–22:12) the mock-trading-plan homework; (19:26) "the setups I do in terms of swing trading… it's only two".
