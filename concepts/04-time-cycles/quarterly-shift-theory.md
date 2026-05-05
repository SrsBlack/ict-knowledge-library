# Quarterly Shift Theory

**Category:** 04-time-cycles
**Aliases:** Quarterly Theory, ICT QT, IPDA quarterly rotation
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2025
**Source IDs:** ICT-2023-QUARTERLY-THEORY, ICT-2025-ADV-LIQUIDITY
**Tags:** time, fractal, quarterly, ipda

## Definition

Quarterly Shift Theory is ICT's fractal model for how time decomposes the algorithm's price delivery. Every higher-order time period (year / month / week / day / 6-hour session) divides into **four quarters**, each carrying an AMD-like role (accumulation → manipulation → distribution → continuation/reversal). The same fractal repeats at every level down to the 90-minute cycle and below, producing a self-similar time hierarchy. In 2024–2025 ICT also taught a **quarterly rotation** at the IPDA level: every ~3–4 months the algorithm shifts its delivery focus between External Range Liquidity and Internal Range Liquidity (the "quarterly shift").

## Formal Criteria

The fractal hierarchy:

| Level | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| Year | Jan–Mar | Apr–Jun | Jul–Sep | Oct–Dec |
| Month | week 1 | week 2 | week 3 | week 4 |
| Week | Mon | Tue | Wed | Thu (Fri = closing) |
| Day (6h NY-clock blocks) | 18:00–00:00 | 00:00–06:00 | 06:00–12:00 | 12:00–18:00 |
| 6-hour session-Q | first 90 min | second 90 min | third 90 min | fourth 90 min |
| 90-min cycle | A 22.5m | M 22.5m | D 22.5m | X 22.5m |

**Note on day quarters vs killzones:** Quarterly Theory's day quartering is a clean **6-hour NY-clock split** anchored at 18:00 NY (the forex daily candle open). The 6-hour blocks do not coincide perfectly with named ICT sessions (Asia 18:00–03:00, London 02:00–11:00, etc.) or killzones — they are a separate fractal lens. Use whichever framing the analysis context calls for.

Roles attached to each quarter:

- **Q1 — Accumulation:** range-building, low-volatility positioning.
- **Q2 — Manipulation:** the Judas swing / sweep.
- **Q3 — Distribution:** the true intended move.
- **Q4 — Continuation or Reversal:** extension to the destination, or rejection that flips intent.

The ~quarterly IPDA rotation:

- ICT teaches that every 3–4 months the algorithm rotates the kind of liquidity it primarily targets (ERL ↔ IRL). This is called the **quarterly shift**.

## Formula / Math

```
fractal levels:
  Year > Month > Week > Day > 6-hour Q > 90-min > 22.5-min mini-Q

each level: split into 4 sub-periods, attach AMD-X roles by index
```

## Machine-Readable

```json
{
  "id": "quarterly-shift-theory",
  "category": "04-time-cycles",
  "aliases": ["quarterly-theory", "ICT-QT"],
  "criteria": [
    {"id": "c1", "expr": "every_period_splits_into_4_quarters == true"},
    {"id": "c2", "expr": "quarter_roles == [A, M, D, X]"},
    {"id": "c3", "expr": "fractal_repeats_at_all_time_scales == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2025",
  "related": ["90-minute-cycle","macro-times-overview","power-of-three","ipda-definition","internal-range-liquidity","external-range-liquidity"],
  "sources": ["ICT-2023-QUARTERLY-THEORY","ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
Day fractal (NY time):

    Q1            Q2            Q3             Q4
    18:00–00:00   00:00–06:00   06:00–12:00    12:00–18:00
    Accumulation  Manipulation  Distribution   Continuation/X
    (overlaps    (overlaps     (overlaps      (overlaps
     Asia)        Asia tail +   London tail +  NY PM session)
                  London open)  NY AM)
```

## Timeframes

Every TF. Quarterly Theory's primary value is making the same lens applicable at every scale — a daily AMD reads exactly the same as a 90-minute AMD just at a different magnification.

## Examples

**Example 1 — daily Q1/Q2/Q3/Q4 mapping (6h NY-clock blocks):**
- Q1 (18:00–00:00 NY, prev day): EURUSD overnight ranges 30 pips, low-volatility accumulation.
- Q2 (00:00–06:00 NY): includes the late-Asia and London-open window; sweeps Asian SSL, manipulation completes.
- Q3 (06:00–12:00 NY): captures London tail + NY AM; displaces 50 pips up to PDH BSL, distribution.
- Q4 (12:00–18:00 NY): NY lunch + NY PM; pulls back, consolidates, continuation drift.

## Common Mistakes

- **Treating quarter roles as deterministic.** AMD-X is a *typical* sequence, not a guarantee. Counter-examples are common; bias and HTF context still matter.
- **Confusing day quarters with calendar quarters.** Day-Q1 = NY 18:00–00:00 (the 6-hour block, not "Asia session" specifically); year-Q1 = Jan–Mar. Same word, different scope.
- **Equating day quarters with named ICT sessions.** They overlap but don't match exactly — Asia session runs 18:00–03:00 NY (9 hours), Day-Q1 runs 18:00–00:00 NY (6 hours). Don't assume the labels interchange.
- **Ignoring quarterly IPDA rotation.** The 3–4 month ERL↔IRL shift is a 2024–2025 refinement; older ICT content may not mention it.

## Related Concepts

- [90-minute-cycle](90-minute-cycle.md) — smallest fractal level.
- [macro-times-overview](macro-times-overview.md) — precision windows that often align with quarter boundaries.
- [power-of-three](../12-power-of-three/power-of-three.md) — AMD source concept.
- [ipda-definition](../23-ipda/ipda-definition.md) — algorithm whose delivery rotates quarterly.
- [internal-range-liquidity](../02-liquidity/internal-range-liquidity.md), [external-range-liquidity](../02-liquidity/external-range-liquidity.md) — what the IPDA quarterly shift rotates between.

## Citations

- `ICT-2023-QUARTERLY-THEORY` — Quarterly Theory taught publicly.
- `ICT-2025-ADV-LIQUIDITY` — quarterly IPDA rotation refined in 2025 advanced-liquidity series.
