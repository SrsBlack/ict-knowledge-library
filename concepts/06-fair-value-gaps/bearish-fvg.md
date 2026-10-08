# Bearish FVG

**Category:** 06-fair-value-gaps
**Aliases:** bearish gap, BeFVG, SIBI (SMC)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-REINFORCED, ICT-2016-MMT-TRENDLINE, ICT-2022-MENTORSHIP-EP06, ICT-2017-STT-LRLR-CONSOLIDATION, ICT-2017-STT-INTRAWEEK-REVERSALS
**Tags:** fvg, bearish, foundational

⚠ **Edited 2026-10-08 per audit.** "SIBI" (sell-side imbalance / buy-side inefficiency) has zero
hits in either corpus — kept only as an alias tagged `(SMC)`. The downward-displacement candle
test and the CE-entry worked example were invented; both removed or corrected below, matching
[fair-value-gap](fair-value-gap.md) and [bullish-fvg](bullish-fvg.md). Re-sourced off the stub
`ICT-2016-FVG-INTRO` to the evidenced Dec-2016/Nov-2016 packets and 2022 episode.

## Definition

A bearish FVG is a 3-candle imbalance where `H_{n+1} < L_{n-1}`: "the upper end of the fair value
gap is going to be the low of candle number one[;] the lower end of the fair value gap is going
to be the high of candle number three... that's the fair value [gap]" (`ICT-2022-MENTORSHIP-EP06`
[16:41]–[17:09]); identically in Nov-2016: "fair value gap from the low of this candle to the
high of this candle. There's only been down movement with this candle's body."
(`ICT-2016-MMT-TRENDLINE` [13:11]–[13:18]); and in Dec-2016: "the low of the previous candle and
the high of the count [candle] to the right of the down candle" (`ICT-2016-FVG-REINFORCED` [04:28]).
Sits as a **premium-array reference** when above current price: "the fair value gap and bearish
order block in the premium level" (`ICT-2017-STT-LRLR-CONSOLIDATION` [08:26]); "up into a fair
value gap premium PD array" (`ICT-2017-STT-INTRAWEEK-REVERSALS` [17:59]).

## Formal Criteria

- Three consecutive candles n-1, n, n+1.
- `H_{n+1} < L_{n-1}` strictly (wick-to-wick).
- Unworked region: `[H_{n+1}, L_{n-1}]`.
- **No downward-displacement test on candle n.** ICT's 2022 context rule for a bearish FVG is a
  setup filter, not a candle test: "optimal formations of the bearish ict fair value gap will be
  found after a run into buy side liquidity" (`ICT-2022-MENTORSHIP-EP06` [14:42]–[15:14]). See
  [fair-value-gap](fair-value-gap.md) Common Mistakes.

## Formula / Math

```
bearish_FVG(n) := H_{n+1} < L_{n-1}

fvg_low  := H_{n+1}
fvg_high := L_{n-1}
fvg_size := fvg_high - fvg_low
```

## Machine-Readable

```json
{
  "id": "bearish-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["BeFVG", "SIBI (SMC, unverified in corpus)"],
  "criteria": [
    {"id": "c1", "expr": "H_{n+1} < L_{n-1}"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["fair-value-gap","bullish-fvg","inversion-fvg","consequent-encroachment","ce-as-primary-entry","premium-array","bearish-order-block","displacement-definition"],
  "sources": ["ICT-2016-FVG-REINFORCED","ICT-2016-MMT-TRENDLINE","ICT-2022-MENTORSHIP-EP06","ICT-2017-STT-LRLR-CONSOLIDATION","ICT-2017-STT-INTRAWEEK-REVERSALS"]
}
```

## Visual Pattern

```
   ▼
   █  ← n-1
     ▼
     █
     █  ← n
     █
     █
        ▼   ← gap region (FVG)
          ▼
          █  ← n+1 (high < n-1 low)
          █
          ▼

   FVG = [H_{n+1}, L_{n-1}], above candle n+1, below candle n-1.
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 bearish FVG, 2022 entry convention:**
- H1: `L_{n-1}` = 1.0945, `H_{n+1}` = 1.0938. FVG = [1.0938, 1.0945], 7 pips.
- HTF bearish; price retraces toward the zone.
- ICT's stated entry is the near edge (candle n+1's high), stop beyond candle n-1 or candle n —
  not a midpoint entry with an invented pip buffer: "the easiest entry would be trading just
  above candle number three's high... place your stop right above can[dle] number one or...
  number two" (`ICT-2022-MENTORSHIP-EP06` [17:09]–[17:38]).

## Common Mistakes

- **Going short into bullish HTF bias.** A bearish FVG alone doesn't defeat bias.
- **Treating SIBI as ICT's own 2016/2022 term.** 0 hits in either corpus; a later label.
- **Claiming a stated CE-frequency ("holds at CE without going further").** No frequency
  statement for CE exists anywhere in the corpus — see [consequent-encroachment](consequent-encroachment.md).
- **Requiring a downward-displacement shape on candle n.** Not in the corpus — see Formal Criteria.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [inversion-fvg](inversion-fvg.md).
- [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md).
- [premium-array](../05-pd-arrays/premium-array.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md).
- [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-REINFORCED` — "Month 04 — ICT Fair Value Gaps FVG" (Dec 2016). Wick-to-wick
  geometry [04:28].
- `ICT-2016-MMT-TRENDLINE` — "Month 03 — Market Maker Trap Trendline Phantoms" (Nov 2016).
  Bearish wick-to-wick restatement [13:11]–[13:18].
- `ICT-2022-MENTORSHIP-EP06` — Bearish geometry [16:41]–[17:09]; context filter (not a candle
  test) [14:42]–[15:14]; near-edge entry convention [17:09]–[17:38].
- `ICT-2017-STT-LRLR-CONSOLIDATION` — "Month 07 — Short Term Trading, Low Resistance Liquidity
  Runs Part 1" — premium-level framing [08:26].
- `ICT-2017-STT-INTRAWEEK-REVERSALS` — "Month 07 — Intraweek Market Reversals & Overlapping
  Models" — premium PD-array framing [17:59].
