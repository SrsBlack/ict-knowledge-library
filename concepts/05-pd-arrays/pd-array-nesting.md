# PD Array Nesting

**Category:** 05-pd-arrays
**Aliases:** nesting, nested arrays, stacked PD arrays, strengthening principle
**ICT Confidence:** high
**Year Introduced:** 2024
**Year Refined:** 2025
**Source IDs:** ICT-2024-MENTORSHIP-MODULE-LIST, ICT-2025-ADV-LIQUIDITY
**Tags:** pd-array, nesting, confluence, 2025-refinement

## Definition

PD array nesting is ICT's principle that **multiple PD arrays overlapping or contained inside one another produce a higher-conviction zone than any single array alone**. A bullish OB whose body contains a bullish FVG is a nested setup — when price returns to that zone, both arrays act simultaneously, multiplying the algorithmic significance. ICT's 2024–2025 advanced-liquidity series formalized this as the **strengthening principle**: nesting raises a setup's quality non-linearly.

## Formal Criteria

A nested PD-array setup requires:

- **Two or more distinct PD arrays** of canonical types (OB, FVG, breaker, mitigation, rejection, vacuum, equilibrium).
- **Spatial overlap** — the price range of one array fully or partially contains another.
- **Same directional polarity** — both bullish or both bearish (a bullish FVG inside a bearish OB is not nesting; it's a conflict).
- **Compatible side of EQ** — both should sit in premium (for shorts) or discount (for longs) of the reference range.
- Bonus: cross-TF nesting (HTF array containing LTF array) is the strongest form.

## Formula / Math

```
nest(A, B) :=
    polarity(A) == polarity(B)
    AND price_range(A) overlaps price_range(B)
    AND side_of_EQ(A) == side_of_EQ(B)

strength(setup) := count(arrays in nest)
                    * (1 + 0.5 if cross_TF_nest else 0)
```

ICT teaches the strength qualitatively as "fireworks" or "high probability" rather than via a numeric formula; the above is a quantification convention.

## Machine-Readable

```json
{
  "id": "pd-array-nesting",
  "category": "05-pd-arrays",
  "aliases": ["nesting", "stacked-PD-arrays", "strengthening-principle"],
  "criteria": [
    {"id": "c1", "expr": "two_or_more_canonical_PD_arrays_overlap == true"},
    {"id": "c2", "expr": "same_polarity == true"},
    {"id": "c3", "expr": "same_side_of_EQ == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2024",
  "year_refined": "2025",
  "related": ["pd-array-definition","pd-array-hierarchy","pd-array-confluence","htf-pd-array-hierarchy","fair-value-gap","bullish-order-block","breaker-block"],
  "sources": ["ICT-2024-MENTORSHIP-MODULE-LIST","ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
   nested bullish setup at discount:

            ▒▒▒▒▒  ← bullish OB body
            ▒░░▒▒
            ▒░░▒▒  ← bullish FVG nested inside OB body
            ▒░░▒▒
            ▒▒▒▒▒
              ↑
              both arrays act when price returns
```

## Timeframes

Same-TF nesting works at any TF. **Cross-TF nesting is the highest-quality form** — e.g., an H4 bullish OB containing an M15 bullish FVG inside its range.

## Examples

**Example 1 — nested H4 OB + M15 FVG:**
- HTF bullish; D dealing range 1.0800–1.1000.
- H4 bullish OB at 1.0820–1.0830 (deep discount).
- M15 bullish FVG at 1.0822–1.0826 (inside OB body).
- → high-conviction nested long: enter on FVG retest at 1.0824, SL below OB at 1.0815, target EQ then LTH.

**Example 2 — same-TF nest, OB + breaker overlap:**
- H1 bearish OB at 1.0945–1.0955 from a previous swing high.
- After CHoCH, the H1 swing low at 1.0950 is broken — that swing low becomes a bearish breaker.
- Both arrays overlap at 1.0950–1.0955 → nested bearish zone.

## Common Mistakes

- **Nesting non-canonical features.** A "nested" wick + round number is not nesting in ICT's sense; both elements must be canonical PD arrays.
- **Polarity mix-up.** A bullish FVG and bearish OB at the same level is a **conflict zone**, not a nest. Conflict zones often resolve violently in either direction; treat with caution.
- **Premium-discount mix.** Nesting requires same side of EQ. An array in shallow premium and another in shallow discount that happen to overlap geometrically across EQ is not a valid nest.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [pd-array-hierarchy](pd-array-hierarchy.md), [pd-array-confluence](pd-array-confluence.md), [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md).
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [breaker-block](../08-breaker-blocks/breaker-block.md).

## Citations

- `ICT-2024-MENTORSHIP-MODULE-LIST` — nesting referenced in 2024 mentorship modules.
- `ICT-2025-ADV-LIQUIDITY` — strengthening principle formalized in October 2025 advanced-liquidity series.
