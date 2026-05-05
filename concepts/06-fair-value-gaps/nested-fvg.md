# Nested FVG

**Category:** 06-fair-value-gaps
**Aliases:** nested FVGs, FVG-in-FVG, multi-TF FVG nest
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW, ICT-2025-ADV-LIQUIDITY
**Tags:** fvg, nesting, multi-tf, confluence

## Definition

A **nested FVG** is when a smaller FVG (typically on a lower timeframe) sits inside the price range of a larger FVG (on a higher timeframe). ICT teaches nested FVGs as **high-conviction confluence zones**: when price returns to fill the HTF FVG, the LTF FVG provides a precise entry trigger inside the broader zone. Nested FVGs are a special case of [pd-array-nesting](../05-pd-arrays/pd-array-nesting.md) and one of the cleanest applications of the 2025 strengthening principle.

## Formal Criteria

A valid nested-FVG setup:

- **HTF FVG** (e.g., H4 or H1) defines the broad zone.
- **LTF FVG** (e.g., M15 or M5) of the **same polarity** sits entirely (or mostly) within the HTF FVG range.
- Both unmitigated.
- Same direction (bullish HTF FVG nests bullish LTF FVG; not mixed).
- Optionally: the LTF FVG straddles or sits at the HTF FVG's CE (highest-conviction nest position).

## Formula / Math

```
nested_fvg(htf_fvg, ltf_fvg) :=
    ltf_fvg.polarity == htf_fvg.polarity
    AND ltf_fvg.range ⊂ htf_fvg.range  (or substantially overlaps)
    AND both_unmitigated == true

# Conviction bonus when LTF FVG sits at HTF CE:
nested_at_ce := abs(ltf_fvg.center - htf_fvg.ce) <= small_tolerance
```

## Machine-Readable

```json
{
  "id": "nested-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["nested-FVGs", "FVG-in-FVG", "multi-tf-FVG-nest"],
  "criteria": [
    {"id": "c1", "expr": "ltf_fvg_inside_htf_fvg_range"},
    {"id": "c2", "expr": "same_polarity == true"},
    {"id": "c3", "expr": "both_fresh_unmitigated == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["fair-value-gap","pd-array-nesting","htf-pd-array-hierarchy","consequent-encroachment","ce-as-primary-entry","pd-array-confluence"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW","ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
   nested bullish FVG (H1 contains M15):

   ──── H1 FVG high ────
        ▒▒▒▒
        ▒▓▓▒  ← M15 FVG nested inside (same polarity)
        ▒▓▓▒
        ▒▒▒▒
   ──── H1 FVG low ─────

   When price returns into H1 FVG zone, the M15 FVG provides
   a precise entry trigger inside the broader HTF zone.
```

## Timeframes

Multi-TF by definition. Common pairings: H4-FVG with M15-FVG nested; H1-FVG with M5-FVG nested.

## Examples

**Example 1 — nested H1 + M15 bullish FVGs:**
- H1 bullish FVG: 1.0850–1.0875 (CE 1.08625).
- M15 bullish FVG: 1.0858–1.0866 (inside H1 FVG, near CE).
- HTF (D) bullish.
- Setup: long entry on M15 FVG CE retest at 1.0862. SL below H1 FVG low at 1.0848.
- Risk = 14 pips. Tight relative to the broader H1 zone — entry trigger is M15-precise but the structural zone is H1-wide.
- Conviction: high (nested + same polarity + HTF bias agree + LTF FVG sits at HTF CE).

## Common Mistakes

- **Cross-polarity "nesting."** A bullish FVG inside a bearish FVG is a **conflict zone**, not a nest. Same direction required.
- **One mitigated, one fresh.** If the HTF FVG is already mitigated (touched at CE), the nest's confluence weakens — re-evaluate.
- **Demanding exact containment.** Substantial overlap (~70%+) is enough; ~100% containment is not required.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [pd-array-nesting](../05-pd-arrays/pd-array-nesting.md), [htf-pd-array-hierarchy](../05-pd-arrays/htf-pd-array-hierarchy.md), [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md), [pd-array-confluence](../05-pd-arrays/pd-array-confluence.md).

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2025-ADV-LIQUIDITY`.
