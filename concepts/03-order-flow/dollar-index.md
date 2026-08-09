# US Dollar Index (USDX / DXY)

**Category:** 03-order-flow
**Aliases:** USDX, DXY, dollar index, the dollar
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-HIGH-REWARD-SETUPS, ICT-2017-SEASONAL-IDEAL
**Tags:** order-flow, intermarket, correlation, fx, commodities, dollar

## Definition

The US Dollar Index is a **basket index of the dollar against a weighted group of
major currencies**, used across ICT's material as the reference instrument for
intermarket context rather than as something to trade directly. Three distinct roles
are taught:

1. **Inverse baseline for FX.** A foreign currency pair quoted against USD moves
   broadly opposite the index; divergence from that relationship is the raw material of
   [smt-divergence](../16-smt-divergence/smt-divergence.md).
2. **Inverse to commodities.** "Commodities and the dollar index are **inversely
   related**" (`ICT-2017-HIGH-REWARD-SETUPS`, 26:26) — commodities are dollar-denominated,
   so dollar strength is a headwind.
3. **Comparison chart for seasonals.** The *ideal* form of a
   [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) is defined by
   opposition between a pair's seasonal chart and the dollar index's seasonal chart.

This page documents the instrument and its intermarket role. The **divergence
patterns** built on it (dollar index makes a higher high while the foreign currency
fails to make a lower low, and the mirrored cases) are documented separately at
[smt-divergence](../16-smt-divergence/smt-divergence.md) and
[index-smt](../16-smt-divergence/index-smt.md) — do not restate them here.

## Formal Criteria

- The index is **not a setup**. It supplies directional context that a setup on another
  instrument is read against.
- **FX:** expect broad inverse correlation with USD-quoted foreign currencies. Where the
  inverse relationship *breaks*, that failure is the signal — see smt-divergence.
- **Commodities:** expect inverse correlation with the dollar index.
- **Seasonals:** the index's seasonal chart is the comparison leg for identifying an
  ideal seasonal window.
- **Interest-rate context** sits alongside it: unexpected hikes or cuts move a currency,
  and the **differential between two interest-rate markets** can produce a carrying-charge
  market with a persistent directional bias (`ICT-2017-HIGH-REWARD-SETUPS`, 25:07–25:35).

## Formula / Math

```
# No formula is taught for the index itself; it is read, not computed.
# The relationships used:

expected_sign( corr(USDX, foreign_currency_vs_USD) ) = negative
expected_sign( corr(USDX, dollar_denominated_commodity) ) = negative

# Divergence from the expected sign is the SMT read (separate concept):
#   USDX makes higher high  AND  foreign currency fails to make lower low
#   -> see smt-divergence

# Interest-rate differential:
carry_bias := rate(currency_A) - rate(currency_B)     # large gap -> carrying-charge market
```

## Machine-Readable

```json
{
  "id": "dollar-index",
  "category": "03-order-flow",
  "aliases": ["USDX", "DXY", "dollar-index"],
  "criteria": [
    {"id": "c1", "expr": "corr(USDX, fx_pair_vs_USD) expected negative"},
    {"id": "c2", "expr": "corr(USDX, commodities) expected negative"},
    {"id": "c3", "expr": "used_as_seasonal_comparison_leg == true"},
    {"id": "c4", "expr": "is_a_setup == false"},
    {"id": "c5", "expr": "divergence_patterns documented_in smt-divergence"}
  ],
  "timeframes": ["H1","H4","D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["smt-divergence", "index-smt", "seasonal-tendency", "open-interest", "institutional-order-flow"],
  "sources": ["ICT-2017-HIGH-REWARD-SETUPS", "ICT-2017-SEASONAL-IDEAL"]
}
```

## Visual Pattern

```
   US Dollar Index          EURUSD (foreign currency vs USD)
        ╱‾╲                        ╲_╱
       ╱   ╲                      ╱   ╲
   ___╱     ╲___              ‾‾‾╱     ╲‾‾‾

   Normal state: mirrored. The index up, the pair down.

   Commodities behave like the foreign currency side:
   dollar index up -> commodity headwind.

   When the mirror BREAKS, that is SMT -> see smt-divergence.
```

## Timeframes

H1 and above. The index is context, and intraday noise in it is not informative on its own.

## Examples

**Example 1 — commodity context (`ICT-2017-HIGH-REWARD-SETUPS`, 26:26):**
- Dollar index trending higher.
- Dollar-denominated commodities face a headwind; a long commodity setup is being taken
  against intermarket context.

**Example 2 — seasonal comparison (`ICT-2017-SEASONAL-IDEAL`):**
- AUD's seasonal chart shows a March rally topping in May.
- The dollar index's seasonal chart declines across the same window.
- The opposition qualifies the window as an *ideal* seasonal tendency.

## Common Mistakes

- **Trading the index itself.** It is a context instrument in this framework.
- **Assuming a rigid inverse.** The relationship is a norm, not a law — and the
  exceptions are the point (SMT), not an error in the model.
- **Restating SMT here.** Divergence patterns belong to
  [smt-divergence](../16-smt-divergence/smt-divergence.md); duplicating them splits one
  concept across two files.
- **Ignoring the basket weighting.** The index is not "USD vs everything" — a move can
  be driven by one heavily weighted component.

## Related Concepts

- [smt-divergence](../16-smt-divergence/smt-divergence.md), [index-smt](../16-smt-divergence/index-smt.md) — the divergence patterns built on this instrument.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — uses the index's seasonal chart as the comparison leg.
- [open-interest](open-interest.md) — the other non-price context input from the same mentorship year.
- [institutional-order-flow](institutional-order-flow.md) — the broader read.

## Citations

- `ICT-2017-HIGH-REWARD-SETUPS` (25:07–25:35) — unexpected rate hikes/cuts, and "we look at differentials between two interest rate markets… that creates what's called a carrying charge market"; (26:26) "commodities and the dollar index are inversely related."
- `ICT-2017-SEASONAL-IDEAL` (01:04–01:20) — the dollar index seasonal chart as the comparison leg for identifying an ideal seasonal window.
