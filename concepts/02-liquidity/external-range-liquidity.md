# External Range Liquidity (ERL)

**Category:** 02-liquidity
**Aliases:** ERL, external liquidity, range-bounding liquidity
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, erl, external, dealing-range

## Definition

External Range Liquidity is liquidity that sits **outside** the current dealing range — at or beyond the LTH and LTL that bound it. ERL is the algorithmic full-delivery destination: when an ERL pool is taken, an [external-structure](../01-market-structure/external-structure.md) break occurs and the dealing range is redefined. Mirror concept to [internal-range-liquidity](internal-range-liquidity.md).

## Formal Criteria

- The reference dealing range has bounds LTH_ext (top) and LTL_ext (bottom).
- ERL = any liquidity at or beyond:
  - LTH_ext (above the range top — buy-side ERL).
  - LTL_ext (below the range bottom — sell-side ERL).
- Examples: prior swing highs/lows beyond the range, equal highs/lows beyond the range, prior session/day/week highs/lows beyond the range.
- Taking ERL = external BOS = bias change.

## Formula / Math

```
is_ERL(level) := level >= LTH_ext OR level <= LTL_ext
```

After ERL is taken, a new dealing range begins forming and the old ERL becomes a historical reference.

## Machine-Readable

```json
{
  "id": "external-range-liquidity",
  "category": "02-liquidity",
  "aliases": ["ERL", "external-liquidity"],
  "criteria": [
    {"id": "c1", "expr": "level >= LTH_ext OR level <= LTL_ext"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["internal-range-liquidity","external-structure","draw-on-liquidity","dealing-range","liquidity-pool","bos-bullish","bos-bearish"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   ─── BSL ERL: PWH, prior LTHs ───  ← above the range
                                       (full-delivery target)

   LTH_ext ────────────────────────
        (current dealing range)
   LTL_ext ────────────────────────

   ─── SSL ERL: PWL, prior LTLs ───  ← below the range
                                       (full-delivery target)
```

## Timeframes

Most useful H1+. ERL on D / W are major reversal/continuation reference points; ERL on M15 are intra-day full-delivery destinations.

## Examples

**Example 1 — H4 ERL ladder:**
- H4 dealing range: LTH_ext 1.1000, LTL_ext 1.0800.
- Bullish-bias H4 sequence: sweep H4 LTL SSL (1.0795 wick, close 1.0810) → CHoCH → eventual run to LTH ERL at 1.1000 → external BOS → new range starts above 1.1000.
- The 1.1000 BSL ERL is the full-delivery target; intermediate IRL gets taken on the way.

## Common Mistakes

- **Calling internal-side liquidity ERL.** ERL is strictly at or beyond the range bounds — internal swing pivots are IRL, not ERL.
- **Misreading ERL take as a sweep only.** When ERL is taken with a close beyond, that's an external BOS / bias flip, not just a sweep. Sweep + return = still inside range.
- **Ignoring the redefinition.** Once ERL is taken with confirmation, the old LTH/LTL stop being ERL and become historical structure inside the new range.

## Related Concepts

- [internal-range-liquidity](internal-range-liquidity.md) — partial-take counterpart.
- [external-structure](../01-market-structure/external-structure.md) — what taking ERL means structurally.
- [draw-on-liquidity](draw-on-liquidity.md) — ERL is the prime full-delivery DOL target.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the bounded zone whose extremes are ERL.
- [bos-bullish](../01-market-structure/bos-bullish.md) / [bos-bearish](../01-market-structure/bos-bearish.md) — what taking ERL produces.

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW` — IRL/ERL distinction formalized.
