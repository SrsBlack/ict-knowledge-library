# HTF PD Array Hierarchy

**Category:** 05-pd-arrays
**Aliases:** multi-TF PDA hierarchy, top-down PD arrays, HTF array prioritization
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2024
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW, ICT-2024-MENTORSHIP-MODULE-LIST
**Tags:** pd-array, hierarchy, multi-tf, top-down

## Definition

HTF PD array hierarchy is the multi-timeframe extension of [pd-array-hierarchy](pd-array-hierarchy.md): higher-timeframe arrays carry more conviction than lower-timeframe arrays of the same type. ICT's discipline is **top-down analysis** — start from monthly / weekly / daily, identify the dealing range and highest-priority PD array on each TF, then descend to entry TF (H1 / M15 / M5) only inside the HTF array's price range.

## Formal Criteria

The TF priority ladder ICT teaches:

1. **Monthly (MN)** — dealing range; if present, primary PD array is the conviction anchor.
2. **Weekly (W)** — sub-range; primary PD array.
3. **Daily (D)** — sub-range; primary PD array. Most ICT day-traders read bias from D.
4. **H4** — sub-range; entry refinement context.
5. **H1** — entry refinement.
6. **M15 / M5** — entry trigger only.

The principle: an entry TF setup is **valid only if the HTF array supports it**. A discount-side long setup on M5 when the D array says price is in premium = wrong-side trade.

## Formula / Math

```
HTF_priority_chain = [MN, W, D, H4, H1, M15, M5]

valid_entry(setup) :=
    setup.entry_TF in HTF_priority_chain
    AND for each higher_TF in chain above setup.entry_TF:
        higher_TF_PDA is compatible with setup direction
```

"Compatible" means: setup is a long → higher-TF PDA is a discount array OR HTF bias is bullish; setup is a short → premium array OR bearish bias.

## Machine-Readable

```json
{
  "id": "htf-pd-array-hierarchy",
  "category": "05-pd-arrays",
  "aliases": ["multi-tf-PDA", "top-down-PD-arrays"],
  "criteria": [
    {"id": "c1", "expr": "HTF_array_supports_entry_TF_setup == true"},
    {"id": "c2", "expr": "TF_priority_order == [MN, W, D, H4, H1, M15, M5]"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2024",
  "related": ["pd-array-definition","pd-array-hierarchy","pd-array-nesting","pd-array-confluence","htf-bias-framework","top-down-analysis","dealing-range"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW","ICT-2024-MENTORSHIP-MODULE-LIST"]
}
```

## Visual Pattern

```
   Daily dealing range
   ───────────────────────────  D LTH
                ▒▒  D bearish OB (premium, primary HTF array)
                ▒▒    │
   ─────────────────── D EQ
                       │
                       ↓ D is bullish bias only if price is below EQ
                       │
                ░░  D bullish OB (discount, primary HTF array)
                ░░  ───── inside this zone, drill down to H4...
   ───────────────────────────  D LTL

   Inside D bullish OB at 1.0820-1.0830:
     H4: contains a bullish FVG at 1.0823-1.0827
     M15: nested bullish OB at 1.0824-1.0826
     M5: entry trigger on M5 bullish FVG re-test inside the M15 OB
```

## Timeframes

The whole concept is multi-TF; every TF in the chain participates.

## Examples

**Example 1 — top-down chain:**
- MN: bullish dealing range, EQ at 1.0750. Current price 1.0890 = MN premium → MN says watch for shorts only at deep premium.
- W: bullish, EQ 1.0850, current 1.0890 = shallow W premium → W also leans toward HTF shorts.
- D: bearish CHoCH last week, current price approaching D bearish OB at 1.0900–1.0920 (premium of D range) → D says short setups valid here.
- H4 / H1: confirm with bearish MSS + FVG.
- → entry valid because all HTFs support the short.

## Common Mistakes

- **Skipping the top-down check.** Trading M5 setups against the daily PD-array context produces low-probability entries that win-rate poorly even when they "look textbook."
- **Mixing TFs incoherently.** A long setup with a discount-array M15 entry inside an HTF premium zone (against HTF bias) needs a very specific HTF reversal context — usually a CHoCH/MSS. Don't take such trades casually.
- **Overweighting MN/W.** MN/W context is structural background; D / H4 set the trade direction. Don't refuse a clean D setup just because MN is technically "in the other half."

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [pd-array-hierarchy](pd-array-hierarchy.md), [pd-array-nesting](pd-array-nesting.md), [pd-array-confluence](pd-array-confluence.md).
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [top-down-analysis](../25-htf-bias/top-down-analysis.md).
- [dealing-range](dealing-range.md).

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW` — top-down analysis taught.
- `ICT-2024-MENTORSHIP-MODULE-LIST` — HTF-LTF alignment refined.
