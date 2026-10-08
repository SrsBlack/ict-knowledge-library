# Bullish FVG

**Category:** 06-fair-value-gaps
**Aliases:** bullish gap, BFVG, BISI (SMC)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-REINFORCED, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP18, ICT-2017-INTRADAY-TOP-DOWN
**Tags:** fvg, bullish, foundational

⚠ **Edited 2026-10-08 per audit.** "BISI" (buy-side imbalance / sell-side inefficiency) has zero
hits in either corpus (153 2016-17/2020-21 packets, 41 2022 Mentorship episodes, searched
`bisi|sibi` word-bounded) — kept only as an alias tagged `(SMC)`, not presented as ICT's own
2016/2022 term. The body/wick-ratio displacement criterion and the CE-entry worked example were
invented; both removed or corrected below, matching the fix applied to
[fair-value-gap](fair-value-gap.md) and [bearish-fvg](bearish-fvg.md). Re-sourced off the stub
`ICT-2016-FVG-INTRO` to the evidenced Dec-2016 packet and 2022 episodes.

## Definition

A bullish FVG is a 3-candle imbalance where `L_{n+1} > H_{n-1}`: "bullish ict fair value gap...
three candle[] formation... candle number one's high[,] that is the low of the fair value gap[;]
candle number three's low is the high of the fair value gap[;] candle number two is where the
fair value gap will be formed" (`ICT-2022-MENTORSHIP-EP06` [22:35]–[23:00]). The unworked zone
between the two non-overlapping wicks stays open as a future revisit target. Bullish FVGs are
**discount-array references** when sitting below current price: "What does that make that area
down here? Premium or discount? Discount. So[,] soon as this fair value gap forms, we know that
it's likely to see it rally up" (`ICT-2022-MENTORSHIP-EP18` [16:01]).

## Formal Criteria

- Three consecutive candles n-1, n, n+1.
- `L_{n+1} > H_{n-1}` strictly (wick-to-wick).
- Unworked region: `[H_{n-1}, L_{n+1}]`.
- Persists until rebalanced.
- **No body/wick-ratio or displacement test on candle n.** No statement in either corpus requires
  "large green body, minimal upper wick" or any comparable shape rule — see
  [fair-value-gap](fair-value-gap.md) Common Mistakes for the displacement finding, which applies
  identically here.

## Formula / Math

```
bullish_FVG(n) := L_{n+1} > H_{n-1}

fvg_low  := H_{n-1}
fvg_high := L_{n+1}
fvg_size := fvg_high - fvg_low
```

## Machine-Readable

```json
{
  "id": "bullish-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["BFVG", "BISI (SMC, unverified in corpus)"],
  "criteria": [
    {"id": "c1", "expr": "L_{n+1} > H_{n-1}"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["fair-value-gap","bearish-fvg","inversion-fvg","consequent-encroachment","ce-as-primary-entry","discount-array","bullish-order-block","displacement-definition"],
  "sources": ["ICT-2016-FVG-REINFORCED","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP18","ICT-2017-INTRADAY-TOP-DOWN"]
}
```

## Visual Pattern

```
         ▲
         █  ← n+1 (low > n-1 high)
         █
       ▲     ← gap region (FVG)
       █
       █  ← n
       █
       █
     ▲
     █  ← n-1
   ▲
   FVG = [H_{n-1}, L_{n+1}], below candle n+1, above candle n-1.
```

## Timeframes

All TFs.

## Examples

**Example 1 — M15 bullish FVG, 2022 entry convention:**
- M15: `H_{n-1}` = 1.0860, `L_{n+1}` = 1.0865. FVG = [1.0860, 1.0865], 5 pips.
- HTF bullish; price returns toward the zone.
- ICT's stated entry is the near edge (candle n+1's low), with the stop beyond candle n-1 or
  candle n — not a midpoint entry with an invented pip buffer: "the easiest entry would be
  trading just above candle number three's high... place your stop right above can[dle] number
  one or... number two" (`ICT-2022-MENTORSHIP-EP06` [17:09]–[17:38], stated for the bearish case
  and mirrored here per "everything i teach... is reversed the same way" [22:35]).

## Common Mistakes

- **Bullish-FVG long against bearish HTF bias.** Even a textbook bullish FVG fails frequently when
  HTF says price should keep falling.
- **Treating BISI as ICT's own 2016/2022 term.** It has 0 hits in either corpus; it is a later
  (plausibly 2023+) label layered onto this geometry.
- **Requiring a body/wick-ratio "displacement" shape on candle n.** Not in the corpus — see
  Formal Criteria.
- **Filtering out small FVGs by ATR.** ICT trades a 2-pip gap directly and works "small little"
  FVGs throughout 2022 — see [fair-value-gap](fair-value-gap.md) Common Mistakes.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bearish-fvg](bearish-fvg.md), [inversion-fvg](inversion-fvg.md).
- [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md).
- [discount-array](../05-pd-arrays/discount-array.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md).
- [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-REINFORCED` — "Month 04 — ICT Fair Value Gaps FVG" (Dec 2016). Wick-to-wick
  geometry, shared basis with [fair-value-gap](fair-value-gap.md).
- `ICT-2022-MENTORSHIP-EP06` — Bullish-specific geometry statement [22:35]–[23:00]; near-edge
  entry convention (stated bearish, mirrored) [17:09]–[17:38], [22:35].
- `ICT-2022-MENTORSHIP-EP18` — Discount-array framing of a bullish FVG [16:01].
- `ICT-2017-INTRADAY-TOP-DOWN` — "Month 12 — Intraday Top Down Analysis" — "a lower time frame
  discount array like a fair value gap" [34:58].
