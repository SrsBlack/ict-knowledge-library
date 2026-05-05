# Bearish Order Block

**Category:** 07-order-blocks
**Aliases:** bearish OB, BeOB, supply OB, supply zone (SMC), supply block (SMC)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-OB-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, bearish, foundational

## Definition

A bearish order block is the **last bullish (up-close) candle before a bearish displacement move that breaks structure to the downside**. Mirror of [bullish-order-block](bullish-order-block.md). Bearish OBs are **premium-array references** when sitting above current price.

## Formal Criteria

- The candle is bullish (close > open).
- It is the **last** bullish candle before a bearish displacement.
- Displacement breaks structure (BOS or bearish CHoCH/MSS) to the downside.
- Best-quality bearish OBs sit at swing highs.
- Fresh.

## Formula / Math

```
bearish_ob_high := close(n)      # since close > open for the OB candle
bearish_ob_low  := open(n)
bearish_ob_mt   := (close(n) + open(n)) / 2

bearish_ob_full_high := high(n)
bearish_ob_full_low  := low(n)
```

## Machine-Readable

```json
{
  "id": "bearish-order-block",
  "category": "07-order-blocks",
  "aliases": ["bearish-OB", "BeOB", "supply-OB", "supply-zone", "supply-block"],
  "criteria": [
    {"id": "c1", "expr": "candle is bullish (close > open)"},
    {"id": "c2", "expr": "last bullish candle before bearish displacement"},
    {"id": "c3", "expr": "displacement breaks structure to downside"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["order-block-criteria","bullish-order-block","mitigated-order-block","unmitigated-order-block","mean-threshold","premium-array","bearish-fvg","bos-bearish","propulsion-block"],
  "sources": ["ICT-2016-OB-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bearish OB:

   ▲               ← OB candle (last up-close before displacement)
   ▲               body: close at top, open at bottom
                   ▼
                   ▼   ← displacement starts
                   ▼
                       ▼
                       ▼   ← FVG forms; structure break (BOS) below
                       ▼
```

## Timeframes

All TFs M5+.

## Examples

**Example 1 — H1 bearish OB:**
- 09:00 NY H1 bullish candle: O=1.0945, C=1.0955, H=1.0958, L=1.0944. Body: [1.0945, 1.0955]. MT = 1.0950.
- 10:00 NY: bearish 25-pip displacement; 11:00: continues; breaks H1 swing low → BOS.
- HTF bearish; price retraces up to 1.0950 (MT).
- Short at MT, SL at 1.0961 (above OB high + 3-pip buffer). Risk = 11 pips.

## Common Mistakes

- **No displacement check.** A bullish candle with weak follow-through isn't an OB.
- **Mixing body and range.** Use body for entry; range for SL.

## Related Concepts

- [order-block-criteria](order-block-criteria.md), [bullish-order-block](bullish-order-block.md), [mitigated-order-block](mitigated-order-block.md), [unmitigated-order-block](unmitigated-order-block.md).
- [mean-threshold](../27-equilibrium/mean-threshold.md), [premium-array](../05-pd-arrays/premium-array.md).
- [bearish-fvg](../06-fair-value-gaps/bearish-fvg.md), [bos-bearish](../01-market-structure/bos-bearish.md), [propulsion-block](propulsion-block.md).

## Citations

- `ICT-2016-OB-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
