# Open Interest

**Category:** 03-order-flow
**Aliases:** OI, outstanding contracts, open interest analysis
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-OPEN-INTEREST
**Tags:** order-flow, futures, commodities, sponsorship, smart-money-footprint

## Definition

Open interest is **the total number of outstanding contracts held by market
participants at the end of each trading day** (`ICT-2017-OPEN-INTEREST`, 02:30). It
exists only in futures and options markets, which is why ICT frames it as a
"built-in advantage" available in commodities and absent in spot FX.

The distinction ICT draws from volume is explicit: "where volume measures the
**pressure or intensity** behind a price trend, open interest measures the **flow of
money into** a futures market" (02:36). Rising open interest in a trend means new
money is sponsoring the move; the trend has backing. ICT attributes the framework to
Larry Williams (01:50).

## Formal Criteria

- Open interest counts **one side only** — buyers or sellers, not both — since every
  contract has a counterparty (02:55).
- It is an **end-of-day** figure, not intraday.
- **Trend reading:** "if prices are in an uptrend and open interest is rising, this is
  a bullish sign" (03:43). "As long as the open interest is increasing in a major
  trend, it will have the necessary **sponsorship** to continue" (04:00).
- Falling open interest in a trend indicates the move is losing sponsorship —
  positions are being closed rather than opened.
- **Contract selection:** the highest-open-interest contract is not always the nearby
  month. ICT notes a case where "the open interest is the highest in September
  contract, even though the nearby contract is June" (00:29). Read the contract where
  the money actually sits.

## Formula / Math

```
open_interest(t) := total outstanding contracts at end of day t
                    (counted on one side only)

delta_OI := open_interest(t) - open_interest(t-1)

# Trend sponsorship read:
uptrend   AND delta_OI > 0  -> bullish; move is sponsored
uptrend   AND delta_OI < 0  -> sponsorship leaving the move
downtrend AND delta_OI > 0  -> bearish; move is sponsored
```

No numeric threshold for "rising" is taught. The read is directional, not gated.

## Machine-Readable

```json
{
  "id": "open-interest",
  "category": "03-order-flow",
  "aliases": ["OI", "outstanding-contracts"],
  "criteria": [
    {"id": "c1", "expr": "open_interest == total_outstanding_contracts_end_of_day"},
    {"id": "c2", "expr": "counted_one_side_only == true"},
    {"id": "c3", "expr": "uptrend AND rising_OI => sponsored_trend"},
    {"id": "c4", "expr": "available_in in [futures, options]"},
    {"id": "c5", "expr": "read_contract_with_highest_OI (not necessarily nearby month)"}
  ],
  "timeframes": ["D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["institutional-order-flow", "seasonal-tendency", "dollar-index"],
  "sources": ["ICT-2017-OPEN-INTEREST"]
}
```

## Visual Pattern

```
   price      open interest      read
   ───────    ─────────────      ────────────────────────────
    ↑ up          ↑ rising       sponsored uptrend  (bullish)
    ↑ up          ↓ falling      sponsorship leaving; trend tiring
    ↓ down        ↑ rising       sponsored downtrend (bearish)
    ↓ down        ↓ falling      sponsorship leaving; trend tiring

   Volume answers "how hard?"  Open interest answers "is new money arriving?"
```

## Timeframes

Daily and weekly only — open interest is published end-of-day.

## Examples

**Example 1 — contract selection (`ICT-2017-OPEN-INTEREST`, 00:29):**
- Nearby contract is June; open interest is highest in September.
- The September contract is where participation sits, so that is the contract to study.

**Example 2 — trend sponsorship (03:43–04:00):**
- Price in a major uptrend, open interest rising day over day.
- Reads as bullish: new money is entering, so the trend has the sponsorship to continue.

## Common Mistakes

- **Confusing it with volume.** Volume is intensity of activity; open interest is net
  new participation. They answer different questions and can diverge.
- **Applying it to spot FX.** There is no open interest in spot forex. The nearest
  equivalent read is via currency futures.
- **Double-counting.** Open interest counts one side; counting both doubles the figure.
- **Defaulting to the nearby contract.** ICT's own example has the money in a later month.

## Related Concepts

- [institutional-order-flow](institutional-order-flow.md) — the broader read this feeds.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — the other non-price context input from the same mentorship year.
- [dollar-index](dollar-index.md) — intermarket context for FX and commodities.

## Citations

- `ICT-2017-OPEN-INTEREST` (00:29) — "the open interest is the highest in September contract, even though the nearby contract is June"; (01:50) attribution to Larry Williams; (02:30) "the total number of outstanding contracts that are held by market participants at the end of each trading day"; (02:36) "where volume measures the pressure or intensity behind a price trend, open interest measures the flow of money into a futures market"; (02:55) one-side counting; (03:43) "if prices are in an uptrend and open interest is rising, this is a bullish sign"; (04:00) "as long as the open interest is increasing in a major trend, it will have the necessary sponsorship to continue."
