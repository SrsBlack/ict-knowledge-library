# Open Interest

**Category:** 03-order-flow
**Aliases:** OI, outstanding contracts, open interest analysis
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-OPEN-INTEREST, ICT-2017-EXPLOSIVE-MARKETS
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
- **Magnitude threshold (refinement, `ICT-2017-EXPLOSIVE-MARKETS`, 19:22–19:49).** When
  open interest is used to qualify a trade, ICT does gate it: a **decline of 10–15 % or
  more is commercial short covering** — "if open interest declines 10% or 15% or more,
  that's indicative of commercial short covering" — and is read **bullish** when the
  commercial net line is simultaneously rising toward zero. The mirror, an **increase of
  10–15 % or more while commercials increase net selling**, is **bearish**. The threshold
  is paired with the COT line; neither leg is read alone.
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

# Qualifying read, gated (ICT-2017-EXPLOSIVE-MARKETS):
dOI_pct   := (OI(t) - OI(t-n)) / OI(t-n)
short_covering := dOI_pct <= -0.10          # 10-15% or more decline
                  AND net_commercial rising toward zero      -> BULLISH
distribution   := dOI_pct >= +0.10
                  AND net_commercial falling (more net short) -> BEARISH
```

For the **trend-sponsorship** read no numeric threshold is taught — it is directional,
not gated. The **10–15 % gate applies only to the qualifying read**, where open interest
is paired with the commercial net position to confirm a specific trade idea.

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
    {"id": "c5", "expr": "read_contract_with_highest_OI (not necessarily nearby month)"},
    {"id": "c6", "expr": "qualifying: delta_OI_pct <= -0.10 AND net_commercial rising => short_covering => bullish"},
    {"id": "c7", "expr": "qualifying: delta_OI_pct >= +0.10 AND net_commercial falling => bearish"}
  ],
  "timeframes": ["D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["institutional-order-flow", "seasonal-tendency", "dollar-index", "commitment-of-traders", "explosive-market-selection"],
  "sources": ["ICT-2017-OPEN-INTEREST", "ICT-2017-EXPLOSIVE-MARKETS"]
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

   QUALIFYING READ — open interest paired with the COT commercial line:

     OI   ‾‾‾╲                 -10% or more
              ╲___                            }  short covering
     COT  ___╱‾‾‾      commercial net rising  }  -> BULLISH

     OI   ___╱‾‾‾              +10% or more
     COT  ‾‾‾╲___      commercial net falling }  -> BEARISH
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
- **Applying the 10–15 % gate to the trend read.** The threshold belongs to the *qualifying*
  read, where open interest is paired with the COT commercial line. Trend sponsorship is
  judged directionally, with no threshold.
- **Reading a fall in open interest as weakness by default.** Paired with a rising
  commercial net line it is short covering — a bullish signature, not a fading trend.

## Related Concepts

- [institutional-order-flow](institutional-order-flow.md) — the broader read this feeds.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — the other non-price context input from the same mentorship year.
- [dollar-index](dollar-index.md) — intermarket context for FX and commodities.
- [commitment-of-traders](commitment-of-traders.md) — the commercial net line the qualifying read is paired with.
- [explosive-market-selection](../31-models/explosive-market-selection.md) — where the 10–15 % gate is taught, as hallmark 4 of 8.

## Citations

- `ICT-2017-OPEN-INTEREST` (00:29) — "the open interest is the highest in September contract, even though the nearby contract is June"; (01:50) attribution to Larry Williams; (02:30) "the total number of outstanding contracts that are held by market participants at the end of each trading day"; (02:36) "where volume measures the pressure or intensity behind a price trend, open interest measures the flow of money into a futures market"; (02:55) one-side counting; (03:43) "if prices are in an uptrend and open interest is rising, this is a bullish sign"; (04:00) "as long as the open interest is increasing in a major trend, it will have the necessary sponsorship to continue."
- `ICT-2017-EXPLOSIVE-MARKETS` (18:00–18:23) open interest as "an X-ray view… of what the smart money is doing"; (19:01–19:15) the worked example — over 500,000 contracts down to about 400,000 between November and December, "over 100,000 contracts taken off that were short"; (19:22–19:36) "if open interest declines 10% or 15% or more, that's indicative of commercial short covering"; (19:36–19:49) the bearish mirror — an increase of 10–15 % or more while commercials increase net selling; (20:04–20:14) a falling open interest alongside a rising commercial line read as bullish.
