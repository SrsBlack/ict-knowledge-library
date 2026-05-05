# Smart Money Footprint

**Category:** 03-order-flow
**Aliases:** SM footprint, institutional footprint, smart-money signature
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-flow, smart-money, footprint

## Definition

The **Smart Money Footprint** is the visible chart evidence that institutional ("smart money") activity has occurred — specific patterns ICT teaches as the algorithm's "signature." When a setup leaves a clear footprint (sweep + displacement + FVG, or breaker formation, or HTF CHoCH with confirmation), it is high-conviction. Setups without a clear footprint are weaker because the algorithmic anchor is ambiguous.

## Formal Criteria

The canonical Smart Money Footprint signatures:

| Signature | Description |
|---|---|
| Liquidity sweep + displacement | wick takes pool, then directional displacement |
| FVG inside displacement | algorithm left orderbook imbalance |
| MSS / CHoCH with displacement | structural intent clear |
| OB at swing pivot with displacement | absorption-then-delivery sequence |
| Breaker formation post-CHoCH | failed-OB polarity flip with delivery |
| SMT divergence at structural extreme | cross-asset confirmation |

Higher-quality setups stack 3-5 of these footprints simultaneously.

## Formula / Math

```
sm_footprint_score = count(footprint_signatures_present)

# Working scale:
# 1-2 signatures: weak footprint (skip or tiny size)
# 3-4 signatures: clear footprint (standard size)
# 5+ signatures:  strong footprint (full size, A+ setup)
```

## Machine-Readable

```json
{
  "id": "smart-money-footprint",
  "category": "03-order-flow",
  "aliases": ["SM-footprint", "institutional-footprint", "smart-money-signature"],
  "criteria": [
    {"id": "c1", "expr": "count signatures: sweep+displacement, FVG, CHoCH, OB+displacement, breaker, SMT"},
    {"id": "c2", "expr": "3+ signatures = clear footprint"},
    {"id": "c3", "expr": "5+ signatures = strong footprint"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["institutional-order-flow","algorithmic-price-delivery","bullish-order-flow","bearish-order-flow","order-flow-shift","liquidity-sweep","displacement-definition","fair-value-gap","mss","smt-divergence"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Smart Money Footprint stack (bullish):

   1. SSL sweep + close back inside           ✓
   2. Bullish displacement candle              ✓
   3. Bullish FVG inside displacement         ✓
   4. M15 CHoCH up                            ✓
   5. SMT divergence vs correlated pair       ✓
   
   = 5 signatures = strong footprint = A+ setup
```

## Timeframes

M5–D.

## Examples

**Example 1 — strong footprint setup:**
- 02:55 NY: M5 wicks Asian SSL (sweep, signature 1).
- 03:05: M5 +18 pip displacement (signature 2).
- 03:10: bullish FVG in displacement (signature 3).
- 03:30: M15 CHoCH up (signature 4).
- Same time: GBPUSD did not confirm new low (SMT bullish divergence, signature 5).
- → 5 footprint signatures present, A+ setup conviction.

## Common Mistakes

- **Counting weak signatures as full points.** A poorly-formed FVG (no real displacement) shouldn't count the same as a clean one.
- **Skipping the cross-asset signature.** SMT requires looking at a second chart; many traders skip it and lose a confluence factor.
- **Footprint without HTF bias.** A clean footprint against HTF bias still has lower base rate; combine with bias.

## Related Concepts

- [institutional-order-flow](institutional-order-flow.md), [algorithmic-price-delivery](algorithmic-price-delivery.md), [bullish-order-flow](bullish-order-flow.md), [bearish-order-flow](bearish-order-flow.md), [order-flow-shift](order-flow-shift.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [mss](../01-market-structure/mss.md), [smt-divergence](../16-smt-divergence/smt-divergence.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
