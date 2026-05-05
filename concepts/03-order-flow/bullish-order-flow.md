# Bullish Order Flow

**Category:** 03-order-flow
**Aliases:** bullish flow, bullish institutional flow, up-flow
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-flow, bullish, foundational

## Definition

Bullish order flow is the **directional state where institutional buying dominates** — characterized by a sequence of bullish-displacement signatures: bullish CHoCH/MSS, bullish FVGs forming, sweeps of SSL pools, sustained higher-highs and higher-lows. Reading bullish order flow correctly is the prerequisite for taking long setups; entries against bullish flow have meaningfully lower base rates.

## Formal Criteria

Bullish order flow signatures:

- **Recent bullish CHoCH or MSS** at HTF.
- **Bullish FVGs forming** during displacement.
- **SSL sweeps** at known pools without continuation down.
- **Higher highs / higher lows** in structure.
- **Bullish closes dominate** intraday session.
- **Range bottom of dealing range** is being respected (price stays above EQ when in discount, returns up).

When 4+ of these align, bullish order flow is committed.

## Formula / Math

```
bullish_order_flow_committed:
    recent_CHoCH_or_MSS_up == true
    AND bullish_FVGs_in_recent_displacement >= 1
    AND SSL_sweeps_with_displacement_up >= 1
    AND HH_HL_structure_intact
    AND bullish_close_majority
```

## Machine-Readable

```json
{
  "id": "bullish-order-flow",
  "category": "03-order-flow",
  "aliases": ["bullish-flow", "bullish-institutional-flow", "up-flow"],
  "criteria": [
    {"id": "c1", "expr": "bullish CHoCH/MSS recent"},
    {"id": "c2", "expr": "bullish FVGs forming"},
    {"id": "c3", "expr": "SSL sweeps without continuation down"},
    {"id": "c4", "expr": "HH/HL structure intact"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["institutional-order-flow","algorithmic-price-delivery","bearish-order-flow","order-flow-shift","smart-money-footprint","htf-bias-framework"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish order flow signatures:

   ▲▲▲ ←  HH (higher high)
        \  HL ▲     
         \ /  \  ▲▲ ← HH again
          ▲    \/
         HL     \
                 ↓
                 SSL swept here, no continuation
                 (sweep → reversal up)
   
   Throughout: bullish FVGs forming, displacement candles up.
```

## Timeframes

M5–D.

## Examples

**Example 1 — clear bullish order flow:**
- D1 CHoCH up two days ago.
- H4 prints higher high yesterday.
- H1 has bullish FVG at 1.0830 still active.
- M15 just swept SSL at 1.0820 with no follow-through; reversed up with displacement.
- 4 of 5 signatures present → bullish order flow committed.

## Common Mistakes

- **Reading flow on a single TF.** Multi-TF agreement matters; H4 bullish + D bearish = mixed flow, not committed bullish.
- **Single-bar reads.** A single bullish candle isn't bullish flow; require sustained signatures.
- **Ignoring the SSL-sweep-without-continuation signal.** This is one of the strongest bullish-flow tells; missing it loses information.

## Related Concepts

- [institutional-order-flow](institutional-order-flow.md), [algorithmic-price-delivery](algorithmic-price-delivery.md), [bearish-order-flow](bearish-order-flow.md), [order-flow-shift](order-flow-shift.md), [smart-money-footprint](smart-money-footprint.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
