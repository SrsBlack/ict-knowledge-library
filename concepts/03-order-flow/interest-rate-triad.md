# Interest Rate Triad

**Category:** 03-order-flow
**Aliases:** interest rate triad, rate triad, 30-10-5 divergence, interest rate divergence, yield triad
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-RATE-TRIAD
**Tags:** order-flow, intermarket, bonds, interest-rates, dollar-index, smt, validation, accumulation-distribution

## Definition

The interest rate triad is the **30-year bond, 10-year note and 5-year note read against each
other** to detect smart-money accumulation and distribution: "interest rate triads provide a
visual depiction of smart money accumulation and distribution"
(`ICT-2016-RATE-TRIAD`, 01:06).

Its job is narrow and specific — it is a **validation filter for a PD array**, not a bias
generator. When price reaches an order block, liquidity pool, liquidity void or fair value gap
on the dollar index, the triad answers whether smart money is actually working that level: "if
there is **no obvious indication** that they are moving large funds, **pass on the trade idea**
and look for new ones that do" (19:01–19:10).

The premise underneath is stated flatly: "**interest rates are the single most influential
driving force behind market moves**" (00:38–00:47).

## Formal Criteria

**The three instruments** (01:15–01:43)

| Instrument | Curve position |
|---|---|
| **30-year bond** | long-term interest-rate benchmark |
| **10-year note** | intermediate-term |
| **5-year note** | short-term |

All three are futures markets; ICT names **barchart.com** as the free data source (09:23).

**The signal — a failure swing in one of the three** (07:35–08:47)

- Baseline expectation: at a significant dollar-index price point, **all three should confirm
  each other's higher high or lower low** (07:17).
- The signal is one instrument **failing** to make the matching swing: "you just need **one** to
  break that pattern… when it happens it invariably will show smart money participation in the
  marketplace" (07:44–07:56).
- That failure is the **interest-rate shift**, and it validates the dollar-index array being
  tested.

**The pairing rule** (08:38–09:23, 19:10–20:14)

| Dollar-index setup | What the triad should show |
|---|---|
| **Bullish** DXY at a discount array (bullish OB, old low, FVG) | the three should be making **higher highs** as the dollar makes a lower low — with **one failing** to make its higher high |
| **Bearish** DXY at a premium array (bearish OB, old high, FVG) | the three should be making **lower lows** — with **one failing** to make its lower low |

**Direction convention** (20:03–20:20)

- Rate-instrument **price up = interest rates down = bearish for the dollar**.
- Rate-instrument **price down = interest rates up = bullish for the dollar**.

**The order of operations** (13:09–13:25, 18:23–19:10)

- "You **don't go into looking at the bond market just for these types of scenarios** — you have
  to have a **predetermined idea** of what the market that you're about to trade should see in
  terms of bullishness or bearishness."
- Sequence: price reaches a focus point (order block / liquidity pool / liquidity void / fair
  value gap) → **then** consult the triad and the dollar index → confirm or pass.

**The general accumulation / distribution frame** (02:44–06:39)

The triad is one instance of a broader comparison ICT teaches with a **base asset or benchmark**
(Dow Jones for stocks, dollar index for currencies, CRB index for commodities):

- **Distribution:** the benchmark makes **higher highs** while closely correlated assets make
  **lower highs** — the rally is heavy selling, not new buying.
- **Accumulation:** the benchmark makes **lower lows** while correlated assets make **higher
  lows** — heavy demand will not let price go to a discount.

## Formula / Math

```
triad := { ZB_30y , ZN_10y , ZF_5y }

# --- baseline (no signal) ---
symmetric := all three confirm the same higher_high (or the same lower_low)

# --- the signal ---
failure_swing := exactly one (or more) of the triad FAILS to make
                 the swing the other two made

# --- pairing with the dollar index ---
validate_long_DXY  := DXY at a discount array
                      AND triad expected to make higher highs
                      AND >= 1 member FAILS to make its higher high

validate_short_DXY := DXY at a premium array
                      AND triad expected to make lower lows
                      AND >= 1 member FAILS to make its lower low

# --- direction convention ---
rate_instrument_price DOWN  =>  interest rates UP    =>  DXY bullish
rate_instrument_price UP    =>  interest rates DOWN  =>  DXY bearish

# --- the gate ---
if NOT failure_swing at the moment price hits the array:
    PASS on the trade idea
```

