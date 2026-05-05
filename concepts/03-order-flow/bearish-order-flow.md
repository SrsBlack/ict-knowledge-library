# Bearish Order Flow

**Category:** 03-order-flow
**Aliases:** bearish flow, bearish institutional flow, down-flow
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-flow, bearish, foundational

## Definition

Bearish order flow is the **directional state where institutional selling dominates** — characterized by bearish CHoCH/MSS, bearish FVGs, sweeps of BSL pools without continuation up, lower-highs and lower-lows. Mirror of [bullish-order-flow](bullish-order-flow.md). Reading bearish flow correctly is the prerequisite for taking short setups.

## Formal Criteria

Bearish order flow signatures:

- **Recent bearish CHoCH or MSS** at HTF.
- **Bearish FVGs forming** during displacement.
- **BSL sweeps** at known pools without continuation up.
- **Lower highs / lower lows** in structure.
- **Bearish closes dominate** intraday session.
- **Range top of dealing range** is being respected.

## Formula / Math

```
bearish_order_flow_committed:
    recent_CHoCH_or_MSS_down == true
    AND bearish_FVGs_in_recent_displacement >= 1
    AND BSL_sweeps_with_displacement_down >= 1
    AND LH_LL_structure_intact
    AND bearish_close_majority
```

## Machine-Readable

```json
{
  "id": "bearish-order-flow",
  "category": "03-order-flow",
  "aliases": ["bearish-flow", "bearish-institutional-flow", "down-flow"],
  "criteria": [
    {"id": "c1", "expr": "bearish CHoCH/MSS recent"},
    {"id": "c2", "expr": "bearish FVGs forming"},
    {"id": "c3", "expr": "BSL sweeps without continuation up"},
    {"id": "c4", "expr": "LH/LL structure intact"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["institutional-order-flow","algorithmic-price-delivery","bullish-order-flow","order-flow-shift","smart-money-footprint","htf-bias-framework"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bearish order flow signatures:

   ↑ BSL swept here, no continuation up
   ▲ /  (sweep → reversal down)
    \/
     \  LH ▼
      \ /  \  ▼▼ ← LL
       ▼    \/
            \
             ▼▼▼ ← LL (lower low)
   
   Throughout: bearish FVGs forming, displacement candles down.
```

## Timeframes

M5–D.

## Examples

**Example 1 — clear bearish order flow:**
- D1 CHoCH down a day ago.
- H4 prints lower low.
- H1 has bearish FVG at 1.0950 still active.
- M15 just swept BSL at 1.0960 with no follow-through; reversed down with displacement.
- → bearish flow committed.

## Common Mistakes

- **Single-TF flow read.** Multi-TF agreement matters.
- **Reading individual bearish candles as bearish flow.** Sustained signatures are what defines flow.
- **Missing BSL-sweep-without-continuation tell.** Strong bearish flow signal; missing loses information.

## Related Concepts

- [institutional-order-flow](institutional-order-flow.md), [algorithmic-price-delivery](algorithmic-price-delivery.md), [bullish-order-flow](bullish-order-flow.md), [order-flow-shift](order-flow-shift.md), [smart-money-footprint](smart-money-footprint.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
