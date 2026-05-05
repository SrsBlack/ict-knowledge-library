# Equal Highs (EQH)

**Category:** 02-liquidity
**Aliases:** EQH, double top liquidity, twin highs, relative equal highs (REH)
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, eqh, buyside, foundational

## Definition

Equal highs are two or more swing highs at (approximately) the same price level — the most concentrated form of [buy-side-liquidity](buy-side-liquidity.md). ICT considers EQH a high-probability sweep target because retail charting routinely places stop-losses just above the second touch of an obvious double-top, creating an unusually dense buystop pool.

## Formal Criteria

- Two or more swing highs (STH or higher) print within a small price tolerance of each other.
- Tolerance is timeframe- and instrument-dependent: a few pips on majors, a few points on indices, a few cents on metals.
- The space between the two highs must contain at least one swing low (i.e., they are distinct pivots, not noise on a single uptrend).
- ICT also uses **relative equal highs (REH)** when the highs are within tolerance but not exact — see [relative-equal-highs-lows](relative-equal-highs-lows.md).

## Formula / Math

```
tolerance = ε   [pair-/TF-specific; e.g. 2 pips on EURUSD H1]

equal_highs(SH_1, SH_2) := |H(SH_1) - H(SH_2)| <= ε
                            AND exists(SL between SH_1 and SH_2)
```

When `ε == 0`, ICT calls them strict EQH; with small `ε > 0` they are REH.

## Machine-Readable

```json
{
  "id": "equal-highs",
  "category": "02-liquidity",
  "aliases": ["EQH", "double-top-liquidity", "twin-highs", "REH"],
  "criteria": [
    {"id": "c1", "expr": "abs(H(SH_1) - H(SH_2)) <= tolerance"},
    {"id": "c2", "expr": "exists_SL_between(SH_1, SH_2) == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["equal-lows","buy-side-liquidity","relative-equal-highs-lows","liquidity-sweep","liquidity-pool","swing-high"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
        SH_1            SH_2          ← equal highs (within ε)
   ──────┬──────────────┬─────────  EQH liquidity pool
        /\              /\
       /  \            /  \
      /    \          /    \
                \    /
                 \  /
                  \/             ← intervening swing low
```

Two same-priced peaks separated by a valley = EQH.

## Timeframes

Every TF. EQH on D / H4 are major liquidity targets; EQH on M5 are common intra-session sweep setups.

## Examples

**Example 1 — H1 EQH on EURUSD:**
- H1 prints highs at 1.0875 and 1.0876 four hours apart, with a clear pullback to 1.0840 between them.
- Tolerance 2 pips → equal highs.
- The 1.0876 area becomes a high-probability BSL sweep target; expect price to wick above before a possible reversal.

## Common Mistakes

- **Over-strict tolerance.** Insisting on exact-tick equality misses obvious EQH. Use a sensible ε for the instrument.
- **No intervening pivot.** Two consecutive bars at the same high in a single uptrend are not EQH — they're a small consolidation. EQH require a pullback between them.
- **Treating sweep as guaranteed reversal.** EQH being swept is high-probability for *some* reaction; whether that reaction is a full reversal depends on PD-array confluence, session, and HTF bias.

## Related Concepts

- [equal-lows](equal-lows.md) — mirror.
- [buy-side-liquidity](buy-side-liquidity.md) — what EQH represents.
- [relative-equal-highs-lows](relative-equal-highs-lows.md) — when within tolerance but not exact.
- [liquidity-sweep](liquidity-sweep.md) — sweep behavior at EQH.
- [liquidity-pool](liquidity-pool.md) — EQH is the densest pool form.
- [swing-high](../01-market-structure/swing-high.md) — building block.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — EQH terminology refined.
- `ICT-2022-MENTORSHIP-OVERVIEW` — EQH as primary sweep targets.
