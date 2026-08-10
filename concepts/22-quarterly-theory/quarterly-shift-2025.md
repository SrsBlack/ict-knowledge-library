# Quarterly Shift (2025 Refinement)

**Category:** 22-quarterly-theory
**Aliases:** QT 2025 update, IPDA quarterly rotation, ERL-IRL quarterly shift
**ICT Confidence:** high
**Year Introduced:** 2025
**Year Refined:** 2025
**Source IDs:** ICT-2025-ADV-LIQUIDITY
**Tags:** quarterly-theory, 2025-refinement, ipda-rotation

## Definition

The **Quarterly Shift (2025 refinement)** is ICT's framing — formalized in the October 2025 advanced-liquidity series — that the **IPDA rotates its delivery focus between External Range Liquidity (ERL) and Internal Range Liquidity (IRL) on roughly 3-4 month cycles**. This refinement layers on top of the original [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md) by specifying a **trade-target rotation**: in some quarters, the algorithm primarily delivers to ERL (sweeps of HTF dealing-range bounds); in others, to IRL (FVG / OB / breaker fills inside the range). Recognizing the current rotation phase informs target selection.

## Formal Criteria

The 2025 framing:

- **ERL-targeting quarter:** algorithm delivers price to swing-extreme HTF liquidity (PWH/PWL/PMH/PML); breakouts and external BOS frequent.
- **IRL-targeting quarter:** algorithm delivers price to internal PD arrays (FVGs, OBs); range-bound behavior, frequent reversals at internal levels.
- Rotation cadence: ~3-4 months (quarterly).
- The rotation isn't time-of-calendar but **algorithm state**: identify the current mode by observing recent setup outcomes.

## Formula / Math

```
quarterly_shift_state(observation_window=3_months):
    if recent_setups_show_HTF_extreme_takeouts:
        return "ERL-targeting"
    elif recent_setups_show_internal_PD_fills:
        return "IRL-targeting"
    else:
        return "transitioning"

# Adjust target framework:
if state == "ERL": prefer HTF-extreme targets
if state == "IRL": prefer internal-PD-array targets
```

## Machine-Readable

```json
{
  "id": "quarterly-shift-2025",
  "category": "22-quarterly-theory",
  "aliases": ["QT-2025-update", "IPDA-quarterly-rotation", "ERL-IRL-shift"],
  "criteria": [
    {"id": "c1", "expr": "IPDA rotates between ERL and IRL targeting"},
    {"id": "c2", "expr": "rotation cadence ~3-4 months"},
    {"id": "c3", "expr": "informs target selection per current mode"}
  ],
  "timeframes": ["D","W","MN"],
  "confidence": "high",
  "year_introduced": "2025",
  "year_refined": "2025",
  "related": ["quarterly-theory-overview","quarterly-shift-theory","ipda-definition","internal-range-liquidity","external-range-liquidity","draw-on-liquidity","pd-array-nesting"],
  "sources": ["ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
   Quarterly Shift rotation:

   Quarter A (ERL-targeting):     Quarter B (IRL-targeting):
   
   ──────── PWH ◄ taken           ──────── PWH (untaken)
                                   ▒  FVG    ◄ filled
                                   ░  OB     ◄ filled
   ──────── PWL ◄ taken           ──────── PWL (untaken)
   
   Major sweeps + BOS              Internal-PD fills + reversals
   Trade: ERL targets              Trade: IRL targets
```

## Timeframes

D / W / MN — quarterly shift is a HTF observation, not intraday.

## Examples

**Example 1 — identifying ERL-targeting mode:**
- Past 8 weeks: recent setups have repeatedly delivered to PWH and PWL extremes; weekly bias frequently flips on external BOS.
- → ERL-targeting mode. Target framework: prefer HTF-extreme (PWH/PWL) targets over internal FVG fills.

**Example 2 — IRL-targeting mode:**
- Past 8 weeks: setups consistently fill at H4 FVGs and OBs without reaching PWH/PWL.
- → IRL-targeting mode. Target framework: scale out at internal PD arrays; full HTF DOL targets less reliable.

## Common Mistakes

- **Treating shift as fixed schedule.** It's algorithm state, not calendar — observe recent setup outcomes.
- **Fighting the rotation.** ERL targets in IRL-mode quarters frequently miss; calibrate to current mode.

## Related Concepts

- [quarterly-theory-overview](quarterly-theory-overview.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [ipda-definition](../23-ipda/ipda-definition.md), [internal-range-liquidity](../02-liquidity/internal-range-liquidity.md), [external-range-liquidity](../02-liquidity/external-range-liquidity.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md), [pd-array-nesting](../05-pd-arrays/pd-array-nesting.md).

## Citations

- `ICT-2024-MENTORSHIP-MODULE-LIST`, `ICT-2025-ADV-LIQUIDITY`.
