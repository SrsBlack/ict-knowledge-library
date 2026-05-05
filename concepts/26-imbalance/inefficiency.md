# Inefficiency

**Category:** 26-imbalance
**Aliases:** market inefficiency, price inefficiency
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** inefficiency, imbalance

## Definition

Inefficiency is ICT's synonym for [imbalance-definition](imbalance-definition.md): a price region where two-sided auction did not happen, leaving the market with an unworked zone. The terms are interchangeable in ICT's vocabulary; "inefficiency" emphasizes the *market microstructure interpretation* (the order flow was one-sided), while "imbalance" emphasizes the *visual pattern* on the chart. Both refer to the same phenomenon. The algorithm tends to revisit inefficiencies to "deliver them efficiently" — i.e., complete the missing trade.

## Formal Criteria

Same as [imbalance-definition](imbalance-definition.md):

- A region where consecutive candles' price ranges do not overlap.
- Formed during displacement.
- Tagged with directional polarity (bullish if formed during an up-displacement, bearish during down).

## Formula / Math

```
inefficiency == imbalance      # synonyms in ICT vocabulary

bullish_inefficiency(n) := L_{n+1} > H_{n-1}     # same as bullish FVG
bearish_inefficiency(n) := H_{n+1} < L_{n-1}     # same as bearish FVG
```

## Machine-Readable

```json
{
  "id": "inefficiency",
  "category": "26-imbalance",
  "aliases": ["market-inefficiency", "price-inefficiency"],
  "criteria": [
    {"id": "c1", "expr": "synonym_of_imbalance == true"},
    {"id": "c2", "expr": "consecutive_price_regions_dont_overlap == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["imbalance-definition","imbalance-vs-fvg","imbalance-rebalance","fair-value-gap","displacement-definition"],
  "sources": ["ICT-2016-FVG-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

See [imbalance-definition](imbalance-definition.md).

## Timeframes

All TFs.

## Examples

See [imbalance-definition](imbalance-definition.md).

## Common Mistakes

- **Treating "inefficiency" as a different concept from "imbalance."** They're synonyms; ICT uses both interchangeably depending on context.
- **Calling any pullback an inefficiency rebalance.** The pullback must reach the imbalance zone (typically at minimum CE) to count as rebalanced.

## Related Concepts

- [imbalance-definition](imbalance-definition.md) — primary entry point for the umbrella concept.
- [imbalance-vs-fvg](imbalance-vs-fvg.md), [imbalance-rebalance](imbalance-rebalance.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
