# Internal Range Liquidity (IRL)

**Category:** 02-liquidity
**Aliases:** IRL, internal liquidity, intra-range liquidity
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, irl, internal, dealing-range

## Definition

Internal Range Liquidity is liquidity (PD arrays, internal swing pivots, FVGs, OBs) that exists **inside** the current dealing range — i.e., between the LTH and LTL that bound the range. ICT pairs IRL with [external-range-liquidity](external-range-liquidity.md) as the two operative target classes: IRL is the staging or partial-take zone, ERL is the full-delivery destination.

## Formal Criteria

- The reference dealing range is bounded by the most recent confirmed LTH and LTL on the analysis TF.
- IRL = any of:
  - Internal swing highs / lows ([internal-structure](../01-market-structure/internal-structure.md)).
  - FVGs whose price range falls inside the dealing range bounds.
  - Order blocks whose price range falls inside the bounds.
  - Internal trendline liquidity (touches all inside the range).
- An IRL target taken does NOT flip HTF bias by itself — only ERL takes do.

## Formula / Math

```
LTH_ext, LTL_ext = bounds of current dealing range

is_IRL(level) := LTL_ext < level < LTH_ext
                  AND level identifies as one of: internal-swing | FVG | OB | trendline-touch

is_ERL(level) := level >= LTH_ext OR level <= LTL_ext
```

## Machine-Readable

```json
{
  "id": "internal-range-liquidity",
  "category": "02-liquidity",
  "aliases": ["IRL", "internal-liquidity"],
  "criteria": [
    {"id": "c1", "expr": "LTL_ext < level < LTH_ext"},
    {"id": "c2", "expr": "level is internal-swing or FVG or OB or trendline-touch"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["external-range-liquidity","internal-structure","fair-value-gap","draw-on-liquidity","dealing-range","liquidity-pool"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   LTH_ext ────────────────────────  ERL above

       internal-swing   FVG          ← IRL targets
              /\        ▒▒▒▒
             /  \       ▒▒▒▒
            /    \      ▒▒▒▒
                  OB
                  ░░░░  ← IRL target
                  ░░░░

   LTL_ext ────────────────────────  ERL below
```

## Timeframes

Most operational on H1+ where dealing ranges are coherent. On M1/M5 the LTH/LTL drift rapidly and IRL/ERL distinctions blur.

## Examples

**Example 1 — Daily range with IRL ladder:**
- Daily LTH 1.1000, daily LTL 1.0800.
- Inside the range: H4 internal swing high at 1.0950, H4 bullish FVG at 1.0870–1.0885, H4 OB at 1.0820–1.0830.
- Bullish-bias H4 setup: take SSL below the OB (deep discount), target IRL FVG and internal SH first, then ERL at the LTH for full delivery.

## Common Mistakes

- **Treating IRL and ERL identically.** IRL = partial / scaling-out target. ERL = full delivery. Conflating them produces premature exits or held-too-long trades.
- **Forgetting the reference TF.** An ERL on M5 is often an IRL on H4. Always state the TF.
- **Stale range bounds.** When a new external BOS occurs, the range is redefined; old IRL/ERL labels need refreshing.

## Related Concepts

- [external-range-liquidity](external-range-liquidity.md) — counterpart.
- [internal-structure](../01-market-structure/internal-structure.md) — internal swings are IRL.
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) — most common IRL form.
- [draw-on-liquidity](draw-on-liquidity.md) — IRL/ERL distinction shapes draw selection.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the bounded zone.

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW` — IRL/ERL distinction formalized in 2022 mentorship.
