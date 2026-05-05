# Continuation Order Block

**Category:** 07-order-blocks
**Aliases:** continuation OB, COB, BOS-anchored OB, trend OB
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, continuation, bos

## Definition

A continuation OB is one whose displacement produced a **BOS in the existing trend direction** (not a CHoCH/MSS reversal). These are the standard OBs traders use during established trends — they don't mark bias change, they refuel continuation. Counterpart: [reversal-order-block](reversal-order-block.md). Most OBs in trending markets are continuation OBs.

## Formal Criteria

- A standard OB qualifies per [order-block-criteria](order-block-criteria.md).
- The displacement produced a **BOS** (not a CHoCH/MSS) — i.e., trend was already in the displacement direction.
- The OB anchors at a pullback swing pivot inside the trend.

## Formula / Math

```
continuation_ob(n) := order_block(n) is true
                       AND structure_break_was_BOS == true
                       AND trend_prior_aligned_with_displacement == true
```

## Machine-Readable

```json
{
  "id": "continuation-order-block",
  "category": "07-order-blocks",
  "aliases": ["continuation-OB", "COB", "BOS-anchored-OB", "trend-OB"],
  "criteria": [
    {"id": "c1", "expr": "OB qualifies per standard criteria"},
    {"id": "c2", "expr": "displacement_produced_BOS_not_CHoCH == true"},
    {"id": "c3", "expr": "trend_aligned_with_displacement == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["bullish-order-block","bearish-order-block","reversal-order-block","order-block-criteria","bos-bullish","bos-bearish"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish continuation OB (mid-trend):

         ▲▲
        ▲▲▲                       ← prior trend already bullish
       ▲▲▲▲
      ▲▲▲▲▲       ▼   ← OB candle (last bearish candle of pullback)
     ▲▲▲▲▲▲       ▼
                ▲▲▲   ← displacement-up candle
               ▲▲▲▲   ← BOS above prior swing high (continuation)
              ▲▲▲▲▲
```

## Timeframes

All TFs.

## Examples

**Example 1 — H4 continuation bullish OB:**
- H4 has been in a clear uptrend for 2 days.
- Pullback occurs; the last bearish H4 candle of the pullback closes at 1.0830 (body 1.0825–1.0835).
- Next H4 candle: 28-pip green displacement, closes at 1.0858, breaks the prior H4 swing high (BOS).
- → continuation OB. On retest at MT (1.0830), high-conviction continuation long.

## Common Mistakes

- **Confusing with reversal OB.** Continuation = BOS in existing trend; reversal = CHoCH/MSS that changes trend.
- **Counter-trend continuation.** A continuation OB in a clearly weakening or transitioning trend is lower-conviction — check HTF bias.
- **Picking late OBs.** OBs from much earlier in the trend may have been superseded by newer ones; use the most recent fresh OB.

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md), [reversal-order-block](reversal-order-block.md), [order-block-criteria](order-block-criteria.md), [bos-bullish](../01-market-structure/bos-bullish.md), [bos-bearish](../01-market-structure/bos-bearish.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
