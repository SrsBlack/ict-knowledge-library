# Mega-Trade

**Category:** 31-models
**Aliases:** megatrade, mega trades, annual big move, large price swing
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-MEGA-COMMODITY, ICT-2017-MEGA-STOCK, ICT-2017-MEGA-BOND, ICT-2017-MEGA-FOREX
**Tags:** models, long-term, seasonality, position-trading, commodities, stocks, bonds, fx

## Definition

A mega-trade is **the one large, prolonged price swing a market makes in a calendar
year** — "a large price swing or trend that can produce massive potential gains that,
when compared to relative markets, outperforms them all" (`ICT-2017-MEGA-COMMODITY`,
01:15). It is a position-trading concept, not a setup: "these are trades that are
significant in magnitude — they're **not little day trades, not short-term trades**,
they're much more prolonged in their duration" (`ICT-2017-MEGA-STOCK`, 00:24).

ICT credits the idea to Larry Williams and states he coined the label himself (01:04).
The same framework is taught across four markets — commodities, stocks, bonds and FX —
which is why one page carries four sources.

## Formal Criteria

- **Duration: months, not days.** In equities "usually they can go about **six to nine
  months or more**" (`ICT-2017-MEGA-STOCK`, 00:38).
- **Recurs annually and is visible historically:** "they're easy to spot historically in
  your price charts, you can see them **every single calendar year**"
  (`ICT-2017-MEGA-COMMODITY`, 01:22).
- **Relative outperformance** — the move must outrun comparable markets, not merely be large.
- **Institutional sponsorship:** "these moves have huge institutional sponsorship" (01:30).
- **Driven by seasonal tendency.** In bonds "we're looking for seasonal tendencies, and
  seasonal tendencies are very specific with the bond market because it's a very
  repeating phenomenon" (`ICT-2017-MEGA-BOND`, 00:34). In FX the driver is stated as
  **quarterly shifts** (`ICT-2017-MEGA-FOREX`, 00:39).
- **Supply and demand are a real input here** — the exception ICT makes for physical
  markets: "while I usually snub my nose at supply and demand as a technical approach to
  trading, supply and demand as it relates to commodities is an **absolute reality**"
  (`ICT-2017-MEGA-COMMODITY`, 01:45).
- **Selective coverage and patience:** follow only a handful of markets, and "if there
  is [no] signal that's very clear, I'm not doing anything" (03:39–03:53).

## Formula / Math

```
# No numeric trigger is taught. A mega-trade is qualified, not computed:

candidate := market where
    seasonal_tendency(market, window) is strong and repeating
    AND expected_duration >= ~6 months          # equities: 6-9 months+
    AND relative_performance(market) > peers
    AND institutional_sponsorship visible        # COT / open interest
    AND (commodity? -> real supply/demand factors support the direction)

# Context inputs feeding the qualification:
#   seasonal-tendency, commitment-of-traders, open-interest,
#   premium-vs-carrying-charge-market, quarterly shifts (FX)
```

The output is a **market-selection and bias decision**. Entry timing comes from the
ordinary entry toolkit, not from this page.

## Machine-Readable

```json
{
  "id": "mega-trade",
  "category": "31-models",
  "aliases": ["megatrade", "annual-big-move"],
  "criteria": [
    {"id": "c1", "expr": "duration_months >= 6", "note": "equities 6-9+; other markets months not days"},
    {"id": "c2", "expr": "recurs_annually_and_visible_in_history == true"},
    {"id": "c3", "expr": "outperforms_relative_markets == true"},
    {"id": "c4", "expr": "institutional_sponsorship_present == true"},
    {"id": "c5", "expr": "driver == seasonal_tendency (FX: quarterly shifts)"},
    {"id": "c6", "expr": "commodity => real_supply_demand_factors_considered"},
    {"id": "c7", "expr": "supplies_entry == false"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["seasonal-tendency", "commitment-of-traders", "open-interest", "premium-vs-carrying-charge-market", "interest-rate-differentials"],
  "sources": ["ICT-2017-MEGA-COMMODITY", "ICT-2017-MEGA-STOCK", "ICT-2017-MEGA-BOND", "ICT-2017-MEGA-FOREX"]
}
```

## Visual Pattern

```
   One calendar year, one market:

   price
     │                        ╱‾‾‾‾‾‾╲
     │                    ╱‾‾╱        ╲___        <- THE mega-trade
     │      ╲__╱╲__╱╲___╱                         (6-9 months, one direction)
     │   ╱╲╱                                       
     └────────────────────────────────────────► months
        Jan        Apr        Jul        Oct

   Chop for much of the year, then one prolonged directional move.
   The seasonal window says WHEN to look; sponsorship says whether it is real.
```

## Timeframes

Daily, weekly, monthly. A mega-trade is invisible intraday by definition.

## Examples

**Example 1 — equity duration (`ICT-2017-MEGA-STOCK`, 00:24–00:42):**
- The move is qualified by magnitude and duration, not by pattern.
- Six to nine months or more in the stock market; day trades and short-term trades are
  explicitly excluded.

**Example 2 — bonds via seasonality (`ICT-2017-MEGA-BOND`, 00:34–00:46):**
- The 30-year treasury seasonal tendency is the starting point.
- Bonds are singled out as an especially repeating seasonal market.

## Common Mistakes

- **Treating it as a setup.** It selects a market and a direction for a season; it has
  no entry, stop or target of its own.
- **Sizing it like a swing trade.** Six-to-nine-month duration implies stop distances and
  holding costs a swing framework does not.
- **Skipping the sponsorship check.** A large seasonal move without COT/open-interest
  backing is a chart pattern, not a mega-trade.
- **Applying commodity supply/demand logic to FX.** ICT makes that exception only for
  physical markets.
- **Forcing one every year in every market.** The taught posture is to watch few markets
  and stand aside without a clear signal.

## Related Concepts

- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — the primary driver; the window to look in.
- [commitment-of-traders](../03-order-flow/commitment-of-traders.md), [open-interest](../03-order-flow/open-interest.md) — how sponsorship is verified.
- [premium-vs-carrying-charge-market](../03-order-flow/premium-vs-carrying-charge-market.md) — commodity demand confirmation.
- [interest-rate-differentials](../03-order-flow/interest-rate-differentials.md) — the FX macro driver.

## Citations

- `ICT-2017-MEGA-COMMODITY` (00:43) "what is mega trades"; (00:55–01:10) attribution to Larry Williams and the coining of the label; (01:15) "a large price swing or trend that can produce massive potential gains that one compared to relative markets and performs them all"; (01:22–01:38) annually visible, huge institutional sponsorship, supply/demand fuel; (01:45–01:59) the supply-and-demand exception for commodities; (03:39–03:53) follow few markets, stand aside without a clear signal.
- `ICT-2017-MEGA-STOCK` (00:12) "ICT Megatrades for Stocks, this is Lesson 3"; (00:24–00:38) "significant in magnitude… not little day trades… six to nine months or more".
- `ICT-2017-MEGA-BOND` (00:34–00:46) seasonal tendencies as the bond driver; the 30-year treasury seasonal chart.
- `ICT-2017-MEGA-FOREX` (00:23–00:39) "lesson two, ICT mega trades… dealing with Forex and currencies"; quarterly shifts as the FX driver.