## Machine-Readable

```json
{
  "id": "interest-rate-triad",
  "category": "03-order-flow",
  "aliases": ["rate-triad", "30-10-5-divergence", "interest-rate-divergence"],
  "criteria": [
    {"id": "c1", "expr": "triad == {30y_bond, 10y_note, 5y_note} futures"},
    {"id": "c2", "expr": "baseline := all three confirm the same higher_high or lower_low"},
    {"id": "c3", "expr": "signal := >=1 member fails that swing (a failure swing)"},
    {"id": "c4", "expr": "signal must coincide with price reaching a DXY PD array"},
    {"id": "c5", "expr": "rate_price_down => rates_up => DXY_bullish"},
    {"id": "c6", "expr": "no failure swing at the array => pass on the trade"},
    {"id": "c7", "expr": "requires a predetermined directional idea BEFORE consulting the triad"},
    {"id": "c8", "expr": "general frame: benchmark higher_highs + correlates lower_highs => distribution; benchmark lower_lows + correlates higher_lows => accumulation"},
    {"id": "c9", "expr": "supplies validation, not bias and not entry"}
  ],
  "timeframes": ["H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["macro-to-micro-framework", "bond-yield-analysis", "dollar-index", "interest-rate-differentials", "smt-divergence", "index-smt", "institutional-order-flow", "order-block-criteria"],
  "sources": ["ICT-2016-RATE-TRIAD"]
}
```

## Visual Pattern

```
   THE TRIAD AT A DOLLAR-INDEX DISCOUNT ARRAY

    5-year   ___╱‾‾╲___╱‾‾‾   higher high        ✓ confirms
   10-year   ___╱‾‾╲___╱‾‾    unchanged / flat   ~ neutral
   30-year   ___╱‾‾╲__╱‾      LOWER high         ✗ FAILURE SWING
                                                   └── the signal

   DXY       ‾‾‾╲___╱          lower low into a bullish order block
                  ▲
                  └── validated: smart money is working this level

   ─────────────────────────────────────────────────────────────
   NO failure swing at the array?  ->  PASS. Find another idea.

   GENERAL FRAME (any benchmark)

     DISTRIBUTION            ACCUMULATION
     benchmark  ╱‾  HH       benchmark  ╲_  LL
     correlate  ╱‾  LH  ✗    correlate  ╲_  HL  ✗
     "strength" is selling   "weakness" is buying
```

## Timeframes

The worked example runs on a **90-minute** chart over 15–18 days; the frame is intraday-to-daily
swing validation, not a macro horizon. For the multi-month horizon see
[macro-to-micro-framework](macro-to-micro-framework.md).

## Examples

**Example — dollar index at 99.50, December (`ICT-2016-RATE-TRIAD`, 10:12–17:47):**
- Setup: the dollar index sold down into **99.50** — an **old order block** from mid-November
  that had already been respected once on 15 November — and rallied aggressively away.
- The triad on a 90-minute chart, 5th–8th of the month:
  - **30-year bond:** a clear **failed higher high** — a lower high.
  - **10-year note:** relatively unchanged; neither a lower high nor a considerable higher high.
  - **5-year note:** a clear **higher high**.
- Read: a pronounced shift across the curve at precisely the moment the dollar index made a
  lower low into the order block. "That gives you the green light to go in and start refining
  the idea on that trade because it's most likely a high probability set up" (15:22–15:48).
- Cascade: dollar bullish → EURUSD sold. Price rallied through 1.0815–1.0820 clearing buy stops
  up to 1.0865, an old low, and rolled over. GBPUSD failed to make a higher high while EURUSD
  made one and the dollar index made a lower low — a second confirmation.
- ICT's caveat: "it doesn't always work like that; sometimes there's a shift that takes place on
  a longer term basis and it may mess up things on a short term basis" (17:56–18:10).

## Common Mistakes

- **Using it to generate a bias.** It validates a level you already had a reason to care about.
  ICT states the order of operations explicitly.
