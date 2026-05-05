# Bullish Breaker

**Category:** 08-breaker-blocks
**Aliases:** bullish breaker block, BBB, demand breaker
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** breaker, bullish

## Definition

A bullish breaker is a **failed bearish order block** — an originally bearish OB whose top edge price violated by closing above with displacement. The OB body now functions as a **bullish support zone** on retest from above. The flipped polarity reflects an institutional intent change: the bearish OB was rejected, and the algorithm now defends the same zone for longs.

## Formal Criteria

- An originally bearish OB existed (last bullish candle before bearish displacement).
- Price subsequently broke ABOVE the OB body (close above the OB high) with bullish displacement.
- Often a bullish CHoCH or BOS accompanies the break.
- On retest from above (price comes back down to OB body), the zone acts as bullish support.

## Formula / Math

```
break_event(bearish_ob) := close_t > high(ob_body)
                            AND bullish_displacement_present_in_break

bullish_breaker_active(ob, retest) := low(retest) reaches high(ob_body)
                                       AND bullish_rejection_with_displacement
```

## Machine-Readable

```json
{
  "id": "bullish-breaker",
  "category": "08-breaker-blocks",
  "aliases": ["bullish-breaker-block", "BBB", "demand-breaker"],
  "criteria": [
    {"id": "c1", "expr": "originally_bearish_OB"},
    {"id": "c2", "expr": "close_above_OB_high_with_bullish_displacement"},
    {"id": "c3", "expr": "retest_acts_as_support"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["breaker-block","bearish-breaker","bearish-order-block","mitigation-block","failed-breaker","choch-bullish","bos-bullish"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish breaker formation:

   Step 1: bearish OB forms (last bullish candle before bearish move)
   Step 2: later, price breaks UPWARD through OB high with displacement
           → bullish CHoCH/BOS
   Step 3: retest comes back down to OB body
   Step 4: bullish rejection at OB body → confirmed bullish breaker
                                       (long entry zone)
```

## Timeframes

M15+.

## Examples

**Example 1 — H1 bearish OB → bullish breaker:**
- H1 bearish OB formed: body 1.0945–1.0955.
- Two days later, H1 closes at 1.0962 with bullish displacement; bullish CHoCH on H1.
- Hours later, H1 retraces down to 1.0950 (inside original OB body).
- Bullish reaction with FVG up → confirmed bullish breaker.
- Long at MT 1.0950, SL below OB low at 1.0942 (3-pip buffer). Risk = 8 pips.

## Common Mistakes

- **Wick-through.** A wick that pokes above OB high but closes back inside doesn't trigger the breaker.
- **No displacement.** A drift through the OB without displacement makes the break low-conviction.
- **Reversed polarity.** A bullish OB doesn't become a bullish breaker — it becomes a bearish one (see [bearish-breaker](bearish-breaker.md)).

## Related Concepts

- [breaker-block](breaker-block.md), [bearish-breaker](bearish-breaker.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [mitigation-block](mitigation-block.md), [failed-breaker](failed-breaker.md), [choch-bullish](../01-market-structure/choch-bullish.md), [bos-bullish](../01-market-structure/bos-bullish.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
