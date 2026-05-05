# Gap Classification

**Category:** 09-displacement
**Aliases:** gap taxonomy, gap types, FVG vs VI vs liquidity-void
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** displacement, gap, classification

## Definition

Gap Classification distinguishes the **three primary types of price gaps** that ICT teaches: **Fair Value Gap (FVG)**, **Volume Imbalance (VI)**, and **Liquidity Void**. Each is a different geometric / structural form of an unworked price region; conflating them produces sloppy analysis. This file is the cross-reference disambiguation between the displacement-side framing of these concepts (here in `09-displacement`) and the FVG-/imbalance-side framings elsewhere in the library.

## Formal Criteria

The three gap types:

| Type | Geometry | Time scope | File |
|---|---|---|---|
| **FVG** | 3-candle wick non-overlap (`L_{n+1} > H_{n-1}`) | 3 candles | [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) |
| **Volume Imbalance** | body-vs-body gap (open(n) ≠ close(n-1)); wicks may overlap | 2 candles | [volume-imbalance](../06-fair-value-gaps/volume-imbalance.md) |
| **Liquidity Void** | multi-candle expansion span with one-sided dominance | 5+ candles | [liquidity-void](../02-liquidity/liquidity-void.md) |

Containment hierarchy:
- A liquidity void typically **contains** one or more FVGs and/or VIs.
- An FVG is the strictest pattern (3-candle wick rule).
- A VI is looser than FVG (allows wick overlap).

## Formula / Math

```
fvg(n)            := 3-candle wick non-overlap
volume_imbalance(n) := 2-candle body gap (wicks may overlap)
liquidity_void(span)  := multi-candle expansion with directional dominance >= 80%
                          AND contains 1+ nested FVGs typically

# Containment:
liquidity_void ⊇ FVGs (often)
FVG ⊇ implied_VI (always — an FVG implies a body gap exists)
```

## Machine-Readable

```json
{
  "id": "gap-classification",
  "category": "09-displacement",
  "aliases": ["gap-taxonomy", "gap-types"],
  "criteria": [
    {"id": "c1", "expr": "FVG = 3-candle wick non-overlap"},
    {"id": "c2", "expr": "VI = 2-candle body gap (wicks may overlap)"},
    {"id": "c3", "expr": "liquidity_void = multi-candle expansion with directional dominance"},
    {"id": "c4", "expr": "containment: void contains FVGs; FVG implies VI"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["displacement-definition","displacement-and-fvg","fair-value-gap","volume-imbalance","liquidity-void","liquidity-void-vs-fvg","imbalance-vs-fvg"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   gap-type comparison:
   
   FVG (3-candle, wicks no overlap):
        ▲
        █  ← n+1
      ▲
      █  ← n
    ▲
    █  ← n-1
   wicks of n-1 and n+1 do not overlap.
   
   VI (2-candle, body gap, wicks may overlap):
   ▲
   █  ← n: opens above prior close
   O_n
   ───  body gap
   C_{n-1}
   █  ← n-1
   ▼
   wicks may overlap visually.
   
   Liquidity Void (5+ bars, one-sided dominance):
   ▲
   ██
   ██
   ██  ← 6 mostly-green bars
   ██   directional dominance >= 80%
   ██   contains 1-3 nested FVGs
   ██
```

## Timeframes

M5+.

## Examples

**Example 1 — gap-type identification:**
- Setup A: M15 with H_{n-1}=1.0860, L_{n+1}=1.0865 → FVG (5 pips, wick non-overlap).
- Setup B: M15 close 1.0855 next candle opens 1.0860, but wicks overlap at 1.0858 → Volume Imbalance, not FVG.
- Setup C: 6 consecutive H1 green candles, total 80 pips with 8% max pullback, contains 2 FVGs → Liquidity Void containing FVGs.

## Common Mistakes

- **Conflating all gap types as "FVG".** They have specific geometric definitions; mislabeling produces inconsistent analysis.
- **Treating a void as a single FVG.** A void usually contains multiple FVGs; treating the whole void as one FVG misses the precise entry levels.
- **Treating VI as FVG.** VIs are softer references; don't claim FVG-level conviction for VI-only setups.

## Related Concepts

- [displacement-definition](displacement-definition.md), [displacement-and-fvg](displacement-and-fvg.md).
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [volume-imbalance](../06-fair-value-gaps/volume-imbalance.md), [liquidity-void](../02-liquidity/liquidity-void.md), [liquidity-void-vs-fvg](../06-fair-value-gaps/liquidity-void-vs-fvg.md), [imbalance-vs-fvg](../26-imbalance/imbalance-vs-fvg.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.