- **Requiring all three to diverge.** One failure swing is the signal; the worked example has
  one clear failure, one confirmation and one neutral.
- **Reading rate-instrument price as yield.** They are inverse — falling bond price means rising
  rates, which is dollar-bullish.
- **Treating a failure swing alone as a trade.** "By itself it doesn't mean anything" (11:41);
  it must coincide with price hitting the array.
- **Confusing it with [interest-rate-differentials](interest-rate-differentials.md).** That page
  compares **policy rates between two central banks**; this one compares **three points on one
  country's yield curve**.
- **Confusing it with [macro-to-micro-framework](macro-to-micro-framework.md).** That framework
  uses the 30-year and 10-year for a **3–6 month directional outlook**; the triad adds the
  5-year and works at **swing-validation** scale.
- **Skipping the pass rule.** No divergence at the array means no trade — that is the deliverable.

## Related Concepts

- [macro-to-micro-framework](macro-to-micro-framework.md) — the same debt-market logic at a 3–6 month horizon, without the 5-year.
- [bond-yield-analysis](bond-yield-analysis.md) — the 10-year seasonal regime read; its lesson refers to qualifying an idea "with an interest rate triad".
- [dollar-index](dollar-index.md) — the benchmark the triad is always paired against.
- [interest-rate-differentials](interest-rate-differentials.md) — policy-rate spreads; a different mechanism entirely.
- [smt-divergence](../16-smt-divergence/smt-divergence.md), [index-smt](../16-smt-divergence/index-smt.md) — the divergence logic applied elsewhere.
- [order-block-criteria](../07-order-blocks/order-block-criteria.md) — the arrays this filter validates.
- [swing-trading-hallmarks](../31-models/swing-trading-hallmarks.md) — hallmark 3, "interest rate markets support the trade", in its most mechanical form.

## Citations

- `ICT-2016-RATE-TRIAD` (00:26–00:56) "smart money accumulation, distribution fundamentally speaking… **interest rates are the single most influential driving force behind market moves**"; (01:06–01:15) "interest rate triads provide a visual depiction of smart money accumulation and distribution"; (01:15–01:50) the 30-year bond, 10-year note and 5-year note as long, intermediate and short-term rates, all futures markets; (01:58–02:07) "failure swings at opportunistic times can validate institutional order flow"; (02:55–04:19) distribution — the benchmark making higher highs while correlated assets make lower highs; (04:24–06:39) accumulation — the benchmark making lower lows while correlates make higher lows, "because that is the basis of supply and demand"; (07:17–07:35) "the three interest rates should confirm each higher high or lower low at moments when the US dollar index is at a significant price point"; (07:44–08:25) "you just need one to break that pattern… it invariably will show smart money participation"; (08:38–09:23) the pairing with a dollar-index bullish order block; (09:23–09:43) barchart.com as the free data source; (10:12–11:11) the dollar index at 99.50 and the aggressive rally away; (11:11–11:41) the 30-year failure swing on the 90-minute chart between the 5th and 8th; "now when this takes place by itself it doesn't mean anything"; (11:41–12:39) the 10-year unchanged and the 5-year clear higher high — "that highlights there's a shift in the interest rate market"; (13:09–13:25) "you don't go into looking at the bond market just for these types of scenarios — you have to have a predetermined idea"; (13:25–14:00) the divergence against the dollar index lower low; (14:00–15:06) the November order block retested on 8 December at 99.50 and strongly rejected; (15:22–15:48) "if you can see the interest rate divergence or interest rate triad… and price is hitting a specific order block on the dollar index, that gives you the green light"; (15:48–17:17) the EURUSD and GBPUSD cascade; (17:17–17:47) "what makes that strong dollar so significant is that it had a divergence in the interest rate triad"; (17:56–18:10) the caveat that longer-term shifts can disrupt the short-term read; (18:23–19:10) the action plan — at an order block, liquidity pool, liquidity void or fair value gap, "you refer to the interest rate triad and dollar index… if there is no obvious indication that they are moving large funds, pass on the trade idea"; (20:03–20:20) the price/rate/dollar direction convention.
