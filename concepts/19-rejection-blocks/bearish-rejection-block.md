# Bearish Rejection Block

**Category:** 19-rejection-blocks
**Aliases:** bearish RB, upper-wick rejection block
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
**Tags:** rejection-block, bearish

## Definition

A bearish rejection block is a candle with a **long upper wick** rejecting upward at a key level, leaving the body near the bottom of the range. Documents a BSL sweep + immediate reversal. Premium-side reference for future short entries. ⚠ **The tradeable level sits just above the candle's body, not at the wick high** — "the rejection block would be just above the candle's body, not the wicks" (`ICT-2017-HTF-PD-ARRAYS` [18:49]). Mirror of [bullish-rejection-block](bullish-rejection-block.md).

## Formal Criteria

- Long upper wick (≥ 60% of range).
- Wick tip reaches known BSL level (swing high, EQH, PWH/PDH, session high).
- Close near bottom of range.
- Next candle confirms with bearish displacement.

## Formula / Math

```
range_n     = high(n) - low(n)
upper_wick  = high(n) - max(open(n), close(n))

bearish_rb := upper_wick / range_n >= 0.60
              AND high(n) reaches known BSL level
              AND close(n) near bottom of range
              AND next-candle displacement down
```

## Machine-Readable

```json
{
  "id": "bearish-rejection-block",
  "category": "19-rejection-blocks",
  "aliases": ["bearish-RB", "upper-wick-rejection-block"],
  "criteria": [
    {"id": "c1", "expr": "upper_wick_pct >= 0.60"},
    {"id": "c2", "expr": "wick reaches known BSL level"},
    {"id": "c3", "expr": "close near bottom of range"},
    {"id": "c4", "expr": "bearish displacement next candle"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["rejection-block","bullish-rejection-block","buy-side-liquidity","liquidity-sweep","bearish-order-block","turtle-soup"],
  "sources": ["ICT-2017-HTF-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
         (high reaches BSL pool)
          ▲
          ▲
          ▲   ← long upper wick (60%+)
          ▼
          █
          █
          █
            ← close near bottom

   ▼▼▼▼   ← next candle: bearish displacement down
```

## Timeframes

M15+.

## Examples

**Example 1 — bearish RB at PDH:**
- H1 candle at 14:00 NY: open 1.0915, close 1.0902, low 1.0900, high 1.0928.
- Upper wick = 13 pips; range = 28 pips; wick% = 46% — borderline. With stricter parameters (e.g., wick 1.0935): wick = 20 pips, wick% = 56%, plus next-candle displacement down → bearish RB.
- Wick reaches PDH at 1.0928. Bearish reaction confirms.
- Short bias for the next move.

## Common Mistakes

- **Confusing RB with OB.** Bearish OB uses the body of a bullish candle before bearish displacement. Bearish RB uses the upper wick of a single rejection candle.
- **Single-candle reliance.** Confirm with next-candle displacement; an isolated long-wick is weak.

## Related Concepts

- [rejection-block](rejection-block.md), [bullish-rejection-block](bullish-rejection-block.md), [buy-side-liquidity](../02-liquidity/buy-side-liquidity.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [turtle-soup](../20-turtle-soup/turtle-soup.md).

## Citations

- `ICT-2017-HTF-PD-ARRAYS` (18:49–18:57) "the rejection block would be just above the candle's body, not the wicks… the next area of importance is the rejection block that would be just above the candle's body".
- `ICT-2022-MENTORSHIP-OVERVIEW` — 2022 restatement.
