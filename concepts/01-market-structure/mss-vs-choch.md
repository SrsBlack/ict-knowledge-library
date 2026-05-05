# MSS vs CHoCH — Disambiguation

**Category:** 01-market-structure
**Aliases:** none (this is a disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-MSS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, disambiguation, mss, choch, terminology

## Definition

This page resolves the most common terminology confusion in ICT structure analysis: when to call a structural break a **CHoCH** versus an **MSS**. The two terms are related but not interchangeable — every MSS is a CHoCH, but not every CHoCH is an MSS.

## Formal Criteria

### CHoCH (Change of Character)

- First candle close beyond the most recent swing point formed during the prior trend leg.
- Bullish version: close above the swing-high of the bearish leg.
- Bearish version: close below the swing-low of the bullish leg.
- **No displacement requirement.** Even a slow, drifting close that barely crosses the level qualifies.

### MSS (Market Structure Shift)

- Everything required for a CHoCH, **plus**:
  - The breaking candle (or sequence) shows displacement (wide range, strong body, minimal opposing wick).
  - An FVG is left behind inside the displacement.

### The Containment Relationship

```
all MSS events ⊂ all CHoCH events
```

If you ever observe an MSS, it is also a CHoCH. The reverse is not true.

## Formula / Math

```
is_choch(n) := first_close_beyond_prior_leg_swing(n)

is_mss(n)   := is_choch(n)
                AND is_displacement(n)
                AND fvg_in_break(n)
```

## Machine-Readable

```json
{
  "id": "mss-vs-choch",
  "category": "01-market-structure",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "every_mss_is_choch == true"},
    {"id": "c2", "expr": "mss_requires_displacement == true"},
    {"id": "c3", "expr": "choch_does_not_require_displacement == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["mss","choch-bullish","choch-bearish","displacement-definition","fair-value-gap"],
  "sources": ["ICT-2017-MSS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern — Side-by-side

```
CHoCH (no displacement)            MSS (with displacement)

   SH ──────┴──                    SH ──────┴──
            \                              ▲
             \  close just                  █  wide candle
              \  above SH                   █  with FVG inside
               \                            █
              close                       close well above
              barely crosses              SH, FVG visible
```

## Timeframes

Both apply on every TF. The distinction matters most on entry timeframes (M5–H1) where ICT looks for MSS to trigger setups; on HTF the difference is often academic because every meaningful HTF reversal includes displacement.

## Examples

**Example A — CHoCH but NOT MSS:**
- M15 bearish leg. Recent SH = 1.0900.
- A candle closes at 1.0901 with a tiny 5-pip body, no FVG.
- → CHoCH (bias change recognized) but NOT MSS (no displacement signature).
- Action: bias is now neutral-to-bullish, but no high-confidence entry yet.

**Example B — Both CHoCH and MSS:**
- M15 bearish leg. Recent SH = 1.0900.
- A candle prints a 30-pip body, closes at 1.0908, leaves an 8-pip FVG inside the move.
- → MSS (which is also a CHoCH).
- Action: FVG = entry zone, prior SH = invalidation reference.

## Common Mistakes

- **Using "MSS" as a synonym for "CHoCH".** They are nested concepts; using them interchangeably loses the displacement filter ICT relies on.
- **Calling a BOS an MSS.** MSS is reversal-context only. A displacement break in the same direction as the prior trend is a displacement-confirmed BOS.
- **Ignoring the FVG test.** Without the FVG, you have CHoCH at most.
- **Forgetting the prior-trend dependency.** If the prior trend was already in the same direction as the break, neither term applies — that's a BOS.

## Related Concepts

- [choch-bullish](choch-bullish.md) / [choch-bearish](choch-bearish.md) — superset.
- [mss](mss.md) — subset of CHoCH that requires displacement + FVG.
- [bos-bullish](bos-bullish.md) / [bos-bearish](bos-bearish.md) — continuation analogue.
- [displacement-definition](../09-displacement/displacement-definition.md) — the filter that turns CHoCH into MSS.
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) — the operational test.

## Citations

- `ICT-2017-MSS` — MSS introduced as a stricter form of CHoCH.
- `ICT-2022-MENTORSHIP-OVERVIEW` — MSS-with-FVG operationalized for live entries.
