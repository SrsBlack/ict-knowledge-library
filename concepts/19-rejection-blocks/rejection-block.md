# Rejection Block

**Category:** 19-rejection-blocks
**Aliases:** RB, wick rejection block, long-wick block
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
**Tags:** rejection-block, wick, foundational

## Definition

A rejection block is a candle (or short cluster) characterized by a **strong wick rejection at a key level**, leaving a long wick relative to the body. The wick documents that price tried to go through a level and was forcibly rejected. ⚠ **The level is the body edge, not the wick.** The long wick is what *identifies* the candle; ICT draws the rejection block "just above the candle's body, not the wicks" and expects the wick itself to be run out (`ICT-2017-HTF-PD-ARRAYS` [18:49–18:57]). Less standardized than OBs and FVGs; ICT teaches RBs as secondary references.

## Formal Criteria

A rejection block:

- A candle has a long wick on one side (≥ 60% of total candle range).
- The wick reaches a known key level (HTF swing, prior FVG/OB edge, round number, session extreme).
- Price rejects the wick extreme strongly (the close is far from the wick tip).
- Often combined with displacement on the next candle confirming the rejection.

For a **bullish** RB: long lower wick rejecting downward (price tried to go down, rejected up).
For a **bearish** RB: long upper wick rejecting upward (price tried to go up, rejected down).

## Formula / Math

```
range_n = high(n) - low(n)
body_n  = abs(close(n) - open(n))

# Bullish RB:
lower_wick = min(open(n), close(n)) - low(n)
is_bullish_rb := lower_wick >= 0.60 * range_n
                  AND wick reaches known key level
                  AND close near top of range

# Bearish RB: symmetric on upper wick
```

## Machine-Readable

```json
{
  "id": "rejection-block",
  "category": "19-rejection-blocks",
  "aliases": ["RB", "wick-rejection-block", "long-wick-block"],
  "criteria": [
    {"id": "c1", "expr": "wick_pct >= 0.60 of candle range"},
    {"id": "c2", "expr": "wick reaches known key level"},
    {"id": "c3", "expr": "rejection confirmed by close + next-candle displacement"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["bullish-rejection-block","bearish-rejection-block","liquidity-sweep","turtle-soup","stop-run-definition","bullish-order-block","bearish-order-block"],
  "sources": ["ICT-2017-HTF-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish rejection block:
          ▲
          █  ← close near top of range
          █
          █
        ▼     ← long lower wick (60%+ of range)
        ▼
        ▼
       (wick tip reaches key level)

   bearish RB: mirror.
```

## Timeframes

M15+. Lower TFs have noisy long wicks that aren't structurally meaningful.

## Examples

**Example 1 — bullish RB at PWL:**
- H1 candle: open 1.0865, close 1.0875, low 1.0848 (deep wick), high 1.0876.
- Lower wick = 0.0017 (17 pips); range = 0.0028 (28 pips); wick% = 60.7%.
- Wick tip 1.0848 = PWL (prior week low) SSL pool.
- Next H1: 22-pip green displacement; bullish FVG.
- → bullish rejection block at the PWL level. Long zone reference for future retests.

## Common Mistakes

- **Calling every long-wick candle "RB."** Without a key-level anchor, the long wick is just noise.
- **Confusing RB with sweep.** Liquidity sweeps and rejection blocks overlap heavily. RBs emphasize the resulting *zone* (the wick + body); sweeps emphasize the *event*.
- **Trading RB without confirmation.** Single-candle RB with no follow-through displacement is low-conviction.

## Related Concepts

- [bullish-rejection-block](bullish-rejection-block.md), [bearish-rejection-block](bearish-rejection-block.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [turtle-soup](../20-turtle-soup/turtle-soup.md), [stop-run-definition](../29-stop-runs/stop-run-definition.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md).

## Citations

- `ICT-2017-HTF-PD-ARRAYS` (18:46–19:05) the rejection block placed second in the premium ladder; (18:49) "just above the candle's body, not the wicks"; (29:02–29:15) the discount mirror.
- `ICT-2022-MENTORSHIP-OVERVIEW` — 2022 restatement.
