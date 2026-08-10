# Premium vs Carrying Charge Market

**Category:** 03-order-flow
**Aliases:** carrying charge market, premium market, delivery-month premium, nearby vs next month out
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-CARRYING-CHARGE
**Tags:** order-flow, commodities, futures, delivery-months, supply-demand, bias

## Definition

A futures term-structure read for commodities. Comparing the **nearby contract**
against the **next month out** answers whether the market is willing to pay up for
immediate delivery:

- **Carrying charge market** — no premium. Each successive delivery month prices
  *higher* than the one before, reflecting the cost of storing and carrying the
  physical commodity forward. This is the normal state.
- **Premium market** — the nearby contract prices *higher* than the months after it.
  Buyers are paying up to take delivery now, which ICT reads as **demand high and
  supply short** (`ICT-2017-CARRYING-CHARGE`, 05:32).

This is one of the few places ICT works with literal supply and demand: "you've never
really heard me talk about supply and demand because I think that way of trading,
especially as it relates to Forex, isn't [useful]… but there are **real supply and
demand factors with commodities** because they're real tangible things" (05:37).

## Formal Criteria

- Applies to **commodity futures** only — it requires a delivery-month curve.
- Compare the **nearby contract** (first delivery month) against the **next month out**
  (02:28–02:42).
- **Carrying charge:** successive months step *up* in price. Worked example — July 2017
  soybeans at 940, August higher, November 945, January 2018 952 (03:01–03:30).
- **Premium:** the nearby prices *above* the later months. "If the price today's nearby
  contract is higher than the contract delivery months that are after it in terms of the
  calendar going forward" (06:09).
- **Strength test:** to gauge whether a premium is significant, "go out to the next month
  beyond" and check the premium persists further along the curve (04:46–04:58).
- **Cadence:** review **every two to three weeks**, not daily (01:05).
- **Interpretation:** a premium means commercials "will be looking to take delivery of it
  right now immediately" rather than wait and pay the expected carrying charge later
  (06:25–06:40).

## Formula / Math

```
nearby        := price of the first delivery-month contract
next_out      := price of the contract immediately after the nearby
further_out   := the month beyond next_out          # strength test

carrying_charge_market := nearby < next_out < further_out     # normal; storage cost
premium_market         := nearby > next_out                   # demand > supply

strong_premium := nearby > next_out AND nearby > further_out

# Worked carrying-charge example (ICT-2017-CARRYING-CHARGE, 03:01-03:30), soybeans:
#   Jul-2017 940  ->  Aug higher  ->  Nov 945  ->  Jan-2018 952
#   monotone increase = carrying charge, no premium
```

## Machine-Readable

```json
{
  "id": "premium-vs-carrying-charge-market",
  "category": "03-order-flow",
  "aliases": ["carrying-charge-market", "premium-market"],
  "criteria": [
    {"id": "c1", "expr": "instrument_class == commodity_futures"},
    {"id": "c2", "expr": "compare nearby vs next_month_out"},
    {"id": "c3", "expr": "nearby < next_out => carrying_charge_market"},
    {"id": "c4", "expr": "nearby > next_out => premium_market (demand high, supply short)"},
    {"id": "c5", "expr": "strong_premium confirmed against the month beyond next_out"},
    {"id": "c6", "expr": "review_cadence_weeks in [2, 3]"}
  ],
  "timeframes": ["W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["open-interest", "commitment-of-traders", "seasonal-tendency", "institutional-order-flow"],
  "sources": ["ICT-2017-CARRYING-CHARGE"]
}
```

## Visual Pattern

```
   CARRYING CHARGE (normal)          PREMIUM (demand > supply)

   price                              price
     │              ● Jan 952           │  ● nearby
     │         ● Nov 945                │       ● next out
     │    ● Aug                         │            ● further out
     │ ● Jul 940                        │
     └──────────────────► months        └──────────────────► months

   each month costs MORE               nearby costs MOST
   = cost of carry                     = commercials want it NOW
```

## Timeframes

Weekly to monthly. The curve is a positioning read, reviewed every two to three weeks.

## Examples

**Example 1 — carrying charge, soybeans (`ICT-2017-CARRYING-CHARGE`, 03:01–03:30):**
- July 2017 contract at 940; August higher; November 945; January 2018 952.
- Monotone increase across delivery months → no premium → carrying charge market.

**Example 2 — premium, feeder cattle (04:05–05:32):**
- Nearby prices above September and the month beyond it.
- Premium confirmed further out on the curve → a strong premium.
- Read: demand is high and supply is short; commercials are paying up for immediate delivery.

## Common Mistakes

- **Applying it to FX.** There is no delivery-month curve in spot forex.
- **Checking only the next month out.** A premium that vanishes one month further along
  is weak; ICT tests it against the month beyond.
- **Reading a carrying charge as bearish.** It is the *normal* state — it reflects storage
  cost, not a directional signal.
- **Monitoring daily.** The cadence taught is every two to three weeks.

## Related Concepts

- [open-interest](open-interest.md), [commitment-of-traders](commitment-of-traders.md) — the other two commodity-positioning reads from the same lesson series.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — annual context layered with this.
- [institutional-order-flow](institutional-order-flow.md) — the broader directional read.

## Citations

- `ICT-2017-CARRYING-CHARGE` (00:19) — "June 2017 ICT Mentorship, ICT Commodity Trading Lesson 4, Premium vs. Carrying Charge Markets"; (01:05–01:27) review "once every two to three weeks… I would look for a premium or a lack of premium in the delivery months"; (02:28–02:42) nearby and next month out defined; (02:50) "when there is no premium, we have what is referred to as a carrying charge market"; (03:01–03:30) the soybean 940 → 945 → 952 curve; (04:46–04:58) strength tested against the month beyond; (05:32) "the demand is high and the supply is short"; (05:37–05:48) real supply/demand factors exist in commodities but not FX; (06:09) premium defined as nearby above later delivery months; (06:25–06:40) commercials taking delivery immediately rather than paying the expected carrying charge later.
