# ICT 2024 Model

**Category:** 31-models
**Aliases:** ICT 2024 setup, 2024 mentorship model
**ICT Confidence:** medium
**Year Introduced:** 2024
**Year Refined:** 2024
**Source IDs:** ICT-2024-MENTORSHIP-MODULE-LIST
**Tags:** model, 2024, mentorship

## Definition

The ICT 2024 Model is the **2024 mentorship cycle's refined setup framework** — extends 2022/2023 with the 2024-era refinements: explicit FVG classification (immediate vs delayed rebalance), propulsion-block re-teaching, IFVG formalization, and stricter sweep-quality requirements. The 2024 model is less a "new" setup than a tightened-discipline iteration of the 2022 model integrating that year's vocabulary expansions.

## Formal Criteria

Extends [ict-2022-model](ict-2022-model.md) and [ict-2023-model](ict-2023-model.md) with:

- **FVG classification awareness** — distinguish immediate vs delayed rebalance ([fvg-classification-2025](../06-fair-value-gaps/fvg-classification-2025.md)).
- **IFVG recognition** — when the original FVG fails, treat it as an inversion zone.
- **Propulsion block** as continuation reference (post-OB displacement candle).
- **Stricter sweep wick** — 60%+ wick percentage required.
- **HTF PD-array nesting** — preference for HTF FVG containing LTF entry FVG.

## Formula / Math

```
ict_2024_model :=
    ict_2023_model_baseline
    AND awareness_of_FVG_classification
    AND IFVG_recognition_after_failure
    AND propulsion_block_as_continuation
    AND sweep_wick_pct >= 0.60
    AND HTF_PD_array_nesting_preferred
```

## Machine-Readable

```json
{
  "id": "ict-2024-model",
  "category": "31-models",
  "aliases": ["ICT-2024-setup", "2024-mentorship-model"],
  "criteria": [
    {"id": "c1", "expr": "extends_2022_and_2023_models"},
    {"id": "c2", "expr": "adds_FVG_classification_awareness"},
    {"id": "c3", "expr": "stricter_sweep_quality"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "medium",
  "year_introduced": "2024",
  "year_refined": "2024",
  "related": ["ict-2022-model","ict-2023-model","fvg-classification-2025","inversion-fvg","propulsion-block","pd-array-nesting","nested-fvg"],
  "sources": ["ICT-2024-MENTORSHIP-MODULE-LIST"]
}
```

## Visual Pattern

Same 7-step base as 2022 Model with 2024 refinements layered:

```
   2022 Model 7 steps
        +
   FVG classification (immediate vs delayed)
        +
   Propulsion-block continuation reference
        +
   IFVG recognition on failure
        +
   60%+ wick on sweep
        +
   HTF-LTF PD-array nesting
        ↓
   2024 Model = disciplined integration
```

## Timeframes

M5–H4.

## Examples

**Example 1 — applying 2024 refinements:**
- Standard 2022/2023 model setup: bullish, NY AM, sweep, displacement, FVG, CE entry.
- 2024 additions: sweep wick = 18 pips on 26-pip range (69%, exceeds 60% threshold ✓).
- The FVG is delayed (filled 12 bars after formation, not within 1-3) → fits the delayed-rebalance category, expects revisit at CE ✓.
- HTF FVG (H1 1.0925–1.0935) contains the M15 FVG (1.0928–1.0932) → nested ✓.
- All 2024 refinements pass; high-conviction execution.

## Common Mistakes

- **Treating 2024 as replacing prior models.** It refines, not replaces. The base structure remains 2022.
- **Demanding all 2024 layers.** Some setups won't have nested FVGs or don't fit the delayed/immediate classification cleanly — that's fine, base 2022/2023 model still applies.

## Related Concepts

- [ict-2022-model](ict-2022-model.md), [ict-2023-model](ict-2023-model.md).
- [fvg-classification-2025](../06-fair-value-gaps/fvg-classification-2025.md), [inversion-fvg](../06-fair-value-gaps/inversion-fvg.md), [propulsion-block](../07-order-blocks/propulsion-block.md), [pd-array-nesting](../05-pd-arrays/pd-array-nesting.md), [nested-fvg](../06-fair-value-gaps/nested-fvg.md).

## Citations

- `ICT-2024-MENTORSHIP-MODULE-LIST`.

> Confidence is `medium` because much of the 2024 mentorship is paywalled; public excerpts confirm the refinements but the canonical "ICT 2024 Model" framing is less standardized than 2022/2023.
