# SMT Confirmation

**Category:** 16-smt-divergence
**Aliases:** SMT-confirmed setup, divergence confirmation, SMT confluence
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** smt, confirmation, confluence

## Definition

SMT Confirmation is the use of SMT divergence as a **confluence signal added to an existing ICT setup**. ICT teaches SMT as the **single highest-quality confluence factor** for entries — when an SB / OTE / FVG setup also has SMT divergence, conviction increases substantially. SMT alone is not an entry; it is a confirmation that the algorithmic intent matches the bias direction at this specific structural level.

## Formal Criteria

A setup is **SMT-confirmed** when:

- A standard ICT setup is forming (SB / OTE / FVG / OB retest).
- At the structural level being entered, an SMT divergence exists between two correlated assets.
- The divergence direction agrees with the entry direction (bullish SMT for longs, bearish SMT for shorts).
- Both assets are at meaningful structural extremes (not random points).

## Formula / Math

```
setup_with_smt_confirmation := standard_ICT_setup
                                AND smt_divergence_at_entry_level
                                AND smt_direction_aligns_with_entry_direction
                                AND structural_extreme_for_both_assets

# Conviction modifier: typically +1 confluence factor in pd-array-confluence scoring
```

## Machine-Readable

```json
{
  "id": "smt-confirmation",
  "category": "16-smt-divergence",
  "aliases": ["SMT-confirmed-setup", "divergence-confirmation", "SMT-confluence"],
  "criteria": [
    {"id": "c1", "expr": "standard_setup_present == true"},
    {"id": "c2", "expr": "smt_divergence_aligned_with_entry_direction == true"},
    {"id": "c3", "expr": "structural_extreme_at_smt_event == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["smt-divergence","correlated-pairs-smt","index-smt","smt-failure","pd-array-confluence","silver-bullet-rules","ote-rules"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   SMT-confirmed bullish SB:

   EURUSD (entry asset):                  GBPUSD (correlation asset):
                                          
   ─── known SSL ────────                 ─── known SSL ────────
       │                                      │
       ╲ ← wick (new low)                    ╲╱ ← wick (higher low — divergence)
        ╲╱                                       ▲ no new low
         ▲ ← bullish FVG                         ▲
   ─── displacement up                    ─── B does NOT confirm new low

   → bullish SMT confirms long bias on EURUSD.
```

## Timeframes

M5–D.

## Examples

**Example 1 — SMT-confirmed NY AM SB:**
- HTF bullish; setup forming on EURUSD at 10:05 NY.
- EURUSD wicks new session low; bullish FVG forms in displacement.
- Same M5: GBPUSD did NOT confirm the new low (made higher low).
- → SMT-confirmed bullish SB. Long EURUSD with extra conviction; SL at SMT-divergent low + buffer; targets via SD + DOL.

## Common Mistakes

- **SMT alone as entry trigger.** SMT is a confluence factor, not a standalone setup. Always pair with PD-array + bias.
- **Mismatched correlation.** Using EURUSD-USDJPY as SMT pair has weak/inverted correlation; signal is unreliable.
- **Ignoring structural context.** SMT at a random pair of bars is noise; require structural extremes.

## Related Concepts

- [smt-divergence](smt-divergence.md), [correlated-pairs-smt](correlated-pairs-smt.md), [index-smt](index-smt.md), [smt-failure](smt-failure.md), [pd-array-confluence](../05-pd-arrays/pd-array-confluence.md), [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md), [ote-rules](../17-optimal-trade-entry/ote-rules.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
