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
| Day | Asia (18–00 NY) | London (00–06) | NY AM (06–12) | NY PM (12–18) |
| 6-hour session-Q | first 90 min | second 90 min | third 90 min | fourth 90 min |
| 90-min cycle | A 22.5m | M 22.5m | D 22.5m | X 22.5m |

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

    Q1 Asia       Q2 London     Q3 NY AM       Q4 NY PM
    18:00–00:00    00:00–06:00   06:00–12:00    12:00–18:00
    Accumulation   Manipulation  Distribution   Continuation/X
```

## Timeframes

Every TF. Quarterly Theory's primary value is making the same lens applicable at every scale — a daily AMD reads exactly the same as a 90-minute AMD just at a different magnification.

## Examples

**Example 1 — daily Q1/Q2/Q3/Q4 mapping:**
- Asia (Q1): EURUSD ranges 30 pips (accumulation).
- London (Q2): sweeps Asian SSL (manipulation), then displaces 50 pips up.
- NY AM (Q3): continues to PDH BSL, prints daily HOD (distribution).
- NY PM (Q4): pulls back into NY AM range and consolidates (X / continuation drift).

## Common Mistakes

- **Treating quarter roles as deterministic.** AMD-X is a *typical* sequence, not a guarantee. Counter-examples are common; bias and HTF context still matter.
- **Confusing day quarters with calendar quarters.** Day-Q1 = Asia (NY 18:00–00:00); year-Q1 = Jan–Mar. Same word, different scope.
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
