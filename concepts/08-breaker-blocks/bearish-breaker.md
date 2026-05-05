# Bearish Breaker

**Category:** 08-breaker-blocks
**Aliases:** bearish breaker block, BeBB, supply breaker
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** breaker, bearish

## Definition

A bearish breaker is a **failed bullish order block** — an originally bullish OB whose body price violated by closing below with displacement. The OB body now functions as a **bearish resistance zone** on retest from below. Mirror of [bullish-breaker](bullish-breaker.md).

## Formal Criteria

- An originally bullish OB existed.
- Price broke BELOW the OB body (close below OB low) with bearish displacement.
- Often a bearish CHoCH or BOS accompanies.
- On retest from below, the zone acts as bearish resistance.

## Formula / Math

```
break_event(bullish_ob) := close_t < low(ob_body)
                            AND bearish_displacement_present_in_break

bearish_breaker_active(ob, retest) := high(retest) reaches low(ob_body)
                                       AND bearish_rejection_with_displacement
```

## Machine-Readable

```json
{
  "id": "bearish-breaker",
  "category": "08-breaker-blocks",
  "aliases": ["bearish-breaker-block", "BeBB", "supply-breaker"],
  "criteria": [
    {"id": "c1", "expr": "originally_bullish_OB"},
    {"id": "c2", "expr": "close_below_OB_low_with_bearish_displacement"},
    {"id": "c3", "expr": "retest_acts_as_resistance"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["breaker-block","bullish-breaker","bullish-order-block","mitigation-block","failed-breaker","choch-bearish","bos-bearish"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bearish breaker formation:

   Step 1: bullish OB forms (last bearish candle before bullish move)
   Step 2: later, price breaks DOWN through OB low with displacement
           → bearish CHoCH/BOS
   Step 3: retest comes back up to OB body
   Step 4: bearish rejection at OB body → confirmed bearish breaker
                                       (short entry zone)
```

## Timeframes

M15+.

## Examples

**Example 1 — H4 bullish OB → bearish breaker:**
- H4 bullish OB formed: body 1.0820–1.0830.
- Days later, H4 closes at 1.0810 with bearish displacement; bearish CHoCH on H4.
- Hours later, H4 retraces up to 1.0825 (inside original OB body).
- Bearish reaction with FVG down → confirmed bearish breaker.
- Short at MT 1.0825, SL above OB high 1.0833 (3-pip buffer). Risk = 8 pips.

## Common Mistakes

- **Mistaken polarity flip direction.** Original bullish OB becomes bearish breaker (this file). Original bearish OB becomes bullish breaker.
- **Insufficient displacement on the break.** Slow drifts through the OB don't qualify.

## Related Concepts

- [breaker-block](breaker-block.md), [bullish-breaker](bullish-breaker.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [mitigation-block](mitigation-block.md), [failed-breaker](failed-breaker.md), [choch-bearish](../01-market-structure/choch-bearish.md), [bos-bearish](../01-market-structure/bos-bearish.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
