# Equal Lows (EQL)

**Category:** 02-liquidity
**Aliases:** EQL, double bottom liquidity, twin lows, relative equal lows (REL)
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, eql, sellside, foundational

## Definition

Equal lows are two or more swing lows at approximately the same price level — the densest form of [sell-side-liquidity](sell-side-liquidity.md). Mirror of [equal-highs](equal-highs.md). EQL is a primary algorithmic sweep target because retail double-bottom stops cluster just below the second touch.

## Formal Criteria

- Two or more swing lows print within a small price tolerance of each other.
- Tolerance is TF- and instrument-specific (a few pips on majors).
- A swing high must exist between them (otherwise they're consecutive bars in a single downleg, not distinct pivots).
- Strict EQL: tolerance = 0. Relative EQL (REL): small ε > 0.

## Formula / Math

```
tolerance = ε

equal_lows(SL_1, SL_2) := |L(SL_1) - L(SL_2)| <= ε
                          AND exists(SH between SL_1 and SL_2)
```

## Machine-Readable

```json
{
  "id": "equal-lows",
  "category": "02-liquidity",
  "aliases": ["EQL", "double-bottom-liquidity", "twin-lows", "REL"],
  "criteria": [
    {"id": "c1", "expr": "abs(L(SL_1) - L(SL_2)) <= tolerance"},
    {"id": "c2", "expr": "exists_SH_between(SL_1, SL_2) == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["equal-highs","sell-side-liquidity","relative-equal-highs-lows","liquidity-sweep","liquidity-pool","swing-low"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
                  /\
                 /  \
                /    \
       /\    /
      /  \  /
     /    \/
    /         ← SH between
  SL_1            SL_2          ← equal lows (within ε)
   ──────┴──────────────┴─────────  EQL liquidity pool
```

## Timeframes

Every TF.

## Examples

**Example 1 — Asian-range EQL:**
- During Asia, M5 prints two lows at 1.0830 and 1.0831 separated by a brief rally.
- Tolerance 2 pips → equal lows. Asian SSL pool established.
- London open often sweeps these before reversing; if HTF bias is bullish, the sweep is the long entry trigger.

## Common Mistakes

- **Tolerance too tight or too loose.** 0-pip strict matching misses obvious patterns; 10+ pips on EURUSD H1 is too loose. Calibrate per instrument.
- **No intervening pivot.** Two adjacent bars at the same low are not EQL.
- **Reversal certainty.** EQL sweep often reverses but not always; require PD-array / session confluence.

## Related Concepts

- [equal-highs](equal-highs.md) — mirror.
- [sell-side-liquidity](sell-side-liquidity.md) — what EQL represents.
- [relative-equal-highs-lows](relative-equal-highs-lows.md) — within-tolerance variant.
- [liquidity-sweep](liquidity-sweep.md) — sweep behavior.
- [swing-low](../01-market-structure/swing-low.md) — building block.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — EQL terminology.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use.
