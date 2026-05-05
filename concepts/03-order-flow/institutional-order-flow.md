# Institutional Order Flow

**Category:** 03-order-flow
**Aliases:** institutional flow, smart-money flow, IOF
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-MENTORSHIP-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-flow, institutional, foundational

## Definition

Institutional order flow is the **directional buying/selling pressure from large market participants** — central banks, hedge funds, market-makers — that drives sustained price delivery. ICT's framework treats institutional flow as the **signal** that retail flow merely reacts to. Reading institutional flow means identifying the structural / displacement / liquidity-sweep signatures that institutional positioning produces, rather than tape-reading volume directly. The concept is **interpretive**: ICT does not claim to read order books literally, but to read the **price patterns** that institutional flow leaves.

## Formal Criteria

Institutional order flow signatures (per ICT's pattern catalog):

- **Displacement candles** — wide, fast, directional moves with minimal opposing wick.
- **FVGs forming** during displacement (the gap = orderbook imbalance).
- **Liquidity sweeps** at known pools (institutions absorbing flow).
- **CHoCH/MSS** at HTF structure (bias change driven by repositioning).
- **Sustained directional close sequences** without meaningful pullback.

When these signatures appear together, ICT teaches that institutional flow is committed in that direction.

## Formula / Math

```
institutional_flow_signal = qualitative_read(
    displacement_candles_present,
    FVGs_in_direction,
    liquidity_sweeps_at_known_pools,
    CHoCH_or_MSS_in_direction,
    directional_close_sequence,
)
```

ICT teaches this qualitatively; no fixed formula yields a numeric "institutional-flow score."

## Machine-Readable

```json
{
  "id": "institutional-order-flow",
  "category": "03-order-flow",
  "aliases": ["institutional-flow", "smart-money-flow", "IOF"],
  "criteria": [
    {"id": "c1", "expr": "displacement + FVG + sweep + structure shift signatures"},
    {"id": "c2", "expr": "interpretive read, not literal orderbook"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["algorithmic-price-delivery","bullish-order-flow","bearish-order-flow","order-flow-shift","smart-money-footprint","displacement-definition","fair-value-gap","liquidity-sweep"],
  "sources": ["ICT-2016-MENTORSHIP-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   institutional-flow signature (bullish):

   prior structure           ←  liquidity-sweep signature
        ▼  swept SSL
        ▲▲▲                  ←  displacement candle
       ▲▲▲▲                  ←  FVG inside displacement
      ▲▲▲▲▲                  ←  CHoCH up + sustained directional close
   
   → institutional-flow read: bullish, committed
```

## Timeframes

M5–D.

## Examples

**Example 1 — clear bullish institutional flow:**
- 02:55 NY (London open): M5 wicks below Asian SSL (sweep).
- 03:05: M5 +18 pip displacement + bullish FVG (orderbook imbalance signature).
- 03:30: H1 prints CHoCH up, breaking prior swing high.
- 04:00–11:00: 6 H1 candles with majority bullish closes, no pullback >40% retracement.
- → institutional flow committed bullish; HTF distribution underway.

## Common Mistakes

- **Treating institutional flow as literal orderbook tape.** ICT's framework is pattern-based, not tape-reading.
- **Reading single candles.** Institutional flow is a sustained pattern; one displacement candle isn't proof of committed flow.
- **Ignoring counter-signals.** When mixed signatures appear (FVG up but recent CHoCH down), institutional flow is in transition.

## Related Concepts

- [algorithmic-price-delivery](algorithmic-price-delivery.md), [bullish-order-flow](bullish-order-flow.md), [bearish-order-flow](bearish-order-flow.md), [order-flow-shift](order-flow-shift.md), [smart-money-footprint](smart-money-footprint.md).
- [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md).

## Citations

- `ICT-2016-MENTORSHIP-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
