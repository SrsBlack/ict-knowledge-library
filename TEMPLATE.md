# <Concept Name>

**Category:** <directory under concepts/>
**Aliases:** <other names this concept goes by>
**ICT Confidence:** <high | medium | community-attributed | disputed | demo-stage>
**Year Introduced:** <YYYY>
**Year Refined:** <YYYY — last meaningful update; same as Year Introduced if never refined>
**Source IDs:** <comma-separated SOURCES.md IDs, e.g. ICT-2022-E03, X-2024-1213>
**Tags:** <comma-separated keywords>

## Definition

One-paragraph plain-English definition of the concept. What it is, why it matters in the ICT framework.

## Formal Criteria

Strict, testable bullet list — what MUST be true for a price-action event to qualify.

- Criterion 1
- Criterion 2
- Criterion 3

## Formula / Math

Exact quantitative criteria. Use precise notation:

- Variables: define each (e.g. `H_n` = high of bar n, `L_n` = low of bar n)
- Conditions: write as inequalities or boolean expressions
- Ranges: state in pips/points/percent

```
example:
bullish_FVG(n) := L_{n+1} > H_{n-1}
gap_size      := L_{n+1} - H_{n-1}
```

## Machine-Readable

```json
{
  "id": "<kebab-case-id matching filename>",
  "category": "<NN-dirname>",
  "aliases": ["<alias1>", "<alias2>"],
  "criteria": [
    {"id": "c1", "expr": "<formal expression>"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "<high | medium | community-attributed | disputed | demo-stage>",
  "year_introduced": "YYYY",
  "year_refined": "YYYY",
  "related": ["<related-concept-id>"],
  "sources": ["<SOURCES.md ID>"]
}
```

## Visual Pattern

ASCII chart or written description of how the concept appears on price charts. Indicate which bars/candles, what direction, what wicks/bodies look like.

## Timeframes

Which timeframes this concept applies to. Note any TF-specific rules (e.g. "daily-only", "M15+").

## Examples

Labeled examples with full conditions:

**Example 1 — <symbol> <date> <TF>:**
- Setup: ...
- Trigger: ...
- Outcome: ...

## Common Mistakes

Frequent misidentifications, edge cases, and what does NOT count as this concept.

## ICT vs Community

> Include this section ONLY if the concept's origin is community-attributed, disputed, or refined by a non-ICT teacher (e.g. CRT by Romeo, Smart Money Concepts terminology).

Explicit attribution paragraph: who first published, when, what ICT has said about it (with source citation), and how this library treats it.

## Related Concepts

Cross-links to other files in this library:

- [Related Concept](../<dir>/<file>.md) — relationship description

## Citations

Sources, in chronological order. Each must reference a SOURCES.md ID:

- `ICT-YYYY-XXX` — quote or paraphrase, optional timestamp
- `X-YYYY-MMDD` — tweet/thread excerpt
