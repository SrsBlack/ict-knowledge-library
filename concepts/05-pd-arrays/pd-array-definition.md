# PD Array — Definition

**Category:** 05-pd-arrays
**Aliases:** Premium/Discount Array, PDA, institutional price level
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PD-ARRAYS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** pd-array, premium, discount, foundational

## Definition

A **PD Array** (Premium / Discount Array) is any institutional price level the algorithm uses as a reference for delivery — the umbrella term that covers Fair Value Gaps, Order Blocks, Breaker Blocks, Mitigation Blocks, Rejection Blocks, equilibrium, equal-highs / equal-lows, liquidity voids, and similar features. Every PD array is classified by which **side of equilibrium** it sits on relative to a reference dealing range: above equilibrium = premium, below = discount. ICT's framework treats PD arrays as the actual decision points for institutional buying and selling, while liquidity pools (BSL/SSL) are the destinations price travels toward.

## Formal Criteria

A PD array must:

- Be a **discrete, identifiable price feature** — a candle, FVG, swing pivot, or measured midpoint.
- Sit on a clear side of equilibrium ([equilibrium-definition](../27-equilibrium/equilibrium-definition.md)) relative to a reference dealing range.
- Be classifiable as either **premium** ([premium-array](premium-array.md), above EQ → sell-side reference) or **discount** ([discount-array](discount-array.md), below EQ → buy-side reference).

The canonical PD array types ICT teaches:

- Fair Value Gap (FVG) and its variants (IFVG, BPR).
- Order Block (bullish / bearish OB).
- Breaker Block.
- Mitigation Block.
- Rejection Block.
- Propulsion Block.
- Vacuum Block.
- Equilibrium (50% midpoint of any reference range).
- Liquidity Void.
- Standard Deviation projection levels (ICT fib targets).

## Formula / Math

```
range_top = LTH of reference dealing range
range_bot = LTL of reference dealing range
EQ        = (range_top + range_bot) / 2

is_premium_array(level)  := level > EQ
is_discount_array(level) := level < EQ
is_equilibrium(level)    := abs(level - EQ) < tolerance
```

Every entry decision asks: "Is the buyable PD array at a discount, or are we long from premium?"

## Machine-Readable

```json
{
  "id": "pd-array-definition",
  "category": "05-pd-arrays",
  "aliases": ["PDA", "premium-discount-array", "institutional-price-level"],
  "criteria": [
    {"id": "c1", "expr": "level identifies as one of: FVG, OB, BB, MB, RB, PB, vacuum, EQ, liquidity-void, SD-projection"},
    {"id": "c2", "expr": "level classifiable as premium or discount relative to reference EQ"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["premium-array","discount-array","pd-array-hierarchy","pd-array-nesting","dealing-range","equilibrium-definition","fair-value-gap","bullish-order-block","bearish-order-block","breaker-block"],
  "sources": ["ICT-2016-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   range_top ─────────── ← LTH
                █▒▒▒
                █▒▒▒  ← premium PD arrays (FVG, bearish OB, etc)
                █▒▒▒    above EQ → sell-side references
   ─────────────────── ← EQ (50% midpoint)
                ░░░
                ░░░  ← discount PD arrays (FVG, bullish OB, etc)
                ░░░    below EQ → buy-side references
   range_bot ─────────── ← LTL
```

## Timeframes

Every TF — PD arrays are fractal. HTF PD arrays (D, H4) are higher-conviction references; LTF PD arrays (M5, M15) are entry refinement levels. ICT's standard practice is HTF-array-with-LTF-confirmation.

## Examples

**Example 1 — premium FVG as a sell-side PD array:**
- H4 dealing range: LTH 1.1000, LTL 1.0800. EQ = 1.0900.
- An H4 bearish FVG forms at 1.0950–1.0960 (above EQ) → premium PD array, valid bearish-bias entry zone.
- A bullish OB at 1.0830 (below EQ) → discount PD array, valid bullish-bias entry zone.

## Common Mistakes

- **Treating any candle pattern as a PD array.** A PD array must be on the canonical list AND classifiable as premium or discount within a reference range.
- **Wrong reference range.** PD-array classification depends on which dealing range you measure against. The same level can be premium on H4 and discount on Daily.
- **Ignoring the equilibrium check.** ICT's discipline: only buy at discount, only sell at premium. Buying a "bullish OB" that sits in premium of the reference range is taking a long at the wrong side of EQ.

## Related Concepts

- [premium-array](premium-array.md), [discount-array](discount-array.md) — sides of EQ.
- [pd-array-hierarchy](pd-array-hierarchy.md), [pd-array-nesting](pd-array-nesting.md), [pd-array-confluence](pd-array-confluence.md) — multi-array structure.
- [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md) — multi-TF version.
- [dealing-range](dealing-range.md), [equilibrium-definition](../27-equilibrium/equilibrium-definition.md) — reference frame.
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [breaker-block](../08-breaker-blocks/breaker-block.md) — specific PD-array types.

## Citations

- `ICT-2016-PD-ARRAYS` — original PD-array introduction.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational framework refined.
