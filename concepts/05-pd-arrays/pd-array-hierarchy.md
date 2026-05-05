# PD Array Hierarchy

**Category:** 05-pd-arrays
**Aliases:** PD array tier ranking, array conviction order, PDA stack
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** pd-array, hierarchy, ranking

## Definition

The PD array hierarchy is ICT's ranked ordering of PD-array types by conviction strength. Not all arrays are equal: a fresh, unmitigated bullish OB at deep discount is stronger than a small bullish FVG mid-range. ICT teaches a rough ranking to help analysts prioritize entries when multiple PD arrays are present in the dealing range.

## Formal Criteria

The canonical conviction ranking ICT teaches (from highest to lower, single-TF):

1. **Order Block (OB) at EXTREMES of the range** — fresh, unmitigated, formed on a clean swing pivot.
2. **Breaker Block** — flipped OB; high conviction on second test.
3. **Fair Value Gap (FVG)** at deep premium/discount — fresh, unfilled, with displacement signature.
4. **Mitigation Block** — relevant when the prior OB was already mitigated.
5. **Rejection Block** — visible long-wick rejection at a level.
6. **Equilibrium (EQ)** — used as a decision pivot when a clean OB or FVG isn't present.
7. **Generic level** (round number, prior small swing) — lowest conviction.

Modifiers that raise rank within type:

- Freshness: unmitigated > mitigated.
- Depth: deeper into premium / discount = higher rank.
- HTF confluence (a level that aligns with a higher-TF array).
- Time-of-day alignment (formed inside or aligned with a killzone).

## Formula / Math

The hierarchy is qualitative, but a working ranking score:

```
score(PDA) =
    base_rank(type)            # OB=7, BB=6, FVG=5, MB=4, RB=3, EQ=2, generic=1
  + freshness_bonus             # +2 if unmitigated, 0 otherwise
  + depth_bonus                 # +1 per 0.1 of depth_into_range_side
  + htf_confluence_bonus        # +3 if aligned with HTF array
  + killzone_alignment_bonus    # +1 if formed inside a KZ
```

(This is not from ICT directly; it's a quantification of the ranking he teaches qualitatively.)

## Machine-Readable

```json
{
  "id": "pd-array-hierarchy",
  "category": "05-pd-arrays",
  "aliases": ["PDA-stack", "array-conviction-order"],
  "criteria": [
    {"id": "c1", "expr": "OB > BB > FVG > MB > RB > EQ > generic at single TF"},
    {"id": "c2", "expr": "fresh > mitigated"},
    {"id": "c3", "expr": "deeper into range side > shallower"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["pd-array-definition","premium-array","discount-array","pd-array-nesting","htf-pd-array-hierarchy","pd-array-confluence","bullish-order-block","breaker-block","fair-value-gap"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   range top ──────────────  premium

           ▒▒  bearish OB (fresh, deep)   ← rank 7+
           ▓▓  breaker                    ← rank 6
           ░░  bearish FVG                ← rank 5

   ────── EQ ──────────────────────────────

           ░░  bullish FVG                ← rank 5
           ▓▓  breaker                    ← rank 6
           ▒▒  bullish OB (fresh, deep)   ← rank 7+

   range bot ──────────────  discount
```

## Timeframes

The hierarchy applies at any TF; what shifts is the **HTF confluence bonus** — an LTF FVG that aligns with an HTF OB ranks higher than an LTF FVG with no HTF support.

## Examples

**Example 1 — picking among multiple discount arrays:**
- HTF bullish; H4 dealing range 1.0800–1.1000, EQ 1.0900.
- Three candidate longs in discount: bullish OB at 1.0820 (fresh), bullish FVG at 1.0860 (fresh), generic equal-low at 1.0850 (no displacement signature).
- Hierarchy: OB > FVG > generic.
- Pick: OB at 1.0820 (rank 7+ depth ~0.8). FVG at 1.0860 is the secondary fallback if 1.0820 is missed.

## Common Mistakes

- **Treating ranks as fixed.** A poorly-formed OB (no displacement, no swing-pivot anchor) can be worse than a clean FVG. Rank type, then sanity-check formation quality.
- **Ignoring depth.** A premium OB at depth 0.3 is much weaker than a premium FVG at depth 0.79.
- **Skipping HTF confluence.** An LTF-only array without HTF support is a low-conviction entry regardless of its single-TF rank.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [premium-array](premium-array.md), [discount-array](discount-array.md).
- [pd-array-nesting](pd-array-nesting.md), [pd-array-confluence](pd-array-confluence.md), [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md) — multi-array structures.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [breaker-block](../08-breaker-blocks/breaker-block.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) — array types in the hierarchy.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — array-type ranking refined.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational hierarchy taught for entry selection.
