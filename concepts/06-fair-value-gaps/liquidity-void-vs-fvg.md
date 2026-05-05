# Liquidity Void vs FVG — Disambiguation

**Category:** 06-fair-value-gaps
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fvg, liquidity-void, disambiguation, terminology

## Definition

This page resolves the confusion between **Liquidity Void** and **Fair Value Gap** — two related but distinct concepts.

**Short version:**
- **FVG** is a **specific 3-candle wick imbalance pattern**.
- **Liquidity Void** is a **multi-candle wider unworked region** that often *contains* one or more FVGs as nested sub-patterns.

A liquidity void is the macroscale; an FVG is the microscale. Voids can be 5–20+ bars wide; FVGs are exactly 3 candles wide.

## Formal Criteria

### FVG (specific)

- 3 candles, `L_{n+1} > H_{n-1}` (bullish) or `H_{n+1} < L_{n-1}` (bearish).
- Tight, well-defined geometric pattern.

### Liquidity Void (broader)

- Multi-candle expansion span (typically 5+ bars).
- Directional close percentage ≥ 80%.
- Minimal pullback within the span (≤ 30% of expansion size).
- Often contains 1–3 nested FVGs as internal patterns.

### Containment Relationship

```
FVG ⊂ liquidity_void  (often, but not always)
```

A liquidity void usually contains FVGs; an FVG is rarely a liquidity void on its own (too narrow geometrically).

## Formula / Math

```
is_fvg(n)         := strict_3_candle_imbalance(n)
is_liquidity_void(span) := multi_candle_expansion(span)
                            AND directional_close_pct(span) >= 0.8
                            AND max_pullback_pct(span) <= 0.3

# void can contain multiple FVGs:
contained_fvgs_in_void(void) := { fvg | fvg.range ⊂ void.range }
```

## Machine-Readable

```json
{
  "id": "liquidity-void-vs-fvg",
  "category": "06-fair-value-gaps",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "fvg == strict_3_candle_pattern"},
    {"id": "c2", "expr": "liquidity_void == multi_candle_expansion_with_directional_dominance"},
    {"id": "c3", "expr": "void_often_contains_FVGs == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["fair-value-gap","liquidity-void","imbalance-definition","displacement-definition","range-expansion"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Liquidity Void (5-bar example) containing FVGs:

   ▲                                      
   █  ← bar 1                             
   █                                      
   ▲▲                                      
   ██  ← bar 2 + nested FVG #1            
   ██                                      
   ▲▲▲                                     
   ███  ← bar 3                            
   ███                                     
   ▲▲▲▲                                    
   ████  ← bar 4 + nested FVG #2          
   ████                                    
   ▲▲▲▲▲                                   
   █████  ← bar 5                          
                                           
   Void = full 5-bar span                 
   FVGs = specific 3-candle patterns inside
```

## Timeframes

All TFs.

## Examples

**Example A — void with 2 FVGs:**
- During an NFP release, M5 prints 6 consecutive green candles, total range 75 pips, max pullback 9 pips (12%).
- Liquidity void: 6 bars.
- Contained FVGs: bars 2-3-4 (FVG #1), bars 4-5-6 (FVG #2).
- Subsequent retracement often returns to fill at least one FVG (typically the deeper one) without filling the entire void.

**Example B — FVG without surrounding void:**
- A single 3-candle FVG forms on a pullback inside a larger ranging market.
- This is an FVG but not a liquidity void (no multi-bar one-sided expansion around it).

## Common Mistakes

- **Treating a wide expansion as a single "FVG."** A 5-bar expansion is a void; the FVGs are the specific 3-candle patterns inside it.
- **Treating a 3-candle FVG as a void.** An FVG alone, without surrounding multi-bar expansion, is just an FVG.
- **Demanding voids fill completely.** Voids often partially rebalance via internal FVG fills without fully closing.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [liquidity-void](../02-liquidity/liquidity-void.md), [imbalance-definition](../26-imbalance/imbalance-definition.md), [displacement-definition](../09-displacement/displacement-definition.md), [range-expansion](../01-market-structure/range-expansion.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.
