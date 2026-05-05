# Bullish Order Block

**Category:** 07-order-blocks
**Aliases:** bullish OB, BOB, demand OB
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-OB-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, bullish, foundational

## Definition

A bullish order block is the **last bearish (down-close) candle before a bullish displacement move that breaks structure to the upside**. ICT teaches it as the institutional buying-zone candle — where the algorithm absorbed the last sell-side flow before driving price up. Bullish OBs are **discount-array references** when sitting below current price.

## Formal Criteria

Per [order-block-criteria](order-block-criteria.md), specifically for bullish OBs:

- The candle is bearish (close < open).
- It is the **last** bearish candle before a bullish displacement.
- Displacement follows in the next 1–3 candles.
- Displacement breaks structure (BOS or bullish CHoCH/MSS).
- Best-quality bullish OBs sit at swing lows or pivots that already had structural significance.
- Fresh (unmitigated).

## Formula / Math

```
bullish_ob_high := open(n)       # since close < open for the OB candle
bullish_ob_low  := close(n)
bullish_ob_mt   := (open(n) + close(n)) / 2

# Range version (less common but used for SL):
bullish_ob_full_low  := low(n)    # below body if there's a wick
bullish_ob_full_high := high(n)
```

## Machine-Readable

```json
{
  "id": "bullish-order-block",
  "category": "07-order-blocks",
  "aliases": ["bullish-OB", "BOB", "demand-OB"],
  "criteria": [
    {"id": "c1", "expr": "candle is bearish (close < open)"},
    {"id": "c2", "expr": "last bearish candle before bullish displacement"},
    {"id": "c3", "expr": "displacement breaks structure to upside"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["order-block-criteria","bearish-order-block","mitigated-order-block","unmitigated-order-block","mean-threshold","discount-array","bullish-fvg","bos-bullish","propulsion-block"],
  "sources": ["ICT-2016-OB-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB:

   ▼               ← OB candle (last down-close before displacement)
   ▼               body: open at top, close at bottom
                   ▲
                   ▲   ← displacement starts
                   ▲
                       ▲
                       ▲   ← FVG forms; structure break (BOS) above
                       ▲

   On retest, MT (midpoint) is the default entry; SL below OB low (with buffer).
```

## Timeframes

All TFs M5+.

## Examples

**Example 1 — H1 bullish OB:**
- 14:00 NY H1 bearish candle: O=1.0830, C=1.0820, L=1.0815, H=1.0832. Body: [1.0820, 1.0830]. MT = 1.0825.
- 15:00 NY: bullish 22-pip displacement candle. 16:00: continues, breaks H1 swing high → BOS.
- HTF bullish; price returns to 1.0825 (MT).
- Long entry at MT, SL at 1.0812 (3-pip buffer below OB low). Risk = 13 pips.
- Targets via SD projections of the displacement leg.

## Common Mistakes

- **Calling random down-candles "bullish OBs."** The displacement + structure-break filter is essential; without it, you're picking arbitrary candles.
- **Pixel-perfect MT.** Use a small buffer; MT entries don't need tick-perfection.
- **Body vs full-range confusion.** Body is the default OB zone; the wick low (high) is for SL placement.

## Related Concepts

- [order-block-criteria](order-block-criteria.md), [bearish-order-block](bearish-order-block.md), [mitigated-order-block](mitigated-order-block.md), [unmitigated-order-block](unmitigated-order-block.md).
- [mean-threshold](../27-equilibrium/mean-threshold.md), [discount-array](../05-pd-arrays/discount-array.md).
- [bullish-fvg](../06-fair-value-gaps/bullish-fvg.md), [bos-bullish](../01-market-structure/bos-bullish.md), [propulsion-block](propulsion-block.md).

## Citations

- `ICT-2016-OB-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
