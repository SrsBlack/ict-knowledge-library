# ICT 2023 Model

**Category:** 31-models
**Aliases:** ICT 2023 setup, 2023 refined model
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2023-QUARTERLY-THEORY
**Tags:** model, 2023, refinement

## Definition

The ICT 2023 Model is a **refined evolution of the 2022 Model** that integrates Quarterly Theory (the fractal time framework introduced 2023) and tightens the FVG protocol. The 2023 framing: same 7-step structure as 2022, with additional emphasis on **time-fractal alignment** (90-min cycles, Q3 distribution windows) and macro-time precision.

## Formal Criteria

Adds to the [ict-2022-model](ict-2022-model.md):

- **Quarterly Theory alignment** — preferred trade execution during the daily Q3 window (NY AM, the distribution quarter).
- **90-min cycle confirmation** — the setup should fire during the M (manipulation) → D (distribution) transition of the active 90-min cycle.
- **Macro-time integration** — entries inside macro windows (02:50–03:10 / 09:50–10:10 / etc.) get conviction bonus.
- **FVG protocol** — preference for HTF FVG with LTF FVG nested inside (per [nested-fvg](../06-fair-value-gaps/nested-fvg.md)).

## Formula / Math

```
ict_2023_model :=
    ict_2022_model
    AND quarterly_theory_phase == distribution (preferred)
    AND 90min_cycle in M_to_D_transition
    AND macro_time_alignment (bonus)
    AND nested_FVG_when_possible
```

## Machine-Readable

```json
{
  "id": "ict-2023-model",
  "category": "31-models",
  "aliases": ["ICT-2023-setup", "2023-refined-model"],
  "criteria": [
    {"id": "c1", "expr": "extends_ict_2022_model"},
    {"id": "c2", "expr": "adds_quarterly_theory_alignment"},
    {"id": "c3", "expr": "adds_macro_time_integration"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2023",
  "related": ["ict-2022-model","ict-2024-model","quarterly-shift-theory","90-minute-cycle","macro-times-overview","nested-fvg","silver-bullet-overview"],
  "sources": ["ICT-2023-QUARTERLY-THEORY"]
}
```

## Visual Pattern

```
   ICT 2023 Model integration:

   2022 Model 7-step base
        +
   Quarterly Theory Q3 window (NY AM, distribution)
        +
   90-min cycle in M → D transition
        +
   Macro time alignment (e.g. 09:50-10:10)
        +
   Nested FVG (HTF FVG containing LTF FVG)
        ↓
   high-conviction integrated setup
```

## Timeframes

M5–H4.

## Examples

**Example 1 — full 2023 model on NY AM:**
- 2022 baseline: bias bullish, killzone NY AM, sweep, displacement, FVG, CE entry, SL, TP. ✓
- QT: 09:00–12:00 = daily Q3 (distribution). ✓
- 90-min: 09:00–10:30; M-phase ended around 09:30 (sweep), D-phase starting 09:35. ✓
- Macro: 09:50–10:10 active. ✓
- FVG: H1 FVG 1.0925–1.0935 contains M15 FVG 1.0928–1.0932. ✓
- → all conditions stack. Highest-conviction 2023 model execution.

## Common Mistakes

- **Treating 2023 as replacing 2022.** It extends, not replaces. A 2022 Model setup is still valid; 2023 just adds optional confluence layers.
- **Forcing all 2023 layers.** Not every setup gets all bonuses; QT-misaligned setups are still tradeable, just lower-conviction.

## Related Concepts

- [ict-2022-model](ict-2022-model.md), [ict-2024-model](ict-2024-model.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [90-minute-cycle](../04-time-cycles/90-minute-cycle.md), [macro-times-overview](../04-time-cycles/macro-times-overview.md), [nested-fvg](../06-fair-value-gaps/nested-fvg.md), [silver-bullet-overview](../11-silver-bullet/silver-bullet-overview.md).

## Citations

- `ICT-2023-QUARTERLY-THEORY`.
