# Mitigation — Definition

**Category:** 18-mitigation
**Aliases:** mitigation, level-mitigation, zone-mitigation
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** mitigation, foundational, status

## Definition

In the ICT framework, **mitigation** is the **state change** that occurs when price returns to a previously-established structural reference (an OB, FVG, breaker, etc.) and **interacts with it sufficiently to be considered "no longer fresh"**. Mitigation is the verb form of "rebalance" / "test" / "fill" — the same underlying event seen from different angles depending on what's being mitigated. Mitigated zones lose their initial-touch conviction; fresh zones retain it. ICT discipline: prefer fresh references for new entries.

## Formal Criteria

Mitigation thresholds vary by structure type:

| Structure | Default mitigation threshold |
|---|---|
| FVG | CE (50% midpoint, per 2025 framing) |
| OB | MT (body midpoint) |
| Breaker | First retest reaches the OB body |
| Mitigation block | Same as breaker (zone touched) |
| Rejection block | Wick rejection occurred at the zone |

Once mitigated, a structure transitions from "fresh" to "tested." A second visit to a tested structure is a **secondary** retest (much lower probability of producing the original setup).

## Formula / Math

```
default_mitigation_threshold(structure):
  FVG:        ce(structure)
  OB:         mt(structure)
  breaker:    body_zone(structure)   # any wick into body
  rejection:  wick_rejection_at_zone

is_mitigated(structure) := exists candle k after structure.formed_bar
                            such that price(k) reaches threshold

state_after_mitigation := "tested"
                          # vs "fresh" before, "fully consumed" after full fill
```

## Machine-Readable

```json
{
  "id": "mitigation-definition",
  "category": "18-mitigation",
  "aliases": ["mitigation", "level-mitigation", "zone-mitigation"],
  "criteria": [
    {"id": "c1", "expr": "price returns and reaches structure-specific threshold"},
    {"id": "c2", "expr": "zone transitions from fresh to tested"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["mitigation-of-ob","mitigation-of-fvg","mitigation-of-breaker","partial-vs-full-mitigation","fvg-mitigation","mitigated-order-block","unmitigated-order-block","imbalance-rebalance"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Generic mitigation lifecycle:

   structure formed → (fresh)
        ↓ price returns
   structure touched at near edge → (partial, in some frameworks)
        ↓
   structure reached at default threshold (CE/MT) → (mitigated / tested)
        ↓
   structure reached at far edge → (fully mitigated / consumed)
```

## Timeframes

All TFs.

## Examples

**Example 1 — mitigation across structure types:**
- Bullish FVG at 1.0860–1.0866 (CE 1.0863); price returns to 1.0863 → FVG mitigated (CE-threshold).
- Bullish OB at 1.0820–1.0830 (MT 1.0825); price returns to 1.0825 → OB mitigated (MT-threshold).
- Bearish breaker at 1.0945–1.0955; price returns and wicks 1.0950 → breaker tested.

## Common Mistakes

- **Inconsistent thresholds.** Pick a default per structure type and stick with it.
- **Treating partial as full.** If price wicks the near edge but doesn't reach CE/MT, the structure is "partially mitigated" or simply "touched" — not fully mitigated.
- **Ignoring mitigation in entry logic.** Entering on a previously-mitigated zone hoping for "second touch magic" is generally lower-probability than waiting for fresh structure.

## Related Concepts

- [mitigation-of-ob](mitigation-of-ob.md), [mitigation-of-fvg](mitigation-of-fvg.md), [mitigation-of-breaker](mitigation-of-breaker.md), [partial-vs-full-mitigation](partial-vs-full-mitigation.md).
- [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md), [mitigated-order-block](../07-order-blocks/mitigated-order-block.md), [unmitigated-order-block](../07-order-blocks/unmitigated-order-block.md), [imbalance-rebalance](../26-imbalance/imbalance-rebalance.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
