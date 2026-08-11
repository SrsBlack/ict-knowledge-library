# Bullish Rejection Block

**Category:** 19-rejection-blocks
**Aliases:** bullish RB, lower-wick rejection block
**ICT Confidence:** medium
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-HTF-PD-ARRAYS, ICT-2022-MENTORSHIP-OVERVIEW

⚠ **Re-dated 2018 → 2017 and the body/wick anchor corrected 2026-08-11.** The page previously
claimed 2018 citing only `ICT-2018-BLOCKS` — a registry stub with no video ID, no quotation and no
distilled content behind it. The rejection block is defined in **Jan 2017** in the PD-array hierarchy
lecture, and it is placed second in the premium ladder, immediately inside the old high
(`ICT-2017-HTF-PD-ARRAYS` [18:46–19:05]).

⚠ **The anchor was inverted.** These pages had the level drawn at the **wick**. ICT draws it at the
**body**: "the rejection block would be **just above the candle's body, not the wicks**. So the actual
high and low is the wick — but then the next area of importance is the rejection block that would be
just above the candle's body" [18:49–18:57]; the discount mirror is "just below the most lowest
candle and its body … if it has wicks, long wicks below it, we're only going to be looking for a move
**just below the bodies** of the candle" [29:02–29:15]. The long wick is what **identifies** the
candle; the **body edge is the level**, and the wick is the part expected to be run out. Same defect
class as the propulsion-block inversion corrected the same day.
**Tags:** rejection-block, bullish

## Definition

A bullish rejection block is a candle with a **long lower wick** that rejects downward at a key level, leaving the body near the top of the range. The wick documents an SSL sweep + immediate reversal. ⚠ **The tradeable level sits just below the candle's body, not at the wick low** — "we're only going to be looking for a move just below the bodies of the candle" (`ICT-2017-HTF-PD-ARRAYS` [29:09]). Functions as a discount-side reference for future long entries.

## Formal Criteria

- Long lower wick (≥ 60% of range).
- Wick tip reaches known SSL level (swing low, EQL, PWL/PDL, session low).
- Close near top of range.
- Next candle confirms with bullish displacement (ideally with FVG).

## Formula / Math

```
range_n     = high(n) - low(n)
lower_wick  = min(open(n), close(n)) - low(n)
upper_body  = max(open(n), close(n))

bullish_rb := lower_wick / range_n >= 0.60
              AND low(n) reaches known SSL level
              AND close(n) near upper_body
              AND next-candle displacement up
```

## Machine-Readable

```json
{
  "id": "bullish-rejection-block",
  "category": "19-rejection-blocks",
  "aliases": ["bullish-RB", "lower-wick-rejection-block"],
  "criteria": [
    {"id": "c1", "expr": "lower_wick_pct >= 0.60"},
    {"id": "c2", "expr": "wick reaches known SSL level"},
    {"id": "c3", "expr": "close near top of range"},
    {"id": "c4", "expr": "bullish displacement next candle"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["rejection-block","bearish-rejection-block","sell-side-liquidity","liquidity-sweep","bullish-order-block","turtle-soup"],
  "sources": ["ICT-2017-HTF-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
            ▲ ← close near top
            █
            █
            █
          ▼   ← long lower wick (60%+)
          ▼
          ▼
         (low reaches SSL pool)
   ▲▲▲▲   ← next candle: bullish displacement up
```

## Timeframes

M15+.

## Examples

**Example 1 — bullish RB at Asian SSL:**
- M15 at 03:00 NY (London open).
- Candle: open 1.0855, close 1.0871, low 1.0846, high 1.0872.
- Lower wick = 9 pips; range = 26 pips; wick% = 35% (not yet a strict RB).
- Compare to a stricter RB candle: open 1.0855, close 1.0871, low 1.0846, high 1.0872 with wick 60%+ requirement → would need low at 1.0840 or so. Adjust the threshold per instrument.
- When all criteria met: bullish RB at 1.0846 (Asian SSL). Long bias for the rest of London open.

## Common Mistakes

- **Body-vs-wick confusion.** RB references the wick rejection zone; OB references the body. Don't mix them.
- **No SSL anchor.** A long lower wick without a key-level anchor is just a hammer candle — interesting but not RB-grade.

## Related Concepts

- [rejection-block](rejection-block.md), [bearish-rejection-block](bearish-rejection-block.md), [sell-side-liquidity](../02-liquidity/sell-side-liquidity.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [turtle-soup](../20-turtle-soup/turtle-soup.md).

## Citations

- `ICT-2017-HTF-PD-ARRAYS` (29:02–29:15) "below the order block would be a rejection block, which is just below the most lowest candle and its body … we're only going to be looking for a move just below the bodies of the candle".
- `ICT-2022-MENTORSHIP-OVERVIEW` — 2022 restatement.
