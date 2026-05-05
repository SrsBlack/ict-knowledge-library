# Manipulation Phase

**Category:** 12-power-of-three
**Aliases:** M-phase, manipulation, Judas phase, fake-out phase
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PO3, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** po3, amd, manipulation, judas

## Definition

The **manipulation phase** is the second phase of the PO3 / AMD cycle: an engineered fake-out move that **sweeps liquidity opposite the true distribution direction**. The manipulation provides counter-flow that allows institutions to fill positions at favorable prices — retail breakout traders' stops feed the institutional book. The London open's [judas-swing](../13-judas-swing/judas-swing.md) is the canonical daily-scale manipulation event.

## Formal Criteria

- Occurs after accumulation, before distribution.
- Direction: **opposite** the true intended (distribution) direction.
- Sweeps a known liquidity pool from the prior accumulation phase.
- Typically wicks the level then reverses; sometimes briefly closes through before reversing.
- Time-of-day correspondence: London open / Asia-London transition (intraday), session Q2 (90-min), week's Q2 = Tuesday.

## Formula / Math

```
manipulation_phase := after_accumulation
                      AND sweep_of_accumulation_bound
                      AND direction OPPOSITE intended distribution direction
                      AND reversal follows (with FVG and displacement)
```

## Machine-Readable

```json
{
  "id": "manipulation-phase",
  "category": "12-power-of-three",
  "aliases": ["M-phase", "manipulation", "Judas-phase", "fake-out-phase"],
  "criteria": [
    {"id": "c1", "expr": "after_accumulation == true"},
    {"id": "c2", "expr": "sweep_of_prior_pool_in_opposite_direction == true"},
    {"id": "c3", "expr": "reversal_with_displacement_follows == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["power-of-three","accumulation-phase","distribution-phase","judas-swing","liquidity-sweep","asian-range-sweep","london-open-killzone"],
  "sources": ["ICT-2016-PO3","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   manipulation in a bullish daily PO3 (MMBM):

   accumulation high
   ─────────────
        /\  /\        ← Asia range
       /  \/  \
   ─────────────
   accumulation low (SSL pool)
        ↓
        ↓ Judas swing sweeps SSL
        ↓ (manipulation phase)
        ↓ then reverses up
        ↑ ↑ ↑ → distribution follows
```

## Timeframes

All TFs M1+.

## Examples

**Example 1 — daily manipulation in MMBM:**
- Asia accumulation 1.0850–1.0875.
- 02:55 NY: M5 wicks 1.0846 (Asian SSL swept).
- 03:10: M5 displaces up 18 pips, FVG forms.
- → manipulation complete; entering distribution phase.

## Common Mistakes

- **Trading the manipulation direction.** This IS the trap. Enter on the *reversal*, not the fake-out leg.
- **Insisting manipulation must happen.** Some sessions skip manipulation and go straight to distribution; not every accumulation produces a clean Judas.
- **Confusing manipulation with reversal.** Manipulation goes *with the wrong direction first* and then reverses; a true reversal CHoCH is structurally different.

## Related Concepts

- [power-of-three](power-of-three.md), [accumulation-phase](accumulation-phase.md), [distribution-phase](distribution-phase.md).
- [judas-swing](../13-judas-swing/judas-swing.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [asian-range-sweep](../14-asian-range/asian-range-sweep.md), [london-open-killzone](../10-killzones/london-open-killzone.md).

## Citations

- `ICT-2016-PO3`, `ICT-2022-MENTORSHIP-OVERVIEW`.
