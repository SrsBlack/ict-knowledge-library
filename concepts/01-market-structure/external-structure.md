# External Structure

**Category:** 01-market-structure
**Aliases:** major structure, external range structure, range-bounding pivots
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, fractal, external, dealing-range

## Definition

External structure is the pair of long-term swings (LTH and LTL) that **define the boundaries of the current dealing range**. A break of external structure flips the higher-timeframe directional bias; it is the only structural event that ICT treats as a real trend change at the reference timeframe.

## Formal Criteria

- The two most recent confirmed LTH and LTL on the reference timeframe are the external structure.
- A bullish external BOS = a candle close strictly above the external LTH.
- A bearish external BOS = a candle close strictly below the external LTL.
- Any swing whose price is between the two external bounds is internal, not external (see [internal-structure](internal-structure.md)).

## Formula / Math

```
LTH_ext = highest LTH not yet broken
LTL_ext = lowest  LTL not yet broken

dealing_range = [LTL_ext, LTH_ext]

bullish_external_bos := close > LTH_ext
bearish_external_bos := close < LTL_ext
```

When an external BOS occurs, a new dealing range starts forming; the old LTH or LTL becomes a historical reference.

## Machine-Readable

```json
{
  "id": "external-structure",
  "category": "01-market-structure",
  "aliases": ["major-structure", "external-range-structure"],
  "criteria": [
    {"id": "c1", "expr": "swing == LTH_ext OR swing == LTL_ext"}
  ],
  "timeframes": ["H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["internal-structure","swing-high","swing-low","bos-bullish","bos-bearish","external-range-liquidity","dealing-range"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   LTH_ext ─────────────────────── external (range top)
            \   internal swings  /
             \   / \    / \    /
              \ /   \  /   \  /
               v     \/     v
   LTL_ext ─────────────────────── external (range bottom)
```

The two horizontal levels are external structure. Everything between them is internal.

## Timeframes

Most useful from H1 upward. The same fractal applies on lower TFs but at the entry timeframe internal breaks dominate decision making; external breaks at HTF set the tradeable bias.

## Examples

**Example 1 — Daily dealing range:**
- Daily LTH = 1.1100 (last confirmed long-term high).
- Daily LTL = 1.0750 (last confirmed long-term low).
- Range = [1.0750, 1.1100].
- A daily candle closing at 1.1115 = bullish external BOS → bias flips to bullish, new range starts forming above.
- A daily candle closing at 1.0735 = bearish external BOS → bias flips to bearish.

## Common Mistakes

- **Promoting internal swings prematurely.** A new STH inside the range does not become an LTH until the surrounding ITHs confirm the fractal.
- **Counting wicks.** External BOS uses candle **close**, not wick. A spike above LTH_ext that closes below it is a stop-run, not a structural break.
- **Confusing range with trend.** Even strongly trending markets have well-defined dealing ranges on every TF; external structure simply tells you the boundaries of the current one.

## Related Concepts

- [internal-structure](internal-structure.md) — pivots inside the bounds.
- [swing-high](swing-high.md) / [swing-low](swing-low.md) — fractal building blocks.
- [bos-bullish](bos-bullish.md) / [bos-bearish](bos-bearish.md) — what triggers a new range.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the range these bounds define.
- [external-range-liquidity](../02-liquidity/external-range-liquidity.md) — liquidity sitting beyond external structure.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — internal vs external concept.
- `ICT-2022-MENTORSHIP-OVERVIEW` — dealing-range / external-BOS framing for live trading.
